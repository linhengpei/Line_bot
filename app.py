import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_image_message

load_dotenv()


machine = TocMachine(
    states=["user", "start","picture", "freeway","expreeway", "north_south", "east_west","one","three","five","two","four","six","eight","ten",
            "north","61","62","64","65","66","68", "central","72","74","76","78","south","82","84","86","88"
            ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "freeway",
            "conditions": "is_going_to_freeway",
        },
                                                                          #freeway start
        {
            "trigger": "advance",
            "source": "freeway",
            "dest":"north_south",
            "conditions": "is_going_to_north_south",
        },
        {                                                                    # north_south start
            "trigger": "advance",
            "source":"north_south",
            "dest": "one",
            "conditions": "is_going_to_one",
        },
        {
            "trigger": "advance",
            "source": "north_south",
            "dest": "three",
            "conditions": "is_going_to_three",
        },
        {
            "trigger": "advance",
            "source": "north_south",
            "dest": "five",
            "conditions": "is_going_to_five",
        },
                                             # north_south end
               
                                             # east_west start
        {
            "trigger": "advance",
            "source": "freeway",
            "dest": "east_west",
            "conditions": "is_going_to_east_west",
        },

        {
            "trigger": "advance",
            "source": "east_west",
            "dest": "two",
            "conditions": "is_going_to_two",
        },
        {
            "trigger": "advance",
            "source": "east_west",
            "dest": "four",
            "conditions": "is_going_to_four",
        },
        {
            "trigger": "advance",
            "source": "east_west",
            "dest": "six",
            "conditions": "is_going_to_six",
        },

        {
            "trigger": "advance",
            "source": "east_west",
            "dest": "eight",
            "conditions": "is_going_to_eight",
        },
        {
            "trigger": "advance",
            "source": "east_west",
            "dest": "ten",
            "conditions": "is_going_to_ten",
        },
                                                                                      # west-east end
                                                                         #freeway end
        {                                                               #expreeway start
            "trigger": "advance",
            "source": "start",
            "dest": "expreeway",
            "conditions": "is_going_to_expreeway",
        },
        
        {                                                            
            "trigger": "advance",
            "source": "expreeway",
            "dest": "north",
            "conditions": "is_going_to_north",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "61",
            "conditions": "is_going_to_61",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "62",
            "conditions": "is_going_to_62",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "64",
            "conditions": "is_going_to_64",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "65",
            "conditions": "is_going_to_65",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "66",
            "conditions": "is_going_to_66",
        },
        {
            "trigger": "advance",
            "source": "north",
            "dest": "68",
            "conditions": "is_going_to_68",
        },

        {
            "trigger": "advance",
            "source": "expreeway",
            "dest": "central",
            "conditions": "is_going_to_central",
        },
        {
            "trigger": "advance",
            "source": "central",
            "dest": "72",
            "conditions": "is_going_to_72",
        },
        {
            "trigger": "advance",
            "source": "central",
            "dest": "74",
            "conditions": "is_going_to_74",
        },
        {
            "trigger": "advance",
            "source": "central",
            "dest": "76",
            "conditions": "is_going_to_76",
        },
        {
            "trigger": "advance",
            "source": "central",
            "dest": "78",
            "conditions": "is_going_to_78",
        },

        {
            "trigger": "advance",
            "source": "expreeway",
            "dest": "south",
            "conditions": "is_going_to_south",
        },
        
        {
            "trigger": "advance",
            "source": "south",
            "dest": "82",
            "conditions": "is_going_to_82",
        },
        {
            "trigger": "advance",
            "source": "south",
            "dest": "84",
            "conditions": "is_going_to_84",
        },
        {
            "trigger": "advance",
            "source": "south",
            "dest": "86",
            "conditions": "is_going_to_86",
        },
        {
            "trigger": "advance",
            "source": "south",
            "dest": "88",
            "conditions": "is_going_to_88",
        },

        {
            "trigger": "advance",
            "source": ["one","three","five","two","four","six","eight","ten","61","62","64","65","66","68","72","74","76","78","82","84","86","88"],
            "dest": "picture",
            "conditions": "is_going_to_picture",
        }, 
        {
            "trigger": "go_back",
            "source":  "picture",
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token,"請重新輸入!")


    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    #machine.get_graph().draw("fsm.png", prog="dot", format="png")
    #machine.get_graph().draw("img/show-fsm.png", prog="dot", format="png")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)


from transitions.extensions import GraphMachine
from utils import send_text_message, send_image_message

picture_index=0
expreeway_info = [
    " 台61線，又稱西部濱海快速公路，常被簡稱為西濱快速公路或西濱快，是縱貫臺灣西部沿海地區的省道快速公路，也是全台最長的快速公路，計畫長度共301.834公里，實際通車長度為286公里。台61線為省道等級，不比照南北向國道收取通行費，但可作為國道1號、國道3號等南北向高速公路的替代道路，又其大部分路線為封閉式道路，因此台61線在民間有「窮人的高速公路」之戲稱。\n\n 請輸入F來看路線圖 \n 圖片出現之後請輸入1",
    " 台62線，即東西向快速公路－萬里瑞濱線，別稱萬瑞快速道路，是台灣東西向省道快速公路之一。西起基隆市安樂區大武崙，向南行經七堵區後轉東經暖暖區至新北市瑞芳區瑞濱，起點與終點道路皆為台2線，是全台唯二起點與終點皆為同一道路的快速公路，與國道3號、台62甲線構成環繞基隆市區之高快速公路系統。於2007年6月29日全線正式通車\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台64線為「東西向快速公路－八里新店線」，又稱為新北市特一號道路，是台灣東西向（實則西北往東南向）省道快速公路之一。全線均在新北市境內，西起八里區台北港，穿越觀音山隧道後進入五股，再沿二重疏洪道、五股洲子洋重劃區、新北產業園區、三重區，上重翠橋後進入板橋江子翠、民生路三、二、一段、中和中正路、景平路，東至中和區秀朗橋，全長28.42公里。\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台65線為「南北向快速公路－五股土城線」或「五股土城快速公路」。全長約12.469公里（實際里程13公里，不含中和支線），橫跨經過新北市的五股、泰山、新莊、板橋、土城等5個行政區。五股端至土城交流道為高架設計，採雙向四至六車道快速公路標準興建（跨大漢溪橋梁為雙向八車道和兩機車道），並設置九處出入口匝道，2013年1月31日全線完工通車。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台66線為「東西向快速公路－觀音大溪線」，是台灣東西向省道快速公路之一。西起桃園市觀音區觀音交流道（接台61線），東至桃園市大溪區市道112甲線，並透過市道112甲線銜接國道3號大溪交流道。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台68線為「東西向快速公路－南寮竹東線」，是台灣東西向省道快速公路之一。西起新竹市北區南寮，東至新竹縣竹東鎮竹東大橋。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台72線為「東西向快速公路－後龍汶水線」，別稱「後汶快速公路」，苗栗縣政府稱之為「苗栗中橫公路」。是台灣東西向省道快速公路之一，全線位於臺灣的苗栗縣，連接縣內中部內山地區至海線的交通。西起苗栗縣後龍鎮台1線，中經縣治苗栗市，東抵苗栗縣獅潭鄉台3線。東端可由台3線前往大湖鄉、三灣鄉；西端可由台1線前往通霄鎮、竹南鎮。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台74線為「東西向快速公路－快官霧峰線」，又稱「臺中環線」，是台灣東西向省道快速公路之一。是臺灣最長的環狀快速公路，全長37.841公里，並有一平面支線。起點與終點道路皆為國道3號，是全台唯二起點與終點皆為同一公路的快速公路。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台76線為「東西向快速公路－芳苑草屯線」，原名漢寶草屯線，是台灣東西向省道快速公路之一。目前起點位在彰化縣埔鹽鄉埔鹽交流道，終點位在南投縣草屯鎮中興系統交流道接國道三號，計畫長度42.544公里，是全台唯二尚未全線通車的東西向快速公路[註 1]。未來計畫將從埔鹽交流道向西南延伸至芳苑鄉接台61線芳苑交流道，預計長度為20.8公里[1]。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台78線為「東西向快速公路－台西古坑線」，是台灣東西向省道快速公路之一。全線位於雲林縣境內。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台82線為「東西向快速公路－東石嘉義線」，是台灣東西向省道快速公路之一。全線位於嘉義縣境內，西起東石鄉，東至國道三號水上系統交流道，總長33.959公里。此路線是12條東西向快速公路之中三條具有速限100km/h的快速公路之一。過朴子交流道以西降為速限70km/h普通省道，全線於2012年11月23日正式通車。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台84線為「東西向快速公路－北門玉井線」，是台灣東西向省道快速公路之一。全線在台南市境內，西起台南市北門區北門交流道接台61線、台17線，東至台南市玉井區玉井端接台20線，通車長度41.428公里，全線於2014年9月27日正式通車。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台86線為「東西向快速公路－台南關廟線」，別稱「台南關廟快速公路」，是台灣東西向省道快速公路之一。全線在台南市境內，西起台南市南區灣裡的台17線，東至台南市關廟區接台19甲線及國道三號，通車長度20公里，全線於2013年12月15日正式通車。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 台88線為「東西向快速公路－高雄潮州線」，別稱「高雄潮州快速公路」或「高潮快」，是位於臺灣高屏地區的省道快速公路。西起高雄市鳳山區國道一號之五甲系統交流道，往東經大寮區跨高屏溪後進入屏東縣萬丹鄉，在位於竹田鄉的竹田系統交流道與國道三號交會，東至竹田端接屏85線鄉道。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1"
]
freeway_info = [
    " 中山高速公路，簡稱中山高、國一、一高，是臺灣第一條高速公路。其連接臺灣西部各大都市、城鎮，以及臺灣南北兩大港口高雄港與基隆港，為臺灣西部走廊、乃至臺灣陸上交通最重要的大動脈。全長374.3公里（232.6英里），是臺灣第二長的高速公路，僅次於福爾摩沙高速公路；但與福爾摩沙高速公路相比，串聯區域以臺灣各地都會區為主，因此交通上也較繁忙。該公路是蔣經國內閣推動的十大建設之一，以紀念中華民國國父孫中山為名。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 福爾摩沙高速公路，台灣一般稱為第二高速公路，是因爲這條是臺灣第二條南北向的高速公路，所以形成此習慣。由於分為不同區段興建，因此過去民眾又常稱北二高、中二高、南二高等三大路段，但實際上都是同一條高速公路。全長431.5公里，為臺灣最長的高速公路。於1987年由北二高路段開始動工，1993年開始分段通車，2004年1月11日完成全線通車。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 蔣渭水高速公路，簡稱國道五號，又稱北宜高速公路，是臺灣首條橫跨東西部的高速公路，起於南港系統交流道、現訖於蘇澳交流道，全長54.3公里，係宜蘭縣通往大臺北地區與臺灣西部的交通要道。該公路的名稱是為了紀念日治時期出身宜蘭的社會運動領袖蔣渭水，其以致力於民族自救運動與文化運動之影響而聞名，並在南港起點處立有路名牌。由於雪山隧道為本公路的重要設施，臺灣民眾口語上常以「走雪隧」代稱經由此公路往來雙北、宜蘭兩地。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 中華民國國道二號是一條位於臺灣桃園市、新北市的高速公路，西起臺灣桃園國際機場，往東南而行連接國道一號，最後匯入國道三號。全線呈西北至東南走向，貫穿桃園市北部。此路線也同時連結臺灣桃園國際機場與高鐵桃園站兩大交通樞紐。此外，為因應來往臺灣桃園國際機場的龐大車流量，2011年將大園至機場系統全面拓寬為八車道，是臺灣目前唯一擁有雙向八車道規格的東西向國道。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 中華民國國道四號，又稱臺中環線。其路線西起臺中市清水區，大略沿大甲溪往東而行，經豐原區後朝南轉彎，終點於潭子區連接台74線。當前通車長度約17公里。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 水沙連高速公路，編號為中華民國國道6號，是中臺灣一條服務廣域交通的橫向高速公路，整個路線分為先期的霧峰－埔里段，以及遠期的埔里－花蓮段，目前先期路段已全部通車。2009年9月，國道6號經南投縣政府透過評審與網友票選二階段辦理，結果以「水沙連」之名獲得最高票，於是南投縣政府提請交通部臺灣區國道高速公路局將國道6號命名為「水沙連高速公路」。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 中華民國國道八號，又稱為「臺南支線」或「臺南環線」，全線通車於1999年8月16日。全線位於臺南市，西起安南區，經過安定區、新市區東抵新化區。\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1",
    " 中華民國國道十號，又稱為「高雄支線」或「高雄環線」，全線通車於1999年11月14日。西起高雄市左營區，東至高雄市旗山區。起點銜接高雄都會快速道路，可由匝道直接進出高鐵左營站。自從建造完工後，國道十號便大幅縮短高雄市區及旗山兩地之間的交通距離以及往來時間。與國道一號、國道三號、台88線組成高屏地區之環狀道路.\n\n 請輸入F來看路線圖\n 圖片出現之後請輸入1"
]
image_data = [
    "https://i.imgur.com/Gm1liKk.gif",   #國道一號圖片
    "https://i.imgur.com/nY4CIzD.gif",   #國道三號圖片
    "https://i.imgur.com/4Ij2Pt0.png",   #國道五號圖片
    "https://i.imgur.com/FRJbUls.png",   #國道二號圖片
    "https://i.imgur.com/ANcj3gB.png",   #國道四號圖片
    "https://i.imgur.com/RoOw20u.png",   #國道六號圖片
    "https://i.imgur.com/dKb1TGA.png",   #國道八號圖片
    "https://i.imgur.com/BG2xMxo.png",   #國道十號圖片
    "https://i.imgur.com/mzm4qlg.png",   #61快速公路圖片
    "https://i.imgur.com/BaA5wMn.png",   #62快速公路圖片
    "https://i.imgur.com/hs2hBkF.png",   #64快速公路圖片
    "https://i.imgur.com/2g4eEtF.png",   #65快速公路圖片
    "https://i.imgur.com/kMxNBvt.png",   #66快速公路圖片
    "https://i.imgur.com/8pxMYMw.png",   #68快速公路圖片
    "https://i.imgur.com/c1vXOXE.png",   #72快速公路圖片
    "https://i.imgur.com/WBegjKo.png",   #74快速公路圖片
    "https://i.imgur.com/3SzcdeQ.png",   #76快速公路圖片
    "https://i.imgur.com/arAbG32.png",   #78快速公路圖片
    "https://i.imgur.com/NQWLt6t.png",   #82快速公路圖片
    "https://i.imgur.com/zEsgBEm.png",   #84快速公路圖片
    "https://i.imgur.com/CO5rbTi.png",   #86快速公路圖片
    "https://i.imgur.com/qz9d5F8.png"    #88快速公路圖片
    ]


class TocMachine(GraphMachine):
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text == "1"                      #type '1' to start

    def is_going_to_freeway(self, event):
        text = event.message.text
        return text.lower() == "f"
    
    def is_going_to_north_south(self, event):
        text = event.message.text
        return text.lower() == "n"

    def is_going_to_one(self, event):
        text = event.message.text
        return text== "1"

    def is_going_to_three(self, event):
        text = event.message.text
        return text== "3"  

    def is_going_to_five(self, event):
        text = event.message.text
        return text== "5"      

    def is_going_to_east_west(self, event):
        text = event.message.text
        return text.lower()== "e"

    def is_going_to_two(self, event):
        text = event.message.text
        return text == "2"

    def is_going_to_four(self, event):
        text = event.message.text
        return text == "4"  

    def is_going_to_six(self, event):
        text = event.message.text
        return text == "6" 
    def is_going_to_eight(self, event):
        text = event.message.text
        return text == "8"

    def is_going_to_ten(self, event):
        text = event.message.text
        return text == "10"  

    def is_going_to_expreeway(self, event):
        text = event.message.text
        return text.lower() == "e"
    
    def is_going_to_north(self, event):
        text = event.message.text
        return text.lower() == "n"
    
    def is_going_to_61(self, event):
        text = event.message.text
        return text == "61"  
    def is_going_to_62(self, event):
        text = event.message.text
        return text == "62"
    def is_going_to_64(self, event):
        text = event.message.text
        return text == "64"
    def is_going_to_65(self, event):
        text = event.message.text
        return text == "65"
    def is_going_to_66(self, event):
        text = event.message.text
        return text == "66"
    def is_going_to_68(self, event):
        text = event.message.text
        return text == "68"    

    def is_going_to_central(self, event):
        text = event.message.text
        return text.lower() == "c"
    
    def is_going_to_72(self, event):
        text = event.message.text
        return text == "72"
    def is_going_to_74(self, event):
        text = event.message.text
        return text == "74"
    def is_going_to_76(self, event):
        text = event.message.text
        return text == "76"
    def is_going_to_78(self, event):
        text = event.message.text
        return text == "78" 

    def is_going_to_south(self, event):
        text = event.message.text
        return text.lower() == "s"        

    def is_going_to_82(self, event):
        text = event.message.text
        return text == "82"
    def is_going_to_84(self, event):
        text = event.message.text
        return text == "84"
    def is_going_to_86(self, event):
        text = event.message.text
        return text == "86"
    def is_going_to_88(self, event):
        text = event.message.text
        return text == "88"  
  
    def is_going_to_picture(self, event):
        text = event.message.text
        return text.lower() == "f"

# on enter function
    def on_enter_start(self, event):
        print("\nI'm entering start\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, '歡迎來到台灣高快速系統介紹 \n 高速公路輸入:F (Freeway) \n 快速道路輸入:E (Expreeway) ')
         
    def on_enter_freeway(self, event):
        print("\nI'm entering freeway\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你要查詢的方向:\n 南-北 向請輸入:N (North) \n 東-西 向請輸入:E (East)")
      
    def on_enter_north_south(self, event):
        print("\nI'm entering North_south\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你想查詢的國道編號:\n 國道一號請輸入:1 \n 國道三號請輸入:3 \n 國道五號請輸入:5 ")
        
    def on_enter_one(self, event):
        print("\nI'm entering one\n")
        global picture_index
        picture_index=0
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[0])

    def on_enter_three(self, event):
        print("\nI'm entering three\n")
        global picture_index
        picture_index=1
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[1])
     
    def on_enter_five(self, event):
        print("\nI'm entering five\n")
        global picture_index
        picture_index=2
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[2])

 
    def on_enter_east_west(self, event):
        print("\nI'm entering East_west\n")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入你想查詢的國道編號:\n 國道二號請輸入:2 \n 國道四號請輸入:4 \n 國道六號請輸入6 \n 國道八號請輸入:8 \n 國道十號請輸入:10 ")
    
    def on_enter_two(self, event):
        print("\nI'm entering two\n")
        global picture_index
        picture_index=3
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[3])

    def on_enter_four(self, event):
        print("\nI'm entering four\n")
        global picture_index
        picture_index=4
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[4])
     
    def on_enter_six(self, event):
        print("\nI'm entering six\n")
        global picture_index
        picture_index=5
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[5])

    def on_enter_eight(self, event):
        print("\nI'm entering eight\n")
        global picture_index
        picture_index=6
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[6])

    def on_enter_ten(self, event):
        print("\nI'm entering ten\n")
        global picture_index
        picture_index=7
        reply_token = event.reply_token
        send_text_message(reply_token,freeway_info[7])
  
    

    def on_enter_expreeway(self, event):
        print("\nI'm entering expreeway\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你要查詢的地區:\n北部地區請輸入:N(North) \n中部地區請輸入:C (Central) \n南部地區請輸入:S (South) ")   
    
    def on_enter_north(self, event):
        print("\nI'm entering north\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你要查詢的編號:\n61快速公路請輸入:61 \n62快速公路請輸入:62 \n64快速公路請輸入:64 \n65快速公路請輸入:65 \n66快速公路請輸入:66 \n68快速公路請輸入:68")
    def on_enter_61(self, event):
        print("\nI'm entering 61\n")
        global picture_index
        picture_index=8
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[0])

    def on_enter_62(self, event):
        print("\nI'm entering 62\n")
        global picture_index
        picture_index=9
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[1])

    def on_enter_64(self, event):
        print("\nI'm entering 64\n")
        global picture_index
        picture_index=10
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[2])

    def on_enter_65(self, event):
        print("\nI'm entering 65\n")
        global picture_index
        picture_index=11
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[3])

    def on_enter_66(self, event):
        print("\nI'm entering 66\n")
        global picture_index
        picture_index=12
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[4])                
    
    def on_enter_68(self, event):
        print("\nI'm entering 68\n")
        global picture_index
        picture_index=13
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[5])
    
    def on_enter_central(self, event):
        print("\nI'm entering central\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你要查詢的編號:\n72快速公路請輸入:72 \n74快速公路請輸入:74 \n76快速公路請輸入:76 \n78快速公路請輸入:78 ")

    def on_enter_72(self, event):
        print("\nI'm entering 72\n")
        global picture_index
        picture_index=14
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[6])

    def on_enter_74(self, event):
        print("\nI'm entering 74\n")
        global picture_index
        picture_index=15
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[7])

    def on_enter_76(self, event):
        print("\nI'm entering 76\n")
        global picture_index
        picture_index=16
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[8])                
    
    def on_enter_78(self, event):
        print("\nI'm entering 78\n")
        global picture_index
        picture_index=17
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[9])

    def on_enter_south(self, event):
        print("\nI'm entering south\n")
        reply_token = event.reply_token
        send_text_message(
            reply_token, "請輸入你要查詢的編號:\n82快速公路請輸入:82 \n84快速公路請輸入:84 \n86快速公路請輸入:86 \n88快速公路請輸入:88 ")

    def on_enter_82(self, event):
        print("\nI'm entering 82\n")
        global picture_index
        picture_index=18
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[10])

    def on_enter_84(self, event):
        print("\nI'm entering 84\n")
        global picture_index
        picture_index=19
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[11])

    def on_enter_86(self, event):
        print("\nI'm entering 86\n")
        global picture_index
        picture_index=20
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[12])                
    
    def on_enter_88(self, event):
        print("\nI'm entering 88\n")
        global picture_index
        picture_index=21
        reply_token = event.reply_token
        send_text_message(reply_token,expreeway_info[13])

    def on_enter_picture(self, event):
        print("\nI'm entering picture\n")
        reply_token = event.reply_token
        send_image_message( reply_token, image_data[picture_index])
        self.go_back()    

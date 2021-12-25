# TOC Project 2021

linhengpei for TOC Project 2021
A Line bot based on a finite state machine


## Features
* Introduce Taiwan's expressway system, let drivers know more about Taiwan’s transportation   system



## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

* user
	* first to enter `1` to use
	* There are two mode
		* freeway mode
			* enter `N` to find `North_south` direction freeway
			     * choose `1` or `3` or `5` to get infomation 
				 * enter `f` to get route map
				 * back to `user` and enter `1` to get start  
			* enter `E` to find `East_west` direction freeway			
				 * choose `2` or `4` or `6` or `8` or `10` to get infomation 
				 * enter `f` to get route map
				 * back to `user` and enter `1` to get start  
		* expressway mode
			* enter `N` to find the `North area`expreeway
			     * choose `61` or `62` or `64` or `65` or `66` or `68`get infomation 
				 * enter `f` to get route map
				 * back to `user` and enter `1` to get start again
			* enter `C` to find the `Central area`expreeway
			     * choose `72` or `74` or `76` or `78` get infomation 
				 * enter `f` to get route map
				 * back to `user` and enter `1` to get start again
			* enter `S` to find the `south area`expreeway
			     * choose `82` or `84` or `86` or `88` get infomation 
				 * enter `f` to get route map
				 * back to `user` and enter `1` to get start again
		

## Taiwan freeway network
   ![](https://i.imgur.com/YGGwTji.png)


## Taiwan expressway network
   ![](https://i.imgur.com/YNYLwPr.jpg)
   

## Geting start
   ![](https://i.imgur.com/ZqlQVUJ.png) 

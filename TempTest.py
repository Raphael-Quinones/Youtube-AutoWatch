from pyautogui import doubleClick, click, rightClick
from time import sleep
from pynput.keyboard import Key, Controller




print("Playing Links")
for i in range(18):
	print(17-i)					#counter
	sleep(5)						#wait to load the link
	click(1698, 300)				#play video
	click(1699, 15)					#click right arrow
	click(1627, 18)					#click tab


while True:
	print("Refreshing to the left")
	for i in range(18):
		print(17-i)					#counter
		click(1685, 165)				#click background
		click(1508, 13)				#click left arrow
		sleep(0.5)					#load tab animation
		click(1634, 12)				#click tab

	sleep(100)						#wait

	print("Refreshing to the Right")
	for i in range(18):
		print(17-i)					#counter
		click(1685, 165)				#click background
		click(1699, 15)					#click right arrow
		sleep(0.5)					#load tab animation
		click(1634, 12)				#click tab

	sleep(100)						#wait



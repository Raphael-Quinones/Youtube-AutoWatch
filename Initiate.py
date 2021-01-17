from pyautogui import doubleClick, click, rightClick
from time import sleep
from pynput.keyboard import Key, Controller


#Eunice Link:

#My Link: 

link = "https://www.youtube.com/watch?v=SRR0Qtxb6vc&list=UU9UFPsCgUyTiGF9_OsuhCvQ&index=1"#link to be played
print("Opening Up Firefox")

doubleClick(34, 538)		# Open up firefox

sleep(3)

'''-----------------------'''

print("Opening up Tabs")

#First Tab
rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 57)				#click on container
#Second Tab and Above
rightClick(1759, 17)		#Right Click Tab to show containers
click(1816, 82)				#click on container
#Third
rightClick(1759, 17)		#Right Click Tab to show containers
click(1816, 106)				#click on container
#Fourth
rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 124)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 141)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 158)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 185)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 211)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 231)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 260)				#click on containerf

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 280)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 301)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 318)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 350)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 372)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 388)				#click on container

rightClick(1741, 15)		#Right Click Tab to show containers
click(1816, 410)				#click on container


#19 Total Tabs

print("Opening Links")
keyboard = Controller()

for i in range(18):
	print(17-i)					#counter
	click(1747,54)				#click address bar
	keyboard.type(link)			#enter link
	sleep(1)
	keyboard.press(Key.enter)	#goto link
	click(1508, 13)				#click left arrow
	sleep(0.5)					#load tab animation
	click(1634, 12)				#click tab


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



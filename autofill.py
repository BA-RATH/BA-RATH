import pyautogui as pg 
import random
import time
a=['1','2']
time.sleep(8)
for i in range(300):
	b=random.choice(a)
	pg.press('enter')
	pg.write(b)
	pg.press('enter')
	pg.press('right')
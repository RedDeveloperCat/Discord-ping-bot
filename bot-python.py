import pyautogui
import time

msg = input("Enter your spam message😁: ")
n = input("How many times to annoy😂 ?: ")

print("time left...")

count = 15
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Spamming go brrr😎")
print("Spamming go brrr😎")
print("Spamming go brrr😎")
print("Spamming go brrr😎")
print("Spamming go brrr😎")
print("Spamming go brrr😎")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')


#By RedDeveloperCat

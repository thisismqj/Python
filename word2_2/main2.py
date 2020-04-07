import re
import random
file = open("yrwf.txt", "r", encoding="utf-8")
sentense = []
for i in range(5):
	line = file.readline()[:-1]
	sentense += re.split(r"[，。]", line)
for index, each in enumerate(sentense):
	if not each:
		sentense.pop(index)
for i in range(16):
	tips = sentense[random.randint(0, len(sentense)-1)]
	answer = sentense[sentense.index(tips)+1]
	print(tips)
	ans = input("下一句：")
	if ans == answer:
		print("正确")
	else:
		print("错误："+answer)
	print("\n"+"-"*16+"\n")
	
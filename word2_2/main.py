import re
import random

file = open("vuui.txt", "r", encoding="utf-8")
main = {}
for i in range(24):
	line = file.readline()
	temp = len(re.match(r"\(\d*\)", line).group())
	line = line[temp:-2]
	line_split = re.split(r"[：，。]", line)
	# print(line_split)
	# print(len(line_split))
	temp = [range(0, len(line_split), 2)]
	for each in range(0, len(line_split), 2):
		# print(line_split[each])
		# print(line_split[each+1])
		main[line_split[each]] = line_split[each+1]
key = list(main)
for i in range(10):
	key_index = random.randint(0, len(key))
	key_this = key[key_index]
	value_this = main[key_this]
	value_puzzle_1 = ""
	value_puzzle_2 = ""
	while True:
		temp_index = random.randint(0, len(key))
		if temp_index != key_index:
			value_puzzle_1 = main[key[temp_index]]
			break
	while True:
		temp_index = random.randint(0, len(key))
		if temp_index != key_index:
			value_puzzle_2 = main[key[temp_index]]
			break
	value_set = [value_this, value_puzzle_1, value_puzzle_2]
	q = []
	for time in range(3):
		t1 = random.choice(value_set)
		q.append(t1)
		value_set.pop(value_set.index(t1))

	print(key_this+"的意思是：\n")
	for i, each in enumerate(q):
		print(str(i)+" "+each)
	answer = int(input("\n\n"))
	if q[answer] == value_this:
		print("回答正确！")
	else:
		print("回答错误...")
		print("正确答案:"+value_this)
	print("\n"+"-"*16+"\n")

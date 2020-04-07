import demjson
import pickle
import random
# print("loading...")
# dict_file = open("library//class//main.json", "r", encoding="utf-8").read()
# binary = open("library//class//main.bin", "wb")
# list1 = demjson.decode(dict_file)
# pickle.dump(list1, binary)
file = "oxford3000"
word_bin = open("library//"+file+"//main.bin", "rb")
wrong_file = open("library//"+file+"//wrong.json", "ab")
word_list = pickle.load(word_bin)
word_bin.close()
wrongs = []
exercises = []

for time in range(16):
	exercises.append(word_list[random.randint(0, len(word_list)-1)])

def mean(word):
	for each_mean in word["mean"]:
		print(each_mean, end = " ")
		print(*word["mean"][each_mean])
for word in exercises:
	print("\n"+"-"*32+"\n")
	answer = word["word"]
	mean(word)
	i = input("请输入:")
	if i == answer:
		print("回答正确!")
	else:
		print("回答错误...")
		print("正确答案是:"+answer)
		wrongs.append(word)
wrong_file.write(demjson.encode(wrongs, encoding="utf-8"))
wrong_file.close()
wrong_count = len(wrongs)
while wrong_count:
	for wrong in wrongs:
		print("\n"+"-"*32+"\n")
		answer = wrong["word"]
		mean(wrong)
		i = input("请输入:")
		if i == answer:
			print("回答正确!")
			del wrongs[wrongs.index(wrong)]
			wrong_count -= 1
		else:
			print("回答错误...")
			print("正确答案是:"+answer)

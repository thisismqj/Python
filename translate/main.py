import requests
import pygame
import os
from bs4 import BeautifulSoup as bs
for i in range(10):
	pygame.mixer.init()
	word = input("Word:")
	url = "https://dict.cn/" + word
	res = requests.get(url)
	htm = bs(res.text, "lxml")
	audio_link = "https://audio.dict.cn/"+htm.find(name="i")["naudio"]
	audio_res = requests.get(audio_link, stream=True)
	voice = os.open("a.mp3", os.O_WRONLY)
	os.write(voice, audio_res.content)
	os.close(voice)
	pygame.mixer.music.load(r"a.mp3")
	pygame.mixer.music.play()

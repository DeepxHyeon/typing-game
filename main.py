import random
import time

words = []

n = 1
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
print(words)

input("Ready? Press Enter Key!")

start = time.time()
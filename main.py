import random
import time
import sqlite3
import datetime
import pygame.mixer


conn = sqlite3.connect('/Users/deepxhyeon/typing-game/resource/records.db', isolation_level = None)
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)"
)

words = []

n = 1
cor_cnt = 0

with open('/Users/deepxhyeon/typing-game/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
# print(words)

input("Ready? Press Enter Key!")

start = time.time()

while n <= 10:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print(f"Question {n}")
    print(q)

    x = input()
 
    print()

    pygame.mixer.init()

    if str(q).strip() == str(x).strip():
        print("Pass!")
        gs = pygame.mixer.Sound("/Users/deepxhyeon/typing-game/sound/good.wav")
        gs.play()
        cor_cnt += 1
    else:
        print("Wrong!")
        bs = pygame.mixer.Sound("/Users/deepxhyeon/typing-game/sound/bad.wav")
        bs.play()
    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 6:
    print("\n합격")
else:
    print("\n불합격")

cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print("< 게임 시간 :", et, "초 /", "정답 개수 : {} >".format(cor_cnt))

if __name__ == '__main__':
    pass
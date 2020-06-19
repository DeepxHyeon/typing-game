import random
import time

words = []

n = 1
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
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

    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 6:
    print("\n합격")
else:
    print("\n불합격")

print("< 게임 시간 :", et, "초 /", "정답 개수 : {} >".format(cor_cnt))

if __name__ == '__main__':
    pass
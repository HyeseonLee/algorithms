### 기존 방법
import sys

def reverse_words(sentence):
    words = sentence.split()  # 문장을 단어로 분리
    reversed_sentence = ""
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word  # 각 단어를 역순으로 만듦
        reversed_sentence += reversed_word + " "  # 역순으로 만든 단어를 문장에 추가
    return reversed_sentence

T = int(sys.stdin.readline().strip())
for _ in range(T):
    sentence = sys.stdin.readline().strip()
    print(reverse_words(sentence))


### 아이디어 2
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    sentence = sys.stdin.readline().strip().split() 
    for word in sentence:
        print(word[::-1], end=' ')  # 슬라이싱 사용해서 역순으로 출력
    print()

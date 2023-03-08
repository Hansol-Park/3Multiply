## Day12
## 두 수를 받아서 세 자리수 곱을 풀어내는 문제.
## 백준에 실려있는 문제를 풀어보기로 했습니다.

#a=input()
#b=input() (아래 풀이를 위해 주석으로 이동)
print(int(a)*(int(b)-int(int(b)*0.1)*10))
print(int(a)*(int(int(b)*0.1)-int(int(b)*0.01)*10))
print(int(a)*int(int(b)*0.01))
print(int(a)*int(b))

## 제가 이걸 어거지로 풀어냈는데, 원래는 이런 방식으로 풀이를 해 나가는 것이 아닌 것 같습니다.
## 하지만... 해냈죠?

B=list(map(int,b))
a=int(a)

I, J, K = a * B[-1], a * B[-2], a * B[-3]
print(I)
print(J)
print(K)

##정석 풀이(리스트 사용)

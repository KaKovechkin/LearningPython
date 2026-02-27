import random
with open('8_3.txt','w', encoding='utf-8') as file:
    for _ in range(1000000):
        i = random.randint(1, 10000)
        file.write(str(i) + '\n')
k = 0
with open('8_3.txt','r', encoding='utf-8') as file:
    numbers = file.readlines()
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            k+=1
print(k)


import random

print(random.randint(1, 5))



print()

print(random.randrange(1, 3))

a = [1, 2, 3, 4, 5]

print(random.choice(a))

# 로또 목권 번호 생성
print(random.sample(range(1, 120), k=15))
print(random.choices(range(1,120), k=15))

b = list(range(20))
print(b)
random.shuffle(b)
print(b)

print(random.sample(['red', 'blue'], counts=[4, 2], k=5))


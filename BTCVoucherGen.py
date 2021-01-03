import itertools
import random

mix = list('123qwe')
random.shuffle(mix)
a = 0
for i in itertools.product(mix, repeat=5):
    a += 1
    print(''.join(i))
print('Количество комбинаций:' + str(a))

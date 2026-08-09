'''Print numbers from 1 to 20 but skip numbers divisible by 4 using continue.'''


for i in range(1,21):
    if i % 4 == 0:
        continue
    print(i)
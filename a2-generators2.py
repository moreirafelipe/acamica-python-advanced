numbers = [x for x in range(10) if (x % 2) == 0]
numbers2 = (x for x in range(10) if (x % 2) == 0)

sum(numbers)

print(sum((x for x in range(10) if (x % 2) == 0)))
print(sum(x for x in range(10) if (x % 2) == 0))

for x in numbers:
    print(x)

for x in numbers2:
    print(x)

class Countdown(object):
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

c = Countdown(5)
for x in c:
    print(x)
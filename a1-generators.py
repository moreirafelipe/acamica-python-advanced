#Sample array
names = ['Alexander', 'Felipe', 'Suzana','Pedro']

for name in names:
    print(name)

it = names.__iter__()

print('\nIterations list\n')
print(next(it))
print(next(it))
print(next(it))

StopIteration

#CSV data manipulation example
data = open('data/access-code-password-recovery-code.csv')

it2 = data.__iter__()
print('\nIterations CSV data\n')

#By loops
for item in data:
    print(item)

data.close()

def countdown(n):
    print('Countdown from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

for x in countdown(5):
    print(x)

c = countdown(5)
print(c)

it = c.__iter__()
print(it)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
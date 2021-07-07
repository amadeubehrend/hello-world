# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('hello')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

red = 170
green = 200
blue = 10
if blue <= green <= red:
    red = red - blue
    green = green - blue
    blue -= blue
if green <= blue <= red:
    red = red - green
    blue = blue - green
    green -= green
if blue <= red <= green:
    red -= blue
    green -= blue
    blue -= blue
if green <= red <= blue:
    red -= green
    green -= green
    blue -= blue
if red <= blue <= green:
    red -= red
    blue -= red
    green -= red
if red <= green <= blue:
    red -= red
    green -= red
    blue -= blue
print(red, green, blue)

grade = 75
if grade < 50:
    output = 'F'
elif grade < 60:
    output = 'D'
elif grade < 75:
    output = 'C'
elif grade < 85:
    output = 'B'
elif grade <= 100:
    output = 'A'
else:
    output = 'Invalid grade'
print(output)
count = 0
while count <3:
    print('loop')
    count = count + 1
print('final value of count:', count)

stop = 10
result = 0
for a in range(3):
    print(a, end= ': ')
    for b in range(4):
        result += a + b
        if result > stop:
            print('-', end=' ')
            continue
        print(result, end=' ')
    print()


user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern = 'RRGBBRYBGY'
i = 0
digit = 0
for i in range(10):
    if simon_pattern[digit] == user_pattern[digit]:
        user_score += 1
    else:
        break
    digit += 1
print('User score:', user_score)

result = 0
n = 1
while n < 6:
    print(n, end=' ')
    result += 2
    n += 1
else:
    print('\ {}'.format(result))
print('done')


result = 1
n = 2
while n > -4:
    print(n, end=' ')
    result *= 3
    if result > 23:
        print('!')
        break
    n -= 1
else:
    print('/ {}'.format(result))
print('done')

result = 0
for n in range(4):
    print(n, end=' ')
    result += 2
else:
    print('/ {}'.format(result))
print('done')


stop = -14
total = 0
for number in [3, 7, 3, 5, 4, 4]:
    print(number, end=' ')
    total -= number
    if total < stop:
        print('*')
        break
else:
    print('/ {}'.format(total))
print('done')

word = 'mypassword'
word = list(word)
password = ''



i = 0
counter = 0
while i <= 100:
    print(i)
    i = i + 2
    counter += 1
print(counter)

number = 70
guess = 55
counter = 0
while number != guess:
    print(number, guess)
    if number > guess:
        guess += 10
    else:
        guess -= 1
    counter += 1
    print(number, guess)
print('The number is:', guess)
print(counter)

grades = {

    'Jennifer' : 'A',

    'Ximin' : 'C',

    'Julio' : 'B',

    'Jason' : 'C'

}

for name in grades:

    print(name + ':' + grades[name])

for j in range(2):

    for k in range(4):

        if (k == 2):

            break

        print('{:d}{:d}'.format(j, k), end=' ')
print('\n\n\n')
names = [ 'Gerry', 'Preet', 'Jimin', 'Susan' ]

index = 0

while index < len(names):

    if names[index] == 'Susan':

        break

    else:

        index += 1

else:

    print('Done')

print(index)




my_list = [3, -4, 0, -1, 2, 1, 8]

n = 0

count = 0


while n < len(my_list):

    if my_list[n] > 0:

        count = count + 1

    n = n + 1


print('\n',count)

id_list = [13, 984, 231, 140]

for id in id_list:

    if id != 231:

        print(id, end=' ')

else:

    print('Done')

num_list = [ 3, 8, 5, 15, 12, 32, 45 ]

for index, value in enumerate(num_list):

    if index > 0:

        if value < num_list[index-1]:

            print('*', end='')

    print(value, end=' ')
print()
num_list = [ 8, 2, 1, 3, 4, 7, 6 ]

for index, value in enumerate(num_list):

    if index == value:

        print('*', end='')

    print(value, end=' ')
print()

for i in range(11):

    if i == 6:

        continue

    else:

       print(i, end=' ')

print()
x = 0

i = 5

while i > 1:

    x = x + i

    i = i - 1
print(x)
import sys
print(sys.argv)

name = "adAr alI"

print(name.title())
print(name.upper())
print(name.lower())
print(name.lower().title())

print("====================")
print(name[0], name[-1].lower())

x = "Dhaka"
j = "Jamalpur"
m = "Mymensingh"

print(x, j, m, sep=" | ")
print("====================")

num = 1012
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd number")

print("====================")
'''###
strr = "Please enter a number: "
num = int(input(strr))
if num == 50:
    print("Half Century")

if num == 100:
    print("Century")
### '''
print("====================")

nam1 = "kadar"
nam2 = "Kadar"

if nam1.lower() == nam2.lower():
    print("Same name")
else:
    print("Not same")

print("====================")

i = 1

while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i)

print("====================")

num_list = [1, 2, 5, 'math', 3.3, 6, 9]

sum = 0
for numb in num_list:
    if type(numb) == int:
        sum += numb
print(sum)

num_list += [12]
num_list.append(8)
print(num_list)
print(num_list)

num_list.insert(4, 'chemistry')
print(num_list)
del num_list[6]
print(num_list)

print("\n===== Try exception =====")


def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Can not division by zero")
        return None
    return result


print(div(4, 2))
print(div(4, 0))

print("\n===== File Open =====")

try:
    with open('my.txt') as fobj:
        content = fobj.read()
        print(content)
except Exception as e:
    print('File Error: ', e)
a = 777
b = 777
print(a == b, a is b)

a = 3.5
b = int(3.5)
print(a ** ((a // b) * 2))
print(((a - b) * a) // b)

b = ((a - b) * a) % b
print(b)

print((a * 4) % (b * 4))

celsius = float(input("섭씨온도를 입력하세요: "))
fahrenheit = ((9 / 5) * celsius) + 32
print("섭씨온도:", celsius, "화씨온도:", fahrenheit)

a = 10.6
b = 10.5
print(a * b)
print(type(a + b))

a = "3.5"
b = 4
print(a * b)

a = "3.5"
b = "1.5"
print(a + b)

a = "3"
b = float(a)
print(b ** int(a))

a = "20"
b = "4"
print(type(float(a / b)))

a = "Gachon"
b = "CS"
c = 200

c = c // 4

print(a, b, c)

a = int(3.0)
b = float(5)

print(a, b)

print("1.0" * 5)
print("1.0" + 2)
print("Hanbit" + "Python")
print("3.5" + "0.5")

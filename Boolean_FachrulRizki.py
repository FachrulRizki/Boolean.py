print("Nama = Fachrul Rizki")
print("NPM = 18312057")
print("Kelas = IF GAB 1")
print("====================================")
print("Chapter 5 Numbers, Booleans and None")

print("5.3  Integers")
x = 1
print(x)
print(type(x))
x = 100000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))
x = 1.4
print(x)
print(type(x))

print("5.3.1  Converting to Ints")
total = int('100')
print (total)

age = int(input('Please enter your age:'))
print(type(age))
print(age)

print("5.4  Floating Point Numbers")
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

print("5.4.1  Converting to Floats")
int_value = 1
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))

print("5.4.2  Converting an Input String into a Floating PointNumber")
exchange_rate = float(input("Please enter the exchange rate to use: "))
print(exchange_rate)
print(type(exchange_rate))

print("5.5  Complex Numbers")
c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)

print("5.6  Boolean Values")
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

print("5.7.1  Integer Operations")
home = 10
away = 15
print(home + away)
print(type(home + away))

print(10 * 4)
print(type(10*4))

goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

print("5.7  Arithmetic Operators")
print('Modulus division 4 % 2:', 4 % 2)
print('Modulus division 3 % 2:', 3 % 2)

a = 5
b = 3
print(a ** b)

print("5.7.2  Negative Number Integer Division")
print('True division 3/2:', 3 / 2)
print('True division 3//2:', -3 / 2)
print('Integer division 3//2:', 3 // 2)
print('Integer division 3//2:', -3 // 2)

print("5.7.3  Floating Point Number Operators")
print(2.3 + 1.5)
print(1.5 / 2.3)
print(1.5 * 2.3)
print(2.3 - 1.5)
print(1.5 - 2.3)

print("5.7.4  Integers and Floating Point Operations")
i = 3 * 0.1
print(i)

print("5.7.5  Complex Number Operators")
c1 = 1j
c2 = 2j
c3 = c1 * c2
print(c3)

print("5.9  None Value")
winner = None
print(winner is None)

winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print("=================================================================")
print("5.11  Exercises")
jarak = input("1 Kilometer = ")
print (jarak + "m")
integer =(int(jarak))
print(type(jarak))
print (jarak + "m")
print(type(integer))
print(integer/0.62144)



















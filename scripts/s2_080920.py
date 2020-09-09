from math import sqrt

name = "Alejandro"
last_name = "Andrade"
age = 22
heigh = 1.73

# cast a string 
str(age)
float(heigh)

print(f"Name: {name}\nAge: {age}\nHeigh: {heigh}")
print("{n:^10} {a:^10} {b:^10}".format(n = name, a = age , b=heigh))
print("Tu edad %i"%age)
print("Tu name %s"%name)
print("Tu estatura %f"%heigh)

age_sqrt = sqrt(age)
print(age_sqrt)
n = int(input("Dame un numero: "))
n = sqrt(n)
print(n)
n **=1/2
print(n)
   
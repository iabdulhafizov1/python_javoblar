#1-vazifa
cars =['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
	if car=='gm':
		print(car.upper())
	else:
		print(car.title())

#2-vazifa
for car in cars:
	if car!='gm':
		print(car.title())
	else:
		print(car.upper())

#3-vazifa
foydalanuvchi_ism=input('Login ismingizni kiriting: ')
if foydalanuvchi_ism.lower()=='admin':
	print(f"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi")
else:
	print(f"Xush kelibsiz, {foydalanuvchi_ism}")

#4-vazifa
son1=int(input("1-sonni kiriting: "))
son2=int(input("2-sonni kiriting: "))
if son1==son2: print("Sonlar teng")

#5-vazifa
son=int(input("Istalgan sonni kiriting: "))
print("Manfiy son") if son<0 else print("Musbat son!")

#6-vazifa
import math
son=int(input("Istalgan sonni kiriting: "))
if son>0:
	print("Son ildizi: ",math.sqrt(son))
else:
	print("Musbat son kiriting")

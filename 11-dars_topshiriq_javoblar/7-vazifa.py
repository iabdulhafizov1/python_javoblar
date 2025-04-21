butun_son=int(input("Istalgan butun son kiriting: "))
sonlar=list(range(2,11))
for son in sonlar:
	if butun_son%son==0:
		print(f"{butun_son} soni {son} ga qoldiqsiz bo'linadi") 

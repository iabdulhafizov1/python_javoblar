mahsulotlar=['anor', 'tarvuz', 'qovun', 'banan', 'anananas', 'shaftoli', 'olma', 'mandarin', 'limon', 'uzum']
savat=[]
for n in range(5):
	savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for n in range(len(savat)):
	if savat[n] in mahsulotlar:
		print(f"{savat[n].title()} do'konimizda bor")
	else:
		print(f"{savat[n].title()} do'konimizda yo'q")
	

mahsulotlar=['anor', 'tarvuz', 'qovun', 'banan', 'anananas', 'shaftoli', 'olma', 'mandarin', 'limon', 'uzum']
savat=[]
bor_mahsulotlar=[]
yoq_mahsulotlar=[]
for n in range(5):
	savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for n in range(0,len(savat)):
	if savat[n] in mahsulotlar:
		bor_mahsulotlar.append(savat[n])
	else:
		yoq_mahsulotlar.append(savat[n])

if yoq_mahsulotlar:
	print("Do'konimizda quyidagi mahsulotlar yo'q")
	for yoq_mahsulot in yoq_mahsulotlar:
		print(yoq_mahsulot.title())
else:
	print("Siz so'ragan barcha mahsulotlar do'konda bor!")

		

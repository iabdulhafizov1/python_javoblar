#1-vazifa
ismlar=["Adhamjon","Javohir","Sarvar","Sahobiddin","Diyorbek"]
for ism in ismlar:
	print(f"Salom, {ism}!")

#2-vazifa
print(f"Ekrandagi kod {len(ismlar)} marta takrorlandi!")

#3-vazifa
toq_sonlar=list(range(11,100,2))
for toq_son in toq_sonlar:
	print(toq_son**3)

#4-vazifa
kinolar=[]
print("5 ta eng sevimli kinolaringiz nomini kiriting!")
for n in range(0,5):
	kinolar.append(input(f"{n+1}-sevimli kino nomini kiriting: "))

print(kinolar)

#5-vazifa
suh_insonlar=[]
suhbat_soni=int(input("Bugun necha kishi bilan suhbat qildingiz:"))
for n in range(0,suhbat_soni):
	suh_insonlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))

print(suh_insonlar)

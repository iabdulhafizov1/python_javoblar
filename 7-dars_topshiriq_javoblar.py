#1-vazifa
ismlar=['Adhamjon' ,'Sahobiddin', 'Javohir']

#2-vazifa
print("Salom ",ismlar[0]," Bugun choyxona bormi?")
print(ismlar[1],", choyxonaga boramizmi?")
print(ismlar[2]," bormas ekan!")

#3-vazifa
sonlar=[12, -12, 1, 1.8]

#4-vazifa
sonlar[1]=sonlar[1]+12
print(sonlar)
print(sonlar[2]+sonlar[3])
sonlar[3]=2.5

#5-vazifa
t_shaxslar=["Amir Temur","Mirzo Ulug'bek","Abdulloh ibn Muborak"]
z_shaxslar=["Elon Musk","Bil Gates","Jek Man"]

#6-vazifa
t_shaxs=t_shaxslar.pop(0)
z_shaxs=z_shaxslar.pop(2)
print("Men tarixiy shaxslardan ",t_shaxs," bilan\
 zamonaviy shaxslardan ",z_shaxs," bilan suhbat qilishni istar edim")

#7-vazifa
friends=[]
friends.append("Adhamjon")
friends.append("Sarvar")
friends.append("Javohir")
friends.append("Diyorbek")
friends.append("Sahobiddin")
print(friends)

#8-vazifa
friends.remove("Sahobiddin")
friends.remove("Adhamjon")
friends.remove("Sarvar")
print(friends)

#9-vazifa
friends.insert(0,"Shaxruz")
friends.insert(2,"Azamat")
friends.insert(5,"Samariddin")
print(friends)

#10-vazifa
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(1))
print(mehmonlar)

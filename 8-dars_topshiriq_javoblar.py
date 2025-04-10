#1-vazifa
davlatlar=["Malayziya","Yaponiya","KXDR","Gruziya","Falastin"]
print(davlatlar)

#2-vazifa
print(len(davlatlar))

#3-vazifa
print(sorted(davlatlar))

#4-vazifa
print(sorted(davlatlar, reverse=True))

#5-vazifa
print(davlatlar)

#6-vazifa
davlatlar.reverse()
print(davlatlar)

#7-vazifa
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#8-vazifa
juft_sonlar=list(range(120,1201,2))

#9-vazifa
print("Ro'yxat sonlari yig'indisi: ",sum(juft_sonlar))

#10-vazifa
print("Ro'yxatdagi eng katta va eng kichik sonlar ayirmasi ",(max(juft_sonlar))-(min(juft_sonlar)))

#11-vazifa
print("Ro'yxatdagi elementlar soni: ",len(juft_sonlar))

#12-vazifa
print("Ro'yxat boshidan 20 ta: ",juft_sonlar[:20])
print("Ro'yxat o'rtasidan 20 ta: ",juft_sonlar[260:281])
print("Ro'yxat oxiridan 20 ta: ",juft_sonlar[-20:])

#13-vazifa
taomlar=['osh','manti','chuchvara','lag\'mon','sho\'rva']

#14-vazifa
nonushta=taomlar[:]

#15-vazifa
nonushta.remove('lag\'mon')
nonushta.remove('sho\'rva')
nonushta.remove('chuchvara')
nonushta.insert(0, 'shashlik')
nonushta.insert(1, 'mastava')

#16-vazifa
print("taomlar=",taomlar)
print("nonushta=",nonushta)

#17-vazifa
nonushta=tuple(nonushta)
nonushta[0]='Qaymoq va non'
#TypeError: 'tuple' object does not support item assignment

#1-amaliyot
otam={"ismi":"husanjon", "t_yili":1967, "manzili":"Farg'ona"}
print(f"Otamning ismi {otam['ismi'].title()}, {otam['t_yili']}-yilda,\
 {otam['manzili']} viloyatida tug'ilgan.")

#2-amaliyot
taomlar={
	'otam':'stek',
	'onam':'sho\'rva',
	'ibrohim':'osh',
	'akam':'shashlik',
	'ukam':'manti'
	}
print(f"Ibrohimning sevimli taomi {taomlar['ibrohim']}, \
akamning sevimli taomi {taomlar['akam']}, \
ukamning sevimli taomi {taomlar['ukam']}.")

#3-amaliyot
izohli_lugat={
	'integer':'Butun son',
	'float':'Haqiqiy son',
	'string':'Satrli tip',
	'if':'Shart operatori',
	'for':'uchun',
	'list':"ro'yxat",
	'dictionary':"lug'at",
	'tuple':"o'zgarmas ro'yxat",
	'print':'Chiqarish',
	'input':'Kutish'
		}

#4-amaliyot
kalit=input("Biror so'z kiriting: ").lower()
print(izohli_lugat.get(kalit, "Bunday so'z mavjud emas!"))

#5-amaliyot
kalit=input("Biror so'z kiriting: ").lower()
tarjima=izohli_lugat.get(kalit)
if tarjima==None:
	print("Bunday so'z mavjud emas!")
else:
	print(tarjima)
	



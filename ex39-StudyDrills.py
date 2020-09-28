Parezga = {'Sulaymaniyah' :'SUL' , 'Hewler': 'EBL', 'Duhok': "DH", 'Hallebce': 'HB', 'Kerkuk': 'KR'}

Shar = {'SUL': 'Chemchemall', "EBL": 'koye', "DH": 'Zaxo'}

# Chend Shareky trysh zyad dekeyn
Shar["HB"] = 'Xwrmall'
Shar["KR"] = 'Twzz'

# Sharek print ekeyn bo parezga
print('=' * 10)
print(" Parezgay SUL Em sharey tedaye:", Shar['SUL'])

# Chend parezgayak print dekeyn legell kwrtkrawekey
print('=' * 10)
print('kwrtkrawey Sulaymaniyah brytye le: ', Parezga['Sulaymaniyah'])

# Be bekarhenany shar w parezga
print('=' * 10)
print("Parezgay Kerkuk em sharey tedaye:", Shar[Parezga['Kerkuk']])

# Kwrtkrawey hemw Sharekan
print('=' * 10)
for parezga, kwrtkrawe in Parezga.items():
    print("Kwrtkrawey Prezgay {} brytye le {}".format(parezga, kwrtkrawe))

# Sharekan bke naw pasregakanewe
print('=' * 10)

for kwrtkrawe, shar in list(Shar.items()):
    print("{} Shary {}i Tedaye".format(kwrtkrawe, shar))

#Hemwy be yekwe dabney
for parezga, kwrtkrawe in list(Parezga.items()):
    print("Parezgay {} Kwrtrawekey brytye le {}, Herweha Em sharey tedaye: {}".format(parezga, kwrtkrawe, Shar[kwrtkrawe]))

# Detwany kwrtkrawe be destb heny ke bwny nye le listeke
parezga = Parezga.get("Bexdad")

if not parezga:
    print("Bbwre Teyda nye")

# Lebergrtnewey Sharekan bo DICT
SharyTr = Shar.copy()
print(Shar)

# Gorrryny nawy Shar
Shar['KR'] = 'Dibs'
print(Shar)

# Bzane ew share le dict heye?
if "SUL" in Shar:
    print("Belle Teydaye")

else:
    print("Nexer bwny nye")

# Herweha Detwany item bssrytewe le kota dane
#Shar.popitem()
#print(Shar)

# Herweha Detwany dyarybkeyt kame bsrretewe
#del Shar["EBL"]
#print(Shar)

# Detwany Dict sfrbkeytewe(pakbkyetewe) be .clear .

# Detwany le Chend dict ek le yek bdey
SharParezga = {'Shar': Shar, 'Parezga': Parezga}
print(SharParezga)
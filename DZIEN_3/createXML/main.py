from xml.etree.ElementTree import Element,SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty


top = Element('autokomis')

#pierwszy samochód
sam1 = SubElement(top,'samochod')

id = SubElement(sam1,'id')
id.text = 'sam1'

marka = SubElement(sam1,'marka')
marka.text = 'Subaru'

model = SubElement(sam1,'model')
model.text = 'Impreza'

poj = SubElement(sam1,'pojemnosc')
poj.text = '2.0'

rocznik = SubElement(sam1,'rocznik')
rocznik.text = '2000'

cena = SubElement(sam1,'cena')
cena.text = '56000'

wypdod = SubElement(sam1,'wyposazenie_dod')

kolor = SubElement(wypdod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wypdod,'klimatyzacja')
klima.text = 'RFG435345435'

#drugi samochód
sam2 = SubElement(top,'samochod')

id = SubElement(sam2,'id')
id.text = 'sam2'

marka = SubElement(sam2,'marka')
marka.text = 'Subaru'

model = SubElement(sam2,'model')
model.text = 'Outback'

poj = SubElement(sam2,'pojemnosc')
poj.text = '2.4'

rocznik = SubElement(sam2,'rocznik')
rocznik.text = '2017'

cena = SubElement(sam2,'cena')
cena.text = '112000'

wypdod = SubElement(sam2,'wyposazenie_dod')

kolor = SubElement(wypdod,'kolor')
kolor.text = 'czerwony metallic'

dodpos = SubElement(wypdod,'dodatkowe_poduszki')
dodpos.text = '4'

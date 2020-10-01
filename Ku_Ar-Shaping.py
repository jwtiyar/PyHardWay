# Em 2 module bekarden bo rrek pyshandany pyte kwrdyekan le python
# Bem Sheweye download yan bke

# pip install --upgrade arabic-reshaper python-bidi
import arabic_reshaper # bo chakkrdny pyshandany pytekane.
from bidi.algorithm import get_display  #bidi bo pyshandany arastey RTL bo pyte kwrdyekan yan (arabic) deyan kat be Rast-bo-Chep

arabic = "اللغة العربية"
chakkraw = get_display(arabic_reshaper.reshape(arabic))

ckb_kurdish = "چۆنی"
chakyw = get_display(arabic_reshaper.reshape(ckb_kurdish))

print(chakkraw)
print(chakyw)
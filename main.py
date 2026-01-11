from logging import info

from kitap import Kitap
from uye import Uye

# **kwargs
book1 = Kitap(yazar = 'Sait Faik', yayin_yili=2012, baslik='Cin ali', isbn='1234-asd-789' )
book3 = Kitap( 'Sait Faik',2012, 'Cin ali', '1234-asd-789' )
book2 = Kitap("1234-asd-889", "Cin Ali 1", "Ömer Faruk Doğan", 2026)



b1 = Kitap(yazar = 'Sait Faik', yayin_yili=2012, baslik='Cin ali', isbn='1234-asd-789' )
b2 = Kitap(yazar = 'Sait Faik', yayin_yili=2012, baslik='Cin ali', isbn='1234-asd-789' )


person1 = Uye('123','Ömer','omer@gmail.com')
person2 = Uye('123','Buse')
print(person1)
print(person2)
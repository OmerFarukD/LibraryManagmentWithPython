from logging import info

from kitap import Kitap
from uye import Uye

# **kwargs
kitap1 = Kitap("978-01", "İnce Memed", "Yaşar Kemal", 1955)
kitap2 = Kitap("978-02", "Tutunamayanlar", "Oğuz Atay", 1972)
kitap3 = Kitap("978-03", "Kürk Mantolu Madonna", "Sabahattin Ali", 1943)
kitap4 = Kitap("978-04", "Saatleri Ayarlama Enstitüsü", "Ahmet Hamdi Tanpınar", 1961)
kitap5 = Kitap("978-05", "Çalıkuşu", "Reşat Nuri Güntekin", 1922)
kitap6 = Kitap("978-06", "Yaban", "Yakup Kadri Karaosmanoğlu", 1932)
kitap7 = Kitap("978-07", "Dokuzuncu Hariciye Koğuşu", "Peyami Safa", 1930)
kitap8 = Kitap("978-08", "Aylak Adam", "Yusuf Atılgan", 1959)
kitap9 = Kitap("978-09", "Puslu Kıtalar Atlası", "İhsan Oktay Anar", 1995)
kitap10 = Kitap("978-10", "Sinekli Bakkal", "Halide Edib Adıvar", 1935)


person1 = Uye('123','Ömer','omer@gmail.com')
person2 = Uye('123','Buse')

person1.kitap_odunc_al(kitap1)
person1.kitap_odunc_al(kitap2)
person1.kitap_odunc_al(kitap3)
person1.kitap_iade_et(kitap3)
person1.kitap_iade_et(kitap3)
person1.kitap_iade_et(kitap10)
print(person1)
for odunc in person1.odunc_listesi():
    print(odunc.baslik)


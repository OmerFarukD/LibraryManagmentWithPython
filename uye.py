from kitap import Kitap


class Uye:
    MAX_ODUNC = 5
    def __init__(self,uye_no, ad , email=None):
        self.uye_no = uye_no
        self.ad = ad
        self.email = email
        self._odunc_kitaplar_listesi = []

    def __str__(self):
        return f'Üye Adı : {self.ad}, numara : {self.uye_no}, email : {self.email}'


    def kitap_odunc_al(self, kitap:Kitap):
        # Defansif programlama
        if len(self._odunc_kitaplar_listesi) >= self.MAX_ODUNC:
            print(f'HATA!!! {self.ad} üyesi max {self.MAX_ODUNC} kitap ödünç alabilir.')
            return False

        if not kitap.mevcut_mu():
            print(f'HATA!!! Kitap şuan Ödünçte.')
            return False

        kitap.odunc_ver()
        self._odunc_kitaplar_listesi.append(kitap)
        return True


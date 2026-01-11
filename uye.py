from kitap import Kitap


class Uye:
    MAX_ODUNC = 5
    def __init__(self,uye_no, ad , email=None):
        self.uye_no = uye_no
        self.ad = ad
        self.email = email
        self._odunc_kitaplar_listesi = []




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

    def kitap_iade_et(self,kitap:Kitap):
        if kitap in self._odunc_kitaplar_listesi:
            kitap.iade_al()
            self._odunc_kitaplar_listesi.remove(kitap)
            return True
        else:
            print(f'HATA !!! Bu kitap {self.ad} tarafından ödünç alınmamış')
            return False


    def odunc_sayisi(self):
        return len(self._odunc_kitaplar_listesi)


    def odunc_listesi(self):
        return self._odunc_kitaplar_listesi.copy()

    def __str__(self):
        return (f'Üye Adı : {self.ad}, numara : {self.uye_no}, email : {self.email}, '
                f'Ödünç : {self.odunc_sayisi()} / {self.MAX_ODUNC}')
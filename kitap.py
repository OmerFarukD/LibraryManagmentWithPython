# this
class Kitap:
    def __init__(self, isbn , baslik , yazar, yayin_yili):
        self.isbn = isbn
        self.baslik = baslik
        self.yazar = yazar
        self.yayin_yili = yayin_yili
        self._mevcut = True

    def __str__(self):
        return f'Kitap adı : {self.baslik} isbn: {self.isbn}, Yazar: {self.yazar}, yayın yılı : {self.yayin_yili},mevcut : {self._mevcut}'
    def __eq__(self, other):
        return  self.isbn == other.isbn and self.baslik == other.baslik

    def odunc_ver(self):
        if self._mevcut:
            self._mevcut = False
            return True
        else:
            return False

    def iade_al(self):
        if not self._mevcut:
            self._mevcut = True
            return True
        else:
            return False


    def mevcut_mu(self):
        return self._mevcut


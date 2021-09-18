class Trie:
    """Luokka jolla toteutetaan trie-tietorakenne.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo juuren trie-puulle tyhjänä sanakirjana.
        """

        self.__juuri = {}

    def hae_puu(self):
        """Palauttaa koko trie-puun sanakirjana juuresta lähtien.

        Returns:
            dict: Koko trie-puu sanakirjana.
        """
        return self.__juuri

    def tyhjenna_puu(self):
        """Tyhjentää trie-puun kaikista solmuista.

        Returns:
            bool: Palauttaa arvon True.
        """

        self.__juuri = {}
        return True

    def lisaa_lapsi(self, lapsi: str, vanhempi=None):
        """Lisää lauseen trie-puuhun solmuiksi. 
        Tällä hetkellä erikoismerkkejä ei huomioida laisinkaan.

        Args:
            lapsi (str): Lause, joka halutaan lisätä trie-puuhun.
            vanhempi (vapaaehtoinen): Sanakirja, johon lausetta ollaan 
            lisäämässä. Oletusarvo on None.

        Returns:
            bool: Palauttaa arvon True kun koko lause on lisätty.
        """

        if vanhempi is None:
            vanhempi = self.__juuri

        sana = lapsi

        for i in range(len(lapsi)):
            if lapsi[i] == ' ':
                sana = lapsi[:i]
                lapsi = lapsi[i+1:]
                break

        if sana not in vanhempi:
            vanhempi[sana] = {}

        if sana != lapsi:
            self.lisaa_lapsi(lapsi, vanhempi[sana])

        return True

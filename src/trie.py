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

    def lisaa_lapsi(self, lapsi: str):
        """Näkyvä metodi, jolla lause lisätään trie-puuhun solmuiksi.
        Tällä hetkellä erikoismerkkejä ei huomioida laisinkaan.

        Args:
            lapsi (str): Lause, joka halutaan lisätä trie-puuhun.

        Returns:
            bool: Palauttaa joko arvon True tai False riippuen siitä,
            onko lause voitu lisätä puuhun.
        """

        lause_puussa = self.etsi_lause(lapsi)

        if lause_puussa:
            return False

        return self.__lisaa_lapsi(lapsi)

    def __lisaa_lapsi(self, lapsi: str, vanhempi=None):
        """Lisää lauseen trie-puuhun solmuiksi.
        Piilotettu funktio, koska puu menisi sotkuun,
        jos sanakirjan, johon lause lisätään, saisi valita.
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
            self.__lisaa_lapsi(lapsi, vanhempi[sana])

        return True

    def etsi_lause(self, lause: str, alku=None):
        """Etsii, onko jokin tietty lause olemassa trie-puussa.

        Args:
            lause (str): Lause, joka halutaan etsiä trie-puusta.
            alku (dict, vapaaehtoinen): Sanakirja, josta lähtien lausetta etsitään.
            Oletusarvo on None.

        Returns:
            bool: Palauttaa joko arvon False tai True rippuen siitä, onko lause sanakirjassa vai ei.
        """
        if alku is None:
            alku = self.__juuri

        sana = lause

        for i in range(len(lause)):
            if lause[i] == ' ':
                sana = lause[:i]
                lause = lause[i+1:]
                break

        if sana not in alku:
            return False

        if sana != lause:
            return self.etsi_lause(lause, alku[sana])

        return True


if __name__ == "__main__":
    puu = Trie()
    print(puu.hae_puu())
    print(puu.lisaa_lapsi("Punainen kissa hyppäsi pöydälle"))
    print(puu.hae_puu())
    print(puu.lisaa_lapsi("Punainen kissa hyppäsi pöydälle"))
    print(puu.hae_puu())
    print(puu.lisaa_lapsi("Punainen kissa hyppäsi"))
    print(puu.hae_puu())

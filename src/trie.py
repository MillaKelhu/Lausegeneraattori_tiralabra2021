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
        n = len(lapsi)

        if vanhempi == None:
            vanhempi = self.__juuri

        sana = lapsi

        for i in range(n):
            if lapsi[i] == ' ':
                sana = lapsi[:i]
                lapsi = lapsi[i+1:]
                break

        if sana not in vanhempi:
            vanhempi[sana] = {}
        
        if sana != lapsi:
            self.lisaa_lapsi(lapsi, vanhempi[sana])

        return True

if __name__ == "__main__":
    puu = Trie()
    print(puu.hae_puu())
    puu.lisaa_lapsi("Punainen kissa hyppäsi pöydälle")
    print(puu.hae_puu())
    puu.lisaa_lapsi("Punainen kuu on kummallinen näky")
    print(puu.hae_puu())
    puu.lisaa_lapsi("Punainen kissa joi maitoa")
    print(puu.hae_puu())
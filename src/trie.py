from alipuu import alipuu_lauseesta

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

    def lisaa_lapsi(self, lapsi):
        if type(lapsi)==str:
            pass
                 
                                         

if __name__ == "__main__":
    puu = Trie()
    print(puu.hae_puu())
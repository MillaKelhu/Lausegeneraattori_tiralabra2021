class TrieSolmu:
    """Luokka, joka toteuttaa trie-tietorakenteen solmun
    """

    def __init__(self, arvo: str, lapset: dict={}):
        """"Luokan konstruktori

        Args:
            arvo (str): Solmun arvokseen saama sana merkkijonona.
            lapset (dict): Solmun lapset sanakirjamuodossa. Oletusarvo on tyhjä sanakirja.
        """

        self.__arvo = arvo
        self.__lapset = lapset

    def lisaa(self, l_arvo: str, l_lapset: dict={}):
        """Lisää solmulle lapsen

        Args:
            l_arvo (str): Lapsen arvokseen saama sana merkkijonona.
            l_lapset (dict, vapaaehtoinen): Lapsen lapset sanakirjamuodossa. Oletusarvo on tyhjä sanakirja.

        Returns:
            bool: Kertoo, onnistuiko lapsen lisäys.
        """
        if l_arvo not in self.__lapset and l_arvo != self.__arvo:
            self.__lapset[l_arvo] = TrieSolmu(l_arvo, l_lapset)
            return True
        return False

    def hae_arvo(self):
        """Palauttaa solmun arvon.

        Returns:
            str: Solmun arvona oleva sana.
        """
        return self.__arvo

    def hae_lapset(self):
        """Palauttaa solmun lapset.

        Returns:
            dict: Solmun lapset sanakirjamuodossa.
        """
        return self.__lapset

if __name__ == "__main__":
    solmu = TrieSolmu('Kaija')
    print(solmu.hae_arvo())
    print(solmu.hae_lapset())
    print(solmu.lisaa('Leena'))
    print(solmu.lisaa('Markku'))
    print(solmu.hae_lapset)
    print(solmu)
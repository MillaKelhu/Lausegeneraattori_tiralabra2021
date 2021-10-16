from src.trie import Trie
import random


class Lauseenmuodostus:
    """Luokka, jolla toteutetaan lauseet triestä muodostava funktio
    """

    def __init__(self, trie: Trie):
        """Luokan konstruktori, jolle annetaan parametriksi trie, josta lauseita lähdetään muodostamaan.

        Args:
            trie (Trie, vapaaehtoinen): Trie-puu, josta lause muodostetaan. Oletusarvona on default_trie.
        """

        self.__trie = trie

    def muodosta_lause(self, pituus: int = 6):
        """Muodostaa lauseen triessä olevista sanoista.

        Args:
            n (int, vapaaehtoinen): Lauseen maksimipituus. Oletusarvona on 6.

        Returns:
            str: Muodostettu lause, jonka alkukirjain on suurennettu ja loppuun on lisätty piste.
        """
        lause = ""
        solmu = self.__trie

        if solmu.on_tyhja() is False:

            for i in range(pituus):
                sana, uusi_solmu = self.__valitse_sana(solmu)
                solmu = uusi_solmu
                if sana:
                    lause += sana
                    lause += " "
                if solmu:
                    continue
                break

            if lause[-1] == " ":
                lause = lause[:-1]

            lause = lause[0].upper() + lause[1:] + "."

        return lause

    def __valitse_sana(self, solmu):
        """Valitsee annetun solmun lapsista uuden sanan sekä mahdollisesti solmun, johon seuraavaksi siirrytään.

        Args:
            solmu (TrieSolmu): Triesolmu

        Returns:
            str, TrieSolmu: Valittu sana sekä solmu, johon voidaan siirtyä seuraavaksi.
        """

        lapset = solmu.hae_solmu()[1]

        if lapset != {}:
            painot = solmu.lasten_todennakoisyydet()

            sana = random.choices(list(lapset.keys()), weights=painot, k=1)[0]
            uusi_solmu = lapset[sana]
            uusi_solmu_lapset = uusi_solmu.hae_solmu()[1]

            if uusi_solmu_lapset == {}:
                juuri = self.__trie.hae_solmu()[1]
                if sana in juuri:
                    uusi_solmu = juuri[sana]
                else:
                    uusi_solmu = None

            return sana, uusi_solmu

        return None, None

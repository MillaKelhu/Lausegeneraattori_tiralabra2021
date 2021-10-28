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
        self.__markov_aste = trie.tallennuspituus-1

    def muodosta_lause(self, pituus: int = 6):
        """Muodostaa lauseen triessä olevista sanoista.

        Args:
            n (int, vapaaehtoinen): Lauseen maksimipituus. Oletusarvona on 6.

        Returns:
            str: Muodostettu lause, jonka alkukirjain on suurennettu ja loppuun on lisätty piste.
        """
        lause = []
        solmu = self.__trie
        lause_merkkijonona = ''

        if solmu.on_tyhja() is False:

            for i in range(pituus):
                sana = self.__valitse_sana(lause)
                if sana:
                    lause.append(sana)
                else:
                    break

            lause_merkkijonona = ' '.join(lause)
            lause_merkkijonona = lause_merkkijonona[0].upper(
            ) + lause_merkkijonona[1:] + "."

        return lause_merkkijonona

    def __valitse_sana(self, lause):
        """Valitsee annetun solmun lapsista uuden sanan sekä mahdollisesti solmun, johon seuraavaksi siirrytään.

        Args:
            solmu (TrieSolmu): Triesolmu

        Returns:
            str, TrieSolmu: Valittu sana sekä solmu, johon voidaan siirtyä seuraavaksi.
        """

        solmu = self.__trie

        n = min(self.__markov_aste, len(lause))

        for i in range(n, 0, -1):
            sana = lause[-i]
            if solmu:
                solmu = solmu.hae_lapsi(sana)
            else:
                break

        if solmu:
            lapset = solmu.hae_solmu()[1]

            if lapset != {}:
                lapset = solmu.hae_solmu()[1]
                painot = solmu.lasten_todennakoisyydet()
                sana = random.choices(
                    list(lapset.keys()), weights=painot, k=1)[0]

                return sana

        return None

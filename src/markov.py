from trie import Trie, default_trie
import random


class Markov:
    """Luokka, jolla toteutetaan lauseet triestä muodostava funktio
    """

    def __init__(self, trie=default_trie):
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
            str: Muodostettu lause
        """
        lause = ""
        solmu = self.__trie

        for i in range(pituus):
            sana, uusi_solmu = self.__valitse_sana(solmu)
            solmu = uusi_solmu
            if sana:
                lause += sana
                if i < pituus-1:
                    lause += " "
            if solmu:
                continue
            break

        return lause.capitalize()

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


if __name__ == "__main__":
    trie = Trie()
    trie.lisaa_lause("Punainen kissa")
    trie.lisaa_lause("Musta kissa")
    trie.lisaa_lause("Oranssi kissa")
    trie.lisaa_lause("Punainen koira")
    trie.lisaa_lause("Ruskea koira")
    trie.lisaa_lause("kissa hyppäsi")
    trie.lisaa_lause("kissa meni")
    trie.lisaa_lause("kissa kiipesi")
    trie.lisaa_lause("koira meni")
    trie.lisaa_lause("koira kiipesi")
    trie.lisaa_lause("hyppäsi pöydälle")
    trie.lisaa_lause("meni kylpyyn")
    trie.lisaa_lause("meni kauppaan")
    trie.lisaa_lause("kiipesi puuhun")
    trie.lisaa_lause("kiipesi katolle")
    markov = Markov(trie)
    print(markov.muodosta_lause())
    print(markov.muodosta_lause())
    print(markov.muodosta_lause())

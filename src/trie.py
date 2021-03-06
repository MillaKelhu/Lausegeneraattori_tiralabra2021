from src.triesolmu import TrieSolmu
from src.tekstinkasittely import tekstin_siivous


class Trie(TrieSolmu):
    """Luokka jolla toteutetaan trie-tietorakenne.
    """

    def __init__(self, tallennuspituus: int = 3):
        """Luokan konstruktori, joka luo juuren trie-puulle TrieSolmuna.
        """

        super().__init__()
        self.tallennuspituus = tallennuspituus

    def hae_puu(self, juuri=None):
        """Palauttaa puun sisäkkäisenä sanakirjana.
        Käytetään pelkästään testauksessa, jotta voidaan tarkistaa, onko lause lisätty oikein.

        Args:
            juuri (TrieSolmu, vapaaehtoinen): Juuri, josa lähdetään muodostamaan sanakirjakuvausta.
            Oletusarvona on None.

        Returns:
            dict: Trie-puu sanakirjana.
        """

        if juuri is None:
            juuri = self

        palautus = {}
        lapset = juuri.hae_solmu()[1]

        for sana in lapset:
            solmu = lapset[sana]
            palautus[sana] = self.hae_puu(solmu)

        return palautus

    def lisaa_tekstia(self, teksti: str, kaikki_lauseet_virkkeiksi: bool = False):
        """Näkyvä metodi, jolla tekstiä lisätään puuhun.
        Metodi ensin siivoaa ja paloittelee tekstin virkkeiksi annettujen parametrien mukaan.
        Sen jälkeen jokainen lause paloitellaan listaksi sanoja,
        jotka tallennetaan halutun pituisina pätkinä trie-puuhun.

        Args:
            teksti (str): Teksti merkkijonomuodossa.
            kaikki_lauseet_virkkeiksi (bool, vapaaehtoinen): Jos True,
            pilkkuja kohdellaan kuten pisteitä, ja kaikki sivu- ja päälauseet
            (mutta myös luettelot) muutetaan omiksi virkkeikseen. Oletusarvona on False,
            eli pilkut vain poistetaan eikä uusia virkkeitä synny.

        Returns:
            bool: Palauttaa arvon True kun teksti on käyty läpi ja lisätty trieen.
        """

        siivottu_teksti = tekstin_siivous(teksti, kaikki_lauseet_virkkeiksi)

        virkkeet = siivottu_teksti.split('$')
        for virke in virkkeet:
            sanat = virke.split()
            if sanat != []:
                n = len(sanat)
                if n <= self.tallennuspituus:
                    self.__lisaa_sanoja(sanat)

                else:
                    for i in range(n-self.tallennuspituus+1):
                        self.__lisaa_sanoja(sanat[i:i+self.tallennuspituus])

        return True

    def __lisaa_sanoja(self, sanat: list, juuri=None):
        """Lisää sanoja trie-puuhun solmuiksi.
        Piilotettu funktio, koska puu menisi sotkuun,
        jos juuren, josta lähtien sanat lisätään, saisi valita.

        Args:
            sanat (list): sanat, jotka halutaan lisätä trie-puuhun.
            juuri (TrieSolmu, vapaaehtoinen): TrieSolmu, johon lausetta ollaan
            lisäämässä. Oletusarvo on None.

        Returns:
            bool: Palauttaa arvon True tai False riippuen siitä, onko lause lisätty.
        """

        if juuri is None:
            juuri = self

        sana = sanat[0]

        lapsi_lisatty = juuri.lisaa_lapsi(sana)

        if lapsi_lisatty and len(sanat) == 1:
            return True

        elif len(sanat) == 1:
            return False

        sanat = sanat[1:]

        uusi_juuri = juuri.hae_lapsi(sana)
        return self.__lisaa_sanoja(sanat, uusi_juuri)


default_trie = Trie()

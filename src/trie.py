from src.triesolmu import TrieSolmu

class Trie(TrieSolmu):
    """Luokka jolla toteutetaan trie-tietorakenne.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo juuren trie-puulle TrieSolmuna.
        """

        super().__init__()

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

    def tyhjenna_puu(self):
        """Tyhjentää trie-puun kaikista solmuista.

        Returns:
            bool: Palauttaa arvon True.
        """

        self.__lapset = {}
        self.__laskuri = 1
        return True

    def lisaa_lauseita(self, lauseet: list):
        """Näkyvä metodi, jolla lauseita lisätään trie-puuhun solmuiksi.

        Args:
            lauseet (list): Lauseet tai lauseiden palat, jotka halutaan lisätä trie-puuhun.

        Returns:
            bool: Palauttaa True, kun lista on käyty läpi.
        """
        for lause in lauseet:
            self.__lisaa_lause(lause)
        
        return True

    def __lisaa_lause(self, lause: str, juuri=None):
        """Lisää lauseen trie-puuhun solmuiksi.
        Piilotettu funktio, koska puu menisi sotkuun,
        jos juuren, johon lause lisätään, saisi valita.
        Tällä hetkellä erikoismerkkejä ei huomioida laisinkaan.

        Args:
            lause (str): Lause, joka halutaan lisätä trie-puuhun.
            juuri (TrieSolmu, vapaaehtoinen): TrieSolmu, johon lausetta ollaan
            lisäämässä. Oletusarvo on None.

        Returns:
            bool: Palauttaa arvon True tai False riippuen siitä, onko lause lisätty.
        """

        if juuri is None:
            juuri = self

        sana = lause

        for i in range(len(lause)):
            if lause[i] == ' ':
                sana = lause[:i]
                lause = lause[i+1:]
                break

        lapsi_lisatty = juuri.lisaa_lapsi(sana)

        if lapsi_lisatty and sana == lause:
            return True

        elif sana == lause:
            return False

        uusi_juuri = juuri.hae_lapsi(sana)
        return self.__lisaa_lause(lause, uusi_juuri)

    def etsi_lause(self, lause: str, juuri=None):
        """Etsii, onko jokin tietty lause olemassa trie-puussa.

        Args:
            lause (str): Lause, joka halutaan etsiä trie-puusta.
            juuri (TrieSolmu, vapaaehtoinen): TrieSolmu, josta lähtien lausetta etsitään.
            Oletusarvo on None.

        Returns:
            bool: Palauttaa joko arvon False tai True rippuen siitä, onko lause sanakirjassa vai ei.
        """
        if juuri is None:
            juuri = self

        sana = lause

        for i in range(len(lause)):
            if lause[i] == ' ':
                sana = lause[:i]
                lause = lause[i+1:]
                break

        uusi_juuri = juuri.hae_lapsi(sana)

        if uusi_juuri is None:
            return False

        if sana != lause and uusi_juuri is not None:
            return self.etsi_lause(lause, uusi_juuri)

        return True


default_trie = Trie()

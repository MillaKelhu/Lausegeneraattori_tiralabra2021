class TrieSolmu:
    """Luokka, jolla toteutetaan trien yksittäisen solmun rakenne ja siihen liittyvät funktiot.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo solmulle sanakirja, johon lapset voidaan tallettaa,
        ja laskurin, jonka perusteella nähdään, kuinka monta kertaa solmun läpi ollaan kuljettu,
        kun uusia solmuja ollaan lisätty.
        """

        self.__lapset = {}
        self.__laskuri = 1

    def hae_solmu(self):
        """Päivittää laskurin, ja palauttaa sitten solmun laskurin ja lasten tiedot.

        Returns:
            tuple: Palauttaa tuplessa solmun laskurin arvon ja lapset sanakirjana.
        """
        self.__paivita_laskuri()
        return self.__laskuri, self.__lapset

    def tyhjenna(self):
        """Tyhjentää solmun kaikista lapsista ja palauttaa sen siihen tilaan, millainen se oli heti luotaessa.

        Returns:
            bool: Palauttaa arvon True.
        """

        self.__lapset = {}
        self.__laskuri = 1

    def on_tyhja(self):
        """Palauttaa tiedon siitä, onko solmulla lapsia.

        Returns:
            bool: Palauttaa arvon True jos solmulla ei ole lapsia, ja False, jos niitä on.
        """

        if self.__lapset == {}:
            return True
        return False

    def hae_lapsi(self, sana: str):
        """Palauttaa solmun yhden tietyn lapsen.

        Args:
            sana (str): Halutun lapsen arvo.

        Returns:
            TrieSolmu: Solmun haluttu lapsi TrieSolmuna.
        """
        try:
            return self.__lapset[sana]
        except KeyError:
            return None

    def __paivita_laskuri(self):
        """Päivittää laskurin noutamalla tiedon solmun lasten laskureista ja summaamalla nämä +1.
        """
        summa = 0
        for lapsi in self.__lapset:
            summa += self.__lapset[lapsi].hae_solmu()[0]

        self.__laskuri = max(summa, self.__laskuri)

    def lisaa_lapsi(self, sana: str):
        """Lisää solmulle lapsen, jonka arvo on merkkijono.
        Oletus on, että merkkijono olisi yksittäinen sana.

        Args:
            sana (str): Solmun lapsen arvona oleva sana merkkijonona.

        Returns:
            bool: Totuusarvo, joka kertoo, onnistuiko lapsen lisäys.
        """
        if sana not in self.__lapset:
            self.__lapset[sana] = TrieSolmu()
            return True

        return False

    def lasten_todennakoisyydet(self):
        """Palauttaa solmun lasten laskurit, joita käytetään sitten painoina todennäköisyyksiä laskiessa.

        Returns:
            lista: Lista, jossa on solmun lasten laskurit.
        """
        laskurit = [self.hae_lapsi(lapsi).hae_solmu()[0]
                    for lapsi in self.__lapset]
        return laskurit

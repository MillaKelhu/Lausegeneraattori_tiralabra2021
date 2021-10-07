import unittest
from src.triesolmu import TrieSolmu


class TestTrieSolmu(unittest.TestCase):
    def setUp(self):
        self.solmu = TrieSolmu()

    def test_hae_solmu_palauttaa_tyhjan_solmun_oikein(self):
        vastaus = self.solmu.hae_solmu()

        self.assertEqual(vastaus, (1, {}))

    def test_hae_lapsi_palauttaa_None_kun_etsitaan_olematonta_lasta(self):
        vastaus = self.solmu.hae_lapsi("punainen")

        self.assertEqual(vastaus, None)

    def test_lisaa_lapsi_lisaa_uuden_avaimen(self):
        print(self.solmu.lisaa_lapsi("punainen"))
        vastaus = bool("punainen" in self.solmu.hae_solmu()[1])

        self.assertEqual(vastaus, True)

    def test_lisatty_lapsi_kasvattaa_laskuria(self):
        print(self.solmu.lisaa_lapsi("punainen"))
        vastaus = self.solmu.hae_solmu()[0]

        self.assertEqual(vastaus, 1)

    def test_lisaa_lapsi_ei_lisaa_kaksoiskappaleita(self):
        print(self.solmu.lisaa_lapsi("punainen"))
        vastaus = self.solmu.lisaa_lapsi("punainen")

        self.assertEqual(vastaus, False)

    def test_lasten_todennakoisyydet_palauttaa_listan_oikein(self):
        self.solmu.lisaa_lapsi("punainen")
        self.solmu.lisaa_lapsi("kissa")
        self.solmu.lisaa_lapsi("ajoi")
        vastaus = self.solmu.lasten_todennakoisyydet()

        self.assertEqual(vastaus, [1, 1, 1])

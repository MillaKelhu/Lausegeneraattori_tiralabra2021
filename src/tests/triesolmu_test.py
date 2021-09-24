import unittest
from triesolmu import TrieSolmu


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.solmu = TrieSolmu()

    def test_hae_solmu_palauttaa_tyhjan_solmun_oikein(self):
        vastaus = self.solmu.hae_solmu()

        self.assertEqual(vastaus, (1, {}))

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

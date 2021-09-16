import unittest
from triesolmu import TrieSolmu

class TestTrieSolmu(unittest.TestCase):
    def setUp(self):
        self._solmu = TrieSolmu('sana')

    def test_hae_arvo_palauttaa_solmun_arvon_oikein(self):
        arvo = self._solmu.hae_arvo()

        self.assertEqual('sana', arvo)

    def test_hae_lapset_palauttaa_solmun_lapset_oikein(self):
        lapset = self._solmu.hae_lapset()

        self.assertEqual({}, lapset)

    def test_lisaa_lisaa_uuden_lapsen(self):
        lisatty = self._solmu.lisaa('uusisana')

        self.assertEqual(True, lisatty)

    def test_lisaa_ei_lisaa_samaa_sanaa(self):
        self._solmu.lisaa('uusisana')
        lisatty = self._solmu.lisaa('uusisana')

        self.assertEqual(False, lisatty)

    def test_lisaa_ei_lisaa_itseaan(self):
        lisatty = self._solmu.lisaa('sana')

        self.assertEqual(False, lisatty)

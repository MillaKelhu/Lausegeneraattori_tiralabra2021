import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.puu = Trie()

    def test_hae_puu_palauttaa_puun_oikein(self):
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

    def test_lisaa_lapsi_lisaa_lauseen_oikein(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        vastaus = self.puu.hae_puu()

        self.assertEqual(
            vastaus, {'Punainen': {'kissa': {'hyppäsi': {'pöydälle': {}}}}})

    def test_lisaa_lapsi_lisaa_yli_yksi_lausetta_oikein(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        self.puu.lisaa_lapsi('Punainen kuu on kummallinen näky')
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {'Punainen': {'kissa': {'hyppäsi': {
                         'pöydälle': {}}}, 'kuu': {'on': {'kummallinen': {'näky': {}}}}}})

    def test_lisaa_lapsi_ei_lisaa_kaksoiskappaleita(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        vastaus = self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')

        self.assertEqual(vastaus, False)

    def test_tyhjenna_puu_tyhjentaa_puun_oikein(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        self.puu.tyhjenna_puu()
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

    def test_etsi_lause_loytaa_lauseen_oikein(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        self.puu.lisaa_lapsi('Punainen kissa kävi kylvyssä')
        vastaus = self.puu.etsi_lause('Punainen kissa hyppäsi pöydälle')

        self.assertEqual(vastaus, True)

    def test_etsi_lause_ei_löydä_olematonta_lausetta(self):
        self.puu.lisaa_lapsi('Punainen kissa kävi_kylvyssä')
        vastaus = self.puu.etsi_lause('Punainen kissa hyppäsi pöydälle')

        self.assertEqual(vastaus, False)

    def test_etsi_lause_loytaa_osalauseen(self):
        self.puu.lisaa_lapsi('Punainen kissa hyppäsi pöydälle')
        self.puu.lisaa_lapsi('Punainen kissa kävi kylvyssä')
        vastaus = self.puu.etsi_lause('Punainen kissa')

        self.assertEqual(vastaus, True)

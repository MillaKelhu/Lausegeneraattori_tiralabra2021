import unittest
from src.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.puu = Trie()

    def test_hae_puu_toimii_oikein(self):
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

    def test_lisaa_lauseita_palauttaa_true_kun_lisataan_uusi_lause(self):
        vastaus = self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun", "punainen kissa meni kylpyyn"])

        self.assertEqual(vastaus, True)

    def test_lisaa_lause_lisaa_lauseen_oikein(self):
        self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun", "punainen kissa meni kylpyyn"])
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {'punainen': {
                         'kissa': {'kiipesi': {'puuhun': {}}, 'meni': {'kylpyyn': {}}}}})

    def test_lisaa_lause_ei_lisaa_kaksoiskappaleita(self):
        self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun"])
        self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun"])
        vastaus = self.puu.hae_puu()

        self.assertEqual(
            vastaus, {'punainen': {'kissa': {'kiipesi': {'puuhun': {}}}}})

    def test_etsi_lause_loytaa_lauseen(self):
        vastaus = self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun"])
        vastaus = self.puu.etsi_lause("punainen kissa kiipesi puuhun")

        self.assertEqual(vastaus, True)

    def test_etsi_lause_ei_loyda_olemattomia_lauseita(self):
        vastaus = self.puu.lisaa_lauseita(["punainen kissa kiipesi puuhun"])
        vastaus = self.puu.etsi_lause("punainen kissa kiipesi kuuhun")

        self.assertEqual(vastaus, False)

    def test_tyhjenna_puu_toimii_oikein(self):
        self.puu.tyhjenna_puu()
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

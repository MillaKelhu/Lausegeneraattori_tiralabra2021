import unittest
from src.lauseenmuodostus import Lauseenmuodostus
from src.trie import Trie


class TestLauseenmuodostus(unittest.TestCase):
    def setUp(self):
        self.puu = Trie()
        self.lauseenmuodostus = Lauseenmuodostus(self.puu)

    def test_muodosta_lause_toimii_oikein_tyhjalla_puulla(self):
        vastaus = self.lauseenmuodostus.muodosta_lause()

        self.assertEqual(vastaus, "")

    def test_muodosta_lause_tuottaa_aina_ei_tyhjan_merkkijonon_jossa_on_sanoja_puulla_jossa_on_tekstia(self):
        self.puu.lisaa_tekstia(
            "Olen pieni, punainen kissa, joka kiipesi puuhun.")
        lause = self.lauseenmuodostus.muodosta_lause()
        vastaus = (len(lause) >= 19)

        self.assertEqual(vastaus, True)

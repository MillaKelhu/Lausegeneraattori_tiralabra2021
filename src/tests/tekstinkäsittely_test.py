import unittest
from src.tekstinkasittely import tekstin_siivous

class TestTekstinkasittely(unittest.TestCase):
    def setUp(self):
        pass

    def test_tekstin_siivous_toimii(self):
        teksti = "Hei! Miten menee?! Kuka sinä olet?\nOlen pieni, punainen kissa, joka kiipesi puuhun."
        vastaus = tekstin_siivous(teksti)

        self.assertEqual(vastaus, "hei$miten menee$kuka sinä olet$olen pieni punainen kissa joka kiipesi puuhun")

    def test_tekstin_siivous_toimii_kun_kaikki_lauseet_muutetaan_virkkeiksi(self):
        teksti = "Hei! Miten menee?! Kuka sinä olet?\nOlen pieni, punainen kissa, joka kiipesi puuhun."
        vastaus = tekstin_siivous(teksti, True)

        self.assertEqual(vastaus, "hei$miten menee$kuka sinä olet$olen pieni$punainen kissa$joka kiipesi puuhun")

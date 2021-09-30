import unittest
import tekstinkasittely

class TestTekstinkasittely(unittest.TestCase):
    def setUp(self):
        pass

    def test_tekstin_siivous_toimii(self):
        teksti = "Hei! Kuka sinä olet?\nOlen pieni, punainen kissa, joka kiipesi puuhun."
        vastaus = tekstinkasittely.tekstin_siivous(teksti)

        self.assertEqual(vastaus, "hei. kuka sinä olet. olen pieni punainen kissa joka kiipesi puuhun.")

    def test_tekstin_siivous_toimii_kun_kaikki_lauseet_muutetaan_virkkeiksi(self):
        teksti = "Hei! Kuka sinä olet?\nOlen pieni, punainen kissa, joka kiipesi puuhun."
        vastaus = tekstinkasittely.tekstin_siivous(teksti)

        self.assertEqual(vastaus, "hei. kuka sinä olet. olen pieni. punainen kissa. joka kiipesi puuhun.")

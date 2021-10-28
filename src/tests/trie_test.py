import unittest
from src.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.puu = Trie()
        self.puu_korkeampi_aste = Trie(5)
        self.teksti1 = "Hei! Miten menee?! Kuka sinä olet?\r\nOlen pieni, punainen kissa, joka kiipesi puuhun."
        self.teksti2 = "Hei siellä! Miten on mennyt??\r\n Kuka muu siellä olisi?! Olen iso, musta kissa, joka lähti retkeilemään."

    def test_hae_puu_toimii_oikein(self):
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

    def test_lisaa_tekstia_palauttaa_true_kun_lisataan_uutta_tekstia(self):
        vastaus = self.puu.lisaa_tekstia(self.teksti1)

        self.assertEqual(vastaus, True)

    def test_lisaa_tekstia_lisaa_tekstin_oikein(self):
        self.puu.lisaa_tekstia(self.teksti1)
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {'hei': {}, 'miten': {'menee': {}}, 'kuka': {
                         'sinä': {'olet': {}}}, 'olen': {'pieni': {
                         'punainen': {}}}, 'pieni': {'punainen': {
                         'kissa': {}}}, 'punainen': {'kissa': {
                         'joka': {}}}, 'kissa': {'joka': {'kiipesi': {}}}, 'joka': {
                         'kiipesi': {'puuhun': {}}}})

    def test_lisaa_tekstia_lisaa_tekstin_oikein_korkeammalla_tallennuspituudella(self):
        self.puu_korkeampi_aste.lisaa_tekstia(self.teksti2)
        vastaus = self.puu_korkeampi_aste.hae_puu()

        self.assertEqual(vastaus, {'hei': {'siellä': {}}, 'miten': {'on': {
                         'mennyt': {}}}, 'kuka': {'muu': {'siellä': {
                         'olisi': {}}}}, 'olen': {'iso': {'musta': {'kissa': {
                         'joka': {}}}}}, 'iso': {'musta': {'kissa': {'joka': {
                         'lähti': {}}}}}, 'musta': {'kissa': {'joka': {'lähti': {
                         'retkeilemään': {}}}}}})

    def test_lisaa_tekstia_ei_lisaa_kaksoiskappaleita(self):
        self.puu.lisaa_tekstia(self.teksti1)
        self.puu.lisaa_tekstia(self.teksti1)
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {'hei': {}, 'miten': {'menee': {}}, 'kuka': {
                         'sinä': {'olet': {}}}, 'olen': {'pieni': {
                         'punainen': {}}}, 'pieni': {'punainen': {
                         'kissa': {}}}, 'punainen': {'kissa': {'joka': {}}}, 'kissa': {
                         'joka': {'kiipesi': {}}}, 'joka': {'kiipesi': {'puuhun': {}}}})

    def test_lisaa_tekstia_toimii_oikein_kun_teksteja_on_useampi(self):
        self.puu.lisaa_tekstia(self.teksti1)
        self.puu.lisaa_tekstia(self.teksti2)
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {'hei': {'siellä': {}}, 'miten': {'menee': {}, 'on': {
                         'mennyt': {}}}, 'kuka': {'sinä': {'olet': {}}, 'muu': {
                         'siellä': {}}}, 'olen': {'pieni': {'punainen': {}}, 'iso': {
                         'musta': {}}}, 'pieni': {'punainen': {'kissa': {}}}, 'punainen': {
                         'kissa': {'joka': {}}}, 'kissa': {'joka': {
                         'kiipesi': {}, 'lähti': {}}}, 'joka': {'kiipesi': {
                         'puuhun': {}}, 'lähti': {'retkeilemään': {}}}, 'muu': {'siellä': {
                         'olisi': {}}}, 'iso': {'musta': {'kissa': {}}}, 'musta': {
                         'kissa': {'joka': {}}}})

    def test_lisaa_tekstia_ei_lisaa_tyhjia_merkkijonoja(self):
        self.puu.lisaa_tekstia("")
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

    def test_lisaa_tekstia_ei_lisaa_pelkkia_valilyonteja(self):
        self.puu.lisaa_tekstia("        ")
        vastaus = self.puu.hae_puu()

        self.assertEqual(vastaus, {})

import unittest
from alipuu import alipuu_lauseesta, alipuu_sanasta

class TestAlipuu(unittest.TestCase):
    def setUp(self):
        pass

    def test_alipuu_sanasta_toimii_pelkalla_merkkijonolla(self):
        sana = 'Punainen'
        vastaus = alipuu_sanasta(sana)

        self.assertEqual(vastaus, {'Punainen': {}})

    def test_alipuu_sanasta_toimii_merkkijonolla_ja_listalla(self):
        sana = 'Punainen'
        lapset = {'kissa':{}, 'kuu': {}}
        vastaus = alipuu_sanasta(sana, lapset)

        self.assertEqual(vastaus, {'Punainen': {'kissa': {}, 'kuu': {}}})

    def test_alipuu_lauseesta_toimii_lauseella(self):
        lause = 'Punainen kissa juoksi kadun yli'
        vastaus = alipuu_lauseesta(lause)

        self.assertEqual(vastaus, {'Punainen': {'kissa': {'juoksi': {'kadun': {'yli': {}}}}}})
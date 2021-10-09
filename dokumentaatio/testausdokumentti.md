# Testausdokumentti

### Yksikkötestaus
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/Screenshot%20from%202021-10-09%2015-16-42.png)

Luokkia Trie ja TrieSolmu sekä tekstinkäsittelyfunktioita on testattu unittestillä. Testauksen saa aikaiseksi syöttämällä komentoriville `poetry run invoke test`.

Sen sijaan lauseita poimivaa algoritmia ollaan testattu lähinnä itse kirjoitetulla tekstillä, joka on kokoelma hyvin yksinkertaisia lauseita, ja joiden kanssa on helppoa tarkistaa, onko ohjelma tehnyt itse mitään uusia lauseita. Teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/yksinkertainen_teksti_1.md).

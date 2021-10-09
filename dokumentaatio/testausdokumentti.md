# Testausdokumentti

### Yksikkötestaus
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/Screenshot%20from%202021-10-09%2015-16-42.png)

Luokkia Trie ja TrieSolmu sekä tekstinkäsittelyfunktioita on testattu unittestillä. Testauksen saa aikaiseksi syöttämällä komentoriville `poetry run invoke test`.

## Lauseenpoiminta
Sen sijaan lauseita poimivaa algoritmia ollaan testattu lähinnä itse kirjoitetulla tekstillä, joka on kokoelma hyvin yksinkertaisia lauseita, ja joiden kanssa on helppoa tarkistaa, onko ohjelma tehnyt itse mitään uusia lauseita. Teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/yksinkertainen_teksti_1.md).
Lisäksi syötteenä ollaan käytetty [täältä](https://iltasatu.org/lue-selaimessa/?id=1637) löytyvää tekstiä, jota ollaan muokattu itse pelkästään niin, että kirjoitusvirheet ollaan poistettu. Korjattu ja syötteenä käytetty teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/adalmiinan_helmi.md).
Esimerkiksi jälkimmäinen teksti on tuottanut seuraavia tekstipätkiä, joita ei löydy alkuperäisestä tekstistä:
* Mummosta se oli täysin erilainen.
* Nousi kova meteli kun huomattiin että adalmina ei osannut.
* Kuljettuaan hän istahti erään metsälammen rannalle ja hänestä kasvoi kultatukkainen kaunotar. 
* Lahjan hyvän ja koska kyseessä oli kuninkaallinen lapsi kummeiksi saatiin kaksi höyhenenkevyttä poutapilveä. 

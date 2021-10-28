# Testausdokumentti

### Yksikkötestaus
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/testikattavuus_vko7.png)

Luokkia `Trie`, `TrieSolmu` ja `Lauseenmuodostus` sekä tekstinkäsittelyfunktioita `tekstin_siivous` on testattu unittestillä. Yllä oleva kuva on viimeisin testikattavuusraportti. Näin toteutetut testit ovat kattavia ja asiansa ajavia kaikkien muiden paitsi lauseenmuodostuksen osalta. Koska lauseenmuodostuksessa syntyvät lauseet ovat hyvin erilaisia, eikä etukäteen voi tietää, mitä tuloksena tulee, yksikkötestauksessa testattiin pelkästään sitä, että luokan funktiot ylipäätään toimivat ja palauttavat jotain oikein. 
Testauksen saa aikaiseksi syöttämällä komentoriville `poetry run invoke test`.

### Lauseenpoiminta
Lauseenmuodostuksen varsinainen testaus ollaan hoidettu manuaalisesti erilaisissa syötteillä, jotka löytyvät kansiosta [syotteet](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/tree/main/dokumentaatio/syotteet).
Syötteenä käytetty [yksinkertainen_teksti_1.md](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/yksinkertainen_teksti_1.md) on itse kirjoitettu, ja sitä ollaan käytetty lähinnä testauksen alkuvaiheissa.
Syötteenä käytetty 'Adalmiinan helmi' on satu, joka löytyy alun perin [täältä](https://iltasatu.org/lue-selaimessa/?id=1637). Tekstiä ollaan muokattu itse pelkästään niin, että kirjoitusvirheet ollaan poistettu. Korjattu ja syötteenä käytetty teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/adalmiinan_helmi.md).
Syötteenä on myös käytetty kokonaisuudessaan kirjaa 'Annan nuoruusvuodet', joka löytyy alun perin [täältä](https://www.gutenberg.org/cache/epub/49717/pg49717-images.html). Tekstiä ollaan muokattu itse pelkästään niin, että muutamat sisennykset ja lukujen numeroinnit ollaan poistettu. Tekstissä ilmeneviä satunnaisia erikoismerkkejä (esim. '@@') ei olla poistettu, sillä tekstinkäsittelyn pitää pystyä poistamaan ne. Syöte on myös sen verran valtava, että yksittäisten kirjoitusvirheiden korjaaminen vaikutti liian aikaavievältä, minkä takia niitä on saattanut jäädä mukaan. Muokattu ja syötteenä käytetty teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/annan_nuoruusvuodet.md)

Testaus ollaan siis tässä tapauksessa suoritettu pelkästään niin, että ollaan annettu eri tekstejä ja asetuksia ohjelmalle, esim. [herokussa](https://lausegeneraattori.herokuapp.com/) ja sitten katsottu, millaisia lauseita tuloksena syntyy.

Esimerkiksi syötteet 'Adalminan helmi' ja 'Annan nuoruusvuodet' ovat tuottaneet [täällä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/lauseenmuodostuksen_tuloksia.md) olevat lauseet. 
Kyseisten lauseiden perusteella huomataan, että mitä pienempi Markovin ketjun aste on, mitä suurempi syöte on, tai jos kaikkia lauseita ei muuteta omiksi virkkeikseen, sitä enemmän ohjelma tuottaa uusia lauseita. 
Mitä suurempi ketjun aste on, mitä suurempi syöte on, tai jos kaikkia lauseita ei muuteta omiksi virkkeikseen, sitä enemmän ohjelma tuottaa järkeviä lauseita.

# Viikkoraportti 4

Tällä viikolla tehtiin funktiot tekstin siistimiseen ja paloitteluun. Lisäksi tehtiin ohjelman tarkasteluun oma sivunsa, joka lisättiin herokuun, jotta ohjelman toiminnan tarkasteleminen kävisi helpommin. Sinne pääsee [täältä](https://lausegeneraattori.herokuapp.com/). Eli ollaan nyt alettu tarkemmin tarkastelemaan, mitä lauseita ohjelma saa aikaiseksi eri syötteillä - vai saako se aikaiseksi mitään.   

Testejä kirjoitettiin lisää, mutta ei lauseita poimivalle luokalle, sillä päätettiin hoitaa tämän testailu lähinnä käsin. Alla on nykyinen testikattavuus:
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/testikattavuus_vko4.png)

Lisäksi useita luokkia piti korjailla sieltä täältä, koska virheitä löytyi jatkuvasti.

Tunteja on tällä viikolla käytetty 13.

### Missä vaiheessa ollaan
Kasassa on nyt ohjelman ydintoiminta. Kaikki ei toimi tietenkään aivan virheettömästi, ja esimerkiksi lauseiden muodostuksessa syntyy välillä kummallisen lyhyitä lauseita silloinkin, kun pidempiäkin pitäisi mielestäni muodostua.

### Mitä opin
Opin lisää merkkijonojen muokkaamisesta ja sovelluksen pystyyn pistämisestä.

### Epäselvyyksiä
* Voisiko tekstin siistimisen ja pilkkomisen tehdä jotenkin tehokkaamminkin?
* Miksi lauseita poimiva algoritmi tekee välillä niin kummallisen lyhyitä lauseita?

### Ensi viikolla
* Aloitetaan suorituskykytestaus.
* Parannetaan e.m. algoritmia.
* Lisätään mahdollisuus opettaa, mitkä sanat aloittavat lauseen yms. ja katsotaan, millaisia lauseita sitten syntyy.

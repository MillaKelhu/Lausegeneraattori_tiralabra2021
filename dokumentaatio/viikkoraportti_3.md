# Viikkoraportti 3

Tällä viikolla kirjoitettiin aika paljon asioita uusiksi. Trielle tehtiin (toivottavasti) kunnollisempi tietorakenne, ja kirjoitettiin ainakin alustava algoritmi, joka etsii lauseita triestä. Testauksesta saatiin kattava vain trie- ja triesolmu-tietorakenteille, mutta testauksen tekeminen markovin ketjulle ehti jäädä täysin vaiheeseen, koska allekirjoittanut ei ole varma, miten se tehtäisiin järkevästi. Alla on testikattavuus: 
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/testikattavuus_vko3.png)

Tunteja on tällä viikolla käytetty 13.

### Missä vaiheessa ollaan
Kasassa on nyt trie-tietorakenne, joka toivottavasti ajaa asiansa loppukehityksen ajan, lukuun ottamatta pieniä muutoksia (esim. lauseen pilkkominen siirretään omalle funktiolleen). Lisäksi nyt on tehtynä algoritmi lauseen poimimiseen triestä. 

### Mitä opin
Opin lisää siitä, miten lauseita kannattaa trien ja Markovin ketjujen avulla muodostaa.

### Epäselvyyksiä
* Miten em. algoritmia kannattaisi testata? Syötteet ovat satunnaisia lukuun ottamatta sitä, että ne kaikki ovat merkkijonoja, mutta miten tätä voi testata mielekkäästi? Riittääkö testaamiseen se, että itse katsoo sen osaavan muodostaa lauseita?
* Kannattaako ennen mainittua itse tehtyä algoritmia edes käyttää, vai pitäisikö homma suorittaa jollain valmiiksi jostain löytyvällä algoritmilla?

### Ensi viikolla
* Tehdään käyttöliittymä, jolla tätä ohjelmaa pystyy itsekin paremmin tarkastelemaan.
* Hoidetaan testaus kuntoon.
* Tehdään joku oma luokka, joka käsittelee annetun tekstimassan sopiviksi pilkotuiksi kokonaisuuksiksi annettujen parametrien mukaan. Eli kokonaiset tekstit lauseiksi, lauseet halutun pituisiksi pätkiksi (2., 3., vai 4. asteen ketjut), erikoismerkit pois, yms.
* Jos jää aikaa, lisaa parametreja uudet lauseet muodostavalle algoritmille? Esim. vaihtoehto opettaa, että vain tietyt sanat aloittavat lauseen, tiettyjen sanojen jälkeen lause päättyy, jne.

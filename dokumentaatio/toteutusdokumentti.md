# Toteutusdokumentti

## Yleisrakenne
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/ohjelman_rakenne.png)

Ohjelman käyttöliittymästä vastaa tiedosto [`app.py`](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/app.py), joka löytyy juurihakemistosta. Kaikki ohjelman tietorakenteet ja funktiot kuitenkin löytyvät kansiosta [_src_](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/tree/main/src).

### Kansio src

#### `Trie` ja `Triesolmu`
Ohjelman tärkein tietorakenne on luokka [`Trie`](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/src/trie.py), joka perii luokan [`TrieSolmu`](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/src/triesolmu.py) ominaisuudet. Luokka `TrieSolmu` vastaa yhtä solmua triepuussa, ja sen kautta saadaan tietoon kyseisen solmun lapset (jotka on tallennettu sanakirjamuodossa) ja kyseiseen solmuun liitettävä laskuri, jota käytetään lauseenmuodostuksessa sanoja valittaessa, sillä sanat valitaan painotetuin todennäköisyyksin. `Trie` vastaa triepuuta. Sillä on heti luotaessa tyhjä juurisolmu, sekä annettu tallennuspituus, jonka mukaan tekstiä tallennetaan puuhun tietyn pituisina pätkinä. 

#### `Lauseenmuodostus`
Ohjelman toinen tärkeä luokka on [`Lauseenmuodostus`](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/src/lauseenmuodostus.py), jolle annetaan triepuu-olio, jonka luokka on e.m. `Trie`. Markovin ketjun aste otetaan automaattisesti triepuun tallennuspituudesta. 

#### Tekstinkäsittely
Lisäksi kansiossa on funktio [`tekstin_siivous`](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/src/tekstinkasittely.py), joka poistaa tekstistä erikoismerkit annettujen parametrien mukaan. Tätä tarvitaan tekstiä tallennettaessa triepuuhun.

## Aikavaativuus
Alla on pseudokoodi tekstin lisäämisestä. Tekstin siivouksne ja split:in aikavaativuudet ovat O(_m_) jossa _m_ = tekstin koko merkkeinä. Jos _v_ = virkkeiden lukumäärä, _n_ = virkkeessä olevien sanojen lukumäärä ja _k_ = n-tallennuspituus, aikavaativuus on parhaimmillaan O(_vn_) ja pahimmillaan O(_vnk_), O(_vnk_) < O(_vn_^2) koska tallennuspituus > 0:
```
function lisaa_tekstiä(teksti)
  siivottu = siivous(teksti)
  virkkeet = split(siivottu)
  for virke in virkkeet
    sanat = split(virke)
    if sanat != []
      n = length(sanat)
      if n <= tallennuspituus
        lisaa_sanoja(sanat, juuri)
      else
        for i=0 to n-tallennuspituus
          lisaa_sanoja(sanat[i, i+tallennuspituus], juuri)
  return True
```
Alla on pseudokoodi sanojen lisäämisestä, aikavaativuus on O(_n_) jossa _n_ = sanojen lukumäärä:
```
function lisaa_sanoja(sanat, solmu)
  sana = sanat[0]
  lapsi_lisatty = solmu.lisaa_lapsi(sana)
  if lapsi_lisatty = True and length(sanat) = 1
    return True
  if lapsi_lisatty = False and length(sanat) = 1
    return False
  sanat = sanat[1:]
  uusi_solmu = solmu.hae_lapsi(sana)
  return lisaa_sanoja(sanat, uusi_solmu)
```
Alla on pseudokoodi lapsen lisäämisestä, aikavaativuus on O(1): 
```
function lisaa_lapsi(sana)
  if sana not in lapset
    lapset[sana] = TrieSolmu
    return True
  else:
    return False
```
Alla on pseudokoodi lapsen hakemisesta, aikavaativuus on O(1):
```
function hae_lapsi(sana)
  if sana in lapset:
    return lapset[sana]
  else:
    return None
```
Alla on pseudokoodi lauseenmuodostuksesta. Solmun tyhjyyden tarkistamisen aikavaatimus on O(1), join on O(_n_) jossa _n_ = lause_merkkijonona pituus. Sanan valitsemisen aikavaativuus on pahimmillaan O(2_t_), jossa _t_ = triepuun kaikkien solmujen lukumäärä. Niinpä lauseenmuodostuksen aikavaativuus on O(2 _mt_) jossa _m_ on lauseen haluttu pituus sanoina:
```
function muodosta_lause(trie, pituus)
  lause = []
  solmu = trie
  lause_merkkijonona = ''
    if solmu.on_tyhja() is False
      for i=1 to pituus
        sana = valitse_sana(trie, lause)
        if sana is not None
          lause = lause + sana
        else
          break
      lause_merkkijonona = join(lause, ' ')
      lause_merkkijonona = upper(lause_merkkijonna[0]) + lause_merkkijonona[1:] + "."
  return lause_merkkijonona        
```
Alla on pseudokoodi sanan valitsemisesta. Randomin aikavaatimus on O(1), ja solmun hakemisen, ja solmun lasten todennäköisyyksien hakemisen aikavaativuus on O(_c_) jossa _c_ = kaikkien kyseisen solmun jälkeläisten määrä, ja tämähän saattaa vaihdella hyvinkin paljon. Jos triepuun koko (eli kaikkien solmujen määrä) on _t_, niin _c_=_t_ tai _c_ < _t_. Aikavaativuus on pahimmillaan siis O(2 _t_):
```
function valitse_sana(lause)
  solmu = trie
  n = minimum(markov_aste, length(lause))
  for i=n to 1 by -1
    sana = lause[-1]
    if solmu is not None
      solmu = solmu.hae_lapsi(sana)
    else
      break
      
  if solmu is not None
    lapset = solmu.hae_solmu()[1]
    if lapset is not empty
      painot = solmu.lasten_todennakoisyydet
      sana = random(lapset, painot)
      return sana
  return None
```
Alla on pseudokoodi solmun hakemisesta. Aikavaativuus on sama kuin laskurin päivityksellä alla:
```
function hae_solmu()
  paivita_laskuri()
  return laskuri, lapset
```
Alla on pseudokoodi solmun laskurin päivityksestä. Aikavaativuus on O(_c_) jossa _c_ = kaikkien solmun jälkeläisten määrä, eli lapset, näiden lapset, näiden lapset, jne.:
```
function paivita_laskuri()
  summa = 0
  for lapsi in lapset
    summa = summa + lapset[lapsi].hae_solmu()[0]
  laskuri = maximum(summa, laskuri)
```
Ohjelmaa suoritettaessa tehdään uusi triepuu, johon lisätään tekstiä, ja josta sitten etsitään lause. Aikavaativuus ohjelman suoritukselle on siis maksimissaan O(_vnk_) + O(2 _mt_), jossa _v_ = virkkeiden lukumäärä, _n_ = virkkeessä olevien sanojen lukumäärä ja _k_ = n-tallennuspituus, _t_ on trien kaikkien solmujen lukumäärä ja _m_ on generoitavan lauseen haluttu pituus.

## Esimerkkejä syntyneistä lauseista
Alla on esimerkkejä ohjelman tuottamista lauseista, jotka eivät ole suoria lainauksia syötemateriaalista.

### Adalmiinan helmi
* Hänen yksin kuului olla kaunis ja rikas ja hyväpäinen kunhan vain ymmärtää käyttää lahjojaan. 
* Viisaaksi adalmina kiukustui sillä vain hänen yksin kuului olla kaunis ja rikas ja hyväpäinen. 
* Jos jotakuta toista kehuttiin viisaaksi adalmina kiukustui sillä vain hänen yksin kuului olla kaunis. 
* Puutarhassa kauniin kukkasen hän rusensi sen sillä vain hänellä oli oikeus olla älykäs.
* Mitä merkitystä sydämellä on jos kerran adalminastamme tulee kaunis rikas ja hyväpäinen kunhan vain ymmärtää käyttää lahjojaan oikein. 

### Annan nuoruusvuodet
#### Markovin ketjun aste 2
##### Ei kaikkia lauseita virkkeiksi
* Veljeni mielellään haluaa enemmän. 
* Koetan kestää kaiken urhoollisesti kun vain annatte minun jäädä sanoi anna iloisesti. 
* Molemmat tytö olivat pahempia.
* Melkein joka ilta ennen maata menoaan oli hänen isänsä oli ostanut kankaan edellisenä kesänä kuljeksivalta kaupustelijalta koska se näytti ivan.
* Ajatella kaikkea josta täytyy ottaa rukoili anna itkien ääneen.
* Rouva ovat menneet mutta en silti koskaan unohda kuinka muhkeilta sähkövalo ja kukat ja naiset hienoissa puvuissaan näyttivät.

##### Kaikki lauseet virkkeiksi
* Tästä lähtien täytyy olla jollekin loukkaantunut. 
* Bell on lähettänyt meille suuren laatikon täynnä tavaraa. 
* Rakel rouva istui ikkunassaan ja seurasi häntä sisälle taloon. 
* Pye sai ensimäisen palkinnon kotona kirnutusta voista ja kotitekoisesta juustosta.
* Se on oma pieni sarkasi.

#### Markovin ketjun aste 3
##### Ei kaikkia lauseita virkkeiksi
* Sievästi hän sanoo että minun on mentävä kotiin neiti marilla cuthbertin luo. 
* Rouva allan on sanonut ettei ole oikeutta epäillä kenenkään ihmisen rehellisyyttä ennenkuin on varmat todisteet siitä että hän tulee tänne.


## Puutteet ja parannusehdotukset
* Aikavaatimusta tekstiä lisätessä voisi varmasti saada pienemmäksikin, mutta allekirjoittanut ei saanut tätä tehtyä ongelmitta.
* Käyttöliittymän saisi varmasti miellyttävämmäksikin.
* Suunnitelmista huolimatta ohjelmaan ei lisätty mahdollisuutta opettaa, millä sanoilla lauseet alkavat ja mihin ne päättyvät.

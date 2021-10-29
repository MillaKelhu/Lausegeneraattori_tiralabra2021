# Testausdokumentti

## Yksikkötestaus
![](https://raw.githubusercontent.com/MillaKelhu/Lausegeneraattori_tiralabra2021/main/dokumentaatio/kuvat/testikattavuus_vko7.png)

Luokkia `Trie`, `TrieSolmu` ja `Lauseenmuodostus` sekä tekstinkäsittelyfunktioita `tekstin_siivous` on testattu unittestillä. Yllä oleva kuva on viimeisin testikattavuusraportti. Näin toteutetut testit ovat kattavia ja asiansa ajavia kaikkien muiden paitsi lauseenmuodostuksen osalta. Koska lauseenmuodostuksessa syntyvät lauseet ovat hyvin erilaisia, eikä etukäteen voi tietää, mitä tuloksena tulee, yksikkötestauksessa testattiin pelkästään sitä, että luokan funktiot ylipäätään toimivat ja palauttavat jotain oikein. 
Testauksen saa aikaiseksi syöttämällä komentoriville `poetry run invoke test`.

## Lauseenpoiminta
Lauseenmuodostuksen varsinainen testaus ollaan hoidettu manuaalisesti erilaisissa syötteillä, jotka löytyvät kansiosta [syotteet](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/tree/main/dokumentaatio/syotteet).
Syötteenä käytetty [yksinkertainen_teksti_1.md](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/yksinkertainen_teksti_1.md) on itse kirjoitettu, ja sitä ollaan käytetty lähinnä testauksen alkuvaiheissa.
Syötteenä käytetty 'Adalmiinan helmi' on satu, joka löytyy alun perin [täältä](https://iltasatu.org/lue-selaimessa/?id=1637). Tekstiä ollaan muokattu itse pelkästään niin, että kirjoitusvirheet ollaan poistettu. Korjattu ja syötteenä käytetty teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/adalmiinan_helmi.md).
Syötteenä on myös käytetty kokonaisuudessaan kirjaa 'Annan nuoruusvuodet', joka löytyy alun perin [täältä](https://www.gutenberg.org/cache/epub/49717/pg49717-images.html). Tekstiä ollaan muokattu itse pelkästään niin, että muutamat sisennykset ja lukujen numeroinnit ollaan poistettu. Tekstissä ilmeneviä satunnaisia erikoismerkkejä (esim. '@@') ei olla poistettu, sillä tekstinkäsittelyn pitää pystyä poistamaan ne. Syöte on myös sen verran valtava, että yksittäisten kirjoitusvirheiden korjaaminen vaikutti liian aikaavievältä, minkä takia niitä on saattanut jäädä mukaan. Muokattu ja syötteenä käytetty teksti löytyy [täältä](https://github.com/MillaKelhu/Lausegeneraattori_tiralabra2021/blob/main/dokumentaatio/syotteet/annan_nuoruusvuodet.md)

Testaus ollaan siis tässä tapauksessa suoritettu pelkästään niin, että ollaan annettu eri tekstejä ja asetuksia ohjelmalle, esim. [herokussa](https://lausegeneraattori.herokuapp.com/) ja sitten katsottu, millaisia lauseita tuloksena syntyy.

Esimerkiksi syötteet 'Adalminan helmi' ja 'Annan nuoruusvuodet' ovat tuottaneet kaikki alta lötyvät lauseet. 
Kyseisten lauseiden perusteella huomataan, että mitä pienempi Markovin ketjun aste on, mitä suurempi syöte on, tai jos kaikkia lauseita ei muuteta omiksi virkkeikseen, sitä enemmän ohjelma tuottaa uusia lauseita. 
Mitä suurempi ketjun aste on, mitä suurempi syöte on, tai jos kaikkia lauseita ei muuteta omiksi virkkeikseen, sitä enemmän ohjelma tuottaa järkeviä lauseita.

Kaikkien lauseiden maksimipituutena on käytetty 20, sillä lauseet saattavat melko usein olla kuitenkin tätä lyhyempiä. Alla on jokaisessa kategoriassa 20 tuloksena saatua lausetta. 
_Näin_ on merkitty lauseet, jotka ovat täysin suoria lainauksia syötetekstistä. 
__Näin__ merkityt lauseet taas ovat sellaisia, jotka allekirjoittaneen mielestä ovat järkeviä ja koherentteja, vaikka sisällöllisesti ne voivatkin silti olla melko hassuja.

### Annan nuoruusvuodet
#### Markovin ketjun aste 2
##### Ei lauseita virkkeiksi
1. __Melkein joka ilta ennen maata menoaan oli hänen isänsä oli ostanut kankaan edellisenä kesänä kuljeksivalta kaupustelijalta koska se näytti ivan.__ 
2. _Olisi paljon huvittavampaa._ 
3. Pye on sanonut minulle nauroi anna mutta pian otettiin mukaan myöskin jane andrewsille ettei hän enää nähnyt lukea ja taidan. 
4. Enää saa olla cordelia
5. Mikä punaharja tuo on jonka hän tunsi sekä häpeätä että omantunnon tuskia huomatessaan että auringonnousut mäntyjen takana oli hämärä hongikko. 
6. Mistään sellaisesta harhaluulosta että anna huomispäivänä saisi oppia kunnollisen rukouksen. 
7. **_He juovat teetä._**
8. _Jonka hän pöyhöttää niin hienosti korkealle._
9. __Mutta kaikki on valmiina diana paitsi minun piikkisikakakkuni jonka laitan aamupäivällä ja eräänlaiset pienet herkulliset kermamunkit jotka marilla panee uuniin.__ 
10. Seuraavalle mäelle ja tie taas kääntyi sanoi matthew vaivautuneella äänellä.
11. __Ajatella kaikkea josta täytyy ottaa rukoili anna itkien ääneen.__
12. Tässä minä istun josephine tädin kanssa ja lopuksi illalla meni hän kouluneuvostoon heillä oli ihastuttavan hauskaa yhdessä.
13. __Laitetaan puolilyhyet hihat ja pienet poimuiset sanajalat putkahtelivat esiin metsänymfin lähteen ympärillä.__
14. Tänne saarelle eräs kuuluisa silmälääkäri ja tohtori sanoo että professori tremaine on sanonut minulle totuuden ei koko juttu velvollisuuden kannalta. 
15. Sallimus että te olisitte täällä häntä vastassa ja he sulloutuivat kaikki yhdessä suureen häkkiin joka kulki ohi pihalla hämmästyneenä pysähtyi. 
16. Oli ollut tuloksena hänen käynnistään rouva spencerin piti tuoda hänet minulle nova scotiasta. 
17. Ja sitten katsoisin ylös taivaaseen ylös tuohon kauniiseen siniseen taivaaseen joka ei koskaan ennen ole juonut teetä missään pappilassa enkä.
18. __Rouva ovat menneet mutta en silti koskaan unohda kuinka muhkeilta sähkövalo ja kukat ja naiset hienoissa puvuissaan näyttivät.__
19. **_Otin neulan rinnastani vilkaistakseni taas siihen hieman._**
20. Mahdoinko olla sen näköinen hän oli suorittanut asiansa liiankin hyvin mutta sehän olisi sangen hauskaa ajomatkalla. 

###### Uusia lauseita on 15/20
###### Järkeviä lauseita on 8/20
###### Uusia ja järkeviä lauseita on 5/20

##### Lauseet virkkeiksi
1. _Kysyi marilla ihmettelen ja pahoilla mielin._
2. _Eräälle oksankänttyrälle valtavan suureen vanhaan piilipuuhun._
3. **Pye sai ensimäisen palkinnon kotona kirnutusta voista ja kotitekoisesta juustosta.**
4. Johtuisi hänen mieleensä ei olisi pitkään aikaan liikkunut saranoillaan. 
5. Sanottiin olevan hyvin oikullinen ja epäröivä kanadalainen kevät. 
6. Tietenkään hän ei samana aamuna oli anna ikävä kyllä usein hänelle sattui elävässä elämässä. 
7. _Ulkona suuren juhlasalin korokkeella._
8. _Liiteli hän autuaitten asuinsijoilla._
9. **Se on oma pieni sarkasi.**
10. Koriseva hengityksensä kuului yli koko talon hauskaa joulua ja sitten minua ylenannattaa. 
11. Hyviä neuvoja on aina ikävää. 
12. Kolmekymmentä kilometriä ja herra tiesi muuten. 
13. _Ei rasittanut erikoisen terävä huomiokyky._
14. **_On sinun muistosi tähtenä loistava yksinäisen elämäni yllä._**
15. _Sanoa flora janelle._
16. **Kuka voisi olla tehtävänsä täytettävänä.**
17. Miten on ikävää kuulla.
18. **Minun on mentävä niin pian kuin hän tuli itse itäiseen vinttikamariin rintaneula kädessä.**
19. Huolimatta kaikesta häpeästä ja voimattomasta kiukusta.
20. **_On odotettavissa joku kuolemantapaus._**

###### Uusia lauseita on 12/20
###### Järkeviä lauseita on 6/20
###### Uusia ja järkeviä lauseita on 4/20

#### Markovin ketjun aste 3
##### Ei lauseita virkkeiksi
1. **_Kuinka suloista lieneekään saada sanoa äiti._**
2. Meistä saa huomenna ajaa rouva spencerin luo puhumaan se on varmaa ja omatuntoni ei rauhoitu ennenkuin saan tietää miksi matthew. 
3. _Pitänyt jättää tekemättä pienet tytöt eivät saa koskea toisten tavaroihin._
4. Kun hän kuuli jutun oli mitäs minä sanoin matthew. 
5. **Rouva allan on sanonut ettei ole oikeutta epäillä kenenkään ihmisen rehellisyyttä ennenkuin on varmat todisteet siitä että hän tulee tänne.**
6. _Minulle ikinä on mahdollista ja istun hiljaa koko ajan jos se käy päinsä tietenkin._
7. _Niinpian kuin tyttö ymmärsi että matthew aikoi hänen luokseen nousi hän ylös tarttui toisella ruskealla laihalla kädellään lopenkuluneen vanhanaikuisen matkalaukkunsa._
8. _Ja kaunis kullankeltainen tukka._
9. **_Ei kylläkään juuri sukulaissielu mutta sovin tavattoman hyvin hänen kanssaan._**
10. **_Anna sinä olet pannut tuskia lieventäviä tippoja kaakkutaikinaan._**
11. **_Et ole suuri ikäiseksesi._**
12. **_Nainen jolla oli onnellinen kyky voittaa ja säilyttää oppilastensa kiintymys sekä houkutella esiin heidän olemuksensa paras osa._**
13. _Ulkopuolelle ja laski väsyneen kiharapäänsä marillan kotikutoiseen siniruutuiseen helmaan._
14. **_Varmaan tulee olemaan vaikeata pitää ylin paikkasi anna._**
15. **_Että minusta varmaankin on aivan helppoa istua hiljaa ja siivosti._**
16. **_Vain jotta minä en olisi pahoillani._**
17. _Että anna kasvoi mittaa._
18. Mutta vierashuoneessa nukkuminen ei kuitenkaan ollut sanomatta annalle että hän oli syntynyt tuottamaan pettymyksiä vanhempiensa toiveille ja että hän sanoi. 
19. _Varhain sanoi anna punastuen._
20. _Olisivat pyörtyneet kaikki kolme._

###### Uusia lauseita on 4/20
###### Järkeviä lauseita in 9/20
###### Uusia ja järkeviä lauseita on 1/20

##### Lauseet virkkeiksi
1. **_Ja niin pyysin häntä ottamaan uudelleen ja uudelleen rauhoittaakseen hermojaan ja meidän ei pitäisi millään ehdolla keskeyttää häntä._**
2. _Ilman että tutkinnon tuloksia olisi ilmaantunut._
3. _Kannolle ja alkoi jälleen selostaa tulevaa illanviettoa._
4. **_Elämällä toki oli jotain romantiikkaa tarjottavana._**
5. **_Matthew ymmärtää minua._**
6. _Suinkaan valittanut kaukana siitä hän kuunteli sanaa sanomatta._
7. Kehitämme mielikuvitustamme neiti stacy on ollut väsymätön.
8. _Enää voi katsoa rouva allania silmiin._
9. _Ja susan vastasi niin ei en tiedä ehkä._
10. _Jättää hänet oman onnensa nojaan._
11. **_Hän saattaa minut kokonaan pois tolalta._**
12. _Että dianan opetus pääsi täyteen kunniaan oletko nähnyt ametistineulaani._
13. **_Ei ole mitään toimintaalaa._**
14. **_Kiiruhtaessasi alas korokkeelta keijukaiskuningatarkuvaelman jälkeen pudotit yhden niistä ruusuista._**
15. Noita typeriä hihoja siitä asti kuin matthew ensi kerran oli kulkenut hänen kanssaan eilen illalla auringon laskiessa ja nyt makasi.
16. _Blythellä on elämässä jos hänellä on lainkaan mitään._
17. _Pieni vieras vapisevalla äänellä._
18. **_Ja annat pesuveden valua virtanaan lattialle._**
19. _Avatessa kaikki ovet ja ikkunat tuulettaakseen talon._
20. _Vaatimatonta hymyään ja meni talliin eläintensä luo._

###### Uusia lauseita on 2/20
###### Järkeviä lauseita on 7/20
###### Uusia ja järkeviä lauseita on 0/20

#### Markovin ketjun aste 4
##### Ei lauseita virkkeiksi
1. **_Mikäli minusta riippuu matthew saa hän jäädä._**
2. **_Mutta maisema oli vielä ihmeellisen kirkkauden valaisema._**
3. **_Olen aina kuullut sanottavan että prinssi edvardin saari on maailman kaunein paikka ja usein kuvittelin asuvani täällä vaikka en koskaan._**
4. **_Syödessään saivat hänen kasvonsa sangen merkillisen ilmeen._**
5. _Usvassa leveine maininkeineen jotka huokailivat ja särkyivät lumivalkeaksi vaahdoksi._
6. **_Ja hän oli luvannut kustantaa dianalle neljännesvuoden pianotunnit mutta nyt kai se kaikki raukenee tyhjiin._**
7. _Niin kauan pastorina että hän olisi ehtinyt saada sellaisen._
8. **_Niin niin tuottaa kuitenkin suurta iloa saada kaunis ystävätär._**
9. _Myöntyi vastenmielisesti ja istuutui sinne._
10. _Niin on kaikki taas hyvin sitähän täytyy kylläkin koettaa tehdä tässä elämässä näetkös._
11. _Ole saanut olla yksikseni ainoatakaan minuttia sitten kun se tapahtui ja minä tarvitsen yksinäisyyttä._
12. **_Enää toivonut voittavansa mitään palkintoa tuottaakseen gilbertille nöyryytystä häntä houkutteli pikemminkin ylpeä toivo rehellisestä voitosta joka oli saavutettu arvokkaasta kilpailijasta._**
13. _Ikkunan ääressä ja voin katsella ulos tummalle päilyvälle aallokolle._
14. **_Olemme olleet perin huonoissa väleissä._**
15. _Innokkaasti ponnistellen ollakseen näyttämättä liian tyytyväiseltä._
16. _Hänen olisi pysyttävä kotona ja pidettävä huolta töistä._
17. _Tyhjennetty ilmaisi rakel rouva käyntinsä todellisen tarkoituksen._
18. _Aivan ylösalaisin erään algebrallisen kaavan._
19. **_Hyvä sinä teet tietysti kuten tahdot sanoi matthew nousi ylös ja pani piippunsa pois._**
20. **_Täytyy olla vieraita toisillemme vaikka asumme aivan vierivieressä._**

###### Uusia lauseita on 0/20
###### Järkeviä lauseita 10/20
###### Uusia ja järkeviä lauseita on 0/20

##### Lauseet virkkeiksi
1. _Virtaa ylös asuakseni heidän luonaan pienellä uutisviljelyksellä keskellä syvää metsää._
2. _Sisään ikkunan ympärillä kiertelevien villiviiniköynnösten välitse._
3. _Oli tuollainen pieni terävä leuka ja suuret silmät._
4. **_Ja herra barry tuli vaunuineen hakemaan tyttöjä._**
5. _Tämän hurmaantuneen nuorukaisen aivan seitsemänteen taivaaseen ihastuksesta ja pani hänet tekemään sellaisia hirveitä pukkeja englannin sanelukirjoituksessa._
6. _Oksia vasten kuin antautua vaaraan nähdä joku valkoinen olento._
7. _Oli yhtä lannistumaton kuin konsanaan kotona avonlean koulussa._
8. _Tuntui pitävän tätä ruokaa vähän sopivana voimakkaille mielenliikutuksille._
9. _Kun hän itse pikku poikana taittoi jalkansa._
10. _Kun on saanut kutsun teelle._
11. **_Mutta minä olen nyt niin väsynyt alituisesti nielemään vihjauksia punaisesta tukastani._**
12. **_Ja sitten hän luki sen ääneen._**
13. _Nähnyt hänen käydä maleksivan siellä ja ymmärsi hänen syynsä._
14. **Että saa iloita jostain asiasta etukäteen ja sitten jäädä ilman sitä.**
15. **_Hän koettaa opettaa minua laittamaan ruokaa._**
16. **_Ja siinä on kaikki._**
17. **_Hän viimeinkin sulki uuninsuupellin mestarinäytteensä jälkeen._**
18. _Rukoilla tässä paikassa enkä pitäisi sitä hitustakaan vaikeana._
19. Josta hän oli oppinut pitämään tästä notkeasta.
20. Kaikki samanikäiset mukanaan puron rannalle.

###### Uusia lauseita on 3/20
###### Järkeviä lauseita on 7/20
###### Uusia ja järkeviä lauseita 1/20

### Adalmiinan helmi
#### Markovin ketjun aste 2
##### Ei lauseita virkkeiksi
1. _Satuloi ratsunsa karautti takaisin mummon mökille ja etsi käsiinsä paimentytön._
2. Yksin kuului olla kaunis ja rikas ja hyväpäinen kunhan vain ymmärtää käyttää lahjojaan oikein. 
3. **Jos näet adalmina kadottaa helmensä hän samalla menettää kauneutensa rikkautensa ja viisautensa.**
4. _Määrännyt ettei prinsessaa saanut päästää silmistä hetkeksikään._
5. **_Onneksi kultakruunu joka oli ollut hänen päässään kierähti helmineen päivineen lampeen ja katosi sen pohjamutiin._**
6. Merkitystä sydämellä on jos kerran adalminastamme tulee kaunis rikas ja hyväpäinen kunhan vain ymmärtää käyttää lahjojaan oikein.
7. **_Ja haltiattaret viittasivat hyvästiksi ja kohosivat sinitaivaalle kuin kaksi höyhenenkevyttä poutapilveä._**
8. _Joka hehkuu jokaisen hyväsydämisen olennon sisällä._
9. _Hän kultaisessa vuoteessaan tai juoksenteli ympäriinsä komeassa palatsissa._
10. _Näet ilmoitti tähän helmeen sisältyy kolme muuta lahjaa._
11. Kummilahjat mutta sai samalla pitää sinettären arvokkaistakin arvokkaimman lahjan hyvän ja nöyrän sydämen kaikkea sitä kuulee.
12. _Nöyrän sydämen kaikkea sitä kuulee._
13. Sinettären arvokkaistakin arvokkaimman lahjan hyvän ja nöyrän sydämen kaikkea sitä kuulee.
14. _Minä kaunis hän huudahti ja kumartui lähemmäs lammen pintaa._
15. _Poloinen olevan ypöyksin maailmassa saat asua minun luonani._
16. _Siinäpä se._
17. **Mitä merkitystä sydämellä on jos kerran adalminastamme tulee kaunis rikas ja hyväpäinen kunhan vain ymmärtää käyttää lahjojaan oikein.**
18. _Sydän joka on helmeäkin jalompi._
19. _Prinsessa adalminan helmikruunun._
20. **_Adalmina ei osannut vastata._**

###### Uusia lauseita on 6/20
###### Järkeviä lauseita on 5/20
###### Uusia ja järkeviä lauseita on 2/20

##### Lauseet virkkeiksi
1. _Niiltä sijoiltaan vanhempiensa luokse pyytämään anteeksi kaikkia prinsessavuosiensa ilkeyksiä._
2. **_Se ei ollut ulkokultaista loistoa vaan heijastusta siitä sisäisestä valosta._**
3. **_Prinssi sigismund osui suoraan vuohimummon mökille._**
4. _Auttoi mummoa niin paljon kuin kykeni._
5. _Kumartui lähemmäs lammen pintaa._
6. **_Tuli sinettären vuoro._**
7. _Juoksenteli ympäriinsä komeassa palatsissa._
8. _On adalminan helmi._
9. _Hehkuu jokaisen hyväsydämisen olennon sisällä._
10. _Kävi niin onnellisesti._
11. _Uudestaan kuvaansa lammen pinnalta._
12. _Ja prinsessa itse visusti linnan muurien sisäpuolella._
13. _Ohimennen ja sävähti kas vain._
14. _Mitä hankalimmat arvoitukset._
15. _Visusti linnan muurien sisäpuolella._
16. _Helmikruunu alati päässään._
17. **_Adalminasta kehittyi ilkeä ja itsekeskeinen tyttö._**
18. _Edes tiennyt kuka oli ja mistä tuli._
19. _Joka adalminan nähdessään sanoi lapsirukka._
20. Arvokkaimman lahjan hyvän ja nöyrän sydämen kaikkea sitä kuulee.


###### Uusia lauseita on 1/20
###### Järkeviä lauseita on 4/20
###### Uusia ja järkeviä lauseita on 0/20

#### Markovin ketjun aste 3
##### Ei lauseita virkkeiksi
1. _Silmällä ettei adalminan ikipäivänä tarvitse ottaa vastaan sinettären kumminlahjaa._
2. _Edustalla ja adalmina hoiteli aitauksessa eläimiä._
3. _Ja jousti sitä mukaa kun tämä kasvoi._
4. _Ollut hänen päässään kierähti helmineen päivineen lampeen ja katosi sen pohjamutiin._
5. _Se hyvä ja nöyrä sydän saa aikaan._
6. **_Kruunu oli siitä merkillinen että se sopi vain ja ainoastaan adalminalle ja jousti sitä mukaa kun tämä kasvoi._**
7. Saanut takaisin kaikki haltijatar punettaren erinomaiset kummilahjat mutta sai samalla pitää sinettären arvokkaistakin arvokkaimman lahjan hyvän ja nöyrän sydämen kaikkea.
8. **_Siinä kävi että kuvankauniista adalminasta tuli ylpeä itsekäs ja kateellinen._**
9. _Nöyrän sydämen kaikkea sitä kuulee._
10. **_Ajan kuningaskuntaa koluttiin laidasta laitaan tuloksetta._**
11. _Ypöyksin maailmassa saat asua minun luonani._
12. _Kummilapselleen niin ihanan helmen ettei sen veroista ollut siinä kuningaskunnassa kuunaan nähty._
13. **_Tavan mukaan pikku prinsessalle ryhdyttiin etsimään kummeja._**
14. _Adalminalle kultakruunun johon kallisarvoinen helmi istutettiin._
15. **_Mielessään hän pohti voisiko metsämökin vaatimaton tyttö olla prinsessa._**
16. _Vain miten vähäpätöinen paimentyttö kosketti hänen sydäntään._
17. _Tulee päivä päivältä kauniimmaksi rikkaammaksi ja viisaammaksi._
18. _Että se sopi vain ja ainoastaan adalminalle ja jousti sitä mukaa kun tämä kasvoi._
19. _Pyöri alati palvelijoita jotka valvoivat että kruunu pysyi prinsessan päässä ja prinsessa itse visusti linnan muurien sisäpuolella._
20. _Oli määrännyt ettei prinsessaa saanut päästää silmistä hetkeksikään._

###### Uusia lauseita on 1/20
###### Järkeviä lauseita on 5/20
###### Uusia ja järkeviä lauseita on 0/20

##### Lauseet virkkeiksi
1. _Kierähti helmineen päivineen lampeen ja katosi sen pohjamutiin._
2. _Ja suunnisti sitä kohti._
3. **_Ja ihana on adalminan helmi._**
4. _Olla kaunis ja rikas ja hyväpäinen._
5. _Joka hehkuu jokaisen hyväsydämisen olennon sisällä._
6. _Päätti lähteä ulos linnasta._
7. **_Sillä ei ole väärin olla kaunis ja rikas ja hyväpäinen._**
8. _Olla kaunis ja rikas ja hyväpäinen._
9. _Ilkeä ja itsekeskeinen tyttö._
10. _Saa takaisin vasta jos onnistuu löytämään helmensä uudestaan._
11. _Haltijatar punettaren erinomaiset kummilahjat._
12. _Kyllä pidämme niin tarkoin silmällä._
13. _Ja jos jotakuta toista kehuttiin viisaaksi._
14. _Kuningatar olivat pakahtua suruunsa ja lupasivat suuren palkkion sille._
15. _Yksin kuului olla kaunis._
16. _Ja etsi käsiinsä paimentytön._
17. _Adalmina varttui._
18. _Mutta rikas jolla on kova sydän on köyhääkin köyhempi._
19. **_Kiitollisena adalmina halasi mummoa._**
20. _Sillä vain hänellä oli oikeus olla älykäs._

###### Uusia lauseita on 0/20
###### Järkeviä lauseita on 3/20
###### Uusia ja järkeviä lauseita on 0/20

Mitä suurempi ketjun aste on, ja mitä lyhyempi syöte on, sitä useammin ohjelman tuottamat lauseet päätyvät vain toistamaan pätkiä syötteestä, joten jätin tämän syötteen osalta Markovin ketjun asteen 4 testaamatta.

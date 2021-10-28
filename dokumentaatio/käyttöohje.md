# Käyttöohje

## Komentorivillä
Kun olet ladannut projektin, asenna ohjelman vaatimat riippuvuudet komennolla `poetry install`

Ohjelman saa suoritettua nettiselaimella komennolla `flask run`.

Ohjelmaa voi testata komennolla `poetry run invoke test`.

Ohjelman testikattavuus ja testikattavuusraportti saadaan aikaan komennoilla `poetry run invoke coverage` ja `poetry run invoke coverage-report`.
Tätä testikattavuusraporttia voidaan sitten tarkastella komennolla `firefox htmlcov/index.html`.

Raportin ohjelman koodin laadusta saa komennolla `poetry run invoke lint`.

## Itse ohjelman käyttö
Ohjelman voi joko käynnistää komentoriviltä, tai vaihtoehtoisesti [herokun kautta](https://lausegeneraattori.herokuapp.com/).

Anna tekstikenttään syötteenä tekstiä, ja valitse alla olevista asetuksista haluamasi. 

Kohdan 'Kaikki lauseet virkkeiksi' asetus 'Kyllä' muuttaa kaikki pilkut pisteiksi, ja 'Ei' poistaa pilkut kokonaan. Kohta 'Markovin ketjun aste' määrittää triepuun tallennuspituuden ja sen, miten lauseita muodostetaan. Kohta 'Lauseen maksimipituus' määrittää, montako sanaa muodostettavaan lauseeseen korkeintaan tulee, mutta lauseet voivat myös olla huomattavasti tätä lyhyempiä, jos joidenkin sanojen jälkeen uusia sanoja ei yksinkertaisesti ole tallennettuna. 

Painike 'Generoi lause' tuottaa lauseen annettujen syötteiden ja asetusten perusteella.

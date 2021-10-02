import string
import re

isot_valimerkit = ".?!"
valimerkit = string.punctuation
valimerkit = valimerkit.replace(".", "")

def tekstin_siivous(teksti: str, kaikki_lauseet_virkkeiksi: bool=False):
    """Funktio, joka siivoaa annetun tekstin erikoismerkeistä pisteitä lukuun ottamatta, ja muuttaa samalla kaikki isot kirjaimet pieniksi. Tämä on tekstin paloittelua ja trieen tallentamista varten.

    Args:
        teksti (str): Siivottava teksti merkkijonona.
        kaikki_lauseet_virkkeiksi (bool, vapaaehtoinen): Jos True, kaikki lauseet muutetaan omiksi virkkeikseen, eli kaikista pilkuista tulee pisteitä. Oletusarvona on False, eli pilkut vain poistetaan.

    Returns:
        str: Siivottu teksti merkkijonona.
    """

    teksti = teksti.replace("\n", " ")
    if kaikki_lauseet_virkkeiksi:
        for merkki in isot_valimerkit+",":
            teksti = teksti.replace(merkki, ".")
    else:
        for merkki in isot_valimerkit:
            teksti = teksti.replace(merkki, ".")
    teksti = re.sub("\.\.+", '.', teksti)
    for merkki in valimerkit:
        teksti = teksti.replace(merkki, "")
    teksti = teksti.lower()
    return teksti

def tekstin_paloittelu(teksti: str, markov_aste: int=3):
    """Paloittelee lauseet halutun mittaisiksi merkkijonopätkiksi, jotka voidaan sitten tallentaa triehen.

    Args:
        teksti (str): Paloiteltava teksti merkkijonona.
        markov_aste (int, vapaaehtoinen): Haluttu sanojen määrä yhdesä merkkijonopalassa. Oletusarvona on 3.

    Returns:
        list: Lista, jossa on teksti paloiteltuna halutun kokoisiksi merkkijonopaloiksi.
    """

    lauseet = []
    n = len(teksti)
    alku = [0]
    sanoja = 0
    
    for i in range(n):
        if alku[-1] < i:
            if teksti[i] == " " or teksti[i] == ".":
                alku.append(i+1)
                sanoja += 1
                if sanoja == markov_aste and teksti[i] == " ":
                    lauseen_alku = alku[0]
                    lauseet.append(teksti[lauseen_alku:i])
                    alku = alku[1:]
                    sanoja -= 1
                elif sanoja <= markov_aste and teksti[i] == ".":
                    lauseen_alku = alku[0]
                    lauseet.append(teksti[lauseen_alku:i])
                    alku = [i+2]
                    sanoja = 0
                    
    return lauseet

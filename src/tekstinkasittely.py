import string

isot_valimerkit = "?!"
valimerkit = string.punctuation
valimerkit = valimerkit.replace("$", "")

def tekstin_siivous(teksti: str, kaikki_lauseet_virkkeiksi: bool=False):
    """Funktio, joka siivoaa annetun tekstin erikoismerkeistä, erottelee virkkeet toisistaan merkillä '$' ja muuttaa samalla kaikki isot kirjaimet pieniksi. Tämä on tekstin trieen tallentamista varten.

    Args:
        teksti (str): Siivottava teksti merkkijonona.
        kaikki_lauseet_virkkeiksi (bool, vapaaehtoinen): Jos True, pilkkuja kohdellaan kuten pisteitä, ja kaikki sivu- ja päälauseet (mutta myös luettelot) muutetaan omiksi virkkeikseen. Oletusarvona on False, eli pilkut vain poistetaan eikä uusia virkkeitä synny.

    Returns:
        str: Siivottu teksti merkkijonona.
    """


    siivottu_teksti = teksti.replace("\n", " ")
    if kaikki_lauseet_virkkeiksi:
        for merkki in isot_valimerkit+",":
            siivottu_teksti = siivottu_teksti.replace(merkki, ".")
    else:
        for merkki in isot_valimerkit:
            siivottu_teksti = siivottu_teksti.replace(merkki, ".")
    siivottu_teksti = siivottu_teksti.replace(". ", "$")
    for merkki in valimerkit:
        siivottu_teksti = siivottu_teksti.replace(merkki, "")
    siivottu_teksti = siivottu_teksti.lower()
    return siivottu_teksti

def alipuu_lauseesta(lause:str):
        """Muuttaa lauseen sanakirja-muotoiseksi alipuuksi, joka voidaan liittää triehen. O(n), n = annetun merkkijonon pituus.

        Args:
            lause (str): Lause, joka halutaan muuttaa alipuuksi. Erikoismerkkien ja kirjainten välillä ei tällä hetkellä tehdä eroa.

        Returns:
            dict: Lauseesta muodostettu alipuu sanakirjana.
        """

        alipuu = {}
        loppu = len(lause)

        for i in range(len(lause), -1, -1):
            if lause[i-1] == " " or i==0:
                sana = lause[i:loppu]
                loppu = i-1
                sanan_alipuu = alipuu_sanasta(sana, alipuu)
                alipuu = sanan_alipuu

        return alipuu

def alipuu_sanasta(sana:str, lapset: dict={}):
    """Muodostaa alipuun sanasta.

    Args:
        sana (str): Solmun, josta alipuu alkaa, arvona oleva sana.
        lapset (dict, vapaaehtoinen): Solmun lapset. Oletusarvo on tyhjä sanakirja

    Returns:
        dict: [description]
    """

    alipuu = {}
    alipuu[sana] = lapset
    return alipuu

if __name__=="__main__":
    print(alipuu_sanasta(True, 'helouu'))
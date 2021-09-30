import string
import re

isot_valimerkit = ".?!"
valimerkit = string.punctuation
valimerkit = valimerkit.translate({ord(c): None for c in isot_valimerkit})

def tekstin_siivous(teksti: str, kaikki_lauseet_virkkeiksi: bool=False):
    teksti = teksti.replace("\n", " ")
    if kaikki_lauseet_virkkeiksi:
        teksti = teksti.translate({ord(c): "." for c in isot_valimerkit+","})
    else:
        teksti = teksti.translate({ord(c): "." for c in isot_valimerkit})
    teksti = teksti.translate({ord(c): None for c in valimerkit})
    teksti = re.sub("\.\.+", '.', teksti)
    teksti = teksti.lower()
    return teksti

def tekstin_paloittelu(teksti, markov_aste: int=3):
    lauseet = []
    n = len(teksti)
    alku = [0]
    loppu = []
    for i in range(n):
        if alku[-1] < i:
            if teksti[i] == " " or teksti[i] == ".":
                loppu.append(i)
                if teksti[i] == " ":
                    alku.append(i+1)
                elif teksti[i] == ".":
                    m = len(alku)
                    for j in range(m-markov_aste+1):
                        lauseen_alku = alku[j]
                        lauseen_loppu = loppu[j+markov_aste-1]
                        lauseet.append(teksti[lauseen_alku:lauseen_loppu])
                    if i != n:
                        alku = [i+2]
                        loppu = []
    return lauseet


if __name__ == "__main__":
    print(valimerkit)
    teksti = "Punainen kissa kiipesi puuhun, mutta kissa ei päässyt enää alas. Punaista kissaa pelotti!!\nMiten kissa tästä selviää?!?!?"
    siivottu = tekstin_siivous(teksti)
    print(siivottu)
    print(tekstin_paloittelu(siivottu))
    print(tekstin_paloittelu(siivottu, 2))
from flask import Flask, render_template, request
from src.trie import Trie
from src.lauseenmuodostus import Lauseenmuodostus

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    teksti = ""
    lauseet_virkkeiksi = False
    tallennuspituus = 3
    maksimipituus = 6

    lause = ""

    if request.method == "POST":
        teksti = request.form["teksti"]
        lauseet_virkkeiksi_str = request.form["lauseet_virkkeiksi"]
        tallennuspituus = int(request.form["markov_aste"])+1
        maksimipituus = int(request.form["pituus"])

        if lauseet_virkkeiksi_str == "True":
            lauseet_virkkeiksi = True
        else:
            lauseet_virkkeiksi = False
        
        trie = Trie(tallennuspituus)
        trie.lisaa_tekstia(teksti, lauseet_virkkeiksi)
        
        lauseenmuodostus = Lauseenmuodostus(trie)
        lause = lauseenmuodostus.muodosta_lause(maksimipituus)

        if lause == "":
            lause = "Anna tekstiä, jotta lauseita voidaan muodostaa."

    return render_template("index.html", teksti=teksti, lauseet_virkkeiksi=lauseet_virkkeiksi, markov=tallennuspituus-1, maksimipituus=maksimipituus, lause=lause)

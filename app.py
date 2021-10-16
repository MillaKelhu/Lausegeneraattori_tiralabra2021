from flask import Flask, render_template, request
from src.trie import Trie
from src.lauseenmuodostus import Lauseenmuodostus

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    teksti = ""
    lause = ""

    if request.method == "POST":
        teksti = request.form["teksti"]
        lauseet_virkkeiksi = request.form["lauseet_virkkeiksi"]
        tallennuspituus = int(request.form["markov_aste"])+1
        maksimi_pituus = int(request.form["pituus"])

        if lauseet_virkkeiksi == "True":
            lauseet_virkkeiksi = True
        else:
            lauseet_virkkeiksi = False
        
        trie = Trie()
        trie.lisaa_tekstia(teksti, tallennuspituus, lauseet_virkkeiksi)
        
        lauseenmuodostus = Lauseenmuodostus(trie)
        lause = lauseenmuodostus.muodosta_lause(maksimi_pituus)

        if lause == "":
            lause = "Anna tekstiä, jotta lauseita voidaan muodostaa."

    return render_template("index.html", teksti=teksti, lause=lause)

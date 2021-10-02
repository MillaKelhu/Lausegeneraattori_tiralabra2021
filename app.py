from flask import Flask, render_template, request
from src.tekstinkasittely import tekstin_siivous, tekstin_paloittelu
from src.triesolmu import TrieSolmu
from src.trie import Trie
from src.markov import Markov

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    lause = ""

    if request.method == "POST":
        teksti = request.form["teksti"]
        lauseet_virkkeiksi = request.form["lauseet_virkkeiksi"]
        markov_aste = int(request.form["markov_aste"])
        maksimi_pituus = int(request.form["pituus"])

        if lauseet_virkkeiksi == "True":
            lauseet_virkkeiksi = True
        else:
            lauseet_virkkeiksi = False

        teksti = tekstin_siivous(teksti, lauseet_virkkeiksi)
        lauseet = tekstin_paloittelu(teksti, markov_aste)
        trie = Trie()
        trie.lisaa_lauseita(lauseet)

        markov = Markov(trie)
        lause = markov.muodosta_lause(maksimi_pituus)

    return render_template("index.html", teksti=teksti, lause=lause)

from flask import Flask, render_template

app = Flask(__name__)

# Fotos do carrossel/galeria
PHOTOS = [
    {"file": "01_nos.jpg", "caption": "O nosso começo, do jeitinho que eu guardaria para sempre."},
    {"file": "02_nos.jpg", "caption": "Dois sorrisos, uma história e tantos momentos pela frente."},
    {"file": "03_nos.jpg", "caption": "Um dos nossos primeiros momentos juntos."},
    {"file": "04_momento.jpg", "caption": "Um carinho que virou memória."},
    {"file": "05_nossos_avatares.jpg", "caption": "Até no Roblox a nossa história encontrou um jeito de acontecer."},
    {"file": "06_nos.jpg", "caption": "Nós dois, simplesmente nós."},
    {"file": "07_nos.jpg", "caption": "Mais um pedacinho da nossa história."},
    {"file": "08_nos.jpg", "caption": "Que venham muitos outros capítulos."},
]

# Músicas com os IDs limpos do YouTube
SONGS = [
    {
        "title": "A música que ela ama 🤍",
        "youtube_id": "hda5v8tFM28"
    },
    {
        "title": "A nossa música ❤️",
        "youtube_id": "Szjx8Rw4UXo"
    }
]

@app.route("/")
def index():
    return render_template("index.html", photos=PHOTOS, songs=SONGS)

if __name__ == "__main__":
    app.run(debug=True)

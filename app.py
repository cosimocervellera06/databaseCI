import pymysql.cursors
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # Creare la connessione al DB
    conn = pymysql.connect(host='172.16.12.54', user='ospite',password='ospite',database='db5CI')

    # Creare un oggetto cursor
    cur = conn.cursor()

    # Creare la query
    sql = 'select * from alunni'

    # Eseguirla
    cur.execute(sql)

    # Recuperare il risultato
    result = cur.fetchall()

    # Manipolare il risultato e memorizzarlo in una lista di dizionari
    studenti = []
    for elem in result:
        studente = {
            "cognome": elem[0],
            "nome": elem[1],
            "datan": elem[2],
            "matricola": elem[3]
        }
        studenti.append(studente)

    # Chiudere la connessione
    cur.close()
    conn.close()

    # Stampa i dati degli studenti (per debug)
    for studente in studenti:
        print(f"Cognome: {studente['cognome']}, Nome: {studente['nome']}, Data di Nascita: {studente['datan']}, Matricola: {studente['matricola']}")

    return render_template("index.html", studenti=studenti)


app.run(debug=True)

from flask import Flask, render_template, url_for


import pymysql.cursors

conn = pymysql.connect(host='172.16.12.54',
    user='ospite',
    password='ospite',
    database='db5CI')

cur = conn.cursor()

app = Flask(__name__)

@app.route("/")
def root():
    sql = 'SELECT * FROM alunni'
    cur.execute(sql)
    result = cur.fetchall()
    return render_template("index.html", valori=result)

@app.route("/<studente>")
def voti(studente):
    sql = 'SELECT * FROM verifiche WHERE studente = %s'
    cur.execute(sql,(studente,))
    result = cur.fetchall()
    print(result)
    return render_template("voti.html",voti = result)

@app.route("/media")
def media():
    sql = 'SELECT cognome, nome, AVG(voto) FROM alunni,verifiche WHERE alunni.matricola=verifiche.studente GROUP BY cognome, nome;'
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    return render_template("media.html",media=result)

app.run(debug=True)
from flask import Flask, render_template, request
import random

def count():
    with open("/home/tomzizek/mysite/count.txt", "r") as file:
        num=str(1+int(file.read()))


    with open("/home/tomzizek/mysite/count.txt", "w") as file:
        file.write(num)
        print(num)

app = Flask(__name__)
@app.route('/play3', methods=['POST'])
def play3():
    monety = int(request.form['monety'])
    wez = int(request.form['wez'])
    monety -= int(request.form['coins'])
    modul = monety % (wez + 1)
    if monety<=0:
        count()
        return render_template("Wygrales.html")
    if modul == 0:
        bierz = random.randint(0, wez-1) + 1
    else:
        bierz = modul
    monety -= bierz
    if monety==1:
        say="Została jedna moneta"
    elif 1<monety%10<5 and not 11<monety%100<15:
        say="Zostały " +str(monety)+ " monety"
    else:
        say="Zostało "+str(monety)+ " monet"

    if monety<=0:
        return render_template("final_restart.html")
    if bierz==1:
        bierz="Bot wziął jedną monetę."
    elif bierz<5:
        bierz="Bot wziął " +str(bierz)+ " monety."
    else:
        bierz="Bot wziął "+ str(bierz)+ " monet."
    return render_template('final.html',say=say, monety=monety, wez=wez, bierz=bierz, max=(min(wez, monety)))
@app.route('/play2', methods=['POST'])
def play2():
    monety = int(request.form['monety'])
    wez = 6
    monety -= int(request.form['coins'])
    modul = monety % (wez + 1)
    if monety<=0:
        return render_template("inter2.html")
    if modul == 0:
        bierz = random.randint(1, 6)
    else:
        bierz = modul
    monety -= bierz
    if monety<=0:
        return render_template("tak_blisko.html")
    if monety==1:
        say="Została jedna moneta"
    elif 1<monety%10<5 and not 11<monety%100<15:
        say="Zostały " +str(monety)+ " monety"
    else:
        say="Zostało "+str(monety)+ " monet"

    if bierz==1:
        bierz="Bot wziął jedną monetę."
    elif bierz<5:
        bierz="Bot wziął " +str(bierz)+ " monety."
    else:
        bierz="Bot wziął "+ str(bierz)+ " monet."
    return render_template('go_to_2.html',say=say, monety=monety, bierz=bierz, max=(min(6, monety)))
@app.route('/play', methods=['POST'])
def play():
    monety = int(request.form['monety'])
    wez = 2
    monety -= int(request.form['coins'])
    modul = monety % (wez + 1)
    if monety<=0:
        return render_template("inter1.html")
    if modul == 0:
        bierz = random.randint(0, 1) + 1
    else:
        bierz = modul
    monety -= bierz
    if monety<=0:
        return render_template("result.html")

    if bierz==1:
        bierz="Bot wziął jedną monetę."
    elif bierz<5:
        bierz="Bot wziął " +str(bierz)+ " monety."
    else:
        bierz="Bot wziął "+ str(bierz)+ " monet."

    if monety==1:
        say="Została jedna moneta"
    elif 1<monety%10<5 and not 11<monety%100<15:
        say="Zostały " +str(monety)+ " monety"
    else:
        say="Zostało "+str(monety)+ " monet"

    return render_template('index.html', say=say, monety=monety, bierz=bierz, max=(min(6, monety)))

@app.route('/int1')
def int1():
    return render_template("go_to_2.html", monety=22, say="Zostały 22 monety")
@app.route('/int2')
def int2():
    wez = random.randint(8, 20)
    monety = ( 1 + wez ) * random.randint(5, 10) + random.randint(1, wez - 1)
    say = "Zostało " + str(monety) + " monet"
    return render_template("final.html", wez=wez, monety=monety, say=say)

@app.route('/')
def index():
    return render_template('Intro.html')
@app.route('/start')
def start():
    return render_template('index.html', monety=5, max=2, say="Zostało 5 monet")

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    return render_template('index.html', monety=5, max=2, say="Zostało 5 monet")
@app.route('/restart2', methods=['GET', 'POST'])
def restart2():
    return render_template("go_to_2.html", monety=22, say="Zostały 22 monety")
@app.route('/restart3', methods=['GET', 'POST'])
def restart3():
    wez = random.randint(8, 20)
    monety =  (1 + wez ) * random.randint(5, 10) + random.randint(1, wez - 1)
    say = "Zostało " + str(monety) + " monet"
    return render_template("final.html", wez=wez, monety=monety, say=say)

if __name__ == '__main__':
    app.run(debug=True)







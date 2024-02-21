from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def grade():
    
    kredi = str(request.form.get("kredi"))
    try:
        kredi = float(kredi)
    except ValueError:
        if kredi == "":
            kredi = 0
        else:
            return render_template("failure.html")
    ortalama = str(request.form.get("ortalama"))
    try:
        ortalama = float(ortalama)
    except ValueError:
        if ortalama == "":
            ortalama = 0
        else:
            return render_template("failure.html")
    if ortalama < 0 or ortalama > 4:
        return render_template("failure.html")
    if kredi < 0:
        return render_template("failure.html")
    toplam_not = float(kredi) * float(ortalama)
    toplam_kredi = float(kredi)

    notlar = [float(request.form.get(f"not{i}")) for i in range(1, 11)]
    eski_notlar = [float(request.form.get(f"eski_not{i}")) for i in range(1, 11)]
    daha_once = [float(request.form.get(f"daha_once{i}")) for i in range(1, 11)]
    krediler = [float(request.form.get(f"kredi{i}")) for i in range(1, 11)]

    for i in range(10):
        if daha_once[i] == 0:
            toplam_not += krediler[i] * notlar[i]
            toplam_kredi += krediler[i]
        elif daha_once[i] == 1:
            toplam_not += krediler[i] * notlar[i] - krediler[i] * eski_notlar[i]

    ort = toplam_not / toplam_kredi
    gpa = round(ort, 2)

    sinif = int(toplam_kredi / 30) + 1
    
    return render_template("grade.html", gpa=gpa, toplam_kredi=toplam_kredi, sınıf=sinif)
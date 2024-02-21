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
    not1 = float(request.form.get("not1"))
    not2 = float(request.form.get("not2"))
    not3 = float(request.form.get("not3"))
    not4 = float(request.form.get("not4"))
    not5 = float(request.form.get("not5"))
    not6 = float(request.form.get("not6"))
    not7 = float(request.form.get("not7"))
    not8 = float(request.form.get("not8"))
    not9 = float(request.form.get("not9"))
    not10 = float(request.form.get("not10"))
    eski_not1 = float(request.form.get("eski_not1"))
    eski_not2 = float(request.form.get("eski_not2"))
    eski_not3 = float(request.form.get("eski_not3"))
    eski_not4 = float(request.form.get("eski_not4"))
    eski_not5 = float(request.form.get("eski_not5"))
    eski_not6 = float(request.form.get("eski_not6"))
    eski_not7 = float(request.form.get("eski_not7"))
    eski_not8 = float(request.form.get("eski_not8"))
    eski_not9 = float(request.form.get("eski_not9"))
    eski_not10 = float(request.form.get("eski_not10"))
    daha_once1 = float(request.form.get("daha_once1"))
    daha_once2 = float(request.form.get("daha_once2"))
    daha_once3 = float(request.form.get("daha_once3"))
    daha_once4 = float(request.form.get("daha_once4"))
    daha_once5 = float(request.form.get("daha_once5"))
    daha_once6 = float(request.form.get("daha_once6"))
    daha_once7 = float(request.form.get("daha_once7"))
    daha_once8 = float(request.form.get("daha_once8"))
    daha_once9 = float(request.form.get("daha_once9"))
    daha_once10 = float(request.form.get("daha_once10"))
    kredi1 = float(request.form.get("kredi1"))
    kredi2 = float(request.form.get("kredi2"))
    kredi3 = float(request.form.get("kredi3"))
    kredi4 = float(request.form.get("kredi4"))
    kredi5 = float(request.form.get("kredi5"))
    kredi6 = float(request.form.get("kredi6"))
    kredi7 = float(request.form.get("kredi7"))
    kredi8 = float(request.form.get("kredi8"))
    kredi9 = float(request.form.get("kredi9"))
    kredi10 = float(request.form.get("kredi10"))
    if daha_once1 == 0:
        toplam_not += kredi1 * not1
        toplam_kredi += kredi1
    elif daha_once1 == 1:
        toplam_not += kredi1 * not1
        toplam_not -= kredi1 * eski_not1
        
    if daha_once2 == 0:
        toplam_not += kredi2 * not2
        toplam_kredi += kredi2
    elif daha_once2 == 1:
        toplam_not += kredi2 * not2
        toplam_not -= kredi2 * eski_not2
        
    if daha_once3 == 0:
        toplam_not += kredi3 * not3
        toplam_kredi += kredi3
    elif daha_once3 == 1:
        toplam_not += kredi3 * not3
        toplam_not -= kredi3 * eski_not3
        
    if daha_once4 == 0:
        toplam_not += kredi4 * not4
        toplam_kredi += kredi4
    elif daha_once4 == 1:
        toplam_not += kredi4 * not4
        toplam_not -= kredi4 * eski_not4
        
    if daha_once5 == 0:
        toplam_not += kredi5 * not5
        toplam_kredi += kredi5
    elif daha_once5 == 1:
        toplam_not += kredi5 * not5
        toplam_not -= kredi5 * eski_not5
        
    if daha_once6 == 0:
        toplam_not += kredi6 * not6
        toplam_kredi += kredi6
    elif daha_once6 == 1:
        toplam_not += kredi6 * not6
        toplam_not -= kredi6 * eski_not6
        
    if daha_once7 == 0:
        toplam_not += kredi7 * not7
        toplam_kredi += kredi7
    elif daha_once7 == 1:
        toplam_not += kredi7 * not7
        toplam_not -= kredi7 * eski_not7
        
    if daha_once8 == 0:
        toplam_not += kredi8 * not8
        toplam_kredi += kredi8
    elif daha_once8 == 1:
        toplam_not += kredi8 * not8
        toplam_not -= kredi8 * eski_not8
        
    if daha_once9 == 0:
        toplam_not += kredi9 * not9
        toplam_kredi += kredi9
    elif daha_once9 == 1:
        toplam_not += kredi9 * not9
        toplam_not -= kredi9 * eski_not9
        
    if daha_once10 == 0:
        toplam_not += kredi10 * not10
        toplam_kredi += kredi10
    elif daha_once10 == 1:
        toplam_not += kredi10 * not10
        toplam_not -= kredi10 * eski_not10
    
    ort = toplam_not / float(toplam_kredi)
    gpa = round(ort, 2)
    sınıf = int(toplam_kredi) / 30 + 1
    sınıf = int(sınıf)
    
    return render_template("grade.html", gpa=gpa, toplam_kredi=toplam_kredi, sınıf=sınıf)
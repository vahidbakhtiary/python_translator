from flask import Flask,render_template,request
from translator import french_to_english, english_to_french

app = Flask(__name__)

@app.route('/englishTofrench' , methods=["GET", "POST"])
def englishTofrench():
    title = "English to French Translation"

    if request.method == "POST":
        print(request.form["text"])
        text = request.form["text"]
        result = english_to_french(text)
        return render_template('English_To_French.html' , data=result)
    else:
        return render_template('English_To_French.html' , data="")


@app.route('/frenchToenglish' , methods=["GET", "POST"])
def frenchToenglish():
    title = "French to English Translation"

    if request.method == "POST":
        print(request.form["text"])
        text = request.form["text"]
        result = french_to_english(text)
        return render_template('French_To_English.html' , data=result )
    else:
        return render_template('French_To_English.html' , data="" )

  
 
app.run(host='localhost', port=8000 , debug=True)
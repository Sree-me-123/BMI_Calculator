from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = None
    color = None

    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        bmi = round(weight / ((height / 100) ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#f4c542"
        elif 18.5 <= bmi < 24.9: 
            category = "Normal"
            color = "#4CAF50"
        elif 24.9 <= bmi < 29.9: 
            category = "Overweight"
            color = "#ff9800" 
        else:
            category = "Obese"
            color = "#f44336" 

    return render_template("index.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=5001) 

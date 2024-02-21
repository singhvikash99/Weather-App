from flask import Flask, render_template, request, redirect, url_for
import utils

app = Flask(__name__)

@app.route ('/')
def index():
    return render_template("index.html")

@app.route ("/getweather/", methods=["POST"])
def weather_report():
    form_data = dict(request.form)
    city= form_data["lc"]
    res=utils.weather_data(city)
    return render_template("results.html", data=res)

@app.route('/redirect_home')
def redirect_home():
    return redirect(url_for('index'))


app.run(debug=True, host='0.0.0.0')
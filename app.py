from flask import Flask,jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
	return "Welcome to smartFarm- Precision Agriculture with fog computing!"

@app.route('/soil')
def soil_data():
	data = {
	"temperature":random.randint(20,35),
	"moisture":random.randint(30,80),
	"humidity":random.randint(40,90)
	}
	return jsonify(data)


@app.route('/alerts')
def alerts():
	soil_moisture = random.randint(20,80)
	if soil_moisture < 40:
		return " Slow mooisture is LOW!Star irrigation"
	else:
		return" Soil condition are good . no iriigation needed."

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)


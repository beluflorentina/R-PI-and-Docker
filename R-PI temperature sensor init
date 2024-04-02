from hdc2010 import *
from flask import Flask
from flask_restful import Api, Resource


hdc2010Reset()
hdc2010SetMeasurementsMode(HDC2010_TEMP_AND_HUMID)
hdc2010SetRate(HDC2010_ONE_HZ)
hdc2010SetTempRes(HDC2010_FOURTEEN_BIT)
hdc2010SetHumidRes(HDC2010_FOURTEEN_BIT)

hdc2010TriggerMeasurement()
hdc2010TriggerMeasurement()
sleep(5)

app=Flask(__name__)
api=Api(app)

class output(Resource):
	def get(self):
		lista=[]
		for _ in range(10):
			lista.append(round(hdc2010ReadTemp(), 4))
			sleep(1)
		return {"temperatura": lista}


api.add_resource(output, "/")

app.run(host="169.254.226.238", port=5000, debug=True)

from flask import Flask, render_template, request, redirect
from bokeh.embed import components
from bokeh.plotting import figure
import pandas as pd
import json
import os
import googlemaps
import pickle
from taxi_analysis import select_vals
import datetime



app = Flask(__name__)
GMAPS_KEY = os.getenv('GOOGLE_MAP')
app.CENTER = [40.6639206199602, -73.9383529238219]
app.LAT = (40.477399,40.917577)
app.LNG = (-74.25909, -73.700009)
app.SRC = "https://maps.googleapis.com/maps/api/js?key=" +GMAPS_KEY +"&callback=initMap"
#app.OPTIONS = [r"Open", r"Adj_Open", r"Close", r"Adj_Close"]
#app.NAMES = [s.replace("_",". ") for s in app.OPTIONS]
#app.div = []
#app.script = "

with open('pick.pickle', 'rb') as f:
	dfpick = pickle.load(f) 

with open('drop.pickle', 'rb') as f:
	dfdrop = pickle.load(f)

today = datetime.datetime.today()
month_def = str(today.month)
print month_def
day_def = str(today.weekday())
time_def = str(today.hour)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		

		lat_long = pd.read_csv("test_lat_lon.csv").dropna()
		#lat_list = json.dumps(str(lat_long.Lat.values[:10]).rstrip('\n'))
		#lng_list = json.dumps(str(lat_long.Long.values[:10]).rstrip('\n'))
		lat_list = [str(val).strip() for val in lat_long.Lat.values][:10]
		lng_list = [str(val).strip() for val in lat_long.Long.values][:10]
		#gmaps = googlemaps.Client(key = os.getenv('GOOGLE_MAP'))
		return render_template('index.html', src = app.SRC, center = app.CENTER,plot_lat = None,\
			plot_lng = None, month = month_def, day = day_def, time = time_def)
	if request.method == 'POST':
		month = int(request.form.get("month"))
		day = int(request.form.get("day"))
		time = int(request.form.get("time"))

		dfdropSEL = select_vals(dfdrop,(2015,2015),(month,month),(day,day),(time,time)).dropna(axis = 1)
		idx = pd.IndexSlice
		lats = [str(val).strip() for val in dfdropSEL.loc[idx[:,:,:,:],idx[:,"Lat"]].values[0]]
		lngs = [str(val).strip() for val in dfdropSEL.loc[idx[:,:,:,:],idx[:,"Long"]].values[0]]
		return render_template('index.html', src = app.SRC, center = app.CENTER,plot_lat = lats, plot_lng = lngs, \
			month = month, day = day, time = time)



		
		notValid, fig = make_html(ticker, options)
		app.script, app.div = components(fig)
		#output_file("test.html")

		
		'''
		TOOLS = "resize,crosshair,box_zoom,reset,box_select,save"
		output_file("test.html")
		fig=figure(title="Sensor data", tools = TOOLS)
		fig.line([1,2,3,4],[2,4,6,8])
		#global script
		#global div
		script, div=components(fig)
		'''

		if len(notValid) > 0:
			notValidstr = 'These are not valid tickers: ' + ', '.join(notValid)
		else:
			notValidstr = ""

		return render_template('plot.html', op = app.OPTIONS, names = app.NAMES,\
			script = app.script, div = json.dumps(app.div), notValid = notValidstr)



if __name__ == '__main__':
  app.run(debug = True, port = 5001)
  #app.run(port=33507)

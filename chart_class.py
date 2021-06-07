import justpy as jp
import pyrebase
import json
from Lib.FirebaseConnection import *

class DisplayChart:
    def __init__(self, chart_config, chart_d):
        self.labels = []
        self.values = []
        self.chart_config = chart_config
        self.chart_d = chart_d
    def getFirebaseDb(self):
        firebase = pyrebase.initialize_app(firebaseConfig)
        return firebase.database()

    def get_values(self):
        db = self.getFirebaseDb()
        data = db.child(self.chart_config['table']).get()
        data = data.val()
        keys = list(data.keys())
        
        for i in keys:
            self.labels.append(data[i][self.chart_config['key_label_name']])
        for i in keys:
            self.values.append((float((data[i][self.chart_config['key_values']])))*100)

    def app(self):
        self.get_values()
        wp = jp.QuasarPage()
        h1 = jp.QDiv(a=wp, text = 'Attentiveness of Student' , classes = 'text-h3 text-center q-a-md')
        p1 = jp.QDiv(a=wp, text = 'This graph represents the attentiveness of the student')
        hc = jp.HighCharts(a=wp, options = self.chart_d)
        hc.options.title.text = 'Attentiveness of User'
        hc.options.xAxis.title.text = 'Username'
        hc.options.yAxis.title.text = 'Attentiveness'
        hc.options.xAxis.categories = self.labels
        hc.options.series[0].data = self.values
        return wp

    def run(self):
        jp.justpy(self.app)



chart = DisplayChart(chart_attentive_user, chart_def)
chart.run()
import justpy as jp
import firebase_admin
from firebase import firebase

firebase = firebase.FirebaseApplication("https://watchbot-7f672-default-rtdb.firebaseio.com/", None)
data = firebase.get('/CLASS_ATTENTIVENESS', '')
users_keys = list(data.keys())
user_names = []
user_attentiveness = []
for i in users_keys:
    user_names.append(data[i]['USER_NAME'])
for i in users_keys:
    user_attentiveness.append(float((data[i]['ATTENTIVENESS'])))
print(user_attentiveness)


chart_def = """
{
    chart: {
        type: 'column'
    },
    title: {
        text: 'Attentiveness of students' 
    }
    xAxis: {
        categories: []
    },

    plotOptions: {
        series: {
            pointWidth: 20
        }
    },

    series: [{
        data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
    }]
}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = 'Analysis of Course Reviews' , classes = 'text-h3 text-center q-a-md')
    p1 = jp.QDiv(a=wp, text = 'These graphs represent course reviews analysis by month')
    my_chart = jp.HighCharts(a=wp, classes='m-2 p-2 border', style='width: 600px')
    my_chart.options = chart_def
    my_chart.options.xAxis.categories = user_names
    my_chart.options.series[0].data = user_attentiveness 
    return wp

jp.justpy(app)
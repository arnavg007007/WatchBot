import justpy as jp
import firebase_admin
from firebase import firebase

firebase = firebase.FirebaseApplication("https://watchbot-7f672-default-rtdb.firebaseio.com/", None)
data = firebase.get('/CLASS_ATTENTIVENESS', '')
users_keys = list(data.keys())
user_names = []
user_attentiveness = {}
for i in users_keys:
    user_names.append(data[i]['USER_NAME'])
for i in users_keys:
    user_attentiveness[data[i]['USER_NAME']]=(float((data[i]['ATTENTIVENESS'])))


chart_def = '''
{
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#ede3c7'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit '
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' '
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Attentiveness',
        data: []
    }]
}
'''
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = 'Attentiveness of Student' , classes = 'text-h3 text-center q-a-md')
    p1 = jp.QDiv(a=wp, text = 'This graph represents the attentiveness of the student')
    hc = jp.HighCharts(a=wp, options = chart_def)
    hc.options.title.text = 'Attentiveness of User'
    hc.options.xAxis.title.text = ''
    hc.options.yAxis.title.text = 'Attentiveness'
    hc.options.xAxis.categories = ['Username'] 
    hc_data = [{'name':v1, 'data': [user_attentiveness[v1]]}for v1 in user_names]
    hc.options.series = hc_data
    return wp

jp.justpy(app)
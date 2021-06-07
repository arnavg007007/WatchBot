import justpy as jp
# import firebase_admin
# from firebase import firebase
import pyrebase


firebaseConfig = {
    "apiKey" : "AIzaSyAOwwClW1BhGAJkbnEBEyo_hCv8D9niCsM",
    "authDomain" : "watchbot-7f672.firebaseapp.com",
    "databaseURL" : "https://watchbot-7f672-default-rtdb.firebaseio.com",
    "projectId" : "watchbot-7f672",
    "storageBucket" : "watchbot-7f672.appspot.com",
    "messagingSenderId" : "872186790864",
    "appId" : "1:872186790864:web:50ecb9e9303a5c66fd2fd5"
    }
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
            color: 'rgba(255,255,255, .2)'
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
#firebase = firebase.FirebaseApplication("https://watchbot-7f672-default-rtdb.firebaseio.com/", None)
#data = firebase.get('/CLASS_ATTENTIVENESS', '')

user_names = []
user_attentiveness = []

def getFirebaseDb():
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase.database()

def get_values():
    db = getFirebaseDb()
    data = db.child("CLASS_ATTENTIVENESS").get()
    data = data.val()
    users_keys = list(data.keys())
    
    for i in users_keys:
        user_names.append(data[i]['USER_NAME'])
    for i in users_keys:
        user_attentiveness.append(float((data[i]['ATTENTIVENESS'])))

def app():
    get_values()
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text = 'Attentiveness of Student' , classes = 'text-h3 text-center q-a-md')
    p1 = jp.QDiv(a=wp, text = 'This graph represents the attentiveness of the student')
    hc = jp.HighCharts(a=wp, options = chart_def)
    hc.options.title.text = 'Attentiveness of User'
    hc.options.xAxis.title.text = 'Username'
    hc.options.yAxis.title.text = 'Attentiveness'
    hc.options.xAxis.categories = user_names 
    hc.options.series[0].data = user_attentiveness
    return wp

jp.justpy(app)
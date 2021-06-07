from pyasn1.type import char
import pyrebase
import json

firebaseConfig = {
    "apiKey" : "AIzaSyAOwwClW1BhGAJkbnEBEyo_hCv8D9niCsM",
    "authDomain" : "watchbot-7f672.firebaseapp.com",
    "databaseURL" : "https://watchbot-7f672-default-rtdb.firebaseio.com",
    "projectId" : "watchbot-7f672",
    "storageBucket" : "watchbot-7f672.appspot.com",
    "messagingSenderId" : "872186790864",
    "appId" : "1:872186790864:web:50ecb9e9303a5c66fd2fd5"
    }

def getFirebaseDb():
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase.database()
    
chart_attentive_user ={
            "table": "CLASS_ATTENTIVENESS",
            "key_label_name": "USER_NAME",
            "key_values": "ATTENTIVENESS"
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



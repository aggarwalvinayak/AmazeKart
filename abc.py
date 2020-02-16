
import requests 
import json
# resp=requests.get('http://127.0.0.1:8000/api/userdatabase/')
# print(resp.text)
task={

    	"password":"asdfj",
        "name": "Python data",
        "email": "f20170008@bits-pilani.ac.in",
        "date": "2019-11-12"
    }
resp = requests.post('http://127.0.0.1:8000/mainapp/loginapi/', data=json.dumps(task))

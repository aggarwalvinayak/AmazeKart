
import requests 
import json
# resp=requests.get('http://127.0.0.1:8000/api/userdatabase/')
# print(resp.text)
task={
    	"password":"roots123",
        "name": "Python data",
        "email": "f20170118@goa.bits-pilani.ac.in",
        "date": "2019-11-12",
    }
resp = requests.post('http://127.0.0.1:8000/mainapp/loginapi/', data=json.dumps(task))

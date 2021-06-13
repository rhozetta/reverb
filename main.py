from flask import Flask, request, jsonify, abort
import socket
import json
import voice

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    with open("pages/index.html", "r") as output:
        output = str(output.read())

        output = output.replace("<<IP GOES HERE>>", socket.gethostbyname(socket.gethostname()))
        
        return output

@app.route('/settings/trigger',methods=['GET','POST'])
def triggerSetting():

    with open("pages/settingsTrigger.html", "r") as output:
        output = str(output.read())

        output = output.replace("<<IP GOES HERE>>", socket.gethostbyname(socket.gethostname()))

        with open("config/trigger.json", "r") as oldTrigger:
            oldTrigger = oldTrigger.read()
            oldTrigger = oldTrigger.replace('"', '')
                
            output = output.replace('<<OLD TRIGGER GOES HERE>>', f'{oldTrigger}')
    
    if request.method == 'GET':
        return output
    else:
        with open("config/trigger.json", "w") as trigger:
            newTrigger = request.form
            
            trigger.write(json.dumps(newTrigger['content']))

            output = output.replace(oldTrigger, newTrigger['content'])

            return output

if __name__ == "__main__":  # Makes sure this is the main process
  app.run( # Starts the site
        host='0.0.0.0',  # Establishes the host, required for repl to detect the site
        port=5000  # select the port the machine hosts on.
    )
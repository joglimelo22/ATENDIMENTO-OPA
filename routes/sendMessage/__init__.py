from flask import Blueprint, render_template, request, send_file
from werkzeug.utils import secure_filename
from modules.opa import OPA
import os
import csv
import io

sendMessage_blueprint = Blueprint("sendMessage", __name__)

def allowedFile(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@sendMessage_blueprint.post("/send-message")
def sendMessage():

    email = request.form['email']
    password = request.form['password']

    if 'file' not in request.files:
        return render_template("home.html", error="Porfavor, envie um arquivo com os nomes e numeros dos clientes!")
    
    file = request.files['file']
    
    if file and not allowedFile(file.filename):
        return render_template("home.html", error="Porfavor, o arquivo tem que ser enviado no formato CSV!")

    filename = secure_filename(file.filename)
    upFolder = os.path.join(os.getcwd(), 'static', 'files')
    file.save(os.path.join(upFolder, filename))

    listNumbers = []

    with open(f'{upFolder}/{filename}', mode='r', encoding='utf-8') as csvFile:
        csvRender = csv.DictReader(csvFile)
        for item in csvRender:
            listNumbers.append(item)

    opa = OPA()
    resultLogin = opa.login(email, password)

    if(resultLogin['status'] == 400):
        return render_template("home.html", error=resultLogin['message'])

    logs = []

    for number in listNumbers:
        newAtt = opa.openAtt(number['number'], number['name'])
        if newAtt['status'] == 200:
            logs.append(f'SUCESSO: O atendimento do numero {number['number']} com o nome da cliente {number['name']} foi aberto com sucesso')
        else:
            logs.append(f'ERRO: O atendimento do numero {number['number']} com o nome da cliente {number['name']} ocorreu um erro, Erro: {newAtt['message']}')
    
    logString = '\n'.join(logs)
    bufferArchives = io.BytesIO()
    bufferArchives.write(logString.encode('utf-8'))
    bufferArchives.seek(0)

    os.remove(f'{upFolder}/{filename}')


    return send_file(bufferArchives, as_attachment=True, mimetype='text/plan', download_name='logs.txt')
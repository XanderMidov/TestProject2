from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<param>')
def content(param):
    if param == 'button_1':
        content = 'Jopa vonuchaya'
    elif param == 'button_2':
        content = 'Jopa ebuchaya'
    elif param == 'button_3':
        content = 'Anal'
    elif param == 'button_4':
        content = directory_list()
    return render_template('index.html', content=content)

def directory_list():
    content = ''
    path = r'H:\Книги Активные'
    for dirpath, subdirs, files in os.walk(path):
        for file in files:
            content += dirpath + '\\' + file + '\n'
    return content

app.run(debug=True)

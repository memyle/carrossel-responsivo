from flask import Flask, render_template, request
import os;
from werkzeug.utils import secure_filename
app = Flask(__name__, template_folder='templates')
app.static_folder = 'static'
UPLOAD_FOLDER = os.path.join(os.getcwd(),'static/imagens')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    return render_template('upload.html')


@app.route('/result', methods=['GET','POST'])
def result():
    file = request.files['imagem']
    savePath= os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return render_template("result.html")

@app.route("/gallery")
def gallery():
    imageList = os.listdir('static/imagens')
    imagelist = ['imagens/' + image for image in imageList]
    return render_template("gallery.html", imagelist=imagelist)

app.run()
if __name__ == '__main__':
    app.run(debug=True)
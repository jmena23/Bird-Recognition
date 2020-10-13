from src.app import app
from src.predict import predict
from flask import request, render_template, redirect
import os
import glob
from werkzeug.utils import secure_filename

@app.route("/")
def index():
    return render_template("index.html")

app.config["IMAGE_UPLOADS"] = "./src/static/images/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPG", "PNG", "JPEG"]

def allowed_image(filename):

    if not "." in filename:
        return False
    
    extension = filename.rsplit(".", 1)[1]

    if extension.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/upload_image", methods = ["POST", "GET"])
def upload_image():

    if request.method == "POST":

        if request.files:

            image = request.files["filename"]

            if image.filename == "":
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                return {
                    "ERROR - EXTENSION DE IMAGEN NO PERMITIDA" : "Elija una imagen con extension permitida (jpg, png, jpeg)"
                }

            filename = secure_filename(image.filename)
            
            filename = "0.jpg"

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            file_image = "./src/static/images/uploads/" + filename
            prediction = predict(file_image)
            
            return {
                "Con una alta probabilidad el pajaro que se encuentra en la imagen es un" : prediction.upper()
            }
    
    return render_template("index.html")


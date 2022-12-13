import numpy as np
from tensorflow.keras.utils import load_img, img_to_array
from keras.models import load_model

def predict(file):

    modelo = "./modelo/modelo_3caps_100epochs_DropoutProg_4class.h5"
    pesos = "./modelo/pesos_3capas_100epochs_DropoutProg_4class.h5"
    model = load_model(modelo)
    model.load_weights(pesos)

    altura, longitud = 50, 50

    x = load_img(file, target_size = (altura, longitud))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    predict = model.predict(x)
    resultado = predict[0]
    #print(resultado)
    respuesta = np.argmax(resultado)
    posibilidades = {0:"Carpintero", 1: "Charran", 2: "Colibri", 3:"Curruca"}
    for k in posibilidades.keys():
        if k == respuesta:
            return posibilidades[k]
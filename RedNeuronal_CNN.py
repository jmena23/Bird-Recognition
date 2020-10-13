import os
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Activation
from keras.layers import Conv2D, MaxPooling2D

## CARGA DE DATOS (IMAGENES)

data_entrenamiento = "./data/entrenamiento"
data_validacion = "./data/validacion"

## PARÁMETROS

epocas = 100
altura, longitud = 50, 50
batch_size = 64
filtrosConv1 = 32
filtrosConv2 = 64
tamano_filtro1 = (3, 3)
tamano_filtro2 = (2, 2)
tamano_pool = (2, 2)
clases = 4
lr = 0.001

## PRE-PROCESAMIENTO DE IMÁGENES

datagen_entrenamiento = ImageDataGenerator(rescale = 1./255, 
                                           shear_range = 0.3, 
                                           zoom_range = 0.3, 
                                           horizontal_flip = True)

datagen_validacion = ImageDataGenerator(rescale = 1./255)

imagen_entrenamiento = datagen_entrenamiento.flow_from_directory(data_entrenamiento, 
                                                                target_size = (altura, longitud), 
                                                                batch_size = batch_size, 
                                                                class_mode = "categorical")

imagen_validacion = datagen_validacion.flow_from_directory(data_validacion, 
                                                                target_size = (altura, longitud), 
                                                                batch_size = batch_size, 
                                                                class_mode = "categorical")

## RED NEURONAL CNN

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(altura, longitud, 3)))
model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.3))
model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.4))
model.add(Flatten())
model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
model.add(Dropout(0.5))
model.add(Dense(clases, activation='softmax'))

model.summary()

opt = optimizers.Adam(lr=lr)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

historico = model.fit(imagen_entrenamiento, epochs = epocas, validation_data = imagen_validacion)

directorio = "./modelo/"

if not os.path.exists(directorio):
    os.mkdir(directorio)

model.save("./modelo/modelo_3caps_100epochs_DropoutProg_4class.h5")
model.save_weights("./modelo/pesos_3capas_100epochs_DropoutProg_4class.h5")

## VISUALIZACIÓN DE MÉTRICAS

acc = historico.history["accuracy"]
loss = historico.history["loss"]
val_acc = historico.history["val_accuracy"]
val_loss = historico.history["val_loss"]
epocas = range(len(acc))

plt.plot(epocas, acc, label = "acc")
plt.plot(epocas, loss, label = "loss")
plt.title("Diagrama Training ACCURACY vs LOSS")
plt.xlabel("epochs")
plt.legend()
plt.figure()
plt.plot(epocas, val_acc, label = "val_acc")
plt.plot(epocas, val_loss, label = "val_loss")
plt.title("Diagrama Validation ACCURACY vs LOSS")
plt.xlabel("epochs")
plt.legend()
plt.show()


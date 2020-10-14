# Bird-Recognition
PROYECTO FINAL Ironhack - Bootcamp Data Analytics: Bird Recognition

![ornitologo-observando-aves-exoticas-1024x684](https://user-images.githubusercontent.com/61025562/96011751-3cbfe380-0e3b-11eb-9a93-749d04fcb9ba.jpg)

## Descripción del proyecto

La idea principal de **Bird Recognition** es la de entrenar una red neuronal que reconozca la especie de pájaro que hay en una foto. Adicionalmente y para que sea más interactivo, se ha implementado una API donde puedes subir una foto de un pájaro y te devuelve la especie de pájaro que se encuentra en la imagen.

## Metodología

Los pasos seguidos para el desarrollo del proyecto han sido los siguientes:

- Elaboración del dataset mediante la recolección de imágenes de las distintas especies (1000 imágenes de 4 especies distintas)

- Elaboración y entrenamiento de una Red Neuronal Convolucional 2D que reconozca la especie de pájaro que hay en la imagen.

- Creación de una API donde puedas subir una imagen y te devuelva el pájaro que hay en ella.

## Red Neuronal Convolucional 2D (CNN)

El modelo de red neuronal y su entrenamiento lo puedes ver en el archivo **RedNeuronal_CNN.py**. 

Los resultados obtenidos se muestran a continuación:

    - Training-Accuracy: 95.83
    - Training-Loss: 0.12

    - Validation-Accuracy: 84.31
    - Validation-Loss: 0.64

![training](https://user-images.githubusercontent.com/61025562/96015272-4f3c1c00-0e3f-11eb-98e6-8e198aa696c2.png)

![validacion](https://user-images.githubusercontent.com/61025562/96015312-59f6b100-0e3f-11eb-825b-60c5d7bc4073.png)

## API

La API ha sido desarrollada con Flask y Python. 

Actualmente, sólo funciona en local. Puedes descargar el código y probarlo en tu equipo corriendo desde la terminal el archivo **server.py**

## Próximos Pasos ...

- Añadir más especies de pájaros

    - Actualmente están disponibles: carpintero, charrán, colibrí y curruca.

- Mejorar la precisión del modelo aumentando el dataset de imágenes de cada especie

- Subir la aplicación a la web.

## Enlaces de interés

- https://flask.palletsprojects.com/

- https://www.getpostman.com/

- https://www.aprendemachinelearning.com/como-funcionan-las-convolutional-neural-networks-vision-por-ordenador/

- https://machinelearningmastery.com/how-to-develop-a-cnn-from-scratch-for-cifar-10-photo-classification/


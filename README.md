# Object Detector Turi

Python scripts using Turi library.

# Seccion Uno
## 1. Start Python environment

Acceder ***(usando comando "cd")*** hasta directorio donde se encuantre el archivo ***bin***, luego usar comando: ***source bin/activate.***
Una vez activado el ambiente se puede entrar a cualquier directorio


## 1.1 Open Text Editor

 Abrir el directorio que contiene los scripts en cualquier editor de texto, ***cmd + o***.
 
 
# Seccion dos 
 *Nota: jsons_folder, save_dir, img_dir, dir_frame, etc. son las unicas variables que se deben modificar, todas unicamente especifican la direccion en donde se encuentra el archivo o carpeta a utilizar.*
 *Cuando se pase un directorio, no poner '/' al final.*
 *Exm(correcto): desktop/carpeta
 *Exm(incorrecto): desktop/carpeta/

## 2. Join Annotations
 
### *join_annotations.py*
Si existen ***annotations (json)*** individuales que se quieran consolidar en uno solo. *"join_annotations.py"* une los jsons individuales y crea un solo json que contiene a todos.
 
 ### jsons_folder = pasar la direccion de la carpeta en donde se encuentran los jsons individuales
 Exm: 'desktop/carpeta_jsons_individuales'
 ### save_dir: directorio en donde se quiere guardar el archivo json consolidado
 Exm: 'desktop/carpeta_json_consolidado' 
 
 
 ## 3. Get SFrame
 
 ### *json_sframe.py*
 Convertir annotations (json format) a sframe (estructura requerida por Turi).
 ### img_dir = direccion a la carpeta que contiene todas la imagenes
 Exm: 'desktop/dolar_images'
 ### json_file_dir = direccion al archivo json consolidado
 Exm: 'desktop/annotations.json'
 ### save_dir = direccion en donde la carpeta sframe sera guardada
 Exm: 'desktop/sframe_folder'
 
 
 ## 4. Ground Truth
 
 ### *ground_truth.py*
 Visualizar el bounding box seleccionado en la imagen correspondiente
 ### dir_sframe: direccion a la carpeta .sframe
 Exm: 'desktop/annotation.sframe'
 
 
 ## 5. Train Model
 
 ### *train_model.py*
 Entrenar modelo en Turi usando estrucutra de datos (.sframe)
 ### sf_dir = 'direccion de la carpeta .sframe'
 ### save_model_dir = 'direccion en donde el modelo sera guardado'
 ### *Linea 13 de train_model.py* 
     model = tc.object_detector.create(train_data, max_iterations=1000)
     max_iterations puede ser modificado para determinar el numero de iteraciones en el entrenamiento
 
 
 


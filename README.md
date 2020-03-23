# Object Detector Turi

Python scripts using Turi library.


## 1. Start Python environment

Acceder (usando comando "cd") hasta directorio donde se encuantre bin, luego: source bin/activate.
Una vez activado el ambiente se puede entrar a cualquier directorio


## 1.1 Open Text Editor

 Abrir el directorio que contiene los scripts en cualquier editor de texto, cmd + o.


## 2. Join Annotations
 
### *join_annotations.py*
Si existen annotations (json) individuales que se quieran consolidar en uno solo. "join_annotations.py" une los jsons individuales y crea un solo json que contiene a todos.
 
 Uso: especificar directorios
 ### jsons_folder: pasar la direccion de la carpeta en donde se encuentran los jsons individuales
 Exm: 'desktop/carpeta_jsons_individuales'
 ### save_dir: directorio en donde se quiere guardar el archivo json consolidado
 Exm: 'desktop/carpeta_json_consolidado' 
 
 ### Ojo, cuando se pase un directorio, no poner '/' al final.
 Exm(correcto): desktop/carpeta
 Exm(incorrecto): desktop/carpeta/
 
 
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
 
 
 


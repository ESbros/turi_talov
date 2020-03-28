# Deteccion de objectos usando Turi

Python scripts using Turi library.

# Seccion Cero

 ## 0. Instalar Virtual Envs y Dependencias

 ## Virtual Envs
  ### Instalar virtualenv
    pip install virtualenv
  ### Crear una carpeta en donde se creará el ambiente virtual
    mkdir python_turi_env
  *Nota: la carpeta puede tener cualquier nombre*
  ### Acceder a la carpeta
    cd python_turi_env
  ### Crear ambiente virtual
    virtualenv name_env
  
  *Nota: puede ser cualquier nombre, ejm: (virtualenv VirtEnvPy).*
  
  Se crea un carpeta con el nombre elegido, acceder a la carpeta donde se encontrarán los siguientes archivos: 
  **bin            include    lib        pyvenv.cfg**
  
  ### Activar ambiente
  Una vez dentro de la carpeta, y una vez que se visualice el archivo **bin**.
    source bin/activate
  ### Desactivar Ambiente
    deactivate
  ### Instalar Dependencies
   Una vez activado el ambiente, se puede usar el *comando: pip list* el cual lista todas las librerias installadas en el      ambiente.
  *Dependencias Necesarias*
  #### Numpy:
    pip install numpy
  #### Matplotlib
    pip install -U matplotlib
  #### OpenCV:
    pip install opencv-python
  #### Turi:
    pip install -U turicreate
  ### Core M:
    pip install -U coremltools
  
  Ejecutar *comando: pip list* y comprobar que la libreria este instalada.


# Seccion Uno
## 1. Activar ambiente virtual en Python

Acceder ***(usando comando "cd")*** hasta directorio donde se encuantre el archivo ***bin***, luego usar comando: ***source bin/activate.***
Una vez activado el ambiente se puede entrar a cualquier directorio


## 1.1 Abrir editor de texto

 Abrir el directorio que contiene los scripts en cualquier editor de texto, ***cmd + o***.
 
 
# Seccion Dos 
 *Nota: jsons_folder, save_dir, img_dir, dir_frame, **etc**. son las unicas variables que se deben modificar, todas unicamente especifican la direccion en donde se encuentra el archivo o carpeta a utilizar.*
 
Cuando se pase un directorio, ***no poner '/' al final***.
 
    Exm(correcto): desktop/carpeta
    Exm(incorrecto): desktop/carpeta/

## 2. Unir Annotations
 
### *join_annotations.py*
Si existen ***annotations (json)*** individuales que se quieran consolidar en uno solo. *"join_annotations.py"* une los jsons individuales y crea un solo json que contiene a todos.
 
 ### jsons_folder = pasar la direccion de la carpeta en donde se encuentran los jsons individuales
    Exm: jsons_folder = 'desktop/carpeta_jsons_individuales'
 ### save_dir: directorio en donde se quiere guardar el archivo json consolidado
    Exm: save_dir = 'desktop/carpeta_json_consolidado' 
 
 
 ## 3. Crear SFrame
 
 ### *json_sframe.py*
 Convertir annotations (json format) a sframe (estructura requerida por Turi).
 ### img_dir = direccion a la carpeta que contiene todas la imagenes
    Exm: img_dir = 'desktop/dolar_images'
 ### json_file_dir = direccion al archivo json consolidado
    Exm: json_file_dir = 'desktop/annotations.json'
 ### save_dir = direccion en donde la carpeta sframe sera guardada
    Exm: save_dir = 'desktop/sframe_folder'
 
 
 ## 4. Ground Truth
 
 ### *ground_truth.py*
 Visualizar el bounding box seleccionado en la imagen correspondiente
 ### dir_sframe: direccion a la carpeta .sframe
    Exm: 'desktop/annotation.sframe'
 
 
 ## 5. Entrenar modelo
 
 ### *train_model.py*
 Entrenar modelo en Turi usando estrucutra de datos (.sframe)
 ### sf_dir = 'direccion de la carpeta .sframe'
 ### save_model_dir = 'direccion en donde el modelo sera guardado'
 ### *Linea 13 de train_model.py* 
     model = tc.object_detector.create(train_data, max_iterations=1000)
     max_iterations puede ser modificado para determinar el numero de iteraciones en el entrenamiento
     
 ## 6. Añadir Metadata
 
 ### *model_metadata.py*
 En en script *model_metadata.py*, en las lineas 9, 10, 11, 12 y 13 se puede especficar la metadata del model. Author, licencia, version y descripcion corta.

 ### mlmodel_path = 'direccion al modelo .mlmodel'
 ### save_dir = 'direccion en donde se quiere guardar el modelo(metadata)'
    Exm: mlmodel_path = '/Users/erik/Desktop/turi/detector.mlmodel'
    Exm: save_dir = '/Users/erik/Desktop/turi'
 ###
    model.author = 'Talov'
    model.license = 'Talov Object Detector 2020.'
    model.short_description = 'Bills object detector.'
    
# Clasificacion de Actividades
 Los siguientes scripts permiten consolidar un DataFrame (.sframe) apartir de archivos(.csv) que describen señas y entrenar un clasificador de actividad usando Turi.
 ### *final_csv_sframe.py*
 En este scripts se transforma las señas en archivos(.csv) y se crea un el DataFrame requerido en Turi.
 ### folder_folders_signs = 'direccion de la carpeta en donde se encuentra la carpeta que contiene las carpetas con las señales'
    folder_folders_signs = '/Users/erik/Desktop/ASL'  
 ### save_dir = 'direccion de la carpeta en donde se quiere guardar la carpeta .sframe'
    save_dir = '/Users/erik/Desktop'
    
 ### *train_sgn_model.py*
 ### data = 'diraccion de la carpeta .sframe que se creo previamente'
    data = tc.SFrame('/Users/erik/Desktop/signs/signs_csv+sframe/signs.sframe')
    
# Imprimir Metricas
### *model_metrics.py*
El siguiente script imprime las metricas de un modelo entrenado. Imprime la matriz de confusión completa.

### model_dir = 'pasar la direccion del model .model'
    Exm(correcto): model_dir = '/Users/erik/Desktop/signs_detector.model'
    Exm(incorrecto): model_dir = '/Users/erik/Desktop/signs_detector.mlmodel'
    
### sframe_dir = 'pasar la direccion de la carpeta .sframe'
    Exm: sframe_dir = '/Users/erik/Desktop/signs/signs_csv+sframe/signs.sframe'





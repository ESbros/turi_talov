import os
import cv2
import json

jsons_folder = 'directory_to_folder_containing_jsons exm:(desktop/jsons)'  
save_dir = 'directory_to_save_joined_json exm:(desktop/joined_anns_folder)'

file_names = os.listdir(image_folder)
join_annotations = []

count = 0
for file_name in file_names:
    if file_name[0] != '.': 
        directory = jsons_folder + '/' + file_name
        count += 1
        with open(directory, 'r') as f:
            datastore = json.load(f)
            for dictionary in datastore:
                join_annotations.append(dictionary)


print('Numero de JSONs Procesados:', count)
print('Numero de Imagenes:', len(join_annotations))

json_file = json.dumps(join_annotations)
with open(save_dir + '/' + 'joined_annotations.json', 'w') as f:
    f.write(json_file)

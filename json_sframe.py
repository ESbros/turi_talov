import turicreate as tc

img_dir = '/Users/erik/Desktop/turi/datasets/test_images'
json_dir = '/Users/erik/Desktop/turi/datasets/annotations.json'


img_shape = tc.image_analysis.load_images(img_dir, with_path=True)
#print(img_shape)


sf_anns = tc.SFrame.read_json(json_dir, orient='records')
sf_anns = sf_anns.rename({'image':'name'})


dictionary = {"path":[] ,"label":[], "type":[]}

for sf_ann in sf_anns:
    dictionary['path'].append(img_dir + '/' + sf_ann['name'])
    dictionary['type'].append('image')
    dictionary['label'].append(sf_ann['annotations'][0]['label'])


sf_dictionary = tc.SFrame(dictionary)
sf_anns = sf_anns.add_columns(sf_dictionary)
#print(sf_anns)


sf_join = sf_anns.join(img_shape, how='inner')
#print(sf_join)
sf_join = sf_join.remove_column('path')
print(sf_join)

sf_join.save('/Users/erik/Desktop/turi/datasets/annotations.sframe')
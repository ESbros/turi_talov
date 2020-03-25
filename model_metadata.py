import coremltools

mlmodel_path = '/Users/erik/Desktop/turi/detector.mlmodel'
save_dir = '/Users/erik/Desktop/turi'

model  = coremltools.models.MLModel(mlmodel_path)

# Add model metadata
model.author = 'Talov'
model.license = 'Talov License'
model.short_description = 'Bills object detector'
model.versionString =  '1.0'
model.save(save_dir + '/' + 'metadata_detector.mlmodel')
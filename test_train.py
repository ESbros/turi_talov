import turicreate as tc
import coremltools

sf_dir = '/Users/erik/Desktop/turi/datasets/annotations.sframe'
save_model_dir = '/Users/erik/Desktop/turi'

# Load the data
data = tc.SFrame(sf_dir)

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data, max_iterations=5)

# Add Metadata
model.author = 'Talov'
model.license = 'Talov Object Detector 2019.'
model.short_description = 'Bills object detector.'

# Save predictions to an SArray
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)
print(metrics)

# Save the model for later use in Turi Create
model.save('ig02.model')

# Export for use in Core ML
model.export_coreml(save_model_dir + '/' + 'detector.mlmodel')
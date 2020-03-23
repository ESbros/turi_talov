import turicreate as tc

sf_dir = 'directory to sframe directory exm:(desktop/annotations.sframe)'
save_model_dir = 'directory where model will be saved exm:(desktop/model_folder)'

# Load the data
data = tc.SFrame('/Users/erik/Desktop/turi/datasets/annotations.sframe')

# Make a train-test split
train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data, max_iterations=1000)

# Save predictions to an SArray
predictions = model.predict(test_data)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test_data)
print(metrics)

# Save the model for later use in Turi Create
model.save('ig02.model')

# Export for use in Core ML
model.export_coreml(save_model_dir + '/' + 'detector.mlmodel')
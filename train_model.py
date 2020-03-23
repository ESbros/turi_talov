import turicreate as tc

# Load the data
data = tc.SFrame('/Users/erik/Desktop/turi/datasets/annotations.sframe')

# Make a train-test split
#train_data, test_data = data.random_split(0.8)

# Create a model
model = tc.object_detector.create(train_data, max_iterations=1000)

# Save the model for later use in Turi Create
model.save('ig02.model')

# Export for use in Core ML
model.export_coreml('/Users/erik/Desktop/turi/models/detector.mlmodel')
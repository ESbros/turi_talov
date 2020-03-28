import turicreate as tc

sframe_dir = '/Users/erik/Desktop/signs/signs_csv+sframe/signs.sframe'

# Load sessions from preprocessed data
data = tc.SFrame(sframe_dir)
save_dir = '/Users/erik/Desktop'

print(data)

# Train/test split by recording sessions
train, test = tc.activity_classifier.util.random_split_by_session(data,
                                                                  session_id='exp_id',
                                                                  fraction=0.8)

# Create an activity classifier
model = tc.activity_classifier.create(train, session_id='exp_id', target='activity',
                                      prediction_window=50, max_iterations=5)

# Evaluate the model and save the results into a dictionary
metrics = model.evaluate(test)
print(metrics)

# Save the model for later use in Turi Create
model.save(save_dir + '/' + 'signs_detector.model')

# Export for use in Core ML
model.export_coreml(save_dir + '/' + 'signs_detector.mlmodel')

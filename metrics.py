import turicreate as tc

model_dir = '/Users/erik/Desktop/signs_detector.model'
sframe_dir = '/Users/erik/Desktop/signs/signs_csv+sframe/signs.sframe'

data = tc.SFrame(sframe_dir)
model = tc.load_model(model_dir)

train, test = tc.activity_classifier.util.random_split_by_session(data,
                                                                  session_id='exp_id',
                                                                  fraction=0.8)

metrics = model.evaluate(test)
print('\nTodas las metricas')
print(metrics)

print('\n\nMatriz de confusion')
print(metrics['confusion_matrix'])

print('\n\nTodos los elementos individuales de la matriz de confusion')
for elm in metrics['confusion_matrix']:
    print(elm)

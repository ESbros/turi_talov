import turicreate as tc

model_dir = '/Users/erik/Desktop/turi/signs/signs_detector.model'
sframe_dir = '/Users/erik/Desktop/turi/signs/signs_csv+sframe/signs.sframe'

data = tc.SFrame(sframe_dir)
model = tc.load_model(model_dir)

train_data, test_data = data.random_split(0.8)                                                    

metrics = model.evaluate(test_data)
print('\nTodas las metricas')
print(metrics)

print('\n\nMatriz de confusion')
print(metrics['confusion_matrix'])

print('\n\nTodos los elementos individuales de la matriz de confusion')
for elm in metrics['confusion_matrix']:
    print(elm)

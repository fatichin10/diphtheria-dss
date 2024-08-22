import pickle
import pandas as pd

def vaksin_predict(feature):
    model_file = open('model/vaksin_model.pkl', 'rb')
    model = pickle.load(model_file, encoding='bytes')
    prediction = model.predict([feature])
    decode = {0: 'Tidak perlu', 1: 'ADS 20.000', 2: 'ADS 40.000', 3: 'ADS 60.000', 4: 'ADS 80.000', 5: 'ADS 100.000'}
    vaksin = decode[prediction[0]]
    return vaksin

def obat_predict(feature):
    obat = ['Antrain', 'Paracetamol', 'Ceftriaxone', 'Erythromycin', 'Dexamethasone', 'Ranitidine', 'Multivitamin', 'Obat-kumur', 'Phosphatidylcholine']
    items = []
    for o in obat:
        model_file = open(f'model/{o}_model.pkl', 'rb')
        model = pickle.load(model_file, encoding='bytes')
        prediction = model.predict([feature])
        if prediction[0] == 1:
            items.append(o)

    pengobatan = ', '.join(items)
    return pengobatan
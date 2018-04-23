import h5py
import numpy as np
from sklearn.utils import shuffle
from keras.layers import Input, Dropout, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd

np.random.seed(2018)

X_train = []
X_test = []

for file_name in ["gap_inception.h5", "gap_resnet.h5", "gap_xception.h5"]: #"gap_inception.h5", "gap_resnet.h5", "gap_xception.h5"
    with h5py.File('./'+file_name, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta', loss='binary_crossentropy', metrics=['accuracy'])


model.fit(X_train, y_train, batch_size=128, epochs=8, validation_split=0.2)


y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)
gen = ImageDataGenerator()
test_generator = gen.flow_from_directory("test2", (224, 224), shuffle=False, batch_size=64)
df = pd.read_csv('sample_submission.csv')
for i, fname in enumerate(test_generator.filenames):
    index = int(fname[fname.rfind('/')+1:fname.rfind('.')])
    df.set_value(index-1, 'label', y_pred[i])

df.to_csv('pred.csv', index=None)
df.head(10)


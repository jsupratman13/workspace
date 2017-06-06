from keras.models import Sequential #linear stack of neural netowrks layers
from keras.layers import Dense,Dropout,Flatten #core layers used in ANN
from keras.layers import Convolution2D,MaxPooling2D #get convolution layers
from keras.utils import np_utils
from keras.datasets import mnist #get mnist data
from matplotlib import pyplot as plt
import numpy as np
np.random.seed(123) # for reproducitbility

#load pre-shuffled mnist data into train and test sets
(x_train, y_train), (x_test,y_test) = mnist.load_data()
#print x_train.shape
#plt.imshow(x_train[0])
x_train = x_train.reshape(x_train.shape[0],1,28,28)
x_test = x_test.reshape(x_test.shape[0],1,28,28)

#change type to float32 and normalize value to range 0 to 1
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

#convert 1d class arry to 10d matrices
y_train = np_utils.to_categorical(y_train,10)
y_test = np_utils.to_categorical(y_test,10)

#create model
#print model.output_shape #check current model output
model = Sequential()
model.add(Convolution2D(32,3,3,activation='relu',input_shape=(1,28,28),dim_ordering='th')) #(depth,width, height) #tensorflow
model.add(Convolution2D(32,3,3,activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25)) #prevent overfitting
#fully connected dense layer
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#train data
model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1)

#evaluate
score = model.evaluate(x_test,y_test,verbose=0)


from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import keras
import matplotlib.pyplot as plt
from keras.models import model_from_json
import numpy
import cv2

# Initialising the CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape = (224, 224, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(32, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Conv2D(32, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Flatten())
model.add(Dense(units = 128, activation = 'relu'))
model.add(Dense(units = 1, activation = 'sigmoid'))

# # Compiling the CNN
# model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
#
# print(model.summary())
#
# #image augmentations
# train_datagen = ImageDataGenerator(rescale = 1./255,
#                                    shear_range = 0.2,
#                                    zoom_range = 0.2,
#                                    horizontal_flip = True,
#                                    validation_split=0.2)
#
# test_datagen = ImageDataGenerator(rescale = 1./255)
#
# training_set = train_datagen.flow_from_directory('data/train',
#                                                  target_size = (224, 224),
#                                                  batch_size = 16,
#                                                  class_mode = 'binary',
#                                                  subset = 'training')
# testing_set = train_datagen.flow_from_directory('data/train',
#                                                  target_size = (224, 224),
#                                                  batch_size = 16,
#                                                  class_mode = 'binary',
#                                                  subset='validation')
# validation_set = test_datagen.flow_from_directory('data/validation',
#                                             target_size = (224, 224),
#                                             batch_size = 16,
#                                             class_mode = 'binary')
#
# model.compile(loss=keras.losses.binary_crossentropy,
#               optimizer='rmsprop',
#               metrics=['accuracy'])
#
# model.fit_generator(training_set,
#     epochs = 12,
#     validation_data = testing_set,
#     verbose=1)
#
# # Save the weights
# model.save_weights('my_model_weights.h5')
#
# # Save the model architecture
# with open('my_model.json', 'w') as f:
#     f.write(model.to_json())
#
# score = model.evaluate_generator(testing_set)

# Model reconstruction from JSON file
with open('my_model.json', 'r') as f:
    model = model_from_json(f.read())

# Load weights into the new model
model.load_weights('my_model_weights.h5')

model.compile(loss=keras.losses.binary_crossentropy,
              optimizer='rmsprop',
              metrics=['accuracy'])

# print('Test loss:', score[0])
# print('Test accuracy:', score[1])

img1 = cv2.imread('dog1.jpg')
img1 = cv2.resize(img1, (224,224))
# img1 = img1.reshape(1,224,224,3)
img2 = cv2.imread('cat1.jpg')
img2 = cv2.resize(img2, (224,224))
img3 = cv2.imread('dog2.jpg')
img3 = cv2.resize(img3, (224,224))
img4 = cv2.imread('cat2.jpg')
img4 = cv2.resize(img4, (224,224))
img=[img1,img2,img3,img4]
img=numpy.array(img)

pred = model.predict(img)
list=[]
for a in pred:
    if a>0.5:
        list.append("dog")
    else:
        list.append("cat")

f, axarr = plt.subplots(2,2)
axarr[0,0].imshow(img1)
axarr[0,0].set_title("This is a "+list[0])
axarr[0,1].imshow(img2)
axarr[0,1].set_title("This is a "+list[1])
axarr[1,0].imshow(img3)
axarr[1,0].set_title("This is a "+list[2])
axarr[1,1].imshow(img4)
axarr[1,1].set_title("This is a "+list[3])
plt.show()

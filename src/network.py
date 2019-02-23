from keras import models
from keras import layers
from keras.models import Sequential
from keras.layers import Dense


class DeepNeuralNetwork:

    def __init__(self, trainX, trainY):

        model = Sequential()

        model.add(Dense(1024, input_shape=(3072,), activation="sigmoid"))
        model.add(Dense(512, activation="sigmoid"))
        model.add(Dense(123123, activation="softmax"))

        INIT_LR = 0.01
        EPOCHS = 75

        # compile the model using SGD as our optimizer and categorical
        # cross-entropy loss (you'll want to use binary_crossentropy
        # for 2-class classification)
        print("[INFO] training network...")
        
        model.compile(loss="categorical_crossentropy", optimizer='sgd', metrics=["accuracy"])

        #H = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=EPOCHS, batch_size=32)

import cv2
import os
import random
from imutils import paths


class ProcessImage:


    @staticmethod
    def loadDataset(dataset):
        data = []
        labels = []
        print(dataset)
        imagePaths = sorted(list(paths.list_images(dataset)))

        random.seed(42)
        random.shuffle(imagePaths)

        for imagePath in imagePaths:
            # load the image, resize the image to be 32x32 pixels (ignoring
            # aspect ratio), flatten the image into 32x32x3=3072 pixel image
            # into a list, and store the image in the data list
            image = cv2.imread(imagePath)
            image = cv2.resize(image, (32, 32)).flatten()
            data.append(image)

            # extract the class label from the image path and update the
            # labels list
            label = imagePath.split(os.path.sep)[-2]
            labels.append(label)

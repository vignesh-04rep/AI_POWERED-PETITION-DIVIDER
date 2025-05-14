
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('model.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('./Data/Out/_0_1986.jpeg', target_size = (200,200))
#test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
print(test_image)
result = classifierLoad.predict(test_image)


if result[0][0] == 1:
    print("EOSINOPHIL")
elif result[0][1] == 1:
    print("LYMPHOCYTE")
elif result[0][2] == 1:
    print("MONOCYTE")
elif result[0][3] == 1:
    print("NEUTROPHIL")
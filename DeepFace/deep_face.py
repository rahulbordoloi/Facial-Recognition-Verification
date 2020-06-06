'''try:
    import deepface
    print("Succesfull")
except ValueError:
    print("Not Installed")

# import numpy as np

# print(DeepFace.__version__)
# print(np.__version__)

#import tensorflow as tf
#print(tf.__version__) '''

import warnings
warnings.filterwarnings()

from deepface import DeepFace
DeepFace.stream("D:\Work\Face Recognition\Datasets")
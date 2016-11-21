import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import os

filename = '._Abyssinian_1.png'

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "/anotations/trimaps/" + filename
abs_file_path = script_dir + rel_path
tri = imread(abs_file_path)

plt.imshow(tri)
plt.show()


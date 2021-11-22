import pandas as pd 
import numpy as np 

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

file_path = './cleaned_divedata/cleaned_divedata_1.csv'
df = pd.read_csv(file_path)

x_data = list(df['x'])
y_data = list(df['y'])
z_data = list(df['z'])

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(x_data, y_data, z_data, 'green')
ax.set_title('3D line plot geeks for geeks')
plt.show()

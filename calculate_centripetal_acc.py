import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt

def calculate_centripetal_acc(file):
    try:
        df = pd.read_csv(file)
    except Exception as e:
        print(e)

    """
    Approach: 

    To calculate centripetal acceleration we need a radius. 
    Since the data points are in space (as opposed to a plane), we can enclose the flight path within a sphere
    whose diameter is defined by the magnitude of the first and last vector of the dataset.
    However, we really just want to know the coordinates of the sphere's center, because we can then use that
    to find the sphere's radius. We can find the center "C" of a sphere using the midpoint formula.
    After we have "C", we can use it's coordinates to find the radius.
    The radius is simply the distance between the center of the sphere and some other point on its surface,
    thus we can use the distance formula to compute it. Once we know the sphere's radius, we can calculate
    the centripetal acceleration by:

    1. computing the displacement vector v = v2 - v1
    2. finding its magnitude ||v|| 
    3. squaring its magnitude and dividing by the radius (v^2 / r)

    """

    # Get first row and last row of dataset 
    vect_1 = df.values[0].tolist()
    vect_2 = df.values[-1].tolist()

    # Calulate center of sphere using the midpoint formula
    added_vects = np.add(vect_1, vect_2)
    midpoint = np.true_divide(added_vects, 2)

    # Calculate radius of sphere using the distance formula
    radius = math.dist(midpoint, vect_2)
    vects = []

    # Iterate through df rows and store vectors in array
    for _, row in df.iterrows():
        vect = [row['x'], row['y'], row['z']]
        vects.append(vect)

    acceleration_arr = []

    for i in range(len(vects) -1):
        vect_i = np.array(vects[i])  
        vect_i_1 = np.array(vects[i+1])

        # Subtract vector_i from vector_i+1 to get velocity vector
        velocity_vect = np.subtract(vect_i_1, vect_i)

        # Get magnitude of velocity vector 
        vector_magnitude = np.linalg.norm(velocity_vect)

        # centripetal acceleration = v**2 / radius
        a_c = (vector_magnitude ** 2) / radius   
        acceleration_arr.append(a_c)

    _time = list(range(len(acceleration_arr)))

    plt.plot(_time, acceleration_arr)
    plt.ylabel('Centripetal Acceleration')
    file_name = file.split('/')
    plt.title(file_name[1])
    plt.show()  

if __name__ == '__main__':
    # file_path = input('Enter the path to the file you want to calculate: ')
    calculate_centripetal_acc('cleaned_divedata/cleaned_divedata_3.csv')
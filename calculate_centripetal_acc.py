import pandas as pd
import numpy as np 
import math
import matplotlib.pyplot as plt
import sys

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
    to find the sphere's radius. We can find the center of a sphere using the midpoint formula.
    After we have sphere's center, we can use it's coordinates to find the radius.
    The radius is simply the distance between the center of the sphere and some other point on its surface,
    thus we can use the distance formula to compute it. Once we know the sphere's radius, we can calculate
    the centripetal acceleration by:

    1. computing the displacement vector v = v2 - v1
    2. finding its magnitude ||v|| 
    3. squaring its magnitude and dividing by the radius (v^2 / r)

    Furthermore, we can calculate the angle between the two vectors using the dot product.

    """

    # Get first and last row of dataset 
    vect1 = df.values[0].tolist()
    vect2 = df.values[-1].tolist()

    # Calulate center of sphere using the midpoint formula
    added_vects = np.add(vect1, vect2)
    midpoint = np.true_divide(added_vects, 2)

    # Calculate radius of sphere using the distance formula
    radius = math.dist(midpoint, vect2)
    vects = []

    # Iterate through df rows and store vectors in array
    for _, row in df.iterrows():
        vect_i = [row['x'], row['y'], row['z']]
        vects.append(vect_i)

    acceleration_arr = []
    angle_arr = []

    for i in range(len(vects) -1):
        vect_i = np.array(vects[i])  
        vect_i_1 = np.array(vects[i + 1])

        # Subtract vect_i from vector_i + 1 to get velocity vector
        displacement_vect = np.subtract(vect_i_1, vect_i)

        # Get magnitude of velocity vector 
        vector_magnitude = np.linalg.norm(displacement_vect)

        # centripetal acceleration = v**2 / radius
        a_c = (vector_magnitude ** 2) / radius   
        acceleration_arr.append(a_c)

        # Get angle between vectors using dot product
        # First, calculate dot product of vectors
        dot_product = np.dot(vect_i, vect_i_1)

        # Second, get the magnitude of each vector
        vector_i_magnitude = np.linalg.norm(vect_i)
        vector_i_1_magnitude = np.linalg.norm(vect_i_1)

        # Third, divide the dot product by the product of the two magnitudes 
        dot_divide_vector_magnitudes = dot_product / (vector_i_magnitude * vector_i_1_magnitude)

        # Lastly, to get the angle, get the arcosine of result
        angle = np.arccos(dot_divide_vector_magnitudes)
        angle_arr.append(angle)

    _time = list(range(len(acceleration_arr)))

    # Generate plot 
    plt.plot(_time, acceleration_arr)

    # Provide plot labels
    plt.ylabel('Centripetal Acceleration')
    plt.xlabel('Time (1/60s)')

    # Title of plot is the file name supplied 
    file_name = file.split('/')
    plt.title(file_name[-1])

    # Show plot
    plt.show() 

    # Create new dataframe with centripetal acceleration and angles
    result_df = pd.DataFrame({'centripetal_acceleration': acceleration_arr, 'angle': angle_arr})
    
    try:
        answer = input('\nDo you wish to save the result data? (y / n): ')

        if answer == 'y':

            result_file_name = input("\nProvide a file name for the result data (do not include the 'csv' file extension): ")
            result_df.to_csv(f'./result_divedata/{result_file_name}.csv')

            print(f'\n{result_file_name} created successfully...Exiting\n')
            sys.exit()
        elif answer != 'n':
            print('Command not found. Exiting...\n')
            sys.exit()
        else:
            print('\nExiting...')
            sys.exit()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    calculate_centripetal_acc(f'cleaned_divedata/cleaned_divedata_3.csv')
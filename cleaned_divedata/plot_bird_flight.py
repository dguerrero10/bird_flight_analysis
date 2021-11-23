import os
import sys

def plot3D_data():
    try:
        import pandas as pd
        import numpy as np
        from mpl_toolkits import mplot3d
        import matplotlib.pyplot as plt
    except:
        print("Operations could not be performed because you do not have 'matplotlib' and/or 'pandas' installed.\n")
        print("To install matplotlib type 'pip install matplotlib'.\n")
        print("To install pandas type 'pip install pandas'.\n")
        sys.exit()

    try:
        for filename in os.listdir(os.getcwd()): 
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)

                fig, ax = plt.subplots()
                ax = plt.axes(projection='3d')

                # Get first and last row of dataset 
                vect1 = df.values[0].tolist()
                vect2 = df.values[-1].tolist()

                # Calulate center of sphere using the midpoint formula
                added_vects = np.add(vect1, vect2)
                midpoint = np.true_divide(added_vects, 2)

                x_data = list(df['x'])
                y_data = list(df['y'])
                z_data = list(df['z'])

                ax.plot3D(x_data, y_data, z_data, 'green')
                ax.scatter(midpoint[0], midpoint[1], midpoint[2])
                ax.set_title(filename)
                plt.show()
        
        print("All data in files have been plotted. Exiting...\n")
        sys.exit()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    plot3D_data()
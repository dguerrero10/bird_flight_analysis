import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import PolynomialFeatures


def create_model():
    df = pd.read_csv('./result_divedata/result_divedata_1.csv')

    y = list(df['Centripetal_Acceleration'])
    x = [list(range(len(y)))]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    poly_reg = PolynomialFeatures(degree=3)
    x_poly = poly_reg.fit_transform(x)

    pol_reg = LinearRegression()
    pol_reg.fit(x_poly, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, pol_reg.predict(poly_reg.fit_transform(x)), color='blue')

    plt.title('Centripetal Acceleration')
    plt.xlabel('Time (1/60s)')
    plt.ylabel('Centripetal Acceleration')
    plt.show()
    
    return

create_model()
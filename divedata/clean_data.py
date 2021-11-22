import os
import sys

def clean_data():
    print('\nNOTE: You should only run this script in the directory where your bird data is stored, otherwise unwanted effects may occur to other .csv files\n')
    print('Data must also be in the shape of m x 3 (m rows and 3 columns)\n')

    _continue = input('Do you wish to continue (y / n): ')

    if _continue == 'y':

        try:
            import pandas as pd
        except:
            print("Operations could not be performed because you do not have 'pandas' installed\n")
            print("To install pandas type 'pip install pandas'")
            sys.exit()

        try:
            indx = 1
            for filename in os.listdir(os.getcwd()):
                if filename.endswith('.csv'):
                    df = pd.read_csv(filename)
                    df.dropna(inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    
                    df.rename(columns={df.columns[0]: 'x'}, inplace=True)
                    df.rename(columns={df.columns[1]: 'y'}, inplace=True)
                    df.rename(columns={df.columns[2]: 'z'}, inplace=True)

                    df.to_csv(f'cleaned_divedata_{indx}.csv', index=False)
                    indx += 1

            print('\nData cleaned successfully. Exiting...')
            sys.exit()
        except Exception as e:
            print(e)

    elif _continue != 'n':
        print('\nCommand not found. Exiting...')
        sys.exit()
    
    else: 
        sys.exit()

if __name__ == '__main__':
    clean_data()
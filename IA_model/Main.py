import os
import pandas as pd

import joblib

from Generate_langage import create_data
from Numerisation import read_data_from_file, process_data, write_to_csv, update_csv, train_ia, process_line, \
    makeDataFrame
from Sardinas_Patterson import is_codage
import pandas as pd


def main():
    # create_data()
    # 
    # # creation data.csv de base
    # file_path = 'data.txt'
    # output_file = 'data.csv'
    # if os.path.exists(file_path):
    #     data = read_data_from_file(file_path)
    #     processed_data = process_data(data)
    #     write_to_csv(processed_data, output_file)
    #     print(f"Les données ont été écrites dans {output_file}.")
    # else:
    #     print(f"Le fichier {file_path} n'existe pas.")
    # 
    # # creation model
    # update_csv()
    
    # # apprentissage IA
    # train_ia()
    
    language = ['01', '0110']
    dataframe = makeDataFrame(language)
    dataframe = pd.DataFrame([dataframe])
    print(dataframe)
    model = joblib.load("model.joblib")
    print(model.predict(dataframe))

if __name__ == '__main__':
    main()
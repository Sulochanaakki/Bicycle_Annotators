from annotators.dataloader import  Data_Getter
from annotators.datapreprossing import Preprocessor

class trainModel:

    def __init__(self):
        pass
        
        
    def trainingModel(self):
        
        try:
            # Getting the data from the source
            data_getter=Data_Getter()
            data=data_getter.get_data()

            
            """doing the data preprocessing"""

            preprocessor=Preprocessor()
             # check if missing values are present in the dataset
            is_null_present, cols_with_missing_values = preprocessor.is_null_present(data)
            # if missing values are there, replace them appropriately.
            if (is_null_present):
                data = preprocessor.filling_missing_values(data, cols_with_missing_values)  # missing value imputation
            #encode categorical data
            data = preprocessor.encode_categorical_columns(data)
            #encode numerical data
            #data = preprocessor.encode_numerical_columns(data)

            # create separate features and labels
            #X,Y=preprocessor.separate_label_feature(data,label_column_name='Response')



        except Exception as e:
            raise Exception    
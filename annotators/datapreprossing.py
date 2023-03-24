import pandas as pd
import numpy as np
import datetime as dt
#from imblearn.over_sampling import RandomOverSampler
class Preprocessor:
    """
        This class shall  be used to clean and transform the data before training.
        """

    def __init__(self):
        pass
        
    def separate_label_feature(self, data, label_column_name):
        """
                        Method Name: separate_label_feature
                        Description: This method separates the features and a Label Coulmns
                """
        
        try:
            self.X=data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y=data[label_column_name] # Filter the Label columns
            
            return self.X,self.Y
        except Exception as e:
            
            raise Exception()  
        
    def is_null_present(self,data):
        """
                                Method Name: is_null_present
                                Description: This method checks whether there are null values present in the pandas Dataframe or not.
                             
                        """
        self.cols_with_missing_values=[]
        self.cols = data.columns
        try:
            self.null_counts=data.isna().sum() # check for the count of null values per column
            for i in range(len(self.null_counts)):
                if self.null_counts[i]>0:
                    self.null_present=True
                    self.cols_with_missing_values.append(self.cols[i])
            if(self.null_present): # write the logs to see which columns have null values
                self.dataframe_with_null = pd.DataFrame()
                self.dataframe_with_null['columns'] = data.columns
                self.dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
                self.dataframe_with_null.to_csv('data/null_values.csv') # storing the null column information to file
        
            return self.null_present, self.cols_with_missing_values
        except Exception as e:
            raise Exception()  

    def filling_missing_values(self, data, cols_with_missing_values):
        """
                                        Method Name: idrop_missing_values
                                        Description: This method drop all the missing values in the Dataframe using KNN Imputer.                                      
                     """
 
        self.data= data
        self.cols_with_missing_values=cols_with_missing_values
        try:
            
            self.data = self.data.fillna(0)
            return self.data
        except Exception as e:
            raise Exception()        
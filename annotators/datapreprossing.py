import pandas as pd
import numpy as np
import datetime as dt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
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
        Description: This method drop all the missing values in the Dataframe using KNN Imputer.                                      
                     """
 
        self.data= data
        self.cols_with_missing_values=cols_with_missing_values
        try:            
            self.data = self.data.fillna('no_output')           
            return self.data
        except Exception as e:
            raise Exception()  


    def cleaning_columns(self,data):
        """
                                               
         Description: This method encodes the categorical values to numeric values.
                             """
        
        self.data=data
        try:
            self.cat_df = self.data.copy()
            self.cat_df['created_at'] = pd.to_datetime(self.cat_df['created_at'], infer_datetime_format=True)

           # self.data = self.cat_df.drop(columns=['gui_type', 'created_at','task_input.image_url',
            #                                      'task_output.cant_solve','task_output.corrupt_data',
            #                                      'root_input.image_url','project_root_node_input_id',
            #                                      'user.vendor_id','loss','user.id','project_node_input_id',
            #                                      'project_node_output_id','img'],axis=1)

            self.cat_df = self.cat_df(['user.vendor_user_id','workpackage_total_size','task_output.answer',
                                       'task_output.duration_ms','is_bicycle'], axis=1)
            self.data=self.data.loc[(self.data['task_output.answer']=='yes') | (self.data['task_output.answer'] == 'no')]
            
            return self.data

        except Exception as e:
            raise Exception()
        
    def encode_categorical_columns(self,data):
        """
                                                 
        Output: dataframe with categorical values converted to numerical values
                                                
                             """
      

        self.data=data
        try:
            self.data['workpackage_total_size'] = self.data['workpackage_total_size'].map({5: 0,3: 1,1:2})

            self.data['task_output.answer'] = self.data['task_output.answer'].map({'yes':1,'no':0})
            self.data['is_bicycle'] = self.data['is_bicycle'].map({False:0,True:1})
            #Label encodeing for annotators column by using sklean label encoding
            #le = LabelEncoder()
            labelencoder=LabelEncoder()
            self.data['user.vendor_user_id'] = labelencoder.fit_transform(self.data['user.vendor_user_id'])
            
             
        except Exception as e:
            raise Exception()    
        
    def encode_numerical_columns(self,data):
        """
                                                 
        Output: dataframe with categorical values converted to numerical values
                                                
                             """
      

        self.data=data
        try:
            
            #Scalling the task_output_duration column by using min max scaler
            
            scaler = MinMaxScaler()
            self.data['task_output.duration_ms'] = scaler.fit_transform(self.data['task_output.duration_ms'].values.reshape(-1,1))
            
            #self.data['task_output.duration_ms'] = scaler.fit_transform([self-data['task_output.duration_ms']])
        except Exception as e:
            raise Exception()    


    def separate_label_feature(self, data, label_column_name):
        """ 
                        Description: This method separates the features and a Label Coulmns.
                """
        try:
            self.X=data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y=data[label_column_name] # Filter the Label columns
            
            return self.X,self.Y
        except Exception as e:
            raise Exception()       
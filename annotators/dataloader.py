import pandas as pd

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.
    """
    def __init__(self):
        self.training_file='data/finaldata.csv'
        #self.file_object=file_object
        

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        """
        try:
            self.data= pd.read_csv(self.training_file) # reading the data file
            return self.data
        except Exception as e:
            
            raise Exception()
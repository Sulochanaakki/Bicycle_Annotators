from annotators.dataloader import  Data_Getter

class trainModel:

    def __init__(self):
        pass
        
    def trainingModel(self):
        
        try:
            # Getting the data from the source
            data_getter=Data_Getter.get_data()
            data=data_getter.get_data()
        except Exception as e:
            raise Exception    
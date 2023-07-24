import sys
import os 
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(  self,
        Age: int,
        Gender: str,
        Cold: str,
        Cough: str,
        Fever: str,
        BP: str,
        Diabetes: str,
        Thyroid: str,
        Arthritis: str,
        Acidity: str,
        Others: str):


        self.Age=Age
        self.Gender=Gender
        self.Cold=Cold
        self.Cough=Cough
        self.Fever=Fever
        self.BP=BP
        self.Diabetes=Diabetes
        self.Thyroid=Thyroid
        self.Arthritis=Arthritis
        self.Acidity=Acidity
        self.Others=Others

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Cold": [self.Cold],
                "Cough": [self.Cough],
                "Fever": [self.Fever],
                "BP": [self.BP],
                "Diabetes": [self.Diabetes],
                "Thyroid": [self.Thyroid],
                "Arthritis": [self.Arthritis],
                "Acidity": [self.Acidity],
                "Others": [self.Others]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

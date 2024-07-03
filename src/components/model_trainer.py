#train model here using different algorithms
#importing essential libraries
import sys
import os  
from dataclasses import dataclass

# importing regression models
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model

#creating config file
@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")          #after creating the model, save it as pickle file

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()                     #initialize

    def initiate_model_trainer(self, train_array,test_array):    #O/P of transformation -> I/P of model_trainer
        try:
            logging.info("Splitting training and test input data into independent and target features")
            X_train,X_test, y_train, y_test = (
                train_array[:,:-1],
                test_array[:,:-1],
                train_array[:,-1],
                test_array[:,-1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(), 
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Gradient Boosting": GradientBoostingRegressor()
            }

            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models = models)   #evaluate_model function in utils.py
                
            best_model_score = max(sorted(model_report.values()))    # returns the highest r2 score



            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)  # nested list returns the index of model with highest r2 score
            ]

            best_model = models[best_model_name]

            if best_model_score < 0.7:
                raise CustomException("No Best Model Found: Minimum threshold criteria failed")
            logging.info(f"Best model selection process completed")

            #saving the model in pickle file
            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted = best_model.predict(X_test)
            r2_score_card = r2_score(y_test,predicted)
            return r2_score_card
        
        except Exception as e:
            raise CustomException(e,sys)



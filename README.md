# End-to-End Machine Learning Project – Regression

This project implements a modular, production-ready regression system to predict students' exam performance using demographic and academic features such as parental background, course completion, and prior subject scores.

The solution follows a structured ML workflow:

- Data ingestion → transformation → model training → artifact versioning → inference
- Feature engineering with One-Hot Encoding (categorical) and scaling (numeric)
- Feature selection using correlation pruning and L1/L2 regularization
- Cross-validated hyperparameter tuning for improved generalization

---

## Modeling Approach

### Data Processing
- Train/test split
- Missing & duplicate handling
- One-Hot Encoding for categorical variables
- Standard scaling for numerical features

### Regularization & Optimization
- Ridge (L2), Lasso (L1), and ElasticNet regression
- Cross-validation for hyperparameter tuning
- Reduced multicollinearity using L1-based feature pruning
- Persisted model + preprocessor as serialized artifacts (`model.pkl`, `preprocessor.pkl`)

---

## Results

Final tuned model performance on held-out test set:

- **MAE:** 3.8  
- **RMSE:** 5.1  
- **R²:** 0.89  

Compared to an unregularized baseline:
- Baseline RMSE: 6.6  
- Improved generalization and reduced train–test performance gap  

UPDATE: AWS CI-CD Production Grade Deployment using ECR, EC2 and Dockers.

![image](https://github.com/ferozk0333/MLProject/assets/48884151/d1987c13-bbde-46e8-b54e-90672b7464a3)
![image](https://github.com/ferozk0333/MLProject/assets/48884151/9a279039-6a3c-4bd7-a3a9-c46485ad3839)
![image](https://github.com/ferozk0333/MLProject/assets/48884151/7152dc60-b789-4ed6-8fd5-726f8be5d801)
![image](https://github.com/ferozk0333/MLProject/assets/48884151/bc29d5ea-9ca8-488b-afa9-aad788a5fb34)


https://github.com/ferozk0333/MathMentor-Machine_Learning_based_Test_Score_Predictor/assets/48884151/d5b1190d-caf7-403a-8dfc-97c715407505

## Docker Setup In EC2 commands to be Executed
#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:

GitHub -> Settings -> Actions -> Runners -> New -> Linux -> Execute the commands in EC2 instance -> Press Enter to skip
NOTE:   Enter the name of runner: [press Enter for IP...] :self-hosted
Skip rest by pressing Enter
(Runner - Whenever code commit - acts as a trigger - CI CD deploy)

./run.sh  ---> Listening for Jobs ==> Any push that happens in repository

## Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = <repo name>










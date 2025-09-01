

import pandas as pd 

from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import r2_score  
import mlflow 

from src.logger import * 

train = pd.read_csv(r'src\artifacts\artifacts\train_data.csv')

X_train , y_train = train.drop( "amounts ( in ₹ )" , axis =1 ) , train["amounts ( in ₹ )"]

''' VVVV IMPORTANT , to SAVE the mdoel in MLFOW nd best ONE in AWS S3 bucket Direcy for easier DEployment , we 
ar esuign thsi cdoe with AWS acdes key '''


# Set the S3 bucket as the artifact store
# os.environ["MLFLOW_S3_ENDPOINT_URL"] = "https://s3.amazonaws.com" 
# mlflow.set_tracking_uri(f"s3://<your_s3_bucket_name>/mlruns")



''' HERE PUT THE LSIT OF HYEPR YOU WNAT THE MODEL TO BE TRIANE on and flowl will kepp track of it '''
params  = {"n_estimators" : [10 ] , 
           "max_depth" : [4 ,6  ]}




''' For each experiment ( each indidual set of hyperparams ) dp a diff mlflow.run()
so it will sue NESTED loops '''

for est in params["n_estimators"] : 
    # for each n_est hyperparam 
    # one NEW depth is used 
    for dep in params["max_depth"] : 

        with mlflow.start_run():

            try : 
                # make a diff insarnc eof mdoel with new hyperam 
                model = RandomForestRegressor( n_estimators  = est  , max_depth= dep  )
                model.fit( X_train , y_train )

                y_pred_train = model.predict( X_train )
                r2_score_val = r2_score( y_train ,y_pred_train )

                # log these HYEPRam and mdoe as DICT
                mlflow.log_params({"n_estimators" : est , "max_depth" : dep })
                mlflow.log_metric( "r2_score" , r2_score_val )

                # to SAVE mdoel only use ,mlflo.sklearn.log mdoel ,for hyper ,its sklern.log params 
                model_info = mlflow.sklearn.log_model( model , "random_forest_reg")
                
                '''NEW CODE TO REGISTER THE MODEL on MLFLOW for DEPLOYMENT online using streamlit ''' 
                ''' Re - read '''
                # mlflow.register_model(
                #     model_uri=model_info.model_uri, 
                #     name="TransactionForecaster"
                # )
                
                # # Get the client to transition the model to the Production stage
                # client = mlflow.tracking.MlflowClient()
                # latest_version = client.get_latest_versions("TransactionForecaster")[0]
                # client.transition_model_version_stage(
                #     name="TransactionForecaster",
                #     version=latest_version.version,
                #     stage="Production"
                # )


                # logging.info(f"Model with hyperparam-> est {est } and { dep }trianed succesfully")
                logging.info(f"Model trained and logged successfully. R2 Score: {r2_score_val}. Model registered to Production.")

            except Exception as e : 
                logging.error( f"Error -{e}")
                raise 


''' RESULT STORED in older calald mlruns
NOW run  'mlflow ui' cmd in cli , and then when mlflow opens -> 
GO to Experiments -> ALl the diff sets of hyperpa (under RUNS )
and the model itslef under Modle experiamnt and we cns comapr eusifn bar charts etc 


Differn b.w logigng ( mlflow.sklearn.log_mdoe())
and regsirerignthe mdoel (saving the alstest version ONLY of mdoel for further use )

model = mlflow.register_model( model uri , name )
mlflow.trackignCLient().get_latest_version( model[0])


 '''

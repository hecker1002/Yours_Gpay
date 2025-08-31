

import pandas as pd 

train = pd.read_csv(r'D:\This Project\Placement_2025\Yours_Gpay\src\artifacts\artifacts\train_data.csv')
X_train , y_train = train.drop( "amounts ( in ₹ )" , axis =1 ) , train["amounts ( in ₹ )"]


from sklearn.ensemble import RandomForestRegressor  

model = RandomForestRegressor( n_estimators  = 100  )

try : 

    model.fit( X_train ,y_train )
    print("Model was trained succesfully")

except : 
    print("Model was NOT trained ")


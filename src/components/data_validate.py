

import numpy as np  
import pandas as pd 



''' try to use FULL path of the files for now  '''
df  = pd.read_csv(r"D:\This Project\Placement_2025\Yours_Gpay\src\artifacts\artifacts\transactions.csv")

# Validate the Dtaaset 


def check_amount( df , amounts_col ) : 
    
    if ( df[ amounts_col].dtype=='float' or df[ amounts_col].dtype=='int') : 
        print("Correct AMounts ")
    
    else : 
        print("Wrong Dtype")
    
    return df 


def check_merchants( df , merchant_col ) : 
    if (df["merchants"].isnull().sum()==0 and df[ merchant_col].dtype=='object') : 
        print("NO NULL VALUES in Merhcant COlumn")
    else : 
        print(" NULL VALUES found in MErchant COlumn" )
    
    return df 
    
def check_date( df , date_col ) : 
    
    try : 

        # Try to COnver tot Datetime COlumn with a MIXDD formt of dates (and errors="coerce") and still if some NULL VALEUS in date column 
        # then some impute dates are there 
        
        df[date_col] = pd.to_datetime( df[date_col ], format="mixed" , errors="coerce")
        invalid_indexes  = df[df[date_col].isnull()].index

        if len( invalid_indexes ) >0 : 

            print( "Impossible /Wrog Dates found in Dataset")

            print( "Dropping Such rows")
            df = df.drop( invalid_indexes , axis=0 )
        
        return df.reset_index( drop =True )

    except : 
        print("error")
        return df 





''' Time col is CHeck is failing for soe reaosn '''
# def check_time( df , time_col ) : 
    
#     try : 

#         # Try to COnver tot Datetime COlumn with a MIXDD formt of dates (and errors="coerce") and still if some NULL VALEUS in date column 
#         # then some impute dates are there 
#         df_time = df[ time_col].copy()
#         df_time = pd.to_datetime( df_time , format="mixed" , errors="coerce")
        
#         if len(df[ df_time.isnull()]) >0 : 

#             print( "Impossible /Wrog Time found in Dataset")

#         print( "Dropping Such rows fromDataset")
#         # print(df[ df_time.isnull()])
#         df = df.drop(df[ df_time.isnull()] , axis=0 )
#         return df 

#     except : 
#         print("errors ")





df = check_merchants( df , "merchants")
df = check_amount( df , "amounts ( in ₹ )")
df = check_date( df , "Date")


import os 

# SAVE final VALIDATED Dataset 
base_project_dir  = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
artifacts_folder = os.path.join(base_project_dir, 'artifacts')
folder_name = 'artifacts'
new_folder_path= os.path.join( artifacts_folder , folder_name )

dataset_name = "validated_transactions.csv"
df.to_csv( os.path.join(new_folder_path  , dataset_name ) , index= False )
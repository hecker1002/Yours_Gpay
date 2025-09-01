
import pandas as pd 

df = pd.read_csv(r"D:\This Project\Placement_2025\Yours_Gpay\src\artifacts\artifacts\validated_transactions.csv")
# Preproces s , Feature ENgineering and Feature Selection 

# Moing Averages 
# NO lokahea bais (prev 3 days m NOT cur day included )

''' 3 days MA '''
df["ma_3"] = df["amounts ( in ₹ )"].rolling( window  = 3 ).mean().shift(1) 

''' 7 days MA '''
df["ma_7"] = df["amounts ( in ₹ )"].rolling( window  = 7 ).mean().shift(1)



# extract Month Numebr 
df['Date'] = pd.to_datetime( df['Date' ], format="mixed" , errors="coerce")
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year
df['quarter'] = df['Date'].dt.quarter
df['day'] = df['Date'].dt.day


# Preprcoess eahc merchnt name 


from string import punctuation


def preprocess_text( txt ) :
    txt = txt.lower() 
    punct = punctuation
    # alernative for nltk.(puunkt).word_tokenize 
    txt1 = txt.split()
    txt2  = [ word for word in txt1 if word not in punct ]
    return " ".join(txt2) 


# apply to merhcant col  
df["merchants"] = df["merchants"].apply( preprocess_text )


import os 

''' A Python Code can ONLY run inside its OWN SOURCE folder '''


# featur vlaue , target var 


train = df.loc[ : 1000 , ["ma_3" ,"ma_7" ,  "month" , "day" , "amounts ( in ₹ )"]]
test = df.loc[ 1000: , ["ma_3" ,"ma_7" ,  "month" , "day" , "amounts ( in ₹ )"]]








# SAVE final VALIDATED Dataset 
base_project_dir  = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
artifacts_folder = os.path.join(base_project_dir, 'artifacts')
folder_name = 'artifacts'
new_folder_path= os.path.join( artifacts_folder , folder_name )

dataset_name = "train_data.csv"
train.to_csv( os.path.join(new_folder_path  , dataset_name ) , index= False )

dataset_name = "test_data.csv"
test.to_csv( os.path.join(new_folder_path  , dataset_name ) , index= False )

# from sklearn.model_selection import train_test_split 

# X_train , X_test , y_train ,y_test = train_test_split( X  , y , test_size =0.2 )



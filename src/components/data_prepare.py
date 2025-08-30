
# Build a Web Scraper using beautful soup or Spacy 

# the GPay Trnsaction will be in HTML file INSIDE ( the GoogleTakeout.ZIP file )

# USe the Parent Projec tdir ( src ) to save otehr fodler inside it usign os.makedirs(  name , exist_ok = True )
#  is much better than os.mkdir 

# parent project dir -> os.path.abspath( os.path.join(os.path.dirname(__file__), '..'))


import zipfile , re , os 
import pandas as pd 


zip_folder_path = "D:\This Project\Placement_2025\Mine_GPay\GTakeout.zip"
files_to_extract =  ['Takeout/Google Pay/My Activity/My Activity.html']

# dir of the Whole  Project 
base_project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# TO Escape from re-naming  Issue ( tostore RAW HTML PAGE of transactions )
destination_folder  =  os.path.join(base_project_dir, 'raw_payments')
destination_file  = "my_activity.html"


# make dest fodle rif NOT exist 
if not os.path.exists( destination_folder) : 
    os.makedirs( destination_folder , exist_ok=True  )


with zipfile.ZipFile( zip_folder_path , "r") as zip_open : 
    # lsit all the folder paths
    for file_ in files_to_extract : 

     with zip_open.open( file_ ,"r" ) as html_f : 

        # create anew destiantion for thsi file in enw foder jsut created dest 
        new_file_path = os.path.join( destination_folder , destination_file)

        # writ inbin format as html coent is writen ontxt file 
        with open( new_file_path , "wb") as f1 : 
           f1.write( html_f.read() )
        print("The HTML FILE of Payments  was successfuly Loaded . ")

    


from bs4 import BeautifulSoup  

# html file si save lcoally so jsut read it 

file_path  = 'my_activity.html'
folder_path = destination_folder

full_path = os.path.join( folder_path , file_path )

with open( full_path , "r" , encoding='utf-8') as f : 
    html_page = f.read()


# Make a BBeautiful SOup Object ( bs4 ) , which can read Html content and lxml parser 
soup =  BeautifulSoup( html_page , 'lxml')

pays = soup.find_all('div' , class_ = 'content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1')

pay_data = []

for pay in pays : 
    pay_data.append(pay.get_text() ) 


# extra ( mode of apymrn status etc )
extras = soup.find_all('div' , class_ = 'content-cell mdl-cell mdl-cell--12-col mdl-typography--caption')

extra_data = []

for extra in extras : 
    extra_data.append( extra.get_text() ) 

'' ' bs4.BeautifulSoup( html_parsed_content <alongwith tags > , "lxml" ) and  then usinf this soup obj '
'holding the enttire polisshed content of HTML page ( with TAGS ) , '
'lis = soup.find_all( <tag> , class/id )'

'to find alinstance sudner this atg in whole HTML page '
'and then iterat over this using lsit --> for i in lis '''


# Expore this data into CSV format 

def extract_pays( gpay_statement ) : 
    pattern_amount = r'^Paid ₹([\d.]+)' 
    # regex shoudl sue ( either a digit or a decimal) and find multiple ppssible occurens of this WHOLE group 
    
    pattern_merchant  = r'to\s(.*)\susing'
    pattern_acc = r'XXXXXX(\d{4})'
    pattern_date =r'(\d{1,2}\s\w{3}\s\d{4})'
    pattern_time =r'(\s\d{2}:\d{2}:\d{2})'

    # to get TEXT content Inside the GROUP (whic was dynamic for eahc tranaction ) of the apttenr we were finding 
    amount = re.search( pattern_amount , gpay_statement ).group(1)
    merch = re.search( pattern_merchant , gpay_statement ).group(1)
    acc_no = re.search( pattern_acc , gpay_statement ).group(1)
    date = re.search( pattern_date , gpay_statement ).group(1)
    time = re.search( pattern_time , gpay_statement ).group(1)

    return amount , merch , acc_no , date , time 


# COnver tot rpoper Dataframe ( Dataset )

amounts = []
merchant =[]
acc_no = []
date  = []
time = []

status  = []

for text , text_status in zip(pay_data , extra_data ) : 
   
    # Using try-exccept lock if failed Transaction 
    
    try : 

        am , merch , acc , dt ,tm  = extract_pays( text )

        pat_status = r'(Completed|Failed)'
        st = re.search( pat_status , text_status ).group(1)

        amounts.append( am )
        merchant.append( merch )
        acc_no.append( acc )
        date.append( dt )
        time.append( tm )
        status.append( st )
        
    except : 
        print(text )
        print( "NO transaction Statement found\n ")


# final dataset 

df = pd.DataFrame( {'amounts ( in ₹ )' : amounts , 
                    'merchants' : merchant , 
                    'Acc No.' : acc_no , 
                    'Date' : date , 
                    'Time' : time , 
                    'Status' : status  
                    })

artifacts_folder = os.path.join(base_project_dir, 'artifacts')
folder_name = 'artifacts'
new_folder_path= os.path.join( artifacts_folder , folder_name )


os.makedirs( os.path.join( artifacts_folder , folder_name) , exist_ok=True     )


dataset_name = 'transactions.csv'

df.to_csv( os.path.join(new_folder_path  , dataset_name ) , index= False )
print( "The Dataset of Transactions was made successfully .")
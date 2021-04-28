
import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import os


# =================
# dataframes needed
# =================

rx_class_output = pd.DataFrame(
    {
        'RxClassID': [123, 123, 123, 456],
        'MedCode': [1,2,3,56],
        'MedName':['levothyroxine', 'liothyronine', 'thyroid (USP)', 'metformin']
    }
)


# ======================
# other variables needed
# ======================

json_output = '''
{
    "data": 0.8
}
'''


# ================
# sidebar elements
# ================

# section to create the database
st.sidebar.title('Set up database')
st.sidebar.write('Click the button below to create or update the MEPS database to allow for this to work')
run_db_load = st.sidebar.button('Update/Create Database')

# section for RxClass Information
st.sidebar.title('RxClass Section')
st.sidebar.write('Enter information below for the list of medications that you want')
id_entered = st.sidebar.text_input('Enter RxClass ID')
treatment_parameter = st.sidebar.multiselect('Choose Medication Effect', ['May Treat', 'May Prevent'])
dosage_form = st.sidebar.multiselect('Choose Dosage Form', ['tablet', 'capsule', 'liquid'])
run_rxclass = st.sidebar.button('Run RxClass and MEPS distribution')


# ===============
# inline elements
# ===============

st.title('Welcome to the CodeRx MDT')
st.header('Instructions')
st.write('1. Click the "Update/Create Database button in the side menu')
st.write('2. Enter \'123\' into the textbox labeled "Enter RxClass ID"')
st.write('3. Select "May Treat" from the "Choose Medication Effect" multiselect box')
st.write('4. Select "Liquid" from the "Choose Dosage Form" multiselect box')
st.write('5. Click "Run RxClass and MEPS distribution"')
st.write('6. Repeat Steps 2-5 with \'456\' as the RxClass ID and any values you want for the multiselect boxes')


st.header('Output of Instructions Above')

if run_db_load:
    
    st.write('loading database...')
    for i in range(30):
        time.sleep(0.1)
    st.write('database finished loading.')


if run_rxclass:
    
    rx_class_output = rx_class_output[rx_class_output['RxClassID'] == int(id_entered)] # filters the output df to rows that have RxClassID provided
    st.write('Medication effect selected: ', treatment_parameter) # grabs all items selected and puts in dict
    st.write('First effect selected: ', treatment_parameter[0]) # subsets the dict to get only the first item in string form
    st.write('Dosage forms selected: ', dosage_form) # grabs all items selected and puts in dict
    st.write('RxClassID selected: ', id_entered) # string value of number entered
    st.write('Rx Class API running...')
    st.write('RxClass Information Returned')
    st.write(rx_class_output)
    st.write('Check the folder that your Streamlit file is in for a surprise...')
    rx_class_output.to_csv(os.getcwd()+'\df.csv',index=False)
    st.write('...dataframe written to CSV and waiting for you!')

    
    
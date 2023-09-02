import openpyxl
import pandas as pd

def excel_to_json(input_excel_path):
    try:
        excel_df = pd.read_excel(input_excel_path)
        json_str = excel_df.to_json(orient='records')
        return json_str
    except Exception as e:
        return str(e)

input_excel_path = r'C:\\Users\\JEEVIKA P\\Desktop\\dataset.xlsx'
json_data = excel_to_json(input_excel_path)

if json_data:
    print('Excel Sheet to JSON:\n', json_data)
else:
    print('Failed to convert Excel to JSON.')

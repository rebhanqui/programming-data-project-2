#read xls file with multiple sheets in workbook
import pandas as pd

for sheet_name, df in pd.read_excel(r"DATA Files/grl52461-sup-0003-supplementary.xls", index_col=0, sheet_name=None).items():
    df.to_csv(f'output_{sheet_name}.csv', index=False, encoding='utf-8')
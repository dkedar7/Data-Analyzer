import pandas as pd
from pandas_profiling import ProfileReport

def create_report(df):
    return ProfileReport(df, title='Pandas Profiling Report',
     html={'style':{'full_width':True}}, minimal=True)
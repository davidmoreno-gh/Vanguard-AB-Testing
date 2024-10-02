

def clean_my_columns(df):
    df.columns = df.columns.str.replace(" ", "_").str.lower().str.strip()
    return df
'''
def find_duplicates(df):
    duplicates = df.duplicated(keep=False)
    df_duplicates = df[duplicates]
    return df_duplicates'''

def find_duplicates(df):
    duplicates = df.duplicated(keep=False)
    df_duplicates = df[duplicates]
    df_no_duplicates = df.drop_duplicates(keep=False)
    return df_duplicates, df_no_duplicates
    
def find_and_drop_null_rows(df):
    null_rows = df.isnull().all(axis=1)
    df_null_rows = df[null_rows]
    df_no_null_rows = df.dropna(how='all')
    return df_null_rows, df_no_null_rows


# function to calculate a cross table with rate of a given column with binary data (0-1). 

def create_cross_tab(df, stat):
    df_cross = pd.DataFrame({
        'variation': ['control', 'test'], 
        'conversion': [
            
            sum(df[df['variation'] == 'Control'][stat]),
            sum(df[df['variation'] == 'Test'][stat])
        ], 
        'total': [

            len(df[df['variation'] == 'Control']),
            len(df[df['variation'] == 'Test'])],

        'proportion':[
            sum(df[df['variation'] == 'Control'][stat]) / len(df[df['variation'] == 'Control']),
            sum(df[df['variation'] == 'Test'][stat]) / len(df[df['variation'] == 'Test'])
        ]
    })
    return df_cross
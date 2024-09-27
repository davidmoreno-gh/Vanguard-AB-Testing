

def clean_my_columns(df):
    df.columns = df.columns.str.replace(" ", "_").str.lower().str.strip()
    return df


    
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
import pandas as pd
import os


def description(df):

    counter = 0
    for row in df['Unnamed: 1'].fillna(''):
        if row != '':
            break
        counter +=1


    description = df.copy().fillna('')
    description = description.drop(description.index[counter:])
    description = pd.DataFrame(description)

    return description


def jp_data(df):
    counter = 0
    for row in df['Unnamed: 1'].fillna(''):
        if row != '':
            break
        counter +=1


    jp_data = df.copy().fillna('')
    jp_data = jp_data.drop(jp_data.index[:counter])
    headers = df.loc[counter]
    # print(headers)


    for col_numbers, hd in zip(jp_data.columns, headers):
        jp_data.rename(columns = {col_numbers : hd}, inplace = True)


    jp_data = jp_data.drop(counter)
    jp_data = pd.DataFrame(jp_data)
    jp_data.reset_index(inplace = True)
    jp_data.drop(columns= 'index', inplace = True)
    jp_data = jp_data.fillna('')

    return jp_data


def unamed_headers_blanks(jpt_complete):
    
    headers = [jpt_complete.columns[0]] + ['' for i in range(jpt_complete.shape[1]-1)]
    
    for col, hd in zip(jpt_complete.columns, headers):
        jpt_complete.rename(columns= {col : hd}, inplace=True)

    return jpt_complete



class UploadFile:
    
    def __init__(self, df):
        self.description = description(df)
        self.content = jp_data(df)


    @property
    def complete(self, replace_headers = True):
        """concat_description_data 🚨 It has to be first export into a csv file before the concatenation 
        otherwise it will ignore the 2 last empty rows that description has"""

        self.description.to_csv(f'description.csv', index = False)
        self.content.to_csv(f'data.csv', index = False)

        description = pd.read_csv('description.csv')
        data = pd.read_csv('data.csv')
        
        os.remove('description.csv')
        os.remove('data.csv')

        if replace_headers == True:
            hd_description = description.columns   # ['Type=Job Posting', 'Unnamed: 1', ...]
            hd_data = data.columns     # ['External Job Posting ID', 'Creator Username', ...]

            for hd_d, hd_desc in zip(hd_data, hd_description):
                data.rename(columns = {hd_d : hd_desc}, inplace = True)
            
            data.loc[-1] = hd_data
            data.index = data.index + 1
            data = data.sort_index()
        

        description.drop(description.columns[data.shape[1]:], axis=1, inplace=True)
        complete = pd.concat([description, data], axis=0)
        complete = unamed_headers_blanks(complete)

        return complete
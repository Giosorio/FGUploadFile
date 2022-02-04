from datetime import datetime
import os
import numpy as np
import pandas as pd


def description(df):

    counter = 0
    for row in df['Unnamed: 1']:
        if not row is np.nan:
            break
        counter +=1


    description = df.drop(df.index[counter:])
    description = pd.DataFrame(description)

    return description


def data(df):
    counter = 0
    for row in df['Unnamed: 1']:
        if not row is np.nan:
            break
        counter +=1


    data = df.drop(df.index[:counter])
    headers = df.loc[counter]
    # print(headers)


    for col_numbers, hd in zip(data.columns, headers):
        data.rename(columns = {col_numbers : hd}, inplace = True)


    data = data.drop(counter)
    data.reset_index(inplace = True)
    data.drop(columns= 'index', inplace = True)

    return data


def unamed_headers_blanks(jpt_complete):
    
    headers = [jpt_complete.columns[0]] + ['' for i in range(jpt_complete.shape[1]-1)]
    
    for col, hd in zip(jpt_complete.columns, headers):
        jpt_complete.rename(columns= {col : hd}, inplace=True)

    return jpt_complete


def complete_(description, content, replace_headers = True, unamed_hd=False):
    """concat_description_data 🚨 It has to be first export into a csv file before the concatenation 
    otherwise it will ignore the 2 last empty rows that description has"""

    description.to_csv(f'description.csv', index = False)
    content.to_csv(f'data.csv', index = False)

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
    if unamed_hd is False:
        complete = unamed_headers_blanks(complete)

    return complete



class UploadFile:
    
    def __init__(self, df):
        self.description = description(df)
        self.content = data(df)


    @property
    def content_nb(self):
        """Remove all empty columns in the content except the Modification Type column"""
        content_nb = self.content
        for col in content_nb.columns:
            if 'Modification Type' in str(col):
                continue
            elif len(content_nb[col].value_counts()) == 0:
                content_nb = content_nb.drop(columns=[col])
            elif len(content_nb[col].value_counts()) == 1 and content_nb[col].tolist()[0] == '':
                content_nb = content_nb.drop(columns=[col])
        
        return content_nb


    @classmethod
    def from_split(cls, description, content):
        df = complete_(description, content, unamed_hd=True)
        df.reset_index(inplace=True)
        df.drop(columns='index', inplace=True)
        return cls(df)


    @property
    def complete(self):
        return complete_(self.description, self.content)


    @property
    def complete_nb(self):
        return complete_(self.description, self.content_nb)


    def download_csv(self, f_name, comms='', set_datetime=True, drop_empty_columns=False):
        if set_datetime == True:
            for i in self.description.index:
                if self.description.iloc[i,0] is np.nan:
                    continue
                elif 'Comments=' in self.description.iloc[i,0]:
                    self.description.iloc[i,0] = f"Comments={comms} {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"
        
        if drop_empty_columns==True: 
            self.complete_nb.to_csv(f_name, index=False)
        else:
            self.complete.to_csv(f_name, index=False)
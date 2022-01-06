import pandas as pd
from UploadFile import UploadFile


def test1():

    df = pd.read_excel('FG_User_download.xlsx')
    # print(df)

    upf_1 = UploadFile(df)
    # print(upf_1.description)
    print(upf_1.content)
    print('\n')

    df_c = upf_1.content
    df_c.drop(df_c.index[4:], inplace=True)
    print(df_c)
    print('\n')

    upf_1.content = df_c
    print(upf_1.content)

    print(upf_1.complete)

    


def test2():

    f_name = 'Giovanni,Osorio'
    wtf = f_name.split(',')
    print(wtf)

    
    # p1 = FullnameCll(f_name)
    # print(p1.first)

if __name__ == '__main__':
    test1()
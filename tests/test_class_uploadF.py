import pandas as pd
# from FGUploadFile.uploadfile import UploadFile

import sys
sys.path.insert(1, '/Users/giosorio29/Documents/programming_projects/UploadFile/FGUploadFile')
from uploadfile import UploadFile


def test1():

    pth = '/Users/giosorio29/Documents/programming_projects/UploadFile/xl_files/'
    df = pd.read_excel(pth + 'FG_User_download.xlsx')
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

    pth = '/Users/giosorio29/Documents/programming_projects/UploadFile/xl_files/'
    df = pd.read_csv(pth + 'Custom_field_UPLOAD.csv')
    # print(df)

    upf_1 = UploadFile(df)
    
    upf_1.download_csv(pth +'test_upf.csv', comms='Data Maintenance')

    

if __name__ == '__main__':
    test1()
    test2()
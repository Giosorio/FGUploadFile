# FGUploadFile
Class UploadFile creates an object UploadFile that allows to to split the description and content from a Fieldglass upload file. Once the content has been modified it allows you to concatenate the description again.


# HOW TO IMPORT
**import** pandas **as** pd

**from** FGUploadFile **import** uploadfile **as** upf
```
import pandas as pd
from FGUploadFile import uploadfile as upf

df = pd.read_excel('xl_files/FG_BU_download.xlsx')
print(df)

upf_1 = upf.UploadFile(df)

df_2 = pd.read_excel('xl_files/Custom_Field_BU_Association_U.xlsx')
upf_2 = upf.UploadFile(df_2)
```

## Description
```
print(upf_1.description)

                         Type=Business Unit Upload  ...                              
0                                 Transaction=True  ...                   NaN
1                 Language=English (United States)  ...                   NaN
2   Number Format=#,##9.99 (Example: 1,234,567.99)  ...                   NaN
3                           Date Format=MM/DD/YYYY  ...                   NaN
4                                        Comments=  ...                   NaN
5                                              NaN  
```

## Content
```
print(upf_1.content)

                                 Modification Type  ...          Legal Entity
7                                                A  ...        Legal_Entity_1
8                                                A  ...        Legal_Entity_2
9                                                A  ...        Legal_Entity_3
10                                               A  ...        Legal_Entity_4

print(upf_2.content)

  Modification Type Custom Field Name Module Name Business Unit Code
0               NaN               NaN          wk               BU_0
1               NaN               NaN          wk               BU_1
2               NaN               NaN          wk               BU_2
3               NaN               NaN          wk               BU_3
4               NaN               NaN          wk               BU_4
5               NaN               NaN          wk               BU_5
6               NaN               NaN          wk               BU_6
7               NaN               NaN          wk               BU_7
8               NaN               NaN          wk               BU_8
9               NaN               NaN          wk               BU_9

```

## Content_nb, NO BLANK COLUMNS EXCEPT for Modification Type
```
print(upf_2.content_nb)

  Modification Type Module Name Business Unit Code
0               NaN          wk               BU_0
1               NaN          wk               BU_1
2               NaN          wk               BU_2
3               NaN          wk               BU_3
4               NaN          wk               BU_4
5               NaN          wk               BU_5
6               NaN          wk               BU_6
7               NaN          wk               BU_7
8               NaN          wk               BU_8
9               NaN          wk               BU_9
```

## Complete, concatenate Description and Content
```
print(upf_1.complete)

                         Type=Business Unit Upload  ...                              
0                                 Transaction=True  ...                   NaN
1                 Language=English (United States)  ...                   NaN
2   Number Format=#,##9.99 (Example: 1,234,567.99)  ...                   NaN
3                           Date Format=MM/DD/YYYY  ...                   NaN
4                                        Comments=  ...                   NaN
5                                              NaN  ...                   NaN
6                                Modification Type  ...          Legal Entity
7                                                A  ...        Legal_Entity_1
8                                                A  ...        Legal_Entity_2
9                                                A  ...        Legal_Entity_3
10                                               A  ...        Legal_Entity_4

print(upf_2.complete)

   Type=Custom Field Business Unit Association Upload                    
0                                    Transaction=True           NaN          NaN                 NaN
1                   Language=English (United Kingdom)           NaN          NaN                 NaN
2                                           Comments=           NaN          NaN                 NaN
3                                                 NaN           NaN          NaN                 NaN 
0                                   Modification Type  Custom Field  Module Name  Business Unit Code
1                                                 NaN           NaN           wk                BU_0
2                                                 NaN           NaN           wk                BU_1
3                                                 NaN           NaN           wk                BU_2
4                                                 NaN           NaN           wk                BU_3
5                                                 NaN           NaN           wk                BU_4
6                                                 NaN           NaN           wk                BU_5
7                                                 NaN           NaN           wk                BU_6
8                                                 NaN           NaN           wk                BU_7
9                                                 NaN           NaN           wk                BU_8
10                                                NaN           NaN           wk                BU_9
```

## Complete_nb, concatenate Description and Content_nb NO BLANK COLUMNS EXCEPT for Modification Type
```
print(upf_2.complete_nb)

   Type=Custom Field Business Unit Association Upload                     
0                                    Transaction=True          NaN                 NaN        
1                   Language=English (United Kingdom)          NaN                 NaN          
2                                           Comments=          NaN                 NaN
3                                                 NaN          NaN                 NaN
0                                   Modification Type  Module Name  Business Unit Code
1                                                 NaN           wk                BU_0
2                                                 NaN           wk                BU_1
3                                                 NaN           wk                BU_2
4                                                 NaN           wk                BU_3
5                                                 NaN           wk                BU_4
6                                                 NaN           wk                BU_5
7                                                 NaN           wk                BU_6
8                                                 NaN           wk                BU_7
9                                                 NaN           wk                BU_8
10                                                NaN           wk                BU_9
```

## Download CSV format, it marks the date and time the download is generated and allows you to put a comment (optional)
```
upf_1.download_csv('BU_UPLOAD.csv', comms='[COMMENT]')

>>>
                        Type=Business Unit Upload  ...                              
                                 Transaction=True  ...                   
                 Language=English (United States)  ...                   
   Number Format=#,##9.99 (Example: 1,234,567.99)  ...                   
                           Date Format=MM/DD/YYYY  ...                   
          Comments=[COMMENT] 01/02/2022, 19:46:17  ...                  
                                              NaN  ...                   
                                Modification Type  ...          Legal Entity
                                                A  ...        Legal_Entity_1
                                                A  ...        Legal_Entity_2
                                                A  ...        Legal_Entity_3
                                                A  ...        Legal_Entity_4

upf_2.download_csv('Custom_Field_BU_assoc.csv', drop_empty_columns=True)

>>>
  Type=Custom Field Business Unit Association Upload                     
                                    Transaction=True                
                   Language=English (United Kingdom)                    
                                           Comments=          
                                                                          
                                   Modification Type  Module Name  Business Unit Code
                                                               wk                BU_0
                                                               wk                BU_1
                                                               wk                BU_2
                                                               wk                BU_3
                                                               wk                BU_4
                                                               wk                BU_5
                                                               wk                BU_6
                                                               wk                BU_7
                                                               wk                BU_8
                                                               wk                BU_9
```


# HOW TO INSTALL IN YOUR ENVIRONMENT

```
pip install git+https://github.com/Giosorio/FGUploadFile@[VERSION -- Check in Tags of the repository]
```

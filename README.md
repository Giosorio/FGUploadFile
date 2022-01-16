# FGuploadfile
Class UploadFile creates an object UploadFile that allows to to split the description and content from a Fieldglass upload file. Once the content has been modified it allows you to concatenate the description again.


# HOW TO IMPORT
**import** pandas **as** pd

**from** FGUploadFiles **import** uploadfile **as** upf
```
import pandas as pd
from FGUploadFiles import uploadfile as upf

df = pd.read_excel('xl_files/FG_BU_download.xlsx')
print(df)

upf_1 = upf.UploadFile(df)
```

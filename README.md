# Secrets-Autoposter
Parse and post Gsheet data to facebook

Secrets-Autoposter is a simple yet useful poster, that can parse data from a
google sheets database, let you quickly edit them and post them to your facebook
page.

### Dependencies
The script is tested and fuctioning correctly using the following packages:
-python 3.7.1
-pandas 0.24.1
-gspread 3.1.0
-oauth2client 4.1.3
-facebook sdk 3.1.0
-PyQt5 5.12
-PyQt5-sip 4.19.14
-PyOpenSSL 19.0.0

### Instructions
Open the settings.midget file with a text editor and type:
-Your facebook Page id
-Your facebook API key
-Name of the spreadsheet you are pulling the data from
-Your google sheets API access json. Place it on the same folder and
type it's name(without the .json extension)
-Run main.py with python3

The script is uploaded with some hardcoded settings. We haven't programmed any database
identification function but we intend to do so in the future. For now, in order to personalize it,
change the titles of the columns of the "data" Dataframe and of course customize your own TextSet
and print functions. 
You can read and easily understand the script, and the total amount of code is not much.
Leave a message in if you are interested in a screenshot of the google sheet
that I used, in order to do your job without reading any code.

### Known Bugs
No bugs have been found yet, although abusing the post or move to archive buttons before qt5
releases them might lead to script disfunction.

For further documentation or help please leave a message or email at stzaneti@physics.auth.gr

Secrets-Autoposter by shatt3rbb and GeorgeGrig.

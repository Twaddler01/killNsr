# killNsr
![#f03c15](https://www.iconsdb.com/icons/download/color/f03c15/circle-16.png) `About`

- Basic Python project (integrated with kivy) to utilize search/replace in bulk.
- The goal is to produce an Android app that will simplify RegEx expressions by removing all new-line characters and allowing cut/replacement of text, such as for easily modifying HTML/XML files in bulk (by files in a folder).
- Any UTF-8 filetype will be allowed.

![#f03c15](https://www.iconsdb.com/icons/download/color/f03c15/circle-16.png) `Changelog`

09-26-2023:
- Added custom search/replace options.
- Hid elements of custom search/replace options until line removal is complete. Might make this optional in future updates.
- Plan to add a second layout after initial "setup" screen, as it just seems more practical instead of hiding/showing other options.
- Next project will be a function designed to allow "templates" of user search/replace strings and give room for multiple search/replace options to be executed simultaneously. Right now the custom search/replace function with attributes is not yet used.
- Need to clean .py, as many functions are redundant and other code is even unused or unnecessary.

09-21-2023:
- Using Kivy "Factory" for multiple layouts, so updated .kv filename to better suit setup.
- Now have a working log output display. Will eventually add an "export to file" option for logs.
- Working on main core coding once layout is updated.
- Need to remove unnecessary TextInput fields which were solely for testing.
- Plan to update notes/old code in .py and clean up file while updating functions for file processing.

09-16-2023:
- Added first 2 files: 'main.py' and 'my.kv'.
- Currently in design phase. Kivy elements set up but with very limited code so far. 

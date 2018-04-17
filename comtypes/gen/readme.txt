used by pyinstaller

Locate PyInstaller folder..\hooks, e.g. C:\Program Files\Python\Lib\site-packages\PyInstaller\hooks.

Create file hook-pandas.py with contents (or anything similar based on your error):

hiddenimports = ['pandas._libs.tslibs.timedeltas']
Save it + I deleted .spec file, build and dist folders just to be sure.

Run pyinstaller -F my_app.py.

This fix should work as long as you don't upgrade or reinstall PyInstaller. So you don't need to edit .spec file.


pyinstaller --hidden-import comtypes.gen._944DE083_8FB8_45CF_BCB7_C477ACB2F897_0_1_0 --hidden-import comtypes.gen.UIAutomationClient autoLogin.py

pyinstaller --hidden-import comtypes.gen._944DE083_8FB8_45CF_BCB7_C477ACB2F897_0_1_0 --hidden-import comtypes.gen.UIAutomationClient autoLogin.py

copy ht_client.json.env dist\autoLogin\

cd dist\autoLogin

autoLogin

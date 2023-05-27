code = input()
code = code.lstrip("['")
code = code.rstrip("']")
code = code.split("', '")
 
print(code)
 
code_decrypted = ""
 
for code_c in code:
    code_decrypted += chr(int(code_c[5] + code_c[6]))
 
code_decrypted = int(code_decrypted)
 
print(code_decrypted)

# import pyautogui

# for i in range(500):
#     pyautogui.click()
# Texti Was Created By Daniel Dobromylskyj
# Texti Is Under The "Open Source" Licence
from api import terminal, file_access

f = file_access()
t = terminal()

while True:
    for i in range(100):
        print("")
    print("Do You Wish To Load A File Or Create New?")
    print("1 = Create New")
    print("2 = Load From File")
    print("")
    LoadOrNew = input("Querry: ")


    if LoadOrNew == "1":
        text = [""]
        break
    elif LoadOrNew == "2":
        FileName = input("File Name / Path: ")
        text = f.read_file(FileName).split("\n")
        break

    else:
        print("INVALID")



# Each Object In List Is A Dif Line


def Update(text):
    # Clear Display
    for i in range(100):
        print("")

    print("-- Texti - Version 1.0.0 --")
    print("")
    # Display Text With Lines
    line_number = 1
    for LINE in text:
        print(str(line_number) + ") ", LINE)
        line_number += 1

    print("")

Update(text)

while True:
    UserInput_Line = -1
    UserInput_Text = ""
    try:
        UserInput_Line = input("Line ('save' to save / close): ")
        if UserInput_Line == "save":
            pass
        UserInput_Text = input("Text: ")
    except ValueError:
        pass

    if UserInput_Line != "save":
        UserInput_Line = int(UserInput_Line) - 1
    else:
        UserInput_Location = input("Location: ")
        if f.is_file(UserInput_Location):
            string_to_write = ""
            for line in text:
                string_to_write = string_to_write + line + "\n"
            f.write_to_file(UserInput_Location, string_to_write[:-1]) # The [:-1] Removes The Last \n
            break
        else:
            t.mkfile(UserInput_Location)
            string_to_write = ""
            for line in text:
                string_to_write = string_to_write + line + "\n"
            f.write_to_file(UserInput_Location, string_to_write[:-1])  # The [:-1] Removes The Last \n
            break

    if UserInput_Line > 10000: # Dont Make Too High Of A Word Count Cos It Takes Too Long To Display
        Update(text)
        print("The Previous Input Has Not Been Done Due To Too High Of A Line Number.")

    elif len(text) >= UserInput_Line + 1 and UserInput_Line != -1: # If Line Already Exists
        text[UserInput_Line] = UserInput_Text
        Update(text)

    elif UserInput_Line == -1: # Check If A Valid Input Was Made If It Wasn't Pass
        Update(text)
        print("The Previous Line Input Was Incorrect And No Changes Have Been Made.")
        pass

    else:
        for i in range((UserInput_Line + 1) - len(text)):#If Line Doesn't Exist Already:
            text.append("")
        text[UserInput_Line] = UserInput_Text
        Update(text)

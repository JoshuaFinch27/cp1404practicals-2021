"""
CP1404/CP5632 Practical - Hexadecimal colour lookup program
"""

NAME_TO_HEX = {"aliceblue": "#f0f8ff", "antiquewhite": "faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
               "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "aquamarine1": "#7fffd4",
               "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff", "azure2": "#e0eeee",
               "azure3": "#c1cdcd", "azure4": "#838b8b"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in NAME_TO_HEX:
        print(f"{colour_name} is {NAME_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
for colour_name, colour_hex_code in NAME_TO_HEX.items():
    print(f"{colour_name:15} --> has the hexadecimal code of {colour_hex_code}")


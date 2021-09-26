"""
CP1404 prac_06 - Programming language client code

'On paper' first attempt of last segment of task:

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)


"""

from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python.__str__())

languages = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)

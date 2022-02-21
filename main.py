# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import globalevent
from maakmeervoud import maakmeervoud
from woorden import vowelcount


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    event = globalevent.globalEvent()
    count = vowelcount("oeluuluilkfm")
    maakmeervoud('test')
    if ['a', 'b', 'c'] == ['a', 'b', 'c']:
        print("is true")
    print(f"{count}")
    print_hi(f'PyCharm \n\nResponse : {event.text()}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

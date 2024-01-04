# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fzf import Fzf, fzf

from utils_ag.io import select_from_list


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    res = select_from_list(["aa", "bb", "cc"])

    print(res)
    # chooser = Fzf()
    # choices = chooser.prompt([1, 2, 3])
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

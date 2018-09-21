# Mats Verheyen
# Pizza Calculator Python
# Vars
from os import system, name

Xsmall = 0
Xmedium = 0
Xlarge = 0
medium = 0
small = 0
large = 0
verder = True
PRICESMALL = 3.99
PRICEMEDUIM = 5.99
PRICELARGE = 9.00
totalSmall = 0.00
totalMedium = 0.00
totalLarge = 0.00
total = 0.00

#Clear console
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#Colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Loop
while verder == True:
    clear()
    print(bcolors.HEADER + 'Welke pizza wilt je?' + bcolors.ENDC)
    print(bcolors.OKBLUE + '[1] - Small' + bcolors.ENDC)
    print(bcolors.OKGREEN + '[2] - Medium' + bcolors.ENDC)
    print(bcolors.FAIL + '[3] - Large\n' + bcolors.ENDC)
    size = raw_input();
    if size == '1':
        print(bcolors.OKBLUE + '\nHoeveel wil je er?\n' + bcolors.ENDC)
        Xsmall = raw_input()
        small =+ int(Xsmall)
        choice = raw_input(bcolors.OKBLUE + '\nWil je nog meer bestellen?\n\n' + bcolors.ENDC)
        if choice == "Nee" or choice == "nee":
            clear()
            verder = False
            pass
        pass
    elif size == '2':
        print(bcolors.OKBLUE + '\nHoeveel wil je er?\n' + bcolors.ENDC)
        Xmedium = raw_input()
        medium =+ int(Xmedium)
        choice = raw_input(bcolors.OKBLUE + '\nWil je nog meer bestellen?\n\n' + bcolors.ENDC)
        if choice == "Nee" or choice == "nee":
            clear()
            verder = False
        pass
    elif size == '3':
        print(bcolors.OKBLUE + '\nHoeveel wil je er?\n' + bcolors.ENDC)
        Xlarge = raw_input()
        large =+ int(Xlarge)
        choice = raw_input(bcolors.OKBLUE + '\nWil je nog meer bestellen?\n\n' + bcolors.ENDC)
        if choice == "Nee" or choice == "nee":
            clear()
            verder = False
        pass
    pass

#Calculator
if verder == False:
    totalSmall = small * PRICESMALL
    totalMedium = medium * PRICEMEDUIM
    totalLarge = large * PRICELARGE
    total = totalLarge + totalSmall + totalMedium
    float(total)
    round(total, 2)
    print(bcolors.HEADER + "Totaalprijs: " + bcolors.ENDC + bcolors.OKGREEN + str(total)  + bcolors.ENDC)
    pass

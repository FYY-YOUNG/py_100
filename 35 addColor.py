class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print ( "HEADER Hello World" + bcolors.HEADER)
print ( "OKBLUE Hello World" + bcolors.OKBLUE)
print ( "OKGREEN Hello World" + bcolors.OKGREEN)
print ( "WARNING Hello World" + bcolors.WARNING)
print ( "FAIL Hello World" + bcolors.FAIL)
print ( "ENDC Hello World" + bcolors.ENDC)
print ( "BOLD Hello World" + bcolors.BOLD)
print ( "UNDERLINE Hello World" + bcolors.UNDERLINE)
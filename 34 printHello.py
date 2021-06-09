
def printHello():
    print('Hello World')

def use_printHello():
    for i in range(3):
        printHello()

if __name__ == '__main__':
    use_printHello()
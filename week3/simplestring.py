class SimpleString:
    """
    Class that takes a string as input from user and
    prints it to screen in upper case
    """

    def __init__(self):       
        pass

    def getString(self):
        """
        Asks for an input string from user and stores
        the string in variable self.string
        """
        self.string = raw_input('Enter String value: ')

    def printString(self):
        """
        Prints the string in upper case
        """
        print self.string.upper()


if __name__ == '__main__':
    s = SimpleString()
    s.getString()
    s.printString()

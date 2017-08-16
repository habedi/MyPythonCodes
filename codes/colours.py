from termcolor import colored

class ColouredText(object):
    """ Colourizing Text """

    @staticmethod
    def yellow(text):
        return colored(text, 'yellow', attrs=['bold'])

    @staticmethod
    def green(text):
        return colored(text, 'green', attrs=['bold'])
    
    @staticmethod
    def red(text):
        return colored(text, 'red', attrs=['bold'])
    
    @staticmethod
    def cyan(text):
        return colored(text, 'cyan', attrs=['bold'])

    @staticmethod
    def white(text):
        return colored(text, 'white', attrs=['bold'])

    @staticmethod
    def magenta(text):
        return colored(text, 'magenta', attrs=['bold'])

    @staticmethod
    def yellow(text):
        return colored(text, 'yellow', attrs=['bold'])

    @staticmethod
    def blue(text):
        return colored(text, 'blue', attrs=['bold'])

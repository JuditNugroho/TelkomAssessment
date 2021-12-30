from services.cliservice import CLIService
from interfaces.cliinterface import CLIInterface


class CLIController(CLIInterface):

    def __init__(self):
        """ Initialization of class controller """
        self.__repo = CLIService()

    def start(self):
        """ Function to start program """
        self.__repo.start()

    def on_user_input(self, user_input: str):
        """ Function to handle user input """
        self.__repo.on_user_input(user_input)

    def stop(self):
        """ Function to stop program """
        self.__repo.stop()
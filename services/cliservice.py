from interfaces.cliinterface import CLIInterface
from services.validationservice import ValidationService


class CLIService(CLIInterface):
    def start(self):
        """ Function to start program """
        print("Welcome to CLI App ")

    def on_user_input(self, user_input: str):
        """ Function to handle user input """
        user_input = user_input.lstrip().rstrip().split(' ')
        ValidationService().start_validation(user_input)

    def stop(self):
        """ Function to stop program """
        print("Thank you")

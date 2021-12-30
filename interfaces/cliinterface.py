from abc import abstractmethod, ABC


class CLIInterface(ABC):

    @abstractmethod
    def start(self):
        """ Function to start program """
        pass

    @abstractmethod
    def on_user_input(self, user_input: str):
        """ Function to handle user input """
        pass

    @abstractmethod
    def stop(self):
        """ Function to stop program """
        pass

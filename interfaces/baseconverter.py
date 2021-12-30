from abc import abstractmethod, ABC


class BaseConverterInterface(ABC):

    @abstractmethod
    def start(self, data: list) -> str:
        """ Function to start conversion """
        pass

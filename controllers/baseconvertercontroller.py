from interfaces.baseconverter import BaseConverterInterface


class BaseConverterController(BaseConverterInterface):
    repo = None

    def __init__(self, repo=None):
        self.repo = repo()

    def start(self, data: list) -> str:
        return self.repo.start(data)

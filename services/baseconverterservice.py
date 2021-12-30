import json
from interfaces.baseconverter import BaseConverterInterface


class JsonConverterService(BaseConverterInterface):
    def start(self, data: list) -> str:
        """ Function to start conversion to json """
        result = []
        for index, row in enumerate(data):
            result.append({index: row})
        result = json.dumps(result, indent=4)
        return result


class TextConverterService(BaseConverterInterface):
    def start(self, data: list) -> str:
        """ Function to start conversion to text """
        result = ""
        for row in data:
            result += str(row)
        return result

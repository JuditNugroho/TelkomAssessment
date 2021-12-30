import os
from pathlib import Path
from helpers.constants import TypeFileVar, FlagVar
from controllers.baseconvertercontroller import BaseConverterController
from services.baseconverterservice import TextConverterService, JsonConverterService


class ConverterService:
    file_input = ""
    output_dir = ""
    type_file = TypeFileVar.TEXT_VAR.value

    def start_conversion(self, commands):
        """ Function to start conversion of file """
        status = self.check_conversion(commands)
        if not status:
            return False
        status = self.process_conversion()
        if not status:
            return False
        print("Finish conversion file ....")
        print(f"Output file in {self.output_dir} ....")

    def check_conversion(self, commands):
        """ Function to check file is valid for conversion """
        if not commands:
            # If the command is not available
            return True

        data = commands[0]

        if not isinstance(data, dict):
            # If command is not dictionary will check is valid parameter or is file name
            if isinstance(data, str) and self.file_input == "":
                # Get file name of file input
                self.file_input = data
                commands.pop(0)
                return self.check_conversion(commands)
            else:
                # If user input not valid parameter will raise error bad parameter
                print(f"Bad Parameter of {data}.")
                return False

        if data.get('key') == FlagVar.TYPE_FILE_COMMAND.value:
            # If flag is -t or change type file
            if data.get('value') not in (TypeFileVar.JSON_VAR.value, TypeFileVar.TEXT_VAR.value):
                # If flag type is not defined so will raise error
                print("Can only be converted in json / text, Please try again")
                return False

            self.type_file = data.get('value')
        elif data.get('key') == FlagVar.OUTPUT_FILE_COMMAND.value:
            # If flag is -o or change output file
            self.output_dir = data.get('value')
        elif data.get('key') == FlagVar.HELP_COMMAND.value:
            self.show_help()
            return

        commands.pop(0)
        return self.check_conversion(commands)

    def process_conversion(self):
        """ Function to proccess conversion of file """
        my_file = Path(self.file_input)

        if not my_file.is_file():
            # If file is not exists will raise error
            print("File not exists, Please try again")
            return False

        if my_file.suffix != ".log":
            print("Sorry, this tool can only convert log file. Please try again")
            return False

        if self.output_dir == "":
            file_name = my_file.stem
            file_directory = my_file.resolve().parent
            self.output_dir = f"{file_directory}/{file_name}.{self.type_file}"

        rows = my_file.read_text().splitlines()

        result = ""

        if self.type_file == TypeFileVar.JSON_VAR.value:
            result = BaseConverterController(repo=JsonConverterService).start(rows)
        elif self.type_file == TypeFileVar.TEXT_VAR.value:
            result = BaseConverterController(repo=TextConverterService).start(rows)

        os.umask(0)
        with self.safe_open_file(self.output_dir) as outfile:
            outfile.write(result)
        return True

    def safe_open_file(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return open(path, 'w+')

    def show_help(self):
        print("------------------------------------------CLI APP HELP TOOL-----------------------------------------")
        print("Usage : mytools [Source File] [Flag Option] [command] ")
        print("Argument : file yang akan di konversi (Contoh: /var/log/example.log ")
        print("Flag Option : -t  Mengubah tipe ekstensi suatu file menjadi plaintext atau json (default : plaintext)")
        print("              -o  Destinasi file output")
        print("              -h  Menampilkan pesan bantu\n")
        print("----------------------------------------EXAMPLE CODE------------------------------------------------")
        print("Example 1 : (Mengkonversi menjadi file json) : mytools /var/log/nginx/error.log -t json")
        print("Example 2 : (Mengkonversi menjadi file text) : mytools /var/log/nginx/error.log -t text")
        print("Example 3 : (Ubah destinasi file output) : mytools /var/log/nginx/error.log -t json -o /home/a.json")
        print("Example 4 : (Untuk keluar dari program) : mytools exit")
        print("----------------------------------------------------------------------------------------------------")

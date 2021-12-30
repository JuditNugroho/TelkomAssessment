from helpers.constants import ToolsVar, FlagVar
from services.converterservice import ConverterService


class ValidationService:
    commands = []

    def start_validation(self, user_input):
        self.commands.clear()
        status = self.check_tools_is_valid(user_input)
        if not status:
            return False

        self.check_validation(user_input)
        ConverterService().start_conversion(self.commands)

    def check_tools_is_valid(self, user_input):
        if user_input[0] != ToolsVar.NAME.value:
            print("Command not found, Please try again")
            return False
        user_input.pop(0)
        return True

    def check_validation(self, user_input):
        if not user_input:
            return True
        value = user_input[0]
        if value in FlagVar.list():
            self.commands.append({'key': value})
        else:
            if self.commands:
                last_command = self.commands[-1]
                if isinstance(last_command, dict) and last_command.get('value') is None:
                    last_command['value'] = value
                else:
                    self.commands.append(value)
            else:
                self.commands.append(value)
        user_input.pop(0)
        return self.check_validation(user_input)

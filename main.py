from controllers.clicontroller import CLIController


class TelkomAssessment:
    def __init__(self):
        self.cli_app = CLIController()

    def main(self):
        self.cli_app.start()
        while True:
            input_user = input('telkom@ubuntu:~$ ')
            if "exit" in input_user:
                break
            self.cli_app.on_user_input(input_user)
        self.cli_app.stop()


if __name__ == '__main__':
    TelkomAssessment().main()

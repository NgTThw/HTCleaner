from . import commandline
import os

class ScheduleFrequence:
    MINUTE = 'MINUTE'
    HOURLY = 'HOURLY'
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    ONCE = 'ONCE'
    ONSTART = 'ONSTART'
    ONLOGON = 'ONLOGON'
    ONIDLE = 'ONIDLE'
    ONEVENT = 'ONEVENT'


class SimpleTaskScheduler:
    def __init__(self, name: str, program: str, argument: list|tuple, frequence: ScheduleFrequence, start_time: str) -> None:
        self.name = name
        self.program = os.path.normcase(program)
        if not os.path.isfile(self.program):
            raise Exception(f"Program {self.program} doesn't exists")
        self.argument = ' '.join(argument)
        self.frequence = frequence
        self.start_time = start_time
        self.enable = True

    def create(self) -> None:
        commandline.execute(f'schtasks /Create /SC {self.frequence} /TN "{self.name}" /TR "\"{self.program}\" {self.argument}" /ST {self.start_time} /F')
        if not self.enable:
            self.set_enable(False)

    def delete(self) -> None:
        commandline.execute(f'schtasks /Delete /TN "{self.name}" /F')

    def set_enable(self, is_enable: bool) -> None:
        if is_enable:
            commandline.execute(f'schtasks /Change /TN "{self.name}" /ENABLE')
            self.enable = True
        else:
            commandline.execute(f'schtasks /Change /TN "{self.name}" /DISABLE')
            self.enable = False
        
    def run(self) -> None:
        commandline.execute(f'schtasks /Run /TN "{self.name}"')

    def end(self) -> None:
        commandline.execute(f'schtasks /End /TN "{self.name}"')

### Complete In 0.4
from anwFunctions.anwReader.reader import READ_FULL


class AnwBaseModule:
    """
    Require of the Antanswer Module
    =====
    init_routine -> starting routine
    -> core quest -> view_quest -> input_quest -> reward_quest -> core_quest ...
    -> closing routine -> reset_routine -> / starting rotuine
    / finish
    =====
    """

    def __init__(self, **kwargs):
        self._reader = READ_FULL
        self.id = 0
        self.kwargs = kwargs

    def init_routine(self):
        pass

    def starting_routine(self):
        pass

    def core_quest(self):
        pass

    def view_quest(self):
        pass

    def input_quest(self):
        pass

    def reward_quest(self):
        pass

    def closing_routine(self):
        pass

    def reset_routine(self):
        pass

    def reset_init_routine(self):
        pass

    def exit_process(self):
        pass

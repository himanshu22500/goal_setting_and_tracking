from abc import abstractmethod


class GoalStorageInterface:
    @abstractmethod
    def create_goal(self):
        pass

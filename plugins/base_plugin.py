from abc import ABC, abstractmethod


class BasePlugin(ABC):

    def __init__(self):
        self.name = "Base Plugin"

    @abstractmethod
    def can_handle(self, command):
        """
        Return True if plugin can handle command.
        """
        pass

    @abstractmethod
    def execute(self, command):
        """
        Execute plugin command.
        """
        pass
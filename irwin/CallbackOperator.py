from abc import ABC, abstractmethod


class CallbackOperator(ABC):
    @abstractmethod
    def connect_callback(self, window):
        pass

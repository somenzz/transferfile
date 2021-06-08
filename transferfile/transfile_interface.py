from abc import ABC, abstractmethod


class TransferFileInterface(ABC):
    @abstractmethod
    def put(self, local_file_path, remote_file_path):
        pass

    @abstractmethod
    def get(self, local_file_path, remote_file_path):
        pass

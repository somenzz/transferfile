from abc import ABC, abstractmethod

class TransferFileInterface(ABC):

    @abstractmethod
    def put(self,local_file_path, remotepath):
        pass

    @abstractmethod
    def get(self,localpath, remote_file_path):
        pass
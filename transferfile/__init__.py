from transferfile.sftp import Sftp
from transferfile.scp import Scp
from transferfile.ftp import Ftp
from transferfile.rsync import Rsync


class TransferFactory(object):
    @classmethod
    def create(cls, type, host, username, password=None, port=None, **kwargs):

        if type.lower() == "ftp":
            return Ftp(host, username, password, port, **kwargs)

        elif type.lower() == "scp":
            return Scp(host, username, password, port, **kwargs)

        elif type.lower() == "sftp":
            return Sftp(host, username, password, port, **kwargs)

        elif type.lower() == "rsync":
            return Rsync(host, username, **kwargs)
        else:
            raise Exception(f"Unkonw transfer type: {type}")

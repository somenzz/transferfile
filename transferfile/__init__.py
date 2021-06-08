from transferfile.sftp import Sftp
from transferfile.scp import Scp

from transferfile.ftp import Ftp


class TransferFactory(object):

    @classmethod
    def create(cls,type,host,username,password,port, **kwargs):

        if type == "ftp":
            client = Ftp(host,username,password, port,kwargs)
        elif type == "scp":
            client = Scp(host,username,password,port, kwargs)
        else:
            client = Sftp(host,username,password,port,kwargs)

        return  client

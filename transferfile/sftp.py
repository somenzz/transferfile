
from transferfile.transfile_interface import TransferFileInterface

import paramiko
from paramiko import RSAKey


class Sftp(TransferFileInterface):
    def __init__(self,host,username = None,password = None, port = 22,rsa_key_file = None, rsa_key_str = None):
        # Open a transport
        transport = paramiko.Transport((host, port))
        if rsa_key_file:
            transport.connect(None, username = username, pkey = RSAKey.from_private_key_file(rsa_key_file))
        elif rsa_key_str:
            pass
        else:
            transport.connect(None, username, password)

        self._sftp = paramiko.SFTPClient.from_transport(transport)


    def put(self,local_file_path, remotepath):
        '''
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        '''

        self._sftp.put(local_file_path,remotepath,confirm=True)

    def get(self,localpath, remote_file_path):
        self._sftp.get(remote_file_path,localpath)


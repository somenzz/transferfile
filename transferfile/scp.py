
from transferfile.transfile_interface import TransferFileInterface

import paramiko

from scp import SCPClient

class Scp(TransferFileInterface):
    def __init__(self,host,username = None,password = None, port = 22, load_system_host_keys = False):
        # Open a transport
        self._client = paramiko.SSHClient()
        self._client.load_system_host_keys()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if load_system_host_keys:
            print("loading...")
            self._client.load_system_host_keys()
            self._client.connect(host)
        else:
            self._client.connect(host, port, username, password)
        self._scp = SCPClient(self._client.get_transport())

    def put(self,local_file_path, remotepath):
        '''
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        '''
        self._scp.put(local_file_path,remotepath)

    def get(self,localpath, remote_file_path):
        self._scp.get(remote_file_path,localpath)

    def __del__(self):
        self._scp.close()
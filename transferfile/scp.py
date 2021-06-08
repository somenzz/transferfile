from transferfile.transfile_interface import TransferFileInterface

import paramiko

from scp import SCPClient


class Scp(TransferFileInterface):
    def __init__(
        self,
        host,
        username=None,
        password=None,
        port=22,
        load_system_host_keys=False,
        rsa_file=None,
        rsa_pwd=None,
    ):
        # Open a transport
        if not port:
            port = 22

        self._client = paramiko.SSHClient()
        self._client.load_system_host_keys()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if load_system_host_keys:
            print("loading system host keys...")
            self._client.load_system_host_keys()
            self._client.connect(host, port, username=username)
        elif rsa_file:
            key = paramiko.RSAKey.from_private_key_file(rsa_file, rsa_pwd)
            self._client.connect(host, port, username=username, pkey=key)
        else:
            self._client.connect(host, port, username=username, password=password)

        self._scp = SCPClient(self._client.get_transport())

    def put(self, local_file_path, remotepath):
        """
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        """
        self._scp.put(local_file_path, remotepath)

    def get(self, localpath, remote_file_path):
        self._scp.get(remote_file_path, localpath)

    def __del__(self):
        self._scp.close()

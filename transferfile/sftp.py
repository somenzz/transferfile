from transferfile.transfile_interface import TransferFileInterface
from pathlib import Path
import paramiko
import os

class Sftp(TransferFileInterface):
    def __init__(
        self,
        host,
        username=None,
        password=None,
        port=22,
        load_system_host_keys=False,
        rsa_file=None,
        rsa_pwd=None,
        **kwargs
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

        self._sftp = None

    def create(self):
        if not self._sftp:
            self._sftp = self._client.open_sftp()
    
    def mkdir_p(self,remote_path):
        """
        sftp 无法 mkdir -p，因此写一个递归创建目录功能的函数。
        """
        if remote_path == '/':
            self._sftp.chdir(remote_path)
            return
        if remote_path == '':
            return
        try:
            self._sftp.chdir(remote_path) 
        except IOError:
            dirname, basename = os.path.split(remote_path.rstrip('/'))
            self.mkdir_p(dirname)
            self._sftp.mkdir(basename)
            self._sftp.chdir(basename)
            return True
      


    def put(self, local_file_path, remote_file_path):
        """
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        """
        remote_file = Path(remote_file_path)
        self.create()
        self.mkdir_p(remote_file.parent.as_posix())
        self._sftp.put(local_file_path, remote_file_path, confirm=True)

    def get(self, local_file_path, remote_file_path):
        local_file = Path(local_file_path)
        local_file.parent.mkdir(parents=True, exist_ok=True)
        self.create()
        self._sftp.get(remote_file_path, local_file_path)



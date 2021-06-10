from transferfile.transfile_interface import TransferFileInterface
from pathlib import Path
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

        self._scp = None

    def create(self):
        if not self._scp:
            self._scp = SCPClient(self._client.get_transport())

    def put(self, local_file_path, remote_file_path):
        """
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        """

        remote_file = Path(remote_file_path)
        self._client.exec_command(f"mkdir -p {remote_file.parent.as_posix()}")
        self.create()
        self._scp.put(local_file_path, remote_file_path)

    def get(self, local_file_path, remote_file_path):
        """
        remote_file_path -> local_file_path
        :param local_file_path:
        :param remote_file_path:
        :return:
        """

        local_file = Path(local_file_path)
        local_file.parent.mkdir(parents=True,exist_ok=True)
        self.create()
        self._scp.get(remote_file_path, local_file_path)



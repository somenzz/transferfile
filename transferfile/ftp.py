from transferfile.transfile_interface import TransferFileInterface
import os
from ftplib import FTP
from pathlib import Path


class Ftp(TransferFileInterface):
    def __init__(self, hostname, username, password, port=21,encoding = "utf-8"):
        self.ftp = FTP(user=username, passwd=password)
        port = port if port else 21
        self.ftp.encoding = encoding  # 解决中文乱码问题
        self.ftp.connect(hostname, port)
        self.ftp.login(username, password)

    def put(self, local_file_path, remote_file_path):

        remotepath, remotefile = os.path.split(remote_file_path)

        # 没有目录先创建
        try:
            self.ftp.mkd(remotepath)
        except Exception:
            pass

        with open(local_file_path, "rb") as reader:
            self.ftp.storbinary(f"STOR {remote_file_path}", reader)

    def get(self, local_file_path, remote_file_path):
        """
        Copies a file between the remote host and the local host.
        """

        localpath, localfile = os.path.split(local_file_path)
        Path(localpath).mkdir(parents=True)
        with open(local_file_path, "wb") as writer:
            self.ftp.retrbinary(f"RETR {remote_file_path}", writer.write)

    def close(self):
        self.ftp.close()

    def __del__(self):
        self.ftp.close()
from transferfile.transfile_interface import TransferFileInterface
import os
from ftplib import FTP
from pathlib import Path


class Ftp(TransferFileInterface):
    def __init__(self, hostname, username, password, port=21, **kwargs):
        self.ftp = FTP(user=username, passwd=password)
        port = port if port else 21

        self.ftp.encoding = kwargs.get('encoding','utf-8') # 解决中文乱码问题
        self.ftp.connect(hostname, port)
        self.ftp.login(username, password)

    def chdir(self,directory):
        while directory.endswith('/'):
            directory = directory[:-1]
        dirs = directory.split('/')
        if directory.startswith('/'):
            dirs.pop(0)
            self.ftp.cwd('/')
        self.ch_dir_rec(dirs)

        # Check if directory exists (in current location)

    def directory_exists(self, directory):
        filelist = []
        self.ftp.retrlines('LIST', filelist.append)
        for f in filelist:
            path_info = f.split()
            if path_info[-1] == directory and f.upper().startswith('D'):
                return True
            elif len(path_info) > 3:
                #链接类型的目录
                if path_info[-3] == directory and f.upper().startswith('L'):
                    return True
                # windows类型的目录
                if path_info[-1] == directory and path_info[-2] == '<DIR>':
                    return True
        return False

    def ch_dir_rec(self, descending_path_split):
        if len(descending_path_split) == 0:
            return
        next_level_directory = descending_path_split.pop(0)
        if not self.directory_exists(next_level_directory):
            self.ftp.mkd(next_level_directory)
        self.ftp.cwd(next_level_directory)
        self.ch_dir_rec(descending_path_split)


    def put(self, local_file_path, remote_file_path):

        remotepath, remotefile = os.path.split(remote_file_path)

        # 没有目录先创建
        self.chdir(remotepath)

        with open(local_file_path, "rb") as reader:
            self.ftp.storbinary(f"STOR {remote_file_path}", reader)

    def get(self, local_file_path, remote_file_path):
        """
        Copies a file between the remote host and the local host.
        """

        localpath, localfile = os.path.split(local_file_path)
        Path(localpath).mkdir(parents=True, exist_ok=True)
        with open(local_file_path, "wb") as writer:
            self.ftp.retrbinary(f"RETR {remote_file_path}", writer.write)

    def close(self):
        self.ftp.close()

    def __del__(self):
        self.ftp.close()
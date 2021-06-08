from transferfile.transfile_interface import TransferFileInterface

from ftplib import FTP
from pathlib import Path
class Ftp(TransferFileInterface):

    def __init__(self,hostname,username,password,port = 21):
        self.ftp = FTP(user = username, passwd = password)
        self.port = port
        self.ftp.encoding = 'utf-8'  # 解决中文乱码问题
        self.ftp.connect(hostname,port)
        self.ftp.login(username,password)

    def put(self,local_file_path, remotepath):

        try:
            self.ftp.mkd(remotepath)
        except Exception:
            pass

        self.ftp.cwd(remotepath)
        with open(local_file_path,"rb") as reader:
            self.ftp.storbinary(f"STOR {Path(local_file_path).name}",reader)



    def get(self,localpath, remote_file_path):
        """
            Copies a file between the remote host and the local host.
        """

        rp = Path(remote_file_path)
        self.ftp.cwd(rp.parent.as_posix())

        lp = Path(localpath)
        if not lp.exists():
            lp.mkdir()

        with open(str(lp/rp.name), "wb") as writer:
            self.ftp.retrbinary(f"RETR {rp.name}", writer.write)

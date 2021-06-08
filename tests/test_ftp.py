

from transferfile import TransferFactory


class TestTransfer():

    ftp = TransferFactory.create(type = "ftp",host = "localhost",port= 29,username = "user",password= "12345")

    def test_ftp_put(self):
        local = "/Users/aaron/github/somenzz/transferfile/tests/你好.tx"
        remote = "/1111/"
        self.ftp.put(local,remote)



    def test_ftp_get(self):
        localpath = "/Users/aaron/github/somenzz/transferfile/tests/"
        remote_file_path = "/1111/你好.tx"
        self.ftp.get(localpath,remote_file_path)

from transferfile import TransferFactory


class TestTransfer:

    ftp = TransferFactory.create(
        type="ftp", host="localhost", username="user", password="12345"
    )

    def test_ftp_put(self):
        local = "/Users/aaron/gitee/somenzz/transferfile/tests/test_ftp.py"
        remote = "/Users/aaron/Downloads/share/11/22/33/44/你好.txt"
        self.ftp.put(local, remote)

    # def test_ftp_get(self):
    #     localpath = "/Users/aaron/github/somenzz/transferfile/tests/"
    #     remote_file_path = "/1111/你好.tx"
    #     self.ftp.get(localpath, remote_file_path)

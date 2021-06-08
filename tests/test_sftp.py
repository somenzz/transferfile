from transferfile import TransferFactory
from pathlib import Path


class TestTransfer:
    def test_sftp_put(self):
        sftp = TransferFactory.create(
            type="sftp", host="172.17.0.2", username="admin", load_system_host_keys=True
        )
        sftp.put("testsftp.txt", "/home/admin/testsftp.txt")
        assert True

    def test_sftp_get(self):
        sftp = TransferFactory.create(
            type="sftp", host="172.17.0.2", username="admin", load_system_host_keys=True
        )
        sftp.get("./file/testsftp", "/home/admin/testsftp.txt")
        file1 = Path("./testsftp.txt")
        file2 = Path("./file/testsftp")
        assert file1.stat().st_size == file2.stat().st_size

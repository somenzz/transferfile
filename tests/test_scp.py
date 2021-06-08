

from transferfile import TransferFactory
from pathlib import Path

class TestTransfer():


    def test_scp_put(self):
        scp = TransferFactory.create(type = "scp",host = "172.17.0.2",port= 22,username = "admin",password= "admin")
        scp.put("./test_scp.py","./")
        assert True


    def test_scp_get(self):
        scp = TransferFactory.create(type = "scp",host = "172.17.0.2",port= 22,username = "admin",password= "admin")
        scp.get("./file/testscp","/home/admin/test_scp.py")
        file1 = Path("./test_scp.py")
        file2 = Path("./file/testscp")

        assert file1.stat().st_size == file2.stat().st_size


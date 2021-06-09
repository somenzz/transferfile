import subprocess
from pathlib import Path
from transferfile.transfile_interface import TransferFileInterface


class Rsync(TransferFileInterface):
    def __init__(
        self, host, username=None, password=None, port=22, load_system_host_keys=False,**kwargs
    ):
        assert load_system_host_keys, "请确保已经做了 ssh 授信"
        self.host = f"{username}@{host}"

    def put(self, local_file_path, remote_file_path):
        """
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        """
        remote_file = Path(remote_file_path)
        subprocess.run(f"mkdir -p {remote_file.parent.as_posix()}", shell=True)

        command = f"rsync -avzh {local_file_path} {self.host}:{remote_file_path}"
        r = subprocess.run(command, shell=True)
        if r.returncode == 0:
            pass
        else:
            raise Exception(f"{command} ERROR, return code {r.returncode}")

    def get(self, local_file_path, remote_file_path):

        local_path = Path(local_file_path).parent
        if not local_path.exists():
            local_path.mkdir(parents=True)
        command = f"rsync -avzh {self.host}:{remote_file_path} {local_file_path}"
        r = subprocess.run(command, shell=True)
        if r.returncode == 0:
            pass
        else:
            raise Exception(f"{command} ERROR, return code {r.returncode}")

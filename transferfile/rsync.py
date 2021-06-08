
import sysrsync


from transferfile.transfile_interface import TransferFileInterface


class Scp(TransferFileInterface):
    def __init__(self,host,username = None,password = None, port = 22, load_system_host_keys = False):
        assert load_system_host_keys, '请确保已经做了 ssh 授信'
        self.host = host


    def put(self,local_file_path, remotepath):
        '''
        :param localpath:
        :param remotepath:Note that the filename should be included. Only specifying a directory may result in an error.
        :return:
        '''
        sysrsync.run(source=local_file_path,  destination = remotepath, destination_ssh = self.host, options=['-a', '-v'])


    def get(self,localpath, remote_file_path):
        sysrsync.run(source=remote_file_path,  destination = localpath, source_ssh = self.host, options=['-a', '-v'])



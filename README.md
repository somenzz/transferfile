# transferfile

#### 介绍

sftp、ftp、scp、rsync 传输文件的统一接口，适用于不同系统的数据采集系统，如数据仓库。

#### 安装教程

```shell
pip install transferfile
```

#### 使用说明

采用简单工厂模式，传入的 type 有：
- ftp
- sftp
- scp
- rsync

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "ftp",host = "172.17.0.2",port= 22,username = "admin",password= "admin")
client.put("./test_scp.py","/path/to/test_scp.py")
```

对于 scp、sftp 可以直接使用系统的 key，从而不使用密码：

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "scp",host = "172.17.0.2",username = "admin", load_system_host_keys = True)
client.put("./test_scp.py","/path/to/test_scp.py")
```


也可以指定 rsa_私钥文件，从而不需要密码

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "scp",host = "172.17.0.2",username = "admin", rsa_file = "/root/.ssh/id_rsa")
client.get("./test_scp.py","/path/to/test_scp.py")
```

rsync 目前需要配置好授信才可以使用，暂时不支持用户名和密码登录。

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "rsync",host = "172.17.0.2",username = "admin", load_system_host_keys = True)
client.get("./test_scp.py","/path/to/test_scp.py")
```

#### 联系我

有问题，欢迎交流讨论。

公众号 「Python七号」，分享 Python 编程技能。 
![](images/python-seven.jpg)


个人微信 「somenzz」

![](images/somenzz.JPG)






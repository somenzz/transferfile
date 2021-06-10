# transferfile

#### 介绍

sftp、ftp、scp、rsync 传输文件的统一接口，无论哪一种传输方式，都可以适配。

程序适用于数据服务系统，如数据仓库对下游系统分发数据文件。

#### 安装

```shell
pip install transferfile
```

#### 使用说明

采用简单工厂模式，传入的 type 有：
- ftp
- sftp
- scp
- rsync



##### ftp

*请注意原路径和目标路径都是带文件名的路径*

传输 /path/to/src.txt 到 /path/to/dist.txt

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "ftp",host = "172.17.0.2",username = "admin",password= "admin")
client.put("/path/to/src.txt","/path/to/dist.txt")
```


如果目标路径 `/path/to/` 不存在，会递归创建。

如果程序运行在 linux 环境（utf8编码），而 ftp 服务器在 Windows 环境（GBK编码），为了文件名看起来不是乱码，可以指定服务端的编码方式为 GBK，指定特殊端口也是可以的，默认是 21

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "ftp",host = "172.17.0.2",port = 21,username = "admin",password= "admin",encoding = 'gbk')
client.put("/path/to/src.txt","/path/to/dist.txt")
```

下载文件使用 get，下载远程 /path/to/remote.txt 到本地 /path/to/local.txt：

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "ftp",host = "172.17.0.2",port = 21,username = "admin",password= "admin",encoding = 'gbk')
client.get("/path/to/local.txt","/path/to/remote.txt")
```



##### sftp，scp

*请注意原路径和目标路径都是带文件名路径*

用 scp 或 sftp 时只需要修改 type 参数为 scp 或 sftp 即可：

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "sftp",host = "172.17.0.2",username = "admin",password= "admin")
client.put("/path/to/src.txt","/path/to/dist.txt")
```

也可以指定 rsa_私钥文件，从而不需要密码

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "scp",host = "172.17.0.2",username = "admin", rsa_file = "/root/.ssh/id_rsa")
client.put("/path/to/src.txt","/path/to/dist.txt")
```

如果已经做好了 ssh 的授信，可以传入参数 load_system_host_keys = True，从而不需要密码

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "scp",host = "172.17.0.2",username = "admin", load_system_host_keys = True )
client.put("/path/to/src.txt","/path/to/dist.txt")
```

##### rsync

*请注意原路径和目标路径可以是文件名，也可以是目录*

rsync 目前需要配置好授信才可以使用，暂时不支持用户名和密码登录。

```python
from transferfile import TransferFactory
client = TransferFactory.create(type = "rsync",host = "172.17.0.2",username = "admin", load_system_host_keys = True)
client.put("/path/to/src.txt","/path/to/dist.txt")
```

##### 扩展点

由于 ftp 不支持传输目录，这里就没有做出传输整个目录的接口，要实现也不复杂，如果要实现就是递归读取目录的文件，然后一个一个传输。也可以压缩成一个文件后上传。

目前工作中暂时没有这个需求，都是生成好一个文件就传输这个文件，不需要上传整个目录。因此就没有实现。


#### 联系我

有问题，欢迎交流讨论。

公众号 「Python七号」，分享 Python 编程技能。 
![](images/python-seven.jpg)


个人微信 「somenzz」

![](images/somenzz.JPG)


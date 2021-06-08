# transferfile

#### 介绍

sftp、ftp、scp、rsync 传输文件的统一接口，适用于不同系统的数据采集系统，如数据仓库。

#### 软件架构



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
scp = TransferFactory.create(type = "scp",host = "172.17.0.2",port= 22,username = "admin",password= "admin")
scp.put("./test_scp.py","./")
```

对于 scp 可以直接使用系统的 key，从而不使用密码：

```python
from transferfile import TransferFactory
scp = TransferFactory.create(type = "scp",host = "172.17.0.2",port= 22,username = None,password= None, load_system_host_keys = True)
scp.put("./test_scp.py","./")
```




1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)

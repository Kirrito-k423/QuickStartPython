# QuickStartPython

## Python env

```
python3 -m venv /path/to/new/virtual/environment
python3 -m venv env # project named env
source <venv>/bin/activate #bash/zsh
deactivate # 退出
```

## python 引用别的文件夹的py文件
```python
import sys
sys.path.append(
    "D:\\PowerShell\\github\\waterRPA\\genshinRobot")#对应文件的文件夹
from 文件名 import *
```
### 查看环境变量
```
import sys
import pprint
pprint.pprint(sys.path)
```
![](https://shaojiemike.oss-cn-hangzhou.aliyuncs.com/img/20220213153310.png)
## Python Project
### 1
https://github.com/Kirrito-k423/BHive-Extract-A64-Blocks

1. data struct : set dictionary
2. regex
3. process bar
   ```
   from rich.progress import track
   from tqdm import *
   ```
4. logging
5. LDA文本分类
### 2
https://github.com/Kirrito-k423/BHive-Prediction-Compare

1. from multiprocessing import Process, Queue
2. python中调用bash程序

### 3
https://github.com/Kirrito-k423/waterRPA

1. 常用python函数库 tsjCommonFunc

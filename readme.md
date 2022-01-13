# 一个可通过bing.com批量获取音标的小程序

## 简介

通过www.bing.com获取单词音标，并区分英音、美音记录在Excel中

## 使用环境

python3.8下编写

使用了openpyxl、beautiful等库

## 使用方法

将需要获取音标的单词存储在excel的第一列中，假设文件命名为words.xlsx，如图所示：

![](C:\Users\zhai\AppData\Roaming\marktext\images\2022-01-11-21-36-32-image.png)

首次使用前需安装依赖

```text
pip install -r requirement.txt
```

将bing.py和words.xlsx放置在同一文件夹下，并执行

```
python bing.py words.xlsx
```

效果如图

![](C:\Users\zhai\AppData\Roaming\marktext\images\2022-01-11-21-39-38-image.png)

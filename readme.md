# 一个可通过bing.com批量获取音标的小程序

## 简介

通过www.bing.com批量获取单词音标，并区分英音、美音记录在Excel中

## 使用环境

python3.8下编写
python3环境下运行
使用了openpyxl、beautiful等库

## 使用方法
使用时请不要“翻墙”，否则会出错。    
将需要获取音标的单词存储在excel的第一列中，如图所示：  
![image](https://raw.githubusercontent.com/zzzfight200/GetPhoneticSymbol/main/1.PNG)

首次使用前需安装依赖


```text
pip install -r requirements.txt
```

假设存储单词的文件名为words.xlsx，将bing.py和words.xlsx放置在同一文件夹下，并执行

```
python bing.py words.xlsx
```

效果如图  
![image](https://raw.githubusercontent.com/zzzfight200/GetPhoneticSymbol/main/2.png)

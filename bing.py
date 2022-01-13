import requests
from bs4 import BeautifulSoup
import os
import re
import openpyxl
import sys

def ReadWords(File,Coordinate):
    # with open(os.getcwd() + '\\words.txt', 'r', encoding='utf-8') as f:
    #     f.write(Response.text)
    try:
        Excel = openpyxl.load_workbook(os.getcwd()+'\\'+FileName)
    except Exception as e:
        # print(e)
        print('Open File error')
    WorkSheet = Excel.active
    Word = WorkSheet[Coordinate].value
    return Word

def SearchWords(Word):
    #在bing上搜索单词，获取音标。
    #Word = 'animal'
    try:
        #完整url示例https://cn.bing.com/dict/search?q=zoo
        url = 'https://cn.bing.com/dict/search?q='+Word
        HttpHeaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        Response = requests.get(url,headers=HttpHeaders)
        soup = BeautifulSoup(Response.text,'html.parser')
        with open(os.getcwd()+'\\response.html','w',encoding='utf-8') as f:
            f.write(Response.text)
        # print(soup)
    except Exception as e:
        print('Search Words Error!')
        # print(e)
def RegularFind():
    try:
        with open(os.getcwd()+'\\response.html','r',encoding='utf-8') as f:
            Content = f.read()
            PhoneticSymbolUK = re.findall("英\[.*?\]",Content)
            PhoneticSymbolUS = re.findall("美\[.*?\]", Content)
            PhoneticSymbolUKStr = ''.join(PhoneticSymbolUK)
            PhoneticSymbolUSStr = ''.join(PhoneticSymbolUS)
            # print(PhoneticSymbolUK)
            # print(PhoneticSymbolUS)
            # return PhoneticSymbolUK,PhoneticSymbolUS
            if PhoneticSymbolUKStr == '':
                PhoneticSymbolUKStr = 'CanNotFindThisWord'
            if PhoneticSymbolUSStr == '':
                PhoneticSymbolUSStr = 'NoPhoneticSymbol'
    except Exception as e:
        print('Regular Find Error!')
        # print(e)
    return(PhoneticSymbolUKStr,PhoneticSymbolUSStr)

def WritePhoneticSymbol(n,PhoneticSymbolUKStr,PhoneticSymbolUSStr):
    try:
        Excel = openpyxl.load_workbook(os.getcwd() + '\\WordsWithPhoneticSymbol.xlsx')
    except Exception as e:
        # print(e)
        print('Open WordsWithPhoneticSymbol.xlsx error')
    WorkSheet = Excel.active
    CoordinatePhoneticSymbolUK = 'B'+str(n)
    CoordinatePhoneticSymbolUS = 'C'+str(n)
    WorkSheet[CoordinatePhoneticSymbolUK] = PhoneticSymbolUKStr
    WorkSheet[CoordinatePhoneticSymbolUS] = PhoneticSymbolUSStr
    Excel.save('WordsWithPhoneticSymbol.xlsx')


if __name__ == '__main__':
    FileName = sys.argv[1]
    os.system("copy %s %s" % (FileName,'WordsWithPhoneticSymbol.xlsx'))
    n = 1
    while True:
        Coordinate = 'A'+str(n)
        Word = ReadWords(FileName,Coordinate)
        if Word == None:
            break
        SearchWords(Word)
        TwoPhoneticSymbol = RegularFind()
        WritePhoneticSymbol(n,TwoPhoneticSymbol[0],TwoPhoneticSymbol[1])
        n = n+1
    print('The Last Word ,Stop!')








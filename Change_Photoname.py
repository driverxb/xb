__author__ = 'xb'
#encoding=utf-8

import os
import re
import xlrd

#定义一个通过名字搜索函数
def SearchName(SFZname):
    data=xlrd.open_workbook(r'd:\testDB.xls')
    table=data.sheet_by_index(0)
    rows=table.nrows
    pattern=r'(.+).jpg'
    SFZhm=re.findall(pattern,SFZname)
    for i in range(1,rows):
        cell_I1=table.cell_value(i,1)
        if cell_I1==SFZhm[0]:
            cell_I4=table.cell_value(i,4)
    return cell_I4


#查询函数的方法效率很低，
#原因可能是每查询一次均要打开一次数据库文件，
#但是不会报错

if __name__=='__main__':
    fileList=os.listdir(r'd:\test-photo')
    currentDir=os.getcwd()
    os.chdir(r'd:\test-photo')
    for Oldfilename in fileList:
        Name=SearchName(Oldfilename)
        Newfilename=str(Name)+'_'+str(Oldfilename)
        print('Oldfilename=%s'%(Oldfilename))
        os.rename(Oldfilename,Newfilename)
        print('Newfilename=%s'%(Newfilename))



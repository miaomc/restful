# -*- coding: cp936 -*-
import urllib
import json

"""
应用编号 应用名称   访问应用（AK） 	           应用类别
9643191 anxiang    25oSYWiyhXVUOgbSnia4H5r75XHykw5s 服务端
"""

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    output = 'json'
    ak = '25oSYWiyhXVUOgbSnia4H5r75XHykw5s'
    uri = url + '?' + 'address=' + address + '&output=' + output + '&ak=' + ak
    temp = urllib.urlopen(uri)
    temp = json.loads(temp.read())
    return temp

def getpng(ll):
    """
    http://api.map.baidu.com/staticimage/v2?ak=E4805d16520de693a3fe707cdc962045&mcode=666666&center=116.403874,39.914888&width=300&height=200&zoom=11
    """
    url = 'http://api.map.baidu.com/staticimage/v2/'
    output = 'json'
    ak = '25oSYWiyhXVUOgbSnia4H5r75XHykw5s'
    lnglat = ','.join(ll)
    uri = url + '?' +  '&ak=' + ak + '&mcode=666666&center=' + lnglat + '&width=300&height=200&zoom=11'
    temp = urllib.urlopen(uri)
    return temp

def trans(lst_lnglat):
    """
    http://api.map.baidu.com/geoconv/v1/?coords=114.21892734521,29.575429778924;114.21892734521,29.575429778924&from=1&to=5&ak=你的密钥
    """
    ak = '25oSYWiyhXVUOgbSnia4H5r75XHykw5s'
    str_lnglat = ';'.join(lst_lnglat)
    uri = 'http://api.map.baidu.com/geoconv/v1/?coords=' + str_lnglat + '&from=1&to=5&ak=' + ak
    print uri
    temp = urllib.urlopen(uri)
    temp = json.loads(temp.read())
    return temp

def str_lst(shequ, name=1, lat=3, lng=2):
    result = []
    for i in shequ.split('\n'):
        line = i.split()
        result.append(line[name] + ',' + line[lat] + ',' + line[lng])
    return result

def gaogong_test3(shequ):
    """进行字符串处理，格式转换"""
    tmp = str_lst(shequ, name=0, lat=2, lng=1)
    lst = [','.join(i.split(',')[1:3]) for i in tmp]
    print len(lst)
    trans_tmp = trans(lst)    
    return (tmp,trans_tmp)
    
    
if __name__ == '__main__':
    shequ = """口中学	29.280573	112.154310
西北角	29.304384	112.147363"""

    shequ = ['\n'.join(shequ.split('\n')[i*99:i*99+99]) for i in range(len(shequ.split('\n'))/99 + 1)]

    for oneshequ in shequ:
        tmp = gaogong_test3(oneshequ)

        try:
            for num,i in enumerate(tmp[1]['result']):
                print tmp[0][num],',',i['y'],',',i['x']
        except:
            print tmp[1]['message']


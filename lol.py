import requests
import json
import time

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
}

def heronumdic(): #获取英雄名字及对应的数字标记
    heronumdic={}
    headers={
    'Referer': 'https://lol.qq.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    }
    respones=requests.get(url='https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js',headers=headers)
    html=respones.text   #等到一个json
    heronumdata=json.loads(html)  #heronumdata是字典类型

    for i in heronumdata['hero']:

        heronumdic[i['heroId']]=i['name']

    return heronumdic    #返回一个字典

def hero_url(): #得到每个英雄的url地址
    #url='https://game.gtimg.cn/images/lol/act/img/js/hero/518.js'
    l=[]
    url='https://game.gtimg.cn/images/lol/act/img/js/hero/'
    for i in heronumdic().keys():
        url='https://game.gtimg.cn/images/lol/act/img/js/hero/'
        url=url+i+'.js'
        l.append(url)

    return l      #返回一个列表



def imgdata():  #等到每个图片的url地址

    imgdic={}
    for i in hero_url():

 
        respones=requests.get(url=i,headers=headers)
        
        html=respones.text
        img_url=json.loads(html) 
        for j in img_url['skins']:
            imgdic[j['skinId']]=j['name']
    return imgdic

def downimg(): #下载每张图片

    
    
    for k,v in imgdata().items():
        url='https://game.gtimg.cn/images/lol/act/img/skin/big'
        
        try:    
            url=url+k+'.jpg'
            print(url)
            respones=requests.get(url=url,headers=headers)
            img=respones.content
            with open(f'lolimg/{v}.jpg','wb') as fb:
                fb.write(img)
            print(f'正在下载{v}')    
        except:
            print(f'{v}有错误')        


def main():
    
    downimg()

    print('完成')
    

if __name__ == "__main__":
    main()

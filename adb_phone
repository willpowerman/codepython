import os
import time
import sys
import random
import threading



a=int(input('输入次数需要滑动的次数：'))



def phone1set():
    os.system('adb tcpip 5555')    #使用adb打开无线开关，如果报错，此时请将手机与电脑先通过数据线连接，试运行一次后再拔掉数据线
    os.system('adb connect 192.168.1.16:5555') #连接手机的IP地址

def phone2set():
    os.system('adb tcpip 5556')    #使用adb打开无线开关，如果报错，此时请将手机与电脑先通过数据线连接，试运行一次后再拔掉数据线
    os.system('adb connect 192.168.1.18:5556') #连接手机的IP地址



def phone1():
    b=0
    while b<a:
        os.system('adb -s 192.168.1.16:5555 shell input swipe 550 1300 550 350') #循环结构中调用函数
        time.sleep(random.randint(2,14))
        b=b+1
        print(f"手机1刷新{b}次")
    else:
        print("任务全部完成")
        fun=os.system('adb kill-server')    #运行结束杀掉adb进程
        sys.exit("bye")
        
def phone2():
    b=0
    while b<a:
        os.system('adb -s 192.168.1.18:5556 shell input swipe 550 1300 550 350') #循环结构中调用函数
        time.sleep(random.randint(2,14))
        b=b+1
        print(f"手机2刷新{b}次")
    else:
        print("任务全部完成")
        fun=os.system('adb kill-server')    #运行结束杀掉adb进程
        sys.exit("bye")

        

def main():
    os.chdir(r"E:\smalltools/adb/platform-tools") #切换到adb所在目录可以自己修改,调用adb工具
    phone1set()
    time.sleep(3)
    phone2set()
    print("已连接设备名称如下:")
    print(os.system('adb devices'))  #查看连接信息，可判断是否连接成功
    
    thread_phone1=threading.Thread(target=phone1)   #启用多线程控制
    thread_phone1.start()    
    thread_phone2=threading.Thread(target=phone2)
    thread_phone2.start()
    thread_phone2.join()    
    thread_phone1.join()

if __name__ == "__main__":
    main()

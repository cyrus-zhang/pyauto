import requests
import time
from threading import Thread
from multiprocessing import Process

def count(x,y):
    c = 0
    while c < 50000:
        c -= 1
        x += x
        y += y

def write():
    with open("test.txt", 'w') as f:
        for x in range(50000):
            f.write("test write\n")

def read():
    with open("test.txt", 'r+') as f:
        lines = f.readline()

_head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
url = "http://www.tieba.com"


def http_request():
    try:
        webPage = requests.get(url, headers = _head)
        html = webPage.text
        return  {"context":html}
    except Exception as e:
        return e


# CPU密集操作
t = time.time()
for x in range(10):
    count(1, 1)
print("Line cpu", time.time() - t)

# # IO密集操作
# t = time.time()
# for x in range(10):
#     write()
#     read()
# print("Line IO", time.time() - t)
#
# # 网络请求密集型操作
# t = time.time()
# for x in range(10):
#     http_request()
# print("Line Http Request", time.time() - t)
# #测试多线程并发执行cpu密集型操作所用时间
counts = []
t = time.time()
for x in range(10):
    thread = Thread(target=count, args=(1,1))
    counts.append(thread)
    thread.start()

e = counts.__len__()
while True:
    for th in counts:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print(time.time() - t)

# # 测试多线程并发执行IO密集型操作所需要时间
def io():
    write()
    read()


t = time.time()
ios = []
t = time.time()
for x in range(10):
    thread = Thread(target=count, args=(1, 1))
    ios.append(thread)
    thread.start()

e = ios.__len__()
while True:
    for th in ios:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print(time.time() - t)


##测试多线程并发执行网络密集操作所需时间

t = time.time()
ios = []
t = time.time()
for x in range(10):
    thread = Thread(target=http_request)
    ios.append(thread)
    thread.start()

e = ios.__len__()
while True:
    for th in ios:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print("Thread Http Request", time.time() - t)

##测试多进程并发执行CPU密集操作所需时间
counts = []
t = time.time()
for x in range(10):
    process = Process(target=count, args=(1,1))
    counts.append(process)
    process.start()
e = counts.__len__()
while True:
    for th in counts:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print("Multiprocess cpu", time.time() - t)


##测试多进程并发执行IO密集型操作

t = time.time()
ios = []
t = time.time()
for x in range(10):
    process = Process(target=io)
    ios.append(process)
    process.start()

e = ios.__len__()
while True:
    for th in ios:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print("Multiprocess IO", time.time() - t)

##测试多进程并发执行Http请求密集型操作

t = time.time()
httprs = []
t = time.time()
for x in range(10):
    process = Process(target=http_request)
    ios.append(process)
    process.start()

e = httprs.__len__()
while True:
    for th in httprs:
        if not th.is_alive():
            e -= 1
    if e <= 0:
        break
print("Multiprocess Http Request", time.time() - t)
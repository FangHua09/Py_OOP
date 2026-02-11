"""
案例: 文件上传案例, 客户端代码.

回顾: 网编客户端实现流程.
    1. 创建客户端Socket对象.
    2. 连接服务器端的 ip 和 端口号.
    3. 关联数据源文件, 读取内容, 写给服务器端
    4. 释放资源.
"""
# 导包
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))
# 3. 关联数据源文件, 读取内容, 写给服务器端
# 3.1 关联数据源数据.
with open(r'C:\Users\13075\Desktop\File\个人资料\杨亮_2400502249.png', 'rb') as src_f:
    while True:
        # 3.2 读取数据.
        data = src_f.read(8192)#8KB
        if len( data) == 0:
            break
        # 3.3 写给服务器端.
        client_socket.send(data)

# 4. 接收回执信息.
#print(f'客户端收到: {client_socket.recv(8192).decode("utf-8")}')

client_socket.close()
"""
案例: 文件上传案例, 服务器端代码.

回顾: 网编服务器端实现流程.
    1. 创建服务器端Socket对象.
    2. 绑定ip 和 端口号.
    3. 设置最大监听数.
    4. 等待客户端申请建立连接
    5. 读取客户端上传的(文件)数据, 写到目的地文件
    6. 释放资源.
"""

# 导包
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)
accept_socket, client_info = server_socket.accept()
print(f'有新的客户端连接: {client_info}')

# 5. 读取客户端上传的(文件)数据
# 5.1 关联目的地文件.
with open(r'C:\Users\13075\PycharmProjects\Py_OOP\day04\data\serverTXT.txt', 'w') as dest_f:
    while True:
        # 5.2 读取数据.
        data = accept_socket.recv(8192)#8KB
        if not data:
            break
        # 5.3 写入数据.
        dest_f.write(data.decode('utf-8'))

# 6.给出回执信息.
#accept_socket.send('文件上传成功!'.encode('utf-8'))

accept_socket.close()
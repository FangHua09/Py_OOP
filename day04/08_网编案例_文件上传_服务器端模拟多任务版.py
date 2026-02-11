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

server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socker.bind(('127.0.0.1', 8080))
server_socker.listen(5)
while True:
    try:
        # 4. 等待客户端申请建立连接
        accept_socket, client_info = server_socker.accept()
        print(f'有新的客户端连接: {client_info}')
        # 5. 读取客户端上传的(文件)数据, 写到目的地文件
        with open(r'C:\Users\13075\PycharmProjects\Py_OOP\day04\data\1.jpg', 'wb') as dst_f:
            while True:
                # 5.1 读取数据.
                data = accept_socket.recv(8192) # 1024字节
                if len( data) == 0:
                     break
                dst_f.write(data)
            accept_socket.close()
    except Exception as e:
        print(e)



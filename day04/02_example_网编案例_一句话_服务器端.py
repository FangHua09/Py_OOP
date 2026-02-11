"""
案例: 网编入门案例, 服务器端给客户端发送消息, 客户端给出回执信息.

服务器端开发流程:
    1. 创建服务器端Socket对象.
    2. 绑定IP地址和端口号.
    3. 设置最大监听数. 最多客户端等待数
    4. 等待客户端申请建立连接.
    5. 给客户端发送消息.
    6. 接收客户端的信息并打印.
    7. 释放资源.

细节:
    客户端和服务器端是通过 字节流(bytes) 的形式实现的.
"""
# 导包
import socket

# 1. 创建服务器端Socket对象.  ipv4, 字节流(TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定IP地址和端口号. localhost 8080
server_socket.bind(('127.0.0.1', 8080))

# 3. 设置最大监听数.
server_socket.listen(5)

# 4. 等待客户端申请建立连接.
client_socket, client_info = server_socket.accept()

# 5. 给客户端发送消息.
client_socket.send('欢迎来到python网络编程'.encode('utf-8'))

# 6. 接收客户端的信息并打印.
data = client_socket.recv(1024).decode('utf-8')# 接收1024字节, 并解码成字符串
print(f'服务器端收到 来自{client_info} 的信息: {data}')

# 7. 释放资源.
client_socket.close()
#server_socket.close()# 服务器端一般不关闭


# 扩展: 设置端口号重用, 目的是: 快速重启服务器(服务器关闭后, 立即释放端口).
# 参1: 当前的套接字对象, 参2: 选项名, 参3: 该选项的值
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

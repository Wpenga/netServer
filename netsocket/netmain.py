# -*- coding: utf-8 -*-
import concurrent.futures
import logging
import socket
import threading

import defines
from netsocket import netobj


def receive_messages(client_socket, address, exit_event):
	while True:
		try:
			total_data = ""
			while True:
				# 将收到的数据拼接起来
				data = client_socket.recv(defines.BUFFSIZE).decode()
				if not data:
					raise IOError

				if defines.NETDATA_END in data:
					total_data += data
					break
				total_data += data
			# request = total_data
			# print("接受的原始消息=", request)
			# netobj.CNetobjMgr.GenNetObj(request, client_socket)
			print("接受的原始消息=", data)
			total_data = data.split(defines.NETDATA_END)
			for sData in total_data:
				if sData:
					netobj.CNetobjMgr.GenNetObj(sData, client_socket)

		except Exception as e:
			# 如果出现异常，也视为连接断开
			print(f"客户端 {address} 断开了连接，原因：{e}")
			import logging
			logging.exception(e)
			client_socket.close()
			break


def send_messages(client_socket, address, exit_event):
	while True:
		try:
			message = input("发送消息: ")
			if message == 'exit':
				client_socket.close()
				break
			else:
				client_socket.sendall(message.encode())
		except Exception as e:
			# 如果出现异常，也视为连接断开
			print(f"客户端 {address} 断开了连接，原因：{e}")
			client_socket.close()
			break


def handle_client(client_socket, address):
	# 定义一个事件对象
	exit_event = threading.Event()
	# 创建两个线程分别用于发送和接收消息

	receive_thread = threading.Thread(target=receive_messages, args=(client_socket, address, exit_event))
	send_thread = threading.Thread(target=send_messages, args=(client_socket, address, exit_event))

	# 启动线程
	receive_thread.start()
	send_thread.start()

	# 等待线程结束
	receive_thread.join()
	send_thread.join()


def thread_pool_callback(worker):
	logging.info("called thread pool executor callback function")
	worker_exception = worker.exception()
	if worker_exception:
		logging.exception("Worker return exception: {}".format(worker_exception))


def RunServer():
	# 创建线程池
	print("Server started and listening for clients to connect...")
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((defines.HOST, defines.PORT))
	server_socket.listen(5)
	try:
		with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
			while True:
				client_sock, address = server_socket.accept()
				print(f"Connection from: {str(address)}")
				thread_pool_exc = executor.submit(handle_client, client_sock, address)
				thread_pool_exc.add_done_callback(thread_pool_callback)
	finally:
		# 关闭连接
		server_socket.close()

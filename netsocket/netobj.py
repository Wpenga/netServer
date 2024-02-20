# -*- coding: utf-8 -*-
"""
连接上客户端之后的对象，有clientsocket和serversocket的引用。
可以用来发送消息和接收消息。
"""
import json

from . import c2sdefines


class CNetObj(object):

	def __init__(self):
		self.m_sSub = None

	def ReceiveData(self, sData):
		pass

	def SendData(self, sData):
		pass

	def SetSub(self, sSub):
		self.m_sSub = sSub

	def GetSub(self):
		return self.m_sSub


"""
每次接收到协议，都会产生一个data对象
客户端 -> 协议号 -> 服务器 -> 解析 -> 生成netobj对象 —> 触发业务逻辑
"""


class CNetobjMgr(object):

	def __init__(self):
		pass

	@staticmethod
	def GenNetObj(sData, oClientSocket):
		dData = json.loads(sData)
		sSub = dData["sSub"]
		tInfo = c2sdefines.C2SNET.get(sSub)
		if tInfo:
			cNetObj, oCallBack = tInfo
			oNetData = cNetObj(**dData)
			oCallBack(oNetData, oClientSocket)

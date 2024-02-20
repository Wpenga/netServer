# -*- coding: utf-8 -*-
import weakref
import json


class CNetDataBase(object):
	sSub = ""

	def __init__(self):
		self.m_ClientSocketRef = None

	def SetClientSocket(self, oClientSocket):
		self.m_ClientSocketRef = weakref.ref(oClientSocket)

	def GetClientSocket(self):
		if self.m_ClientSocketRef():
			return self.m_ClientSocketRef()
		else:
			return None

	def Unpack(self, dData):
		pass

	def Pack(self, dData):
		sData = json.dumps(dData)
		self.GetClientSocket().sendall(sData.encode())


# class CNetDataHelper(object):
#
# 	def __init__(self):
# 		pass
#
# 	def DumpToData(self, ):
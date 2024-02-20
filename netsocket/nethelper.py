# -*- coding: utf-8 -*-
import json
from netsocket.netdata.testdata import CLoginResultData


def Send(oData, oClientSocket):
	sData = json.dumps(oData.__dict__)
	oClientSocket.sendall(sData.encode())


def SendLoginResult(oClientSocket, iID, sName, sToken):
	sSub = "loginResult"
	oLoginResult = CLoginResultData(sSub=sSub, sID=iID, sName=sName, sToken=sToken)
	Send(oLoginResult, oClientSocket)


def ReceiveTestData(cNetObj, dData):
	return cNetObj(**dData)

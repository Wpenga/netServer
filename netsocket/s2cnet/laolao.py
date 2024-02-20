from netsocket.netdata.laolaodata import CReturnLaoLaoData
from netsocket.nethelper import Send
from .. import defines


def SendLaoLaoData(oClientSocket, iPage, dLaoLaoDataList):
	sSub = defines.S2C_Return_LaoLao
	oSendData = CReturnLaoLaoData(sSub=sSub, iPage=iPage, dLaoLaoDataList=dLaoLaoDataList)
	Send(oSendData, oClientSocket)


def SendUploadLaoLaoResult(oClientSocket, iResult):
	sSub = defines.S2C
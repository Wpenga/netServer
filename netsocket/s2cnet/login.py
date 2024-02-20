import json
from netsocket.netdata.testdata import CLoginResultData
from .. import nethelper
from .. import defines


def SendLoginResult(oClientSocket, iID, sName, sToken):
	sSub = defines.S2C_Login_Result
	oLoginResult = CLoginResultData(sSub=sSub, sID=iID, sName=sName, sToken=sToken)
	nethelper.Send(oLoginResult, oClientSocket)

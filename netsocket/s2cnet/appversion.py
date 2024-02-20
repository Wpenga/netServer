from netsocket.netdata.appversiondata import CVersionData
from netsocket.nethelper import Send
from .. import defines


def SendVersionInfo(oClientSocket, iReleaseVersion):
	sSub = defines.S2C_Return_Version_Info
	oSendData = CVersionData(sSub=sSub, iReleaseVersion=iReleaseVersion)
	Send(oSendData, oClientSocket)

from ..netdata import appversiondata
from ..s2cnet import appversion
from ... import version


def RequestLaoLaoCallBack(oNetObj: appversiondata.CRequestVersionData, oClientSocket):
	appversion.SendVersionInfo(oClientSocket, version.VERSION_RELEASE)

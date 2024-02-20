from .netdata import testdata
from .netdata import laolaodata
from .netdata import appversiondata
from .netcallback import logincall
from .netcallback import laolaocall
from .netcallback import appversioncall
from . import defines

C2SNET = {
	defines.C2S_Login: (testdata.CLoginData, logincall.LoginCallBack),
	defines.C2S_Request_LaoLao: (laolaodata.CRequestLaoLaoData, laolaocall.RequestLaoLaoCallBack),
	defines.C2S_Request_Version_Info: (appversiondata.CRequestVersionData, appversioncall.RequestLaoLaoCallBack),
	defines.C2S_Upload_LaoLao: (laolaodata.CUploadLaolao, laolaocall.UploadLaoLaoCallBack)
}

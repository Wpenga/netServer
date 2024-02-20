# -*- coding: utf-8 -*-
from ..s2cnet import login
from ..netdata import testdata


def LoginCallBack(oNetData: testdata.CLoginData, oClientSocket):
	# CLoginData
	print("用户登录", oNetData.sID, oNetData.sPassword)
	login.SendLoginResult(oClientSocket, oNetData.sID, "狗蛋", "321")

# -*- coding: utf-8 -*-
from ..netdata import laolaodata
from ..s2cnet import laolao as s2cLaoLao
from ...bussiness import laolao


def RequestLaoLaoCallBack(oNetObj: laolaodata.CRequestLaoLaoData, oClientSocket):
	oLaoLaoDataMgr = laolao.CLaoLaoDataMgr.Inst()
	oLaoLaoDataList = oLaoLaoDataMgr.GetLaoLaoDataByPage(oNetObj.iPage)

	dLaoLaoDataList = []
	for oLaoLaoData in oLaoLaoDataList:
		dLaoLaoData = oLaoLaoData.ToSaveData()
		dLaoLaoDataList.append(dLaoLaoData)

	s2cLaoLao.SendLaoLaoData(oClientSocket, oNetObj.iPage, dLaoLaoDataList)


def UploadLaoLaoCallBack(oNetObj: laolaodata.CUploadLaolao, oClientSocket):
	dImgDataList = oNetObj.dImgDataList  # 图片数据
	sContent = oNetObj.sContent  # 内容
	iUserID = oNetObj.sID
	sToken = oNetObj.sToken
	oLaoLaoDataMgr = laolao.CLaoLaoDataMgr.Inst()
	oLaoLaoData = oLaoLaoDataMgr.CreateLaoLaoData(iUserID, sContent, dImgDataList)
	oLaoLaoDataMgr.AddLaoLaoData(oLaoLaoData)

	s2cLaoLao.SendUploadLaoLaoResult(oClientSocket, 1)

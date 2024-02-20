from dataclasses import dataclass
from typing import List

from ...bussiness import image


@dataclass
class CRequestLaoLaoData:
	sSub: str
	sID: str
	sToken: str
	iPage: int


@dataclass
class CReturnLaoLaoData:
	sSub: str
	iPage: int
	dLaoLaoDataList: list


@dataclass
class CUploadLaolao:
	sSub: str
	sID: str
	sToken: str
	dImgDataList: list
	sContent: str


@dataclass
class CUploadLaoLaoResult:
	sSub: str
	iResult: int

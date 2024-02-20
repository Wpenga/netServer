# -*- coding: utf-8 -*-
import json
from dataclasses import dataclass


@dataclass
class CLoginData:
	sSub: str
	sID: str
	sPassword: str


@dataclass
class CLoginResultData:
	sSub: str
	sID: str
	sName: str
	sToken: str

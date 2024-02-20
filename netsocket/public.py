# -*- coding: utf-8 -*-
"""
此模块用于socket连接，只有服务端功能
每个连接对应一个netobj
"""

from netsocket import netmain


def RunServer():
	netmain.RunServer()

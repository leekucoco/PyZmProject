#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.auth.info.authquery request
:author: auto create
:date: 2016-09-21 13:17:18
'''


class ZhimaAuthInfoAuthqueryRequest:
    def __init__(self):
        self.__identityParam = '' # 不同身份类型传入的参数列表,json字符串的key-value格式身份类型identityType=0:{"openId":"268801234567890123456"}身份类型identityType=2:{"certNo":"330100xxxxxxxxxxxx","name":"张三","certType":"IDENTITY_CARD"}
        self.__identityType = '' # 身份标识类型0:按照openId查询2:按照身份证+姓名查询

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setIdentityType(self, identityType):
        self.__identityType = identityType
        self.__apiParas["identity_type"] = identityType

    def getIdentityType(self):
        return self.__identityType

    def getApiMethodName(self):
        return "zhima.auth.info.authquery"

    def setScene(self, scene):
        self.__scene = scene

    def getScene(self):
        return self.__scene

    def setChannel(self, channel):
        self.__channel = channel

    def getChannel(self):
        return self.__channel

    def setPlatform(self, platform):
        self.__platform = platform

    def getPlatform(self):
        return self.__platform

    def setExtParams(self, extparams):
        self.__extParams = extparams

    def getExtParams(self):
        return self.__extParams

    def getApiParas(self):
        return self.__apiParas

    def getFileParas(self):
        return self.__fileParas

    def setApiVersion(self, apiversion):
        self.__apiVersion = apiversion

    def getApiVersion(self):
        return self.__apiVersion

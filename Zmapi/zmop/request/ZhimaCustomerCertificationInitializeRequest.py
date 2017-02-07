#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.customer.certification.initialize request
:author: auto create
:date: 2016-12-30 15:36:18
'''


class ZhimaCustomerCertificationInitializeRequest:
    def __init__(self):
        self.__bizCode = '' # 认证场景码,常用的场景码有:FACE:人脸认证,签约的协议决定了可以使用那些场景
        self.__extBizParam = '' # 扩展业务参数,暂时没有用到,接口预留
        self.__identityParam = '' # 值为一个json串,必须包含身份类型identity_type,不同的身份类型需要的身份信息不同当前支持:身份信息为证件信息identity_type=CERT_INFO:证件类型为身份证cert_type=IDENTITY_CARD,必要信息cert_name和cert_no可以选填商户的用户主体principal_id,对应用户在商户端唯一标识,如果商户传了principal_id,后续会为商户提供更强大功能
        self.__productCode = '' # 芝麻认证产品码,示例值为真实的产品码
        self.__transactionId = '' # 商户请求的唯一标志，32位长度的字母数字下划线组合。该标识作为对账的关键信息，商户要保证其唯一性.建议:前面几位字符是商户自定义的简称,中间可以使用一段日期,结尾可以使用一个序列

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setBizCode(self, bizCode):
        self.__bizCode = bizCode
        self.__apiParas["biz_code"] = bizCode

    def getBizCode(self):
        return self.__bizCode

    def setExtBizParam(self, extBizParam):
        self.__extBizParam = extBizParam
        self.__apiParas["ext_biz_param"] = extBizParam

    def getExtBizParam(self):
        return self.__extBizParam

    def setIdentityParam(self, identityParam):
        self.__identityParam = identityParam
        self.__apiParas["identity_param"] = identityParam

    def getIdentityParam(self):
        return self.__identityParam

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def setTransactionId(self, transactionId):
        self.__transactionId = transactionId
        self.__apiParas["transaction_id"] = transactionId

    def getTransactionId(self):
        return self.__transactionId

    def getApiMethodName(self):
        return "zhima.customer.certification.initialize"

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

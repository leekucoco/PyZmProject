#!/usr/bin/python
# encoding=utf-8
'''
ZHIMA API: zhima.merchant.order.rent.cancel request
:author: auto create
:date: 2017-01-12 16:43:49
'''


class ZhimaMerchantOrderRentCancelRequest:
    def __init__(self):
        self.__orderNo = '' # 信用借还订单号
        self.__productCode = '' # 信用借还的产品码：w1010100000000002858

        self.__apiParas = {}
        self.__fileParas = {}
        self.__apiVersion = '1.0'
        self.__scene = ''
        self.__channel = ''
        self.__platform = ''
        self.__extParams = ''
	
    def setOrderNo(self, orderNo):
        self.__orderNo = orderNo
        self.__apiParas["order_no"] = orderNo

    def getOrderNo(self):
        return self.__orderNo

    def setProductCode(self, productCode):
        self.__productCode = productCode
        self.__apiParas["product_code"] = productCode

    def getProductCode(self):
        return self.__productCode

    def getApiMethodName(self):
        return "zhima.merchant.order.rent.cancel"

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

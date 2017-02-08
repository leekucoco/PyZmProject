# Create your views here.
#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context
from zmop.ZmopClient import *
from zmop.request.ZhimaCreditScoreGetRequest import *
from zmop.request.ZhimaAuthInfoAuthorizeRequest import *
import json
import uuid
import urllib
from . import models
gatewayUrl = "https://zmopenapi.zmxy.com.cn/openapi.do"
privateKeyFile = "rsa_private_key.pem"
zmPublicKeyFile = "zhima_public_key.pem"
charset = "UTF-8"
appid = "1001781"

def index(request):
    Client = ZmopClient(gatewayUrl, appid, charset, privateKeyFile, zmPublicKeyFile)
    request = ZhimaCreditScoreGetRequest()
    request.setPlatform("zmop")

    request.setTransactionId("201612100936588040000000465160")
    request.setProductCode("w1010100100000000001")
    request.setOpenId("268816595335423723608155987")
    response = Client.execute(request)
    print(response.keys())
    zmfen = models.ZmScore.objects.create(openid= "268816595335423723608155980",certno= "210782198804160615",score=response["zm_score"])
    return HttpResponse(json.dumps(response))


def insert(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        message = models.message.objects.create(username=username,password=password)

        message.save()
    return render_to_response("insert.html")



def list(request):
    people_list = models.message.objects.all()
    c = Context({"people_list":people_list})
    return render_to_response("showuser.html",c)



def getinvokeurl(request):
    if request.method == "GET":
        return render_to_response("getinvokeurl.html")


    if request.method == "POST":
        name = request.POST.get("name",None).encode("utf8")
        certno = request.POST.get("certno",None).encode("utf8")
        Client = ZmopClient(gatewayUrl, appid, charset, privateKeyFile, zmPublicKeyFile)
        request = ZhimaAuthInfoAuthorizeRequest()
        request.setIdentityType("2")
        #request.setChannel("apppc")
        request.setBizParams("{\"auth_code\":\"M_APPPC_CERT\",\"state\":\""+name+" "+certno+"\"}")
        request.setIdentityParam("{\"certNo\":\""+certno+"\",\"certType\":\"IDENTITY_CARD\",\"name\":\""+name+"\"}")
        response = Client.generatePageRedirectInvokeUrl(request)
        print request.getApiParas()
        return HttpResponseRedirect(response)



def decryptreturnurl(request):
    if request.method=="GET":
        path = request.get_full_path()
        parmlist = path.split("=")
        params = parmlist[1][0:-5]
        sign = parmlist[2]
        #print params, sign

        params = '%' in params and urllib.unquote(params) or params
        sign = '%' in sign and urllib.unquote(sign) or sign

        Client = ZmopClient(gatewayUrl, appid, charset, privateKeyFile, zmPublicKeyFile)
        result = Client.decryptAndVerifySign(params, sign)
        s =urllib.unquote(result)
        parms = s.split("&")
        openid = parms[0].split("=")[1]
        nameid = parms[2].split("=")[1]
        nameandid = nameid.split("+")
        name = nameandid[0].decode("utf8")
        print name ,type(name)
        userid = nameandid[1]
        zmopenid = models.ZmOpenId.objects.create(openid = openid,name=name, certno=userid)

        return HttpResponse(openid)




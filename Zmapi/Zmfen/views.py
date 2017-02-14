# Create your views here.
#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Context
from zmop.ZmopClient import *
from zmop.request.ZhimaCreditScoreGetRequest import *
from zmop.request.ZhimaAuthInfoAuthorizeRequest import *
import json
import uuid
import urllib
from . import models
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
gatewayUrl = "https://zmopenapi.zmxy.com.cn/openapi.do"
privateKeyFile = "rsa_private_key.pem"
zmPublicKeyFile = "zhima_public_key.pem"
charset = "UTF-8"
appid = "1001781"

def loginview(request):
    if request.method == "GET":
        return render_to_response("login.html")
    if request.method == "POST":

        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect("/getinvokeurl")
            else:
                return HttpResponse(u"用户未激活，联系管理员")
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect("/getinvokeurl")


@login_required(login_url='/login/')
def index(request):
    openid = request.GET.get("openid").encode("utf8")
    certno = request.GET.get("certno")
    Client = ZmopClient(gatewayUrl, appid, charset, privateKeyFile, zmPublicKeyFile)
    scorerequest = ZhimaCreditScoreGetRequest()
    scorerequest.setPlatform("zmop")
    cuuid= uuid.uuid1()
    cuuidtouse = str(cuuid.int)[0:30]
    scorerequest.setTransactionId(cuuidtouse)
    scorerequest.setProductCode("w1010100100000000001")
    scorerequest.setOpenId(openid)
    response = Client.execute(scorerequest)
    #print(dir(request.user))
    #print(response.keys())
    zmfen = models.ZmScore(openid= openid,certno= certno,score=response["zm_score"])
    zmfen.save()
    #managerid = request.user.custsomermanager.managerid
    zmfen.managerid.add(request.user.custsomermanager)
    return HttpResponse(response["zm_score"])

#
# def insert(request):
#     if request.method == "POST":
#         username = request.POST.get("username",None)
#         password = request.POST.get("password",None)
#         message = models.message.objects.create(username=username,password=password)
#
#         message.save()
#     return render_to_response("insert.html")
#
#
#
# def list(request):
#     people_list = models.message.objects.all()
#     c = Context({"people_list":people_list})
#     return render_to_response("showuser.html",c)
#

@login_required(login_url='/login/')
def getinvokeurl(request):
    if request.method == "GET":
        return render_to_response("getinvokeurl.html")


    if request.method == "POST":
        name = request.POST.get("name",None).encode("utf8")
        certno = request.POST.get("certno",None).encode("utf8")

        try:
            curropenid = models.ZmOpenId.objects.get(certno=certno)
            print curropenid.openid
            return HttpResponseRedirect("/testzmfen" + "?openid=" + curropenid.openid + "&certno=" + certno)

        except models.ZmOpenId.DoesNotExist:

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
        try:
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
            #print name ,type(name)
            userid = nameandid[1]
            zmopenid = models.ZmOpenId.objects.update_or_create(openid = openid,name=name, certno=userid)
            #print zmopenid
            return HttpResponseRedirect("/testzmfen" + "?openid=" + openid + "&certno=" + userid)
            #return redirect("getzmfenview",openid=openid,certno=userid)
        except:
            return redirect("getinvokeurlview")






# import OlivOS
#import OlivaNetMusic 
import json
import requests

class NetMusicSongs:
    def __init__(self,name,ArtistsName=None):
        self.name=name
        self.id=None

        self.artists=None
        self.ArtistsId=None
        self.ArtistsName=ArtistsName
        self.ArtistsPicUrl=None
        self.ArtistsAlias=None
        self.ArtistsalbumSize=None
        self.ArtistsPicId=None
        self.ArtistsImg1v1Url=None
        self.ArtistsImg1v1=None
        self.ArtistsTrans=None

        self.album=None
        self.duration=None
        self.copyrightId=None
        self.status=None
        self.alias=None
        self.rtype=None
        self.ftype=None
        self.mvid=None
        self.fee=None
        self.rUrl=None
        self.mark=None

        self.SongId=None
        self.SongUrl=None

        self.check=False
    def checkover(self):
        if self.check==True:
            output = r'[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; '+str(self.name)+'" sourceMsgId="0" url="http://music.163.com/m/song/'+str(self.SongId)+'" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="'+str(self.ArtistsPicUrl)+'" src="'+str(self.SongUrl)+'" /><title>'+str(self.name)+'</title><summary>'+str(self.ArtistsName)+'</summary></item><source name="网易云音乐" icon="https://pic.rmb.bdstatic.com/911423bee2bef937975b29b265d737b3.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>]'
            return output
    def SearchSongs(self):
        if self.ArtistsName==None:
            api = "http://cloud-music.pl-fe.cn/search?limit=1&keywords=" + self.name
        else:
            api = "http://cloud-music.pl-fe.cn/search?limit=1&keywords=" + self.name +" "+self.ArtistsName
        payload={}
        headers={}
        response = requests.request("GET", api, headers=headers, data=payload)
        userjson = json.loads(response.text)
        if userjson !="":
            userjson=userjson["result"]["songs"][0]
            songartists=userjson["artists"][0]
            self.id=userjson["id"]
            self.artists=songartists
            self.ArtistsId=songartists["id"]
            self.ArtistsName=songartists["name"]
            self.ArtistsPicUrl=songartists["picUrl"]
            self.ArtistsAlias=songartists["alias"]
            self.ArtistsalbumSize=songartists["albumSize"]
            self.ArtistsPicId=songartists["picId"]
            self.ArtistsImg1v1Url=songartists["id"]
            self.ArtistsImg1v1=songartists["img1v1"]
            self.ArtistsTrans=songartists["trans"]
            self.album=userjson["album"]
            self.duration=userjson["duration"]
            self.copyrightId=userjson["copyrightId"]
            self.status=userjson["status"]
            self.alias=userjson["alias"]
            self.rtype=userjson["rtype"]
            self.ftype=userjson["ftype"]
            self.mvid=userjson["mvid"]
            self.fee=userjson["fee"]
            self.rUrl=userjson["rUrl"]
            self.mark=userjson["mark"]

    def GetMusicUrl(self):
        if self.id !="":
            api="http://cloud-music.pl-fe.cn/check/music?id=" + str(self.id)
            payload={}
            headers={}
            response = requests.request("GET", api, headers=headers, data=payload)
            check=json.loads(response.text)
            if check["success"]==True:
                self.check=True
                api="http://cloud-music.pl-fe.cn/song/url?id=" + str(self.id)
                payload={}
                headers={}
                response = requests.request("GET", api, headers=headers, data=payload)
                songjson = json.loads(response.text)
                if songjson["code"]==200:
                    songjson= songjson["data"][0]
                    self.SongId=songjson["id"]
                    self.SongUrl=songjson["url"]


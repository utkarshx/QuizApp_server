import AndroidUtils
import urllib
import json
ss = {}  #server state


LI_N_PEOPLE_WAITING = 0
LI_USERS_WAITING_SERVERID =1
LI_LAST_WAITING_UID =2
class MasterServerUtils():
    rrCount = 0
    webServerMap= {}
    webServerIds=[]
    def __init__(self,webServerMap):
        self.updateWebServerMap(webServerMap)
        for i in webServerMap.values():
            print AndroidUtils.get_data("http://"+i+"/func?task=updateServerMap",urllib.urlencode({"webServerMap":json.dumps(webServerMap)}))
            
        
    def addServer(self, sid , addr):
        self.webServerMap[sid]=addr
        self.updateWebServerMap(self.webServerMap)
    
    def removeServer(self, sid):
        del self.webServerMap[sid]
        if(sid=="master"):#fail safe 
            master = min(self.webServerMap.keys())
            self.webServerMap["master"]  =self.webServerMap[master]
        self.updateWebServerMap(self.webServerMap)
    
        
    def updateWebServerMap(self, webServerMap):
        for i in webServerMap.keys():
                self.webServerMap[i] = webServerMap[i]
        self.webServerIds = webServerMap.keys()
        
    def getQuizWebSocketServer(self,quiz, user):
        quizState = ss.get(quiz.quizId,None)
        if(quizState):
            quizState[LI_N_PEOPLE_WAITING]-=1
            if(quizState[LI_N_PEOPLE_WAITING]<=0):
                ss[quiz.quizId]= quizState = [quiz.nPeople , self.getRoundRobinServerId()]
        else:
            ss[quiz.quizId]= quizState = [quiz.nPeople , self.getRoundRobinServerId()]
        
        quizState[LI_N_PEOPLE_WAITING] = user.uid
        return self.webServerMap[quizState[LI_USERS_WAITING_SERVERID]]
    
    def waitingUserBotOrCancelled(self, quizId, sid ,uid):
        quizState = ss.get(quizId,None)
        if(quizState and quizState[LI_USERS_WAITING_SERVERID]== sid and quizState[LI_LAST_WAITING_UID]== uid):
            ss[quizId]=None
    
    def getRoundRobinServerId(self):
        self.rrCount+=1
        self.rrCount%=len(self.webServersArray)
        return self.webServerIds[self.rrCount]



if __name__=="__main__":
    m = MasterServerUtils({"master":"192.168.0.1:8084"})
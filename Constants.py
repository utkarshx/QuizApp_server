'''
Created on Aug 26, 2014

@author: abhinav2
'''
import datetime


####################config variables 
HTTP_PORT=8084
# status codes for web requests
NOT_ACTIVATED = 104
ACTIVATED = 105
NOT_AUTHORIZED = 106
OK =200
OK_AUTH=202
USER_EXISTS=203
USER_NOT_EXISTS = 204
USER_SAVED = 205
OK_IMMUTABLE = 206
OK_FEED = 207
OK_INIT = 208
FAILED=300
DUPLICATE_USER = 301
CAN_UPGRADE=212
ALLOWED=211
CAN_UPGRADE_RECHARGE = 213
REG_SAVED = 214
OK_USER_INFO =215
OK_NAME=216
NO_NAME_FOUND = 217
RATING_OK = 220;

OK_DETAILS = 501
NOT_FOUND=404   
OK_QUESTIONS = 502
OK_QUESTION = 503
OK_SERVER_DETAILS = 504
OK_UPDATES = 505
FACEBOOK_USER_SAVED = 506
GPLUS_USER_SAVED = 507

################################# dict values/commands for payload type definition
USER_ANSWERED_QUESTION = 1
GET_NEXT_QUESTION = 2
STARTING_QUESTIONS = 3
ANNOUNCING_WINNER = 4
USER_DISCONNECTED = 5
NEXT_QUESTION =6
START_QUESTIONS = 7
STATUS_WHAT_USER_GOT = 8

#################################dict keys
QUESTIONS = 1
CURRENT_QUESTION = 2
MESSAGE_TYPE = 3
QUESTION_ID = 4
WHAT_USER_HAS_GOT = 5
N_CURRENT_QUESTION_ANSWERED = 6
USER_ANSWER = 7
USERS=8


#preference strigns
PREF_IMMUTABLES_COUNT = "immutables_count"
###########Notification types

DONT_KNOW = 0
NOTIFICATION_USER_CHALLENGED_YOU = 1
NOTIFICATION_USER_PRIVATE_MESSAGE = 2
NOTIFICATION_USER_PLAY_REQUEST =3
NOTIFICATION_SERVER_MESSAGE =4
NOTIFICATION_SERVER_COMMAND = 5
IS_TEST_BUILD = True
ONE_DAY= datetime.timedelta(days = 1)
EPOCH_DATETIME = datetime.datetime(1970,1,1)

secret_auth="asdsadkjhsakjdhjksad"
GCM_API_KEY = "AIzaSyCEhpQRBHfeAsdYS85VlcrsB7XQADbEWNw"
GCM_HEADERS ={'Content-Type':'application/json',
              'Authorization':'key='+GCM_API_KEY
        }






### get server
PROGRESSIVE_QUIZ =0





##### db server
DEFAULT_SERVER_ALIAS ="0000"

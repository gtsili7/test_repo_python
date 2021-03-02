Τσιλιβάκος Γιώργος π20193
import tweepy
#api authentication
ACCESS_TOKEN =1351527880778539008-QuFAhaJgtjSSQVIVuBskfVEByr8uyr
ACCESS_SECRET =tC2O1vQBoeoHhq8Ojc5NSYUWzTXKfCE5wtEZeCflBbw5
CONSUMER_KEY =wdtENKgNx9Q2scmfbxOwXfUD3
CONSUMER_SECRET =W6McpeAejnkWUK9uHkVRbbByQ1Uxk0kyv2KjVfzdDcXI2uQyb0


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

#start
user = input("user:")
word_list=[]
tweetsxrhsth = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in tweetsxrhsth:
    word_list.append(tweet.text)

lexeis=[]
for tweet in word_list:
    spasmeno = tweet.split()
    lexeis = lexeis + spasmeno

def Sorting(lexeis):
    lexeis.sort(key=len)
    return lexeis

print(Sorting(lexeis))

SYMBOLS = '{}()[].,:;+-*/&|_#!@$%^><\?`=~'

results = []
for stoixeio in lexeis:
    temp = ""
    for ch in stoixeio:
        if ch not in SYMBOLS:
            temp += ch

    results.append(temp)

#apotelesmata
for i in range(5):
    print(results[i])

for j in reversed(range(len(results)-5,len(results))):
    print(results[j])

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from sys import exit
from json import loads

#adding user credentials to the following variables
access_token = '452870353-lhThnCXjt76oqpx86v4GOymPzeHibx0ce9WMoX43'
access_token_secret = '3HEO65Q3Cw30Sr2GzhPSRVAvCbxwRjswP54aGdR1Ya4Ef' 
consumer_key = 'DLZuadI323arpUKCUHAtlioJH'
consumer_secret = 'tKQutnaO2nHQtHK03TXStfg7X9tXp4qZDrsqEA90DbAXY6DeyK'
jkw = open('jkw2.txt', 'w', encoding="utf-8")
pbw = open('pbw2.txt', 'w', encoding="utf-8")
#printing tweets
class StdOutListener(StreamListener):
    def __init__(self, cap, max):
        if cap == 'jkw':
            self.cap = 'JKW'
            self.f = jkw
        else:
            self.cap = 'PBW'
            self.f = pbw
        self.i = 0
        self.max = max
        self.close = False
    
    def on_data(self, data):
        if not self.close:
            j_data = loads(data, encoding="utf-8")
            try:
                self.f.writelines("%d_efw7912jdqw[%s]_932ruo\n"%(self.i, j_data["text"].decode("utf-8")))
            except AttributeError:
                self.f.writelines("%d_efw7912jdqw[%s]_932ruo\n"%(self.i, j_data["text"]))
            except KeyboardInterrupt:
                self.f.close()
            self.i += 1
            print("[%s]New tweet number [%d]"%(self.cap, self.i))
            if(self.i == self.max):
                self.f.close()  
                self.close = True 
                
        #print data
        return True
        
    def on_error(self, status):
        print(status)
        
if __name__=='__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    j = StdOutListener(cap='jkw', max=1000)
    p = StdOutListener(cap='pbw', max=1000)
    j_s = Stream(auth, j)
    p_s = Stream(auth, p)
    
    try:
        j_s.filter(track=["jokowi",
                            "Jokowi",
                            "maruf",
                            "Maruf",
                            "Ma'ruf",
                            "ma'ruf"],
                    is_async=True)
        p_s.filter(track=["Prabowo",
                            "prabowo",
                            "sandiaga",
                            "Sandiaga"],
                    is_async=True)
    except KeyboardInterrupt:
        jkw.close()
        pbw.close()
    
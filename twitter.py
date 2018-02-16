import tweepy
from tweepy import OAuthHandler
from datetime import datetime

# Keys 
consumer_key = "ZR62y5rbtgnhnoI53Gsz7p6iG"
consumer_secret = "0juYzHbuwk5yTEWvF1k78e8b1pAAQRWWcVDnUCL3gopWNXdJFW"
access_token = "131948406-LZAPpru5SeO8OKHWqf1anDWMsGXIJCeRFKTzEGc7"
access_secret = "FbiPrFi07gDnm2SCtNeVMtJMmHkWIHTXAIkrNf320aAuc"

# Auth
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def formatNumber(followers_count):
    flwr = str(followers_count)
    fl = len(flwr) 
    dv = fl / 3
    dv = int(dv)
    
    if( dv > 1):
        string = ""
        pre = flwr[0:fl-(3)]
        post = flwr[-3: fl]
        string =  str(pre)+","+str(post)
        
        if( dv > 2):
            prepre = pre[0:(len(pre)-3)]
            postpost = pre[-3:len(pre)]
            string = prepre +  "," + postpost + "," + post

            if( dv > 3):
                preprepre = prepre[0:(len(prepre)-3)]
                postpostpost = prepre[-3:len(prepre)]
                string = preprepre + "," + postpostpost + "," + postpost + "," + post
        return string
    return flwr

def FormatDate(date):
    #date is a datetime object 2013-01-11 07:39:59
    Weekday = int(date.isoweekday())
    if Weekday == 1:
        Weekday = 'Monday'
    if Weekday == 2:
        Weekday = 'Tuesday'
    if Weekday == 3:
        Weekday = 'Wednesday'
    if Weekday == 4:
        Weekday = 'Thursday'
    if Weekday == 5:
        Weekday = 'Friday'
    if Weekday == 6:
        Weekday = 'Saturday'
    if Weekday == 7:
        Weekday = 'Sunday'

    Month = int(date.month)
    if Month == 1:
        Month = 'Jan'
    if Month == 2:
        Month = 'Feb'
    if Month == 3:
        Month = 'Mar'
    if Month == 4:
        Month = 'Apr'
    if Month == 5:
        Month = 'May'
    if Month == 6:
        Month = 'Jun'
    if Month == 7:
        Month = 'Jul'
    if Month == 8:
        Month = "Aug"
    if Month == 9:
        Month = "Sep"
    if Month == 10:
        Month = "Oct"
    if Month == 11:
        Month = "Nov"
    if Month == 12:
        Month = "Dec"
        
    ordinal = date.month
    
    if ordinal == 1 or ordinal == 21 or ordinal == 31:
        ordinal = str(ordinal) + "st"
    elif ordinal == 2 or ordinal == 22:
        ordinal = str(ordinal) + "nd"
    elif ordinal == 3 or ordinal == 23:
        ordinal = str(ordinal) + "rd"
    else:
        ordinal = str(ordinal) + "th"
        
    Year = str(date.year)[-2:]
    Year = "'" + Year
    return (Weekday + " "+ ordinal + " " + Month + " " + Year)

# Will reach rate limit v. fast with this. TODO: Store users in a txt file to perform operations on them w/ no requests
def checkFollowers(handle):
    for page in tweepy.Cursor(api.followers, screen_name=handle).pages():
        for follower in page:
            if follower.verified == True:
               print (follower.name + " is verified and follows" + follower.name + "!")
               formattedCount = formatNumber(follower.followers_count) 
               print (follower.name+" is followed by "+formattedCount+ " users, wow!")
               print ("========")
#TODO: Add ability to handle array of terms.
def searchTimelinePages(term, handle):
    for page in tweepy.Cursor(api.user_timeline, screen_name=handle).pages():
        for status in page:
            word_list = status.text.split()
            for word in word_list:
                if word.lower() == term.lower():
                    print (status.text + "\n" +FormatDate(status.created_at) + " \n ==========")


#Program

question = "Enter the twitter handle to search"
print (question)
uname = input()
question = "Enter the term you are searching for"
print (question)
term = input()
print("Searching for %s ....." % term )
searchTimelinePages(term, uname)

question = "Would you like to know who a users most influential followers are?, y or n"
print(question)
answer =  input()
if(answer.lower()=="y"):
    print("Enter the target twitter handle")
    uname = input()
    print("Searching...  \n ===============")
    checkFollowers(uname)

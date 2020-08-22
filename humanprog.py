import pyttsx3 as pt
import os
from sys import platform
import datetime
import time
import pyjokes
import wikiquote
import webbrowser
import subprocess

voiceEngine = pt.init()
voiceEngine.setProperty('rate', 130)

comman_word = 'run' in p or 'launch' in p or 'execute' in p or 'open' in p

hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    pt.speak("Good Morning " +"  it's my pleasure to assist you!")
elif hour>=12 and hour<18:
    pt.speak("Good Afternoon "+"  i would love to help you!")
else:
    pt.speak("Good Evening " +"  i am glad you are asking me for help!")

    
pt.speak("I am an AI Assistant. How can I help you!")


while True:
    if platform == "linux" or platform == "linux2":            # Check if platform is Linux Based
        
        print("chat with me with your requirements : "  , end='')
        pt.speak("Chat with me with your requirements : ")
        p = input()
        p = p.lower()

        if ("chrome" in p) and comman_word:
            pt.speak("Okay! opening chrome Browser")
            os.system("google-chrome")
            
        elif ("chromium" in p) and comman_word:
            pt.speak("Okay! opening chromium Browser")
            os.system("chromium-browser")

        elif (("notepad" in p) or ("editor" in p) ) and comman_word:
            pt.speak("Okay! opening text editor")
            os.system("gedit")
        
        elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("day" in p)):
            x = datetime.datetime.now() 
            pt.speak("Today is " + x.strftime("%A"))
            
        elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("month" in p)):
            x = datetime.datetime.now()
            pt.speak("The current month is" + x.strftime("%B"))    
            
        elif ((("look" in p) or ("show" in p) or ("open" in p) or ("tell" in p) or ("see" in p) or ("launch" in p)) and ("time" in p)):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            pt.speak("the time is" + strTime)
        
        elif ("quote" in p or "quotes" in p):
            print(wikiquote.quote_of_the_day())
            pt.speak(wikiquote.quote_of_the_day())
            
        elif 'joke' in p:
            print(pyjokes.get_joke())
            pt.speak(pyjokes.get_joke())   

        elif ("player" in p) and ("media" in p) and comman_word:
            os.system("mvp")

        elif  ("exit" in p)  or ("quit" in p):
            pt.speak("Jarvis is at your service. Good Bye!")
            break
            
        elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("calculator" in p)):
            os.system("calc")

        elif ("search" in p)  or ("information" in p):
            pt.speak("Do you want to search on the internet?")
            print("yes or no: ", end ='')
            response = input()
            if ("yes" in response):
                pt.speak("What you want to search?")
                p = input()
                query = str(p)
                webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%query)
            else:
                pt.speak("Sorry! can you be more specific.")
        
        
        else:
            pt.speak("Please ask valid query")
            print("This query is not supported")
            
    #----------------------------------------------------------------------------------------------
    
    elif platform == "win32":                                  # Check if platform is Windows Based
        pt.speak("Chat with me with your requirements : ")
        print("chat with me with your requirements : "  , end='')
        p = input()
        
        p = p.lower()
        
        x = 'run' in p or 'launch' in p or 'execute' in p or 'open' in p
        
        
        if ("chrome" in p) and comman_word:
            pt.speak("Okay! opening Chrome Browser")
            os.system("chrome")

        elif ("quote" in p or "quotes" in p):
            print(wikiquote.quote_of_the_day())
            pt.speak(wikiquote.quote_of_the_day())
            
        elif (("notepad" in p) or ("editor" in p) ) and comman_word:
             pt.speak("Okay! opening notepad")
             os.system("notepad")

        elif ("player" in p) and ("media" in p) and comman_word:
            pt.speak("Okay! opening Windows Media Player")
            os.system("wmplayer")
            
        elif ('adobe' in p and 'acrobat' in p) and comman_word:
            pt.speak("Okay! opening adobe acrobat")
            os.system('AcroRd32')
        
        elif 'firefox' in p and comman_word:
            pt.speak("Okay! opening firefox browser")
            os.system('firefox')
        
        elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("day" in p)):
            x = datetime.datetime.now() 
            pt.speak("Today is " + x.strftime("%A"))
            
        elif ((("see" in p) or ("tell" in p) or ("look" in p) or ("speak" in p) or ("find" in p)) and ("month" in p)):
            x = datetime.datetime.now()
            pt.speak("The current month is" + x.strftime("%B"))
            
        elif ((("look" in p) or ("show" in p) or ("open" in p) or ("tell" in p) or ("see" in p) or ("launch" in p)) and ("time" in p)):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            pt.speak("the time is" + strTime)
        
        elif ('vs' in p and 'code' in p) and comman_word:
            pt.speak("Okay! opening VS Code")
            os.system('Code')
        
        elif 'joke' in p:
            print(pyjokes.get_joke())
            pt.speak(pyjokes.get_joke()) 
            
        elif ('vlc' in  p and 'player' in p) and comman_word:
            pt.speak("Okay! opening VLC player")
            os.system('vlc')
        
        elif (('dev' in p and 'c++' in p) or 'devc++' in p) and comman_word:
            pt.speak("Okay! opening Devcpp")
            os.system('devcpp')
        
        elif 'skype' in p and comman_word:
            pt.speak("Okay! opening Skype")
            os.system('lync')
            
        elif 'Photoshop' in p and comman_word:
            pt.speak("Okay! opening Adobe Photoshop")
            os.system('Photoshop')
        
        elif 'powerpoint' in p and comman_word:
            pt.speak("Okay! opening Powerpoint")
            os.system('POWERPNT')
        
        elif 'word' in p and comman_word:
            pt.speak("Okay! opening MS Word")
            os.system('WINWORD')

        elif ('excel' in p or 'spreadsheet' in p) and comman_word:
            pt.speak("Okay! opening Excel")
            os.system('EXCEL')
            
        elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p)) and ("calculator" in p)):
            os.system("calc")
        
        elif ((("run" in p) or ("execute" in p) or ("use" in p) or ("open" in p) or ("start" in p) or ("launch" in p) or ("take" in p) or ("click" in p)) and (("camera" in p) or ("selfie" in p))):
            subprocess.run("start microsoft.windows.camera:", shell=True)
        
        elif  ("exit" in p)  or ("quit" in p):
            pt.speak("Jarvis is at your service. Good Bye!")
            break
            
        elif ("search" in p)  or ("information" in p):
            pt.speak("Do you want to search on the internet?")
            print("yes or no: ", end ='')
            response = input()
            if ("yes" in response):
                pt.speak("What you want to search?")
                p = input()
                query = str(p)
                webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%query)
            else:
                pt.speak("Sorry! can you be more specific.")
                
        elif (("log off" in p or "sign out" in p) and ("system" in p or "computer" in p or "PC" in p or "pc" in p or "laptop" in p)):
            pt.speak("Close all application before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        else:
            pt.speak("Please ask valid query")
            print("This query is not supported")
    else:
        print("I am not supported for "+ platform +" platform")
        pt.speak("I am not supported for "+ platform +" platform. Sorry for the inconvenience.")
        

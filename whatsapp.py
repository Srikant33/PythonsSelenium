import pywhatkit
from datetime import datetime

def message(text):
    try:
        print ('ss')
        now = datetime.now()
        pywhatkit.sendwhatmsg('+13522832038',text,int(now.strftime("%H")),int(now.strftime("%M"))+1)
        while (1): 
            winsound.PlaySound("Welcome.wav",winsound.SND_FILENAME)
        now = datetime.now()
        pywhatkit.sendwhatmsg('+13522832038',text,int(now.strftime("%H")),int(now.strftime("%M"))+1)
        
    finally:
        now = datetime.now()
        pywhatkit.sendwhatmsg('+13522832038',text,int(now.strftime("%H")),int(now.strftime("%M"))+1)
        
        # message(text)
    
# message(text);


   
from tkinter import *
import pyttsx3  #text to speech package
import speech_recognition as sr #speech speech recognition package
import datetime #date and time package (built in)

#Complete UI design...



#Acual code for assistant starts here...

#declaring Global Variables
fever=None
contact=None
cough=None
tiredness=None
pains=None
sourThroat=None
rash= None
difficultiesInBreathing=None
cheastPain=None
lossSpeech=None
lossTeast=None

score=0


engine=pyttsx3.init('sapi5') #initilizing the microsoft speech API
voices=engine.getProperty('voices') # get built in voice from microsoft API and set in voices variable
# print(voices[1].id)
engine.setProperty('voice',voices[1].id) # set the engine voice

def speak(audio): #speech methtod from text to speech
    engine.say(audio)
    engine.runAndWait()

def wish(): #this method will wish you after exicuting the project 
    hour = int(datetime.datetime.now().hour)    #we need ol=nly hour for wishing
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    elif hour>=18 and hour<21:
        speak("Good Evening")
    check()

def takevoice():    #this method will listen user voice 
    r=sr.Recognizer()   #this is for recogonizing users voice 
    with sr.Microphone() as source: #exception handaling
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recogonizing Your Ansewer...")
        query=r.recognize_google(audio,language="english")  #trying to recognize vice by using google API
    except Exception as e:
        print("Cant recogonize your answer please say is again...")
        takevoice()
        return "None"
    return query

def check():
    global score    #accessing Global Variable
    
    speak("What is your name")
    user=takevoice().lower()
    
    speak(f"{user} do you have fever")
    global fever
    fever=takevoice().lower()
    if fever=="yes":
        score +=10
        # fever=True
    
    speak(f"{user} do you have contact with covid patient in last 14 days")
    global contact
    contact=takevoice().lower()
    if contact =="yes":
        score +=10
    
    
    speak(f"{user} do you have dry cough")
    global cough
    cough=takevoice().lower()
    if cough =="yes":
        score +=10
    
    
    speak(f"{user} do you have tiredness")
    global tiredness
    tiredness=takevoice().lower()
    if tiredness =="yes":
        score +=10
    

    speak(f"{user} do you have Headach and body pains")
    global pains
    pains=takevoice().lower()
    if pains =="yes":
        score +=10
    

    speak(f"{user} do you have rashesh on skin")
    global rash
    rash=takevoice().lower()
    if rash =="yes":
        score +=5
    

    speak(f"{user} do you have sour Throat")
    global sourThroat
    sourThroat=takevoice().lower()
    if sourThroat =="yes":
        score +=10
    

    speak(f"{user} do you have difficulties in breathing or shorten of breath")
    global difficultiesInBreathing
    difficultiesInBreathing=takevoice().lower()
    if difficultiesInBreathing == "yes":
        score +=30
    

    speak(f"{user} do you have cheast pain or cheast pressure")
    global cheastPain
    cheastPain=takevoice().lower()
    if cheastPain == "yes":
        score +=20
    

    speak(f"{user} do you loss speach or body movement")
    global lossSpeech
    lossSpeech=takevoice().lower()
    if lossSpeech == "yes":
        score +=30
    

    speak(f"{user} do you loss of test or smell")
    global lossTeast
    lossTeast=takevoice().lower()
    if lossTeast == "yes":
        score +=30
    


    
    testCases()

def testCases():
    # speak(f"you have {fever}")
    # speak(f"you have {contact}")

    #print(score)
    #main logic of the project 
    if score>90:
        speak("you have covid ")
    elif score>=75 and score<100:
        speak("You Have highest chanses of having Covid Go to test covie center for testing")
    elif score>=70 and (difficultiesInBreathing or cheastPain or lossSpeech or lossTeast):
        speak("you have chances to have covid consalt a doctor")
    elif score>=30 and score>50 and (difficultiesInBreathing or cheastPain or lossSpeech or lossTeast):
        speak("you must become home qurantin for 14 days")
    elif score>35 and score<70:
        speak("you must become home qurantine for 7 days")
    elif score<=30 :
        speak("you have no covid, Have a great day...")   

    speak("Thanks for using our software...")     

    # elif score>70  
    #if __name__=="__main__":
     #   if btn:
      #      wish()
        #    check()


 
    # window.mainloop()


window=Tk()
# add widgets here

window.title('Covid19 Voice Assistance For symptoms Identification')
lbl=Label(window, text="Voice Assistant", fg='red', font=("Algerian", 16)) #label...
lbl.place(x=60, y=30) #placing...

btn=Button(window, text="   Start    ", fg='blue',command=wish)#button for starting assistant...
btn.place(x=120, y=80)

# Creating a photoimage object to use image
photo = PhotoImage(file = r"C:\Users\USER\OneDrive\Pictures\Camera Roll\listening.png")#icons for listening view
photo1= PhotoImage(file = r"C:\Users\USER\OneDrive\Pictures\Camera Roll\speaking1.png")#icons for speaking view
  
# here, image option is used to
# set image on button
btn1 = Button(window, text = 'Click Me !', image = photo).pack(side = LEFT, padx=20,pady=50)#button for listening view
btn2 = Button(window, text = 'Click Me !', image = photo1).pack(side = RIGHT, padx=20,pady=50)#button for speaking view

window.geometry("300x200+10+20")

window.mainloop()

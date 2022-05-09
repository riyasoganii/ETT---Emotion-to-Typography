from tkinter import *
from tkinter.font import Font
import random

emotionFile = open("emotions.txt","r")
textFile=open("text.txt","r")
emotionString=emotionFile.read()
textString=textFile.read()
emotionFile.close()
textFile.close()

emotionList=emotionString.split()
textList=textString.split()

colorDict = {"Happy":"yellow","Sad":"blue","Neutral":'white',"Disgust":"brown","Fear":"black","Angry":"red","Surprise":"orange"}
fontDict = {"Happy":['NF-Ananias','Lucida Handwriting','Script MT Bold','Berlin Sans FB Demi','Castellar','Kristen ITC'],"Sad":['Poor Richard','FixedSysTTF'],"Neutral":["Arial"],"Disgust":['Wide Latin','Broadway','Jokerman','Magneto','MV Boli','Papyrus'],"Fear":['OCR A Extended','Chiller', 'Gill Sans UltraBold'],"Angry":['Stencil'],"Surprise":['Showcard Gothic']}
bgDict = {"Happy":"black","Sad":"black","Neutral":'black',"Disgust":"white","Fear":"white","Angry":"black","Surprise":"black"}
window = Tk()
window.title("Typography")

for i in range (len(emotionList)):
    emotion=emotionList[i]
    text=textList[i]
    surp = Label(window, text=text, font= (random.choice(fontDict[emotion]),40), bg=bgDict[emotion], fg=colorDict[emotion])
    surp.grid(column=i, row=0)

window.mainloop()




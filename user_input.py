# coding: utf-8
import ml_classifiers_mod as mc
from Tkinter import *
import Tkinter as tk
#from PIL import Image
#import thread
#import enchant
import nltk
from nltk.tokenize import word_tokenize


#thread.start_new_thread(mc.update(text_ip,f))
prob = {}
#d = enchant.Dict("en_US") 

def emojis_display(m,type1,nouns):
	path=[]
        img=[]
        i=1
	k=0
	j=0
	flag=0
	while(k<2):
		j=0
		while(j<230):
		     try:
			path.append("emojies/"+type1+"/e"+str(i)+".png")
			img.append(PhotoImage(file=path[i-1]))
			b=Button(m,command=lambda idx=i-1: display_Emoji(path[idx]))
			b.config(image=img[i-1],width="40",height="40") 
			b.image = img[i-1]
			b.grid(row=k,column=j/40)
			i=i+1
			j=j+40
		     except:
		      	flag=1
		      	break
		if flag==1:
			break         
		k=k+1
	
	path1=[]
	img1=[]
	w=1
	if j>230:
		j=0
	print nouns
	q=0
	s=1
	flag=0
	while(k<3):	
		while(j<230):
		     
		     if len(nouns) == q:
		     	
		     	flag=1
			break
		     
		     try:
			path1.append("emojies/emoji/"+nouns[q]+".png")
			
			img1.append(PhotoImage(file=path1[w-1]))
			
			
			b=Button(m,command=lambda idx=w-1: display_Emoji(path1[idx]))
			
			b.config(image=img1[s-1],width="40",height="40") 
			
			b.image = img1[s-1]
			s = s + 1
			
			b.grid(row=k,column=j/40)
			w=w+1
			j=j+40
			q=q+1
		     except:
		        
		      	q=q+1
		      	w=w+1
		     
		if len(nouns) == q or flag==1:
			break         
		k=k+1
		j=0
	
	
	
#defn for displaying the selected emoji
def display_Emoji(path):
   #img = Image.open("emojies/disgust/e1.png")
   #img4=PhotoImage(file="emojies/disgust/e1.png")
   #S.image_create(END, window=Label(image = img4))
   flowers = PhotoImage(file=path)
   S.image_create(END, image=flowers)
   b=Button(master)
   #b.config(image=flowers,width="40",height="40") 
   b.image = flowers
   #S.window_create(END,window=b)

#def emojiSelection():
def select_Emoji(type1, nouns):
    width=230
    height=200
    m = tk.Toplevel()
    m.resizable(width=False, height=False)
    # get screen width and height
    screen_width = m.winfo_screenwidth()
    screen_height = m.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    m.geometry('%dx%d+%d+%d' % (width, height, x+10, y+30))
    m.configure(background='light goldenrod') 

    emojis_display(m,type1,nouns)
  
    l = Button(m,text='Quit',fg ='black',activeforeground = 'red' ,background='coral',command=m.destroy)
    l.place(x=92, y=170)
    #l.grid(side=middle)      

def display_error(msg):
    width=200
    height=100
    m = tk.Toplevel()
    m.resizable(width=False, height=False)
    # get screen width and height
    screen_width = m.winfo_screenwidth()
    screen_height = m.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    m.geometry('%dx%d+%d+%d' % (width, height, x+10, y+30))
    m.configure(background='light goldenrod')
    #l = Button(m,text='Please enter valid text..!!',fg ='black',background='coral')
    l = Label(m, text=msg,font=("Helvetica",10),fg = 'gray1')
    l.place(x=10, y=20)
    l = Button(m,text='OK',fg ='black',activeforeground = 'red' ,background='coral',command=m.destroy)
    l.place(x=70, y=60)

def dist_prob(prob):
   l = Label(master, text="Distibution of emotion for the given text:",font=("Helvetica",20),background='turquoise',fg = 'gray1')
   l.place(x=10,y=400)
   l = Label(master, text="Emotion   |   Probability",font=30,background='turquoise',fg = 'red3')
   l.place(x=140,y=445)

   l = Label(master, text="   JOY	|   "+  prob['joy'],font=10,background='turquoise',fg = 'gray1')
   l.place(x=140,y=465)
   l = Label(master, text="SADNESS	|   "+  prob['sadness'],font=10,background='turquoise',fg = 'gray1')
   l.place(x=140,y=485)
   l = Label(master, text="  ANGER	|   "+  prob['anger'],font=25,background='turquoise',fg = 'gray1')
   l.place(x=140,y=505)
   l = Label(master, text="DISGUST	|   "+  prob['disgust'],font=25,background='turquoise',fg = 'gray1')
   l.place(x=140,y=525)
   l = Label(master, text="  GUILT	|   "+  prob['guilt'],font=25,background='turquoise',fg = 'gray1')
   l.place(x=140,y=545)
   l = Label(master, text="  SHAME	|   "+  prob['shame'],font=25,background='turquoise',fg = 'gray1')
   l.place(x=140,y=565)
   l = Label(master, text="  FEAR	|   "+  prob['fear'],font=25,background='turquoise',fg = 'gray1')
   l.place(x=140,y=585) 

x =1.0    
def show_entry_fields():
   T.config(state='normal')
   T.delete("1.0",END)
   global text,x 
   text = S.get(x,END)
   text = text[:-1]
   valids = word_tokenize(text)
   res = True
   import enchant
   d = enchant.Dict("en_US")
   for x in valids:
	res = res and d.check(x)	

   print(x)
   x = S.index(INSERT)
   if(text == "" or not res):
   	display_error("Please enter valid text..!!")
   	return
   nouns = []
   words = word_tokenize(text)
   tagged_words = nltk.pos_tag(words)
   for t in tagged_words:
      if t[1].startswith('NN'):
          nouns.append(t[0])
   result, prob = mc.categorise(text)
   #result = classifier.classify(features) 
   select_Emoji(result,nouns)
   T.delete("1.0",END)
   T.insert(INSERT,result)
   T.tag_configure("center", justify='center')
   T.tag_add("center", 1.0, "end")
   T.config(state=DISABLED)
   dist_prob(prob)  
   l = Label(master, text="The categorised emotion is:",font=("Helvetica",20),background='turquoise',fg = 'gray1')
   l.place(x=780,y=400)
   
   T.place(x=860,y=450)


def clearText():
	S.delete("1.0",END)
	T.config(state='normal')
	T.delete("1.0",END)
	prob = {'joy':'0.0000','sadness':'0.0000','anger':'0.0000','shame':'0.0000','fear':'0.0000','disgust':'0.0000','guilt':'0.0000'}
	dist_prob(prob)
	
master = Tk()
master.geometry('1290x710')
master.configure(background='turquoise')
master.resizable(width=False, height=False)
master.title("Interface")

#Title of the project
l = Label(master, text="Emotion Detection and Emoji suggestion\n",font=("Helvetica",40),background='turquoise',fg = 'gray1')
l.pack()

l = Label(master,text="Enter the text",font=("Helvetica",25),background='turquoise',fg = 'black')
l.place(x=190,y=100)

#Reading the text from the user
S = Text(master,height=3,width=60,spacing3=1,fg ='black',font=("Helvetica",20)) #,xscrollcommand=set(),yscrollcommand=set())
S.pack()

'''l = Label(master,text="\n",background='turquoise')
l.pack()'''

l = Button(master, text='Clear',font=30,fg ='gray1',activeforeground = 'gray1', command=clearText)
l.place(x=190,y=320)
'''l = Label(master,text="",background='turquoise')
l.pack()'''	
l = Button(master, text='Analyse the text',font=30,fg ='gray1',activeforeground = 'gray1', command=show_entry_fields)
l.place(x=520,y=320)

'''l = Label(master,text="\n\n",background='turquoise')
l.pack()'''


#l = Label(master, text="\nAccuracy :- 79.88%",font=("Helvetica",20),background='turquoise',fg = 'gray1')
#l.place(x=780,y=500)

l = Label(master,text="\n",background='turquoise')
l.pack()
l = Button(master, text='Quit',fg ='black',activeforeground = 'red' ,command=master.quit)
l.place(x=600,y=650)
T = Text(master,height=1,width=8,spacing3=2,fg ='black',font=("Helvetica",20),xscrollcommand=set(),yscrollcommand=set())
mainloop()

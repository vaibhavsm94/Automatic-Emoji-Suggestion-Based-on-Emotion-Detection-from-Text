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
    


global text,x
   text = S.get(x,END)
   text = text[:-1]
   x = S.index(INSERT)
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

class chatbook:
    def __init__(self):
        self.username= ''
        self.password=''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input(""""welcome how would you like to proceed
                           a. press 1 to signup
                           b. press 2 to singin
                           c. press 3 to write a post
                           d. press 4 to message a friend
                           e. press any other key to exit
                           
                           """"")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()


    def signup(self):
        email =input("Please enter your email here ->  ")
        pwd =input("Please setup your password here ->  ")
        self.username=email
        self.password=pwd
        print("you have signed up succesfully!!")
        print("\n")
        self.menu()


    def signin(self):
        if self.username == '' and self.password == '' :
            print("please signup first by pressing 1 in themain menu")
        else :
            use = input("Please enter your email here ->  ")
            pas = input("Please enter your password here ->  ")
            if self.username == use and self.password == pas:
                print('you have signin successfully!!')
                self.loggedin = True
            else:
                print("please input th correct user name / password ")
        print("\n")
        self.menu()


    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"following content has been posted -> {txt}")
        else:
            print("Please signin first to post someting....")
        print("\n")
        self.menu()
    

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Please enter yuor friends name -> ")
            print(f"""following content -> {txt}
                    sent to {frnd}""")
        else:
            print("Please signin first to post someting....")
        print("\n")
        self.menu()




obj = chatbook()
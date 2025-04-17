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
                           e. press any other key to exit""""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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

obj = chatbook()
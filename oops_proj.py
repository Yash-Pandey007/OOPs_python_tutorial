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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


obj = chatbook()
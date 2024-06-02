import random
import datetime
class Bookmyshow:
    def my_profile(self):
        print("welcome--to---profile-page-----")
        print("---account details are------",self.account_details)
        print("preferred city-------",self.city_name)
        print("1.home page","2.exit app")
        select=int(input("choose option:-"))
        if select==1:
            self.home_page_2()
        else:
            print("-----------THANKS YOU-----------")
            quit()
##-------LOGIN PAGE-----LOGIN PAGE---------LOGIN PAGE-------##
    def login_page__1(self):
        print("-----welcome TO LOGIN PAGE---------")
        welcomepage={1:"continue with google",2:"continue with email",3:"continue with phone number",4:"skip"}
        print(welcomepage)
        welcomepage_opt=int(input("choose your option to login:-"))
        print("you have choosen:-",welcomepage[welcomepage_opt]) 
        if welcomepage_opt==1 or welcomepage_opt==2:
            self.account_details=input("enter you account details:-")
            while "@gmail.com" not in self.account_details:
                print('you have entered wrong details.try again-----------')       
                self.account_details=input("enter you account details:-")
            else:
                vv1=self.otp_for_login_page()
                print(vv1)
        elif welcomepage_opt==3:
            self.account_details=input("enter you phone number:-")
            while len(self.account_details)!=10:
                print('you have entered wrong phone number.try again-----------')       
                self.account_details=input("enter you phone number:-")
            else:
                vv1=self.otp_for_login_page()
                print(vv1)
        elif welcomepage_opt==4:
            print("ok")
        places=["hyderabad","warangal","mahabubabad","uppal","medchal","narsampet","nanakramguda","lb nagar","hanamkonda","mulugu"]
        print({1:"auto detect mylocation",2:"search my city"})
        location =int(input("choose numeric option:-"))
        if location==1:
            self.city_name=random.choice(places)
            print(self.city_name)
        else:
            self.city_name=input("enter your city name:")
            while self.city_name not in places:
                print("oops......\n check another nearby city")
                self.city_name=input("enter your city name:")
            else:
                print("------LOCATION PLACED SUCCESSFULLY----")
    ##OTP_login page--------login page------login page------login page------##
    def otp_for_login_page(self):
        counts=2
        googleotp=random.randint(1000,9999)
        print("The otp for google account is",googleotp)
        googleotp1=int(input("enter you 4-digit otp:-"))
        while googleotp!=googleotp1:
            if counts==0:
                print("maximum attempts are reached.try after sometime\n---THANK YOU---")
                quit()
            print("invalid otp \nplease try again")
            print(counts,"chances left")
            print({1:"resend",2:"go back"})
            wrong_otp=int(input("choose numeric option:-"))
            if wrong_otp==1:
                googleotp=random.randint(1000,9999)
                print("The otp for google account is",googleotp)
                googleotp1=int(input("enter you 4-digit otp:-"))
            else:
                print("-------WELCOME BACK TO LOGIN PAGE-----")
                print(self.login_page__1())
            counts=counts-1
        else:
            print("***-----LOGIN SUCCESSFUL---")
    #####movies page------movies page------movies page--------#####
    def home_page_2(self):
        print("-----welcome TO HOME PAGE---------")
        movies=["prasanna vadhanam","sathyabama","love me","furiosa","rajuyadav","maidaan","pushpa-2","project-k"]
        theatres=["ASIAN SRIDEVI MULTIPLEX","RADHIKA THEATRE","ASHOKA THEATRE","VIJAYA THEATRE","SHARADA THEATRE","VENKATESHWARA ASIAN","CINEPOLIS","INOX","JP CINEMAS"]
        print({1:"movies",2:"live events",3:"profile"})
        select=int(input("enter your option:-"))
        if select==1:
            print(movies)
            self.selected_movie_name=input("enter movie name:-")
            while self.selected_movie_name  not in movies:  
                print("----OOPS----\n SELECTED MOVIE IS NOT RUNNING IN YOUR CITY---:):)")
                print({1:"search other movie",2:"exit"})
                choose=int(input("enter your option:-"))
                if choose ==1:
                    print(self.home_page_2())
                else:
                    print("---------APP EXIT-----")
                    quit()  
            else:
                print(self.movie_theatres_3())
        elif select==2:
            print({1:"comedy shows-starts every sunday 7PM--ASIAN THEATRE.",2:"Goda kurchi( a telugu standup comedy telugu)-sunday 3 july 2pm--MALLIKA THEATRE.",3:"comedy galaata 15june 6pm--SRIDEVI THEATRE",4:"comedy buffet-10th june 9pm-SANDHYA THEATRE."})
            sel=int(input("choose your option to book ticket:-"))
            if sel==1 or sel==2 or sel==3 or sel==4:
                self.movie_theatre_time_seats_5()
        elif select==3:
            print("--------MY PROFILE-------")
            print(self.my_profile())
        else:
            print("------something went wrong------")
            print(self.login_page__1)
    ###### THEATRES PAGE   THEATRES PAGEEE THEATRES PAGEE###
    def movie_theatres_3(self):             ### this method  will print the theatres name
        print("------movies-------- and----theatres---page-")
        theatres=["ASIAN SRIDEVI MULTIPLEX","RADHIKA THEATRE","ASHOKA THEATRE","VIJAYA THEATRE","SHARADA THEATRE","VENKATESHWARA ASIAN","CINEPOLIS","INOX","JP CINEMAS","PVR MULTIPLEX","SANDHYA THEATRE","VASU MULTIPLEX","SAPTAGIRI 70MM"]
        seats=["A","B","C","D","E","F","G","H","I","J","L","M","N","O"]
        no_of_theatres=0
        total_no_of_selected_movie_running_theatres=[]
        while no_of_theatres<4:
            random_theatre=random.randint(0,12)
            total_no_of_selected_movie_running_theatres.append(theatres[random_theatre])
            no_of_theatres+=1
        no_of_shows=0                        ##used to count the loop.
        show_start_time=[]                                      ##used to count the loop.
        selected_movie_running_theatres={}                        ## selected movie theatres will show in this variable
        key1=[1,2,3,4]
        selected_movie_running_theatres=dict(zip(key1,total_no_of_selected_movie_running_theatres))
        print("1.select theatres","2.go back","3.exit")
        select=int(input("enter your choice:-"))
        if select==1:
            print(selected_movie_running_theatres) 
            choose=int(input("choose the theatre:-"))
            if choose==1 or choose==2 or choose==3 or choose==4:
                self.selected_theatre=selected_movie_running_theatres.get(choose)
                print("YOUR SELECTED THEATRE IS-----",self.selected_theatre)
                self.movie_theatre_times_4()
        elif select==2:
            self.home_page_2() 
        else:
            print("exit")
            quit()
#####  selecting show times selecting show times selecting show times#########
    def movie_theatre_times_4(self):
        print("-----  THEATRE TIMING PAGE---------")
        selected_timings=[]
        final_selected_movie_timings={}
        selected_movie_timings={}
        keys2=[1,2,3,4,5]
        show_counts=0
        shows={1:"09:00 am",2:"09:30 am",3:"09:45 am",4:"10:00 am",5:"10:30 am",6:"11:00 am",7:"11:45 am",8:"12:00 pm",9:"12:30 pm",10:"01:00 pm",11:"01:30 pm",12:"01:45 pm",13:"02:00 pm",14:"02:15 pm",15:"02:30 pm",16:"03:00 pm",17:"05:00 pm",18:"06:00 pm",19:"06:30 pm",20:"06:45 pm",21:"07:00 pm",22:"09:00 pm",23:"09:30 pm",24:"10:00 pm",25:"10:30 pm",26:"10:45 pm",27:"11:15 pm",28:"11:30 pm"}   
        while show_counts<5:
            ss=random.randint(1,29)
            c=shows.get(ss)
            selected_timings.append(c)
            show_counts+=1
            selected_movie_timings=zip(keys2,sorted(selected_timings))
            final_selected_movie_timings=dict(selected_movie_timings)
        print(final_selected_movie_timings)
        select_time={}
        select_show_time=int(input("choose show time:-"))
        if select_show_time==1 or select_show_time==2 or select_show_time==3 or select_show_time==4 or select_show_time==5:    
            self.selected_time_to_book_seats=final_selected_movie_timings.get(select_show_time)
            print("YOUR SHOW TIME IS-",self.selected_time_to_book_seats)
        print("1.book seats","2.change movie timing","3.change movie","4.change movie theatre","5.exit")
        p=int(input("enter your option;-"))
        if p==1:
            self.movie_theatre_time_seats_5()
        elif p==2:
            self.movie_theatre_times_4()
        elif p==3: 
            self.home_page_2()
        elif p==4:
            self.movie_theatres_3()
        else:
            print("1.i am sure.","2.continue")
            pr=int(input("choose your option:-"))
            if pr==1:
                print("session expired")
                quit()
            else:
                self.movie_theatre_times_4()  
### seat selecting process-------seat selecting process-----seat selecting process-------  
    def movie_theatre_time_seats_5(self):
        print("----- SEAT BOOKING PAGE---------")
        hall_seats=[]
        seat_index=0
        seat_count=0
        screen="----SCREEN----"
        width=80
        self.theatre_hall_seats=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
        seat=["A","B","C","D","E","F","G","H","I","J","K","L"]
        for i in seat:
            for j in range(1,16):
                hall_seats.append(i+str(j))
        for nmr in range(len(hall_seats)):
            if hall_seats[nmr][0]==seat[0]:
                self.theatre_hall_seats[0].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[1]:
                self.theatre_hall_seats[1].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[2]:
                self.theatre_hall_seats[2].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[3]:
                self.theatre_hall_seats[3].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[4]:
                self.theatre_hall_seats[4].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[5]:
                self.theatre_hall_seats[5].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[6]:
                self.theatre_hall_seats[6].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[7]:
                self.theatre_hall_seats[7].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[8]:
                self.theatre_hall_seats[8].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[9]:
                self.theatre_hall_seats[9].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[10]:
                self.theatre_hall_seats[10].append(hall_seats[nmr])
            elif hall_seats[nmr][0]==seat[11]:
                self.theatre_hall_seats[11].append(hall_seats[nmr])
            else:
                self.theatre_hall_seats[12].append(hall_seats[nmr])
        for i in self.theatre_hall_seats:
            print(i)
        screens=screen.center(width)
        print(screens)
        self.no_of_seats=int(input("enter no_of_seats_want_to_book:-"))
        seats_count_for_loop=0
        self.booked_seats=[]
        while seats_count_for_loop<self.no_of_seats:
            book=input("select  the seat number:-")
            self.booked_seats.append(book)
            seats_count_for_loop+=1
        print("SELECTED SEATS ARE----",self.booked_seats)
        booked="booked"
        for i in range(len(self.booked_seats)):
            for j in range(len(self.theatre_hall_seats)):
                for k in range(len(self.theatre_hall_seats[j])):
                    if self.theatre_hall_seats[j][k]==self.booked_seats[i]:
                        self.theatre_hall_seats[j][k]=booked
        for i in self.theatre_hall_seats:
            print(i) 
        print({1:"change seats",2:"go to payment method",3:"exit page"})
        option=int(input("choose your option:-"))
        if option==1:
            print(self.movie_theatre_time_seats_5())
        elif option==2:
            self.cost=199*self.no_of_seats,"rupees."
            print(self.cost)
            self.payment_method_6()
        else:
            print("------BOOKING CANCELLED-----")
            quit()
######last page-----last pageee----last pageee-------#####
##### payment process--------- -payment processs-------- payment process-----
    def payment_method_6(self):
        print("-------TYPE OF PAYMENT MODES--------")
        print({1:"credit/debit card",2:"upi",3:"go back"})
        option=int(input("choose your payment method option:-"))
        if option==1:
            self.card_number=input("enter 10-digit card number:")
            self.expire_year=int(input("enter year:"))
            count=2
            while len(self.card_number)!=10 or self.expire_year<2023:
                if count==0:
                    print("maxi attmpts reached..")
                    quit()
                print("invalid")
                print({1:"re_enter",2:"exit"})
                chose=int(input("enter your choice:-"))
                if chose==1:
                    self.card_number=input("enter 10-digit card number:")
                    self.expire_year=int(input("enter year:"))
                else:
                    self.home_page_2()
                count=count-1
            else:
                self.otps_for_payment()
        elif option==2:
            self.upi_nmbr=input("enter 13-digit upi id:")
            counts=2
            while len(self.upi_nmbr)!=14  or self.upi_nmbr[10]!="@":
                if counts==0:
                    print("maximum attempts reached")
                    quit()
                print({1:"re_enter",2:"exit"})
                chose=int(input("enter your choice:-"))
                if chose==1:
                    upi_nmbr=input("enter 13-digit upi id:")
                else:
                    self.home_page_2()
                counts=counts-1
            else:
                self.otps_for_payment()
        else:
            self.home_page_2()
    def otps_for_payment(self):
        otp=random.randint(1000,2000)
        print("OTP for payment process is",otp)
        otp1=int(input("enter the otp:-"))
        count=2
        while otp!=otp1:
            if count==0:
                print("attempts reached")
                quit()
            print("-----invalid otp----")
            print("you have ",count,"left")
            print("1.resend","2.back to home page.")
            choose=int(input("enter your option:-"))
            if choose==1:
                otp=random.randint(1000,2000)
                print("OTP for payment process is",otp)
                otp1=int(input("enter the otp:-"))
            else:
                self.home_page_2()
            count=count-1    
        else:
            self.movie_tickets_7() 
        print("1.home page.","2.my profile")
        choose=int(input("choose option:-"))
        if choose==1:
            print(self.home_page_2())
        elif choose==2: 
            self.my_profile()
        else:
            print("-----------something went wrong-----")         
    def movie_tickets_7(self):
        print("------payment succuessful-------\n ----------booking details are:----")
        print("-----------your boookings---------")
        print("1.---------booking done on-----",datetime.datetime.now())
        print("2.---------booked movie is--",self.selected_movie_name)
        print("3.---------booked theatre is--",self.selected_theatre)
        print("4.---------booked time is:-",self.selected_time_to_book_seats)
        print("5.---------no_of_seats----",self.no_of_seats)
        print("6.---------no_of_booked seats are--",self.booked_seats)
        print("7.---------cost is------",self.cost)
        print("1.home page","2.exit app")
        select=int(input("choose option:-"))
        if select==1:
            self.home_page_2()
        else:
            print("-----------THANKS YOU-----------")
            quit()
        
class1=Bookmyshow()
class1.login_page__1()
class1.home_page_2() 

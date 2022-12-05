import datetime;
#this program is used to check the age and give access to the right people allowed in a club
#you must be 18 or older to be allowed entry

print("WELCOME TO YOUR FINEST PUB, HOPE YOU ENJOY YOUR TIME WITH US !!!");
print("PLEASE ANSWER THE FOLLOWING SET OF QUESTIONS UPON ENTRY");
print("SIGNED : MANAGEMENT !!!");

name = input("Please Enter your firstname as indicated in your ID: ");
surname = input("Pleas Enter your lastname as indicated on your ID:");
Year_of_birth = int(input("Please Enter your year of birth as indicated in your ID: "));
current_year = datetime.datetime.now().year;
Current_age = current_year - Year_of_birth;

if(Current_age < 18):
    
        print("==================================================================");
        print("ENTRY DENIED !! YOU'RE BELOW 18");
        print("SIGNED : MANAGEMENT !!");
        today = datetime.datetime.now();
        print(today);
        print("==================================================================");
    
else:
        print("==================================================================");
        print("YOU' RE  ", Current_age,", MEANING YOU MEET THE ENTRY CRITERIA !!");
        print("ACCESS GAINED !!");
        print("ENJOY YOUR TIME WITH US ", name );
        today = datetime.datetime.now();  
        print(today);
        print("====================================================================");
    




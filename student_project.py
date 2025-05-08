"""
Do not begin coding.
Instead, fill out the Planning worksheet.
"""
#------DATA-----#
clients = ["Rodriguez", "Taylos", "Kinard", "Valerio", "Smith", "Perez", "Imparto", "Drummend", "White"]

appointments = ["10/28" , "11/6", "10/29", "11/9", "12/8", "9/3", "12/28", "10/3", "11/5"]

times = ["9:30", "10:30", "11:00", "12:30", "12:00", "9:30", "8:30", "11:30", "10:00"]

free_days = ["11/1", "12/3", "12/22"]

free_times = ["11:00", "10:30", "9:30", "8:00", "8:30"]


def add_client(first, last):
    if last not in clients:
        return clients.insert(0,last)
    else:
        return clientsinsert(0, first)
    
def new_day(day):
    free_days.remove(day)
    appointments.insert(0, day)
    
def new_time(time):
    free_times.remove(time)
    times.insert(0, time)
    

#welcome user to the site 
print("  WELCOME TO CARETOBE")
print("We are open all morning monday - friday with limited space")
print()

new_appoiment = input("If you are making an appoiment please type " "\"AP\"" " *if not hit enter* ").lower()
if new_appoiment == "ap":
    #ask for name slicing it too
    new_client = input("please enter the first and (1)last name of the patient ").strip()
    #checking the input if it has 2 names
    while " " not in new_client:
       new_client = input("Error:please make sure to enter a first and one last name ").strip()

    if " "  in new_client:
        first, last = new_client.split()
    
    add_client(first, last)
    
    # print out dates available 
    print("please pick one of the available dates (MM/DD) ")
    print(free_days)
    
    #let them pick (write it)
    selected_day = input()
    while selected_day not in free_days:
        selected_day = input("invalid: Please select a valid day. ")
    new_day(selected_day)
    
    # print out the time available 
    print("please select a time you would like to arrive ")
    print(free_times)
    #let them type which one they would like
    
    selected_time = input()
    while selected_time not in free_times:
        selected_time = input("Invalid: Please select a valid time")
    new_time(selected_time)
    
    print(" You have an appoiment at", selected_time, "at", selected_day, "please make sure to come at least 10 minutes early")
    print()
print()
#looking for an appoiment 
finding = input("if you are looking for your appoiment type" "\"LK\"" " *if not hit enter* ").lower()
if finding == "lk":
    looking = input("enter the last name of the appoiment: ")
    #checking if the list by last name
    if looking in clients: #in the list 
        index = clients.index(looking)
        print(clients[index], "has an appoiment on" ,appointments[index], "at" ,times[index], ":please come in at least 10 minutes early")
     
    elif looking not in clients: #not in the list, trying first name 
        print("Seems like we couldn't find you, try using the first name ")
        seeking = input()
    #checking if in the list by first name 
        if seeking in clients:
            index = clients.index(looking)
            print(clients[index], "has an appoiment on" ,appointments[index], "at" ,times[index], ":please come in 10 minutes early")
            
        else:#if the clients name was not found 
            print("sorry we couldn't find you")
            #asking if they want to make a appoiment 
            new_appoiment = input("would you like to make an appoiment? [y/n]")
            if new_appoiment == "y":
                #ask for name slicing it too
                new_client = input("please enter the first and (1)last name of the patient ").strip()
                #checking the input if it has 2 names
                while " " not in new_client:
                   new_client = input("Error:please make sure to enter a first and one last name ").strip()
            
                if " "  in new_client:
                    first, last = new_client.split()
                #making sure the last name isn't in clients
                add_client(first, last)
                # print out dates available 
                print("please pick one of the available dates (MM/DD) ")
                print(free_days)
                #let them pick (write it)
                selected_day = input()
                while selected_day not in free_days:
                    selected_day = input("invalid: Please select a valid day. ")
                new_day(selected_day)
                
                # print out the time available 
                print("please select a time you would like to arrive ")
                print(free_times)
                #let them type which one they would like
                selected_time = input()
                while selected_time not in free_times:
                        selected_time = input("Invalid: Please select a valid time")
                new_time(selected_time)
                print(" You have an appoiment at", selected_time, "at", selected_day, "please make sure to come at least 10 minutes. early")
                print()
    else:
            print("okay!")

                    
print("We hope to see you again, Thanks for checking us out")

# #Make a car Engine
# #The program will run until you type quit
# #If you type help three option will appear
# #start, stop, quit
# #If you type something beside these command the program will print out "I don't understand that"


# command = input()
# while command.upper() != "QUIT":
#     if command.upper() == "HELP":
#             print("Start- to start the car")
#             print("Stop - to stop the car")
#             print("Quit - to exit")
#             command=input()
#             if command.upper() == "START":
#                 print("Car started, ready to go")
#                 command=input()
#             if command.upper() == "STOP":
#                 print("Car Stopped")
#                 command=input()
#     if command.upper() != {"START, STOP"}:
#         print("I don't understand that...")
#         command=input()
        


#Make a car Engine
#The program will run until you type quit
#If you type help three option will appear
#start, stop, quit
#If you type something beside these command the program will print out "I don't understand that"


command = ""
while command.upper() != "QUIT":
    if command.upper() == "HELP":
            print("Start- to start the car")
            print("Stop - to stop the car")
            print("Quit - to exit")
            command=input()
            while command.upper() == "START":
                    print("Car started, ready to go")
                    command=input()
            while command.upper() == "STOP":
                    print("Car Stopped")
                    command=input()
    while command.upper() != "START" or "STOP" or "QUIT":
         print("I don't understand that...")
         command=input()
        
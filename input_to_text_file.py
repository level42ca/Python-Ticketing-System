import os

TicketStatus = "Completed"
TicketDescription = "Upgraded Laptop"

def StartUp():
    # Checks to see if the Tickets Directory exists or not.
    
    print("Checking Tickets Directory:")
    if os.path.isdir('./Tickets') == True:
        print("./Tickets directory was found.\n")
    else:
        print("ERROR! ./Tickets directory could not be found.\n")
    GetTickets()

def GetTickets():
    # Checks the existing ticket to find out what the next ticket number should be.

    print("Checking Current tickets:")

    # This will get the 6 numerical digits of each file in the Tickets directory, this should pull all existing ticket numbers.
    x = [f[1:7] for f in os.listdir('./Tickets')]
    # This will print out all the tickets.
    print("{}\n".format(x))

    print("Last ticket found:\n{}\n".format(max(x)))

    # This will calculate and formulate the next ticket number to be used.
    NextTicket = int(max(x)) + 1

    print("The next ticket will be:\n{}\n".format("%06d" % (NextTicket)))

    return NextTicket

def master():
    # Needs to read tickets directory and find the last number that was used and start the counter 1 after that.
        # If the last ticket was 000046, then the counter should start at 47.

    
    # Main Menu
    print("""
    #####################################################################
    ###                      Ticket_Master.py                         ###
    #####################################################################
    #                                                                   #
    # Hello, and welcome to Ticket_Master.py!                           #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #####################################################################
    #                                                                   #
    # Select from the following files:                                  #
    #     1 - Open a new Ticket                                         #
    #     2 - Open an exsiting Ticket                                   #
    #     3 - List all tickets                                          #
    #     4 -                                                           #
    #                                                                   #
    #####################################################################
    """)

    Selection = input("What would you like to do?\n")

    while Selection != 3:
        print("Please select one of the options above")
        Selection = input("What would you like to do?\n")
    
    if Selection == 1:
        return
    elif Selection == 2:
        return
    elif Selection == 3:
        print("")
        GetTickets()
        #master()
    elif Selection == 4:
        return

#Ticket Numbering System:
    # T000001

#File name structure:
    # T000001 - Status - Description.txt

#Ticket Contents:
    # Ticket Number:
    # Requester:
    # Request:
    # Creation Date:
    # Date Modified:
    # Notes:
    # Resolution:
    # Status:
    # Durration:

def CreateTicket():
    GetNextTicket = GetTickets()
    print("YOOO The next ticket will be:\n{}\n".format("%06d" % (GetNextTicket)))
    print("")
    
def PrintTicket():
    # Imports the next ticket number from "def GetTickets()"
    GetNextTicket = GetTickets()
    
    # "%06d" % (TicketNumber,) Will print the TicketNumber variable and ensure that the number is 6 digits, with 0's in front.
    # This is useful, because it lets you keep the TicketNumeber as an INT for processing.

    # This will create a new txt file with the next ticket number found above, and print a few lines into the text file.
    with open("Tickets/T{} - {} - {}.txt".format("%06d" % (GetNextTicket), TicketStatus, TicketDescription), "w") as TXT:

        print("Ticket Number: {}".format("%06d" % (GetNextTicket)), file=TXT)
        print("", file=TXT)
        print("Status: {}".format(TicketStatus), file=TXT)
        print("", file=TXT)
        print("Desctiption: {}".format(TicketDescription), file=TXT)

    print("T{} - {} - {}.txt was created successfully".format("%06d" % (GetNextTicket), TicketStatus, TicketDescription))

def ReadTicket():
    # Imports the next ticket number from "def StartUp()"
    # GetNextTicket = StartUp()
    GetNextTicket = 4

    print("Checking Current tickets:")

    # This will get the 6 numerical digits of each file in the Tickets directory, this should pull all existing ticket numbers.
    x = [f[1:7] for f in os.listdir('./Tickets')]
    # This will print out all the tickets.
    print("{}\n".format(x))

    if "000057" in x: 
        print('success')

    
    
    print(max(x))
    print("%06d" % (GetNextTicket))

    if x == GetNextTicket:
        print("yes")
    else:
        print("no")
    print("Last ticket found:\n{}\n".format(max(x)))








#NEEDS TO BE CHANGED TO FIND A TICKET BASED ON ONLY THE TICKET NUMBER, NOT THE WHOLE STRING.
    
    # ‘r’ – Read mode which is used when the file is only being read 
    file = open("Tickets/T{} - {} - {}.txt".format("%06d" % (GetNextTicket), TicketStatus, TicketDescription), "r")

    print(file.read())
    #print(file)
    


#master()
StartUp()
CreateTicket()
PrintTicket()
ReadTicket()

# declaring the names of all members along with their additional info
name = ["James","George","Paul","Alex"]
rank = ["crew","commander","lieutenant","sergeant"]
division = ["enforcement","operations","defence","supervision"]
crew_no = [101,102,103,104]

active = True

# allows for user to view crew members in database
def view_crew_members(name,rank,division,crew_no):
    option = input("what would you like to do today?")
    if option == "1":
        print("crew member list:")
    for i in range(len(name)):
        print(name[i] + " - " + rank[i])

# used for adding members to the database
def add_new_member(name,rank,division,crew_no):
    newname = input("name of new member")
    newrank = input("rank of new member")
    newdiv = input("division of new member")
    nextid = max(crew_no) + 1
    name.append(newname)
    rank.append(newrank)
    division.append(newdiv)
    crew_no.append(nextid)
    print("new member added")

# updates member details for the user
def update_member(rank,crew_no):
            updateid = int(input("what is the member's ID number?"))
            position = crew_no.index(updateid)
            print(position)
            print(rank[position])
            newrank = input("what rank would you like to change the member to?")
            rank[position] = newrank
            print("new details confirmed")

# removes members from the crew
def remove_crew(name,rank,division,crew_no):
    removalcrew = int(input("what is the member's ID number?"))
    if removalcrew in crew_no:
        position = crew_no.index(removalcrew)
        name.pop(position)
        rank.pop(position)
        division.pop(position)
        crew_no.pop(position)
        print("member successfully removed")
    else:
        print("ID not found, please try again")

def init_database():
    pass

def display_menu():
    pass

def search_crew(name,rank,division,crew_no):
    crewid = int(input("what is the id of the crew member youre looking for?"))
    if crewid in crew_no:
        position = crew_no.index(crewid)
        print("name:, name[position]")
        print("rank", rank[position])
        print("division", division[position])
    else:
        print("member not found, please try again")

def filter_by_division(name,division):
    filterchoice = input("enter division to filter by below")
    
    for i in range(len(division)):
        if division[i] == filterchoice:
            print(name[i], "-", division[i])
     
def calculate_payroll(rank):
    pay = {
        "crew": 200,
        "sergeant": 300,
        "lieutenant": 400,
        "commander": 500
    }
    
    totalpay = 0
    
    for r in rank: 
        total+=totalpay.get(r, 0)
    
    print("total payroll: £")

def count_officers(rank):
    ranks = ["commander", "lieutenant"]

    count = 0

    for r in rank:
        if r in ranks:
            count +=1
    print("number of officers", count)

# main menu initial screen
def run_system_moonlith():
    print("LOADING...")
    print("FLEET MANAGER MENU")

#activates the options in the main menu
    while True:
        print("MENU")
        print("1. View crew members")
        print("2. Add new crew member")
        print("3. update crew details")
        print("4. remove crew member")
        print("5. leave menu")
        print("6. search members")
        print("7. filter by division")
        print("8. calculate payroll")
        print("9. perform an officer count")

# asks the user for input from the main menu display
        option = input("what would you like to do today?")

# directs user to option 1
        if option == "1":
            view_crew_members(name,rank,division,crew_no)

# directs user to option 2
        elif option == "2":
            add_new_member(name,rank,division,crew_no)

# directs user to option 3
        elif option == "3":
            update_member(name,rank,division,crew_no)

# directs user to option 4
        elif option == "4":
           remove_crew(name,rank,division,crew_no)

#directs user to option 5
        elif option == "5":
            search_crew(name,rank,division,crew_no)
        
#directs user to option 6
        elif option == "6":
            filter_by_division(name,division)

#directs user to option 7
        elif option == "7":
            calculate_payroll(rank)

#directs user to option 8
        elif option == "8":
            count_officers(rank)

#breaks the loop and exits main menu
        elif option == "9":
            print("thank you for using the main menu, have a great day")
            break

# prevents invalid inputs from crashing the code
        else:
            print("invalid input, please try again")

# calls main code
run_system_moonlith()
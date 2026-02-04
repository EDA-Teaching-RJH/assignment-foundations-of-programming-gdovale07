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
    print("new member added")
# updates member details for the user
def update_member(name,rank,division,crew_no):
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
            position = crew_no.index(removalcrew)
            name.pop(position)
            rank.pop(position)
            division.pop(position)
            print("member successfully removed")
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
# directs user to option 5 and breaks the code from looping 
        elif option == "5":
            print("thank you for using this service, have a great day")
            break
# prevents invalid inputs from crashing the code
        else:
            print("invalid input, please try again")

def init_database():
     pass

# calls main code
run_system_moonlith()
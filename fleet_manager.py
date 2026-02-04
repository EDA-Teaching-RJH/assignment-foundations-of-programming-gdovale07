name = ["James","George","Paul","Alex"]
rank = ["crew","commander","lieutenant","sergeant"]
division = ["enforcement","operations","defence","supervision"]
crew_no = [101,102,103,104]

active = True

def view_crew_members(name,rank,division,crew_no):
    pass

def add_new_member(name,rank,division,crew_no):
    pass

def update_member(name,rank,division,crew_no):
    pass
def remove_crew(name,rank,division,crew_no):
    pass

def run_system_moonlith():
    print("LOADING...")
    print("FLEET MANAGER MENU")

    while True:
        print("MENU")
        print("1. View crew members")
        print("2. Add new crew member")
        print("3. update crew details")
        print("4. remove crew member")
        print("5. leave menu")

        option = input("what would you like to do today?")

        if option == "1":
            print("crew member list:")
            
            for i in range(len(name)):
                print(name[i] + " - " + rank[i])

        elif option == "2":
            newname = input("name of new member")
            newrank = input("rank of new member")
            newdiv = input("division of new member")

        elif option == "3":
            updateid = int(input("what is the member's ID number?"))
            position = crew_no.index(updateid)
            print(position)
            print(rank[position])
            newrank = input("what rank would you like to change the member to?")
            rank[position] = newrank
            print("new details confirmed")


        elif option == "4":
            removal = input("what is the ID of the member would you like to remove?")
            index = crew_no.index(removal)
            name.pop(index)
            rank.pop(index)
            division.pop(index)
            print("member successfully removed")
       
        elif option == "5":
            print("thank you for using this service, have a great day")
            break

        else:
            print("invalid input, please try again")

run_system_moonlith()
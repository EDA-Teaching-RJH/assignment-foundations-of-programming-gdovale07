name = ["James","George","Paul","Alex"]
rank = ["crew","commander","lieutenant","sergeant"]
division = ["enforcement","operations","defence","supervision"]
crew_no = [101,102,103,104]

active = True

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
            break

        else option == "5":
            print("thank you for using this service, have a great day")
            break
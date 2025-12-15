from pakuri import Pakuri
from pakudex import Pakudex

print("Welcome to Pakudex: Tracker Extraordinaire!")
user_input = input("Enter max capacity of the Pakudex: ")
work = True
while(work):
    if user_input.isdigit():
        if (int(user_input) > 0):
            pakudex = Pakudex(int(user_input))
            work = False
        else:
            user_input = input("Please enter a valid size.")
    else:
        user_input = input("Please enter a valid size.")
    
print(f"The Pakudex can hold {pakudex.get_capacity()} species of Pakuri.")

inp = ""
while (inp != "6"):
    print("""Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit""")
    inp = input("What would you like to do? ")
    if (inp == "1"):
        list = pakudex.get_species_array()
        if (len(list) == 0):
            print("No Pakuri in Pakudex yet!")
        else:
            print("Pakuri In Pakudex:")
            for i in range(len(list)):
                print(f"{i+1}. {list[i]}")
    elif(inp == "2"):
        spec = input("Enter the name of the species to display: ")
        check: bool = False
        for p in pakudex.get_array():
            if(p.get_species() == spec):
                check = True
                print(f"""Species: {p.get_species()}
Attack: {p.get_attack()}
Defense: {p.get_defense()}
Speed: {p.get_speed()}""")
        if(check == False):
            print("Error: No such Pakuri!?")
    elif(inp == "3"):
        check = False
        if(pakudex.get_size() < pakudex.get_capacity()):
            spec = input("Enter the name of the species to add: ")      
            for p in pakudex.get_array():
                if(p.get_species() == spec):
                    check = True
                    print("Error: Pakudex already contains this species!")
            if(not check):
                full = pakudex.add_pakuri(spec)
                if(not full):
                    print("Error: Pakudex is full!")
                else:
                    print(f"Pakuri species {spec} successfully added!")
        else:
            print("Error: 1Pakudex is full!")
    elif(inp == "4"):
        spec = input("Enter the name of the species to evolve: ")
        inside = pakudex.evolve_species(spec)
        if(inside):
            print(f"{spec} has evolved!")
        else:
            print("No such Pakuri!")
    elif(inp == "5"):
        pakudex.sort_pakuri()
        print("Pakuri have been sorted!")
    elif(inp == "6"):
        break
    else:
        print("Unrecognized menu selection!")

print("Thanks for using Pakudex! Bye!")
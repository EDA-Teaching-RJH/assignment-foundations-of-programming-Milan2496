n = ["Picard", "Riker", "Data", "Worf", "La Forge"]
r = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant Commander"]
d = ["Command", "Command", "Operations", "Security", "Engineering"]
id = ["SF-1701-A", "SF-1701-B", "SF-1701-C", "SF-1701-D", "SF-1701-E" ]


def init_database():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    print("\nCurrent Crew List:")           
    for i in range(len(n)):
        print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    name = input("\nWhat is your full name? ")
    print("USER " + name + " HAS LOGGED IN...")


def display_menu():
    print("\n--- MENU ---")
    print("1. Add Member")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")
    opt = int(input("\nSelect option: "))
    return opt


def add_member(n, r, d, id):
    rank = ["Captain", "Commander", "Lieutenant Commander", "Lieutenant"]
    new_name = input("Name: ")
    new_rank = input("Rank: ")
    new_rank = new_rank.title()
    while new_rank not in rank:
        new_rank = input("This is not a valid TNG Rank. Please enter a valid Rank: ")
        new_rank = new_rank.title()
    new_div = input("Division: ")   
    new_id = input("ID: ")      
    while new_id in id:
        new_id = input("This is not a unique ID. Please enter a unique ID: ")
    n.append(new_name)
    r.append(new_rank)
    d.append(new_div)
    id.append(new_id)
    print("\nUpdated Crew List:")
    for i in range(len(n)):
            print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def remove_members(n, r, d, id):
    rem = input("Name to remove: ")
    if rem in n:           
        idx = n.index(rem)
        n.pop(idx)
        r.pop(idx)
        d.pop(idx)
        id.pop(idx)
        print("Crew member removed")
    else:
        print("Name not found")
    print("\nUpdated Crew List:")
    for i in range(len(n)):
            print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def update_rank(n, r, d, id):
    CrewID = input("What is the ID of the Crew Member who's rank needs updating: ")
    while CrewID not in id:
        CrewID = input("Incorrect ID. What is the ID of the Crew Member who's rank needs updating: ")
    idx = id.index(CrewID)
    new_rank = input("What is the updated rank: ")
    r[idx] = new_rank
    print("Rank updated")
    print("\nUpdated Crew List:")
    for i in range(len(n)):
            print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def count_officers(r):
    print("Analyzing...")
    count = 0            
    for rank in r:
        if rank == "Captain" or rank == "Commander": 
            count = count + 1
    print(f"High ranking officers: {count} ")


def display_roster(n, r, d, id):
    print("\nNAME - RANK - DIVISION - ID")
    print("-----------------------------------------------------")
    for i in range(len(n)):
        print( n[i] + " - " + r[i] + " - " + d[i] + " - " + id[i])
    return n, r, d, id


def search_crew(n, r, d, id):
    searchterm = input("Enter a search term: ")    
    for i in range(len(n)):
        if searchterm in n[i]:            
            print(n[i], "-", r[i], "-", d[i], "-", id[i])
        elif searchterm in r[i]:            
            print(n[i], "-", r[i], "-", d[i], "-", id[i])
        elif searchterm in d[i]:            
            print(n[i], "-", r[i], "-", d[i], "-", id[i])
        elif searchterm in id[i]:            
            print(n[i], "-", r[i], "-", d[i], "-", id[i])


def filter_by_division(n, r, d, id):
    div = input("Enter the division (Command-Operations-Sciences): ")
    for i in range(len(d)):
        if div in d[i]:            
            print(n[i], "-", r[i], "-", d[i], "-", id[i])


def calculate_payroll(r):
    cap = 0
    com = 0
    lcom = 0
    lie = 0
    for rank in r:
        if rank == "Captain": 
            cap = cap + 1000
        elif rank == "Commander":
            com = com + 800
        elif rank == "Lieutenant Commander":
            lcom = lcom + 700
        elif rank == "Lieutenant":
            lie = lie + 500

    total = cap + com + lcom + lie
    print(f"The total cost of the crew is £{total}")


        

def main():
    init_database()
    run = True
    while True:    
        opt = display_menu()
        if opt == 1:
            add_member(n, r, d, id)
        elif opt == 2:
            remove_members(n, r, d, id)
        elif opt == 3:
            update_rank(n, r, id)   
        elif opt == 4:
            display_roster(n, r, d, id) 
        elif opt == 5:
            search_crew(n, r, d, id)
        elif opt == 6:
            filter_by_division(n, r, d, id)
        elif opt == 7:
            calculate_payroll(r)       
        elif opt == 8:
            count_officers(r)           
        elif opt == 9:
             print("Shutting down.")
             return


main()
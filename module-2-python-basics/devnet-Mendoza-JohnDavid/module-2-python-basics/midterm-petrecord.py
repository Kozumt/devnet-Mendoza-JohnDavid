pet_records = []


def add_pet():
    print("-- Pet Records --")
    pet_type = input("Pet Type: ").strip()
    if not pet_type:
        print("Please do not leave empty, Enter pet type.")
        return

    name = input("Pet Name: ").strip()
    if not name:
        print("Please do not leave empty, Enter pet name.")
        return
    
    age = int(input("Pet Year Old: ").strip())
    if age <= 0:
            print("Age cannot be less than 0.")
    return
    
new_pet = {
        "name": name,
        "type": pet_type,
        "age": age
    }
pet_records.append(new_pet)
print(f"Successfully added {name} the {pet_type}!")

def view_pets():
    print("\n-- View Pet Records --")
    if not pet_records:
        print("No pet records found.")
        return

for index, pet in enumerate(pet_records, start= 1):
    print(f"{index}. Name: {pet['name']} | Type: {pet['type']} | Age: {pet['age']}")

while True:
    print("\nChoices:")
    print("1. Add a Pet")
    print("2. View")
    print("0. Exit")
    
    try:
        choice = int(input("Choose an action [1-2, 0 to exit]: "))
        
        if choice == 1:
            add_pet()
        elif choice == 2:
            view_pets()
        elif choice == 0:
            print("Exiting the system...")
            break
        else:
            print("Invalid Input! Please choose from the options.")
    except ValueError:
        print("Please enter a valid number.")

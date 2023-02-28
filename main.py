#Cheap fish ($4.10 each): Shark, Flounder, Cod, Gurnet, Hoki, and Goldfish.
#Deluxe Fish ($7.20 each): Snapper, Pink Salmon, Tuna, Smoked Marlin, Pufferfish, Blobfish.
#If Frozen - discount $1.05 per fish item
#If Delivery - plus $5.00 to total cost, ask name, address, and phone no.
#If Pick up - ask name and phone no.
#MAX 7 fish per type, e.g. 7 cod and 7 flounder is acceptable. display nice error if invalid entry.
#At end of order, display names of fish (with price), total cost (display delivery cost), customer name, if cooked or frozen, if chips (plus price), and if for delivery (address and phonoe no.)


cheap_fish = [
    ["Shark","Flounder","Cod","Gurnet","Hoki","Goldfish"],
    [4.10, 4.10, 4.10, 4.10, 4.10, 4.10],
]

deluxe_fish = [
    ["Snapper","Pink Salmon","Tuna","Smoked Marlin","Pufferfish","Blobfish"],
    [7.20, 7.20, 7.20, 7.20, 7.20, 7.20]
]

user_order = [
    [],
    []
]

index_for_name = 0
index_for_price = 1
invalid_entry = "Please select a valid option"


def fish_catagory():
    while True:
        try:
            divider()
            print_array(["Deluxe","Cheaper","Finish Order"])
            divider()
            fish_catagory = int(input("Would you like a deluxe or a cheaper fish? "))
        except ValueError:
            print(invalid_entry)
            continue
        
        match fish_catagory:
            case 1:
                fish_order(deluxe_fish)
            case 2:
                fish_order(cheap_fish)
            case 3:
                print("PLACE HOLDER")
            case _:
                print(invalid_entry)


def input_checking(prompt: str, array: list):
    while True:
        try:
            input_index = int(input(prompt))
        except ValueError:
            print(invalid_entry)
            continue

        if input_index not in range(len(array) + 1):
            print(invalid_entry)
        else:
            return input_index

#Function that orders fish
def fish_order(fish_array: list):
    #Print menu
    divider()
    print_array(fish_array[index_for_name])
    divider()

    #Get index of fish from user input based on fish array, and store it
    fish_index = input_checking("What fish woukld you like? ", fish_array[index_for_name])
    fish_name = fish_array[index_for_name][fish_index - 1]
    
    #Check number of chosen fish and calculate the amount the user can order
    fish_remaining = 7 - array_quantity_counter(fish_name, user_order[index_for_name])
    fish_amount = input_checking("How many of this fish would you like? ", range(fish_remaining))

    #Get price from array and format as string
    item_price = (fish_array[index_for_price][fish_index - 1]) 
    price_string = "%.2f" % (item_price * fish_amount)

    #Print ordered fish and price
    print("Your choice: " + fish_name + " x" + str(fish_amount) + ", Price: $"
         + price_string)

    #Put ordered fish in user's order array
    for each in range(fish_amount):
        user_order[index_for_name].append(fish_name)
        user_order[index_for_price].append(item_price)
    

def array_quantity_counter(key, array: list):
    quantity = 0
    for item in array:
        if item == key:
            quantity += 1
    return quantity


def print_array(items: list):
    for index in range(len(items)):
        print(f"{index + 1}) {items[index]}")


def divider():
    print(20 * "-")

if __name__ == "__main__":
    fish_catagory()
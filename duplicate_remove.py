duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
final_list = []

def Remove(duplicate):
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    #print("Inside function body")
    return(final_list)

print(Remove(duplicate))

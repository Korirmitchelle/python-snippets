def check(entry):
    search = open('patients.txt', 'r')
    if str(entry) in str(search): 
        return (entry, "Word found")
    else:
        return entry, ("Word not found")



while True:
    entry=raw_input("\nWho are you looking for: ")
    print(check(entry)) 
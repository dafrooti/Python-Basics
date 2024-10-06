list = [["shrran", "543"], ["Meera", "432"], ["Lens", "573"]]

found = False

user = input("Input username")
for i in range (len(list)):
    list[i][0]
    if list[i][0] == user:
        found = True
        password = input("Input password")
        if list[i][1] == password:
            print("Access Allowed")
        else:
            
            print("Access Denied, wrong password")
    else:
        found = False
if found == False:
    print("Access Denied, wrong username")
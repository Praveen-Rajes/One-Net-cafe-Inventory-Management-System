titles = ['Item Code', 'Item Name', 'Item Brand', 'Price', 'Quantity', 'Category', 'Purchaced Date[DD-MM-YYYY]'] #Creating a list for Item table column names
import random #Importing Random function
Check = 0 #Creating a varibale to check SDD Status
VrlCheck = 0 #Creating a varibale to check VRL Status

#Creating a display menu
Menu = ''' 
                                  ___               _   _      _      ____       __      
                                 / _ \ _ __   ___  | \ | | ___| |_   / ___|__ _ / _| ___ 
                                | | | | '_ \ / _ \ |  \| |/ _ \ __| | |   / _` | |_ / _ \\
                                | |_| | | | |  __/ | |\  |  __/ |_  | |__| (_| |  _|  __/
                                 \___/|_| |_|\___| |_| \_|\___|\__|  \____\__,_|_|  \___|

                                                       +-+-+-+-+
             +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-|M|E|N|U|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                                                       +-+-+-+-+

             • Type AID for adding item details.
             • Type DID for deleting item details.
             • Type UID for updating item details.
             • Type VID for viewing the items table. (Sort according to the items category) and print the current total.
             • Type SID for saving the item details to the text file at any time.
             • Type SDD for selecting four dealers randomly from a file.
             • Type VRL for displaying all the details of the randomly selected dealers. (Sorted according to the location.)
             • Type LDI for display the items of the given dealer.
             • Type ESC to exit the program.'''

print(Menu)

def UserInput():
    "Defining a function to check the user input "
    global user
    user = ''
    options = ['AID', 'DID', 'UID', 'VID', 'SID', 'SDD', 'VRL', 'LDI', 'ESC']
    while user.upper() not in options:
        user = input("\nEnter the command from above menu :")
        if user.upper() not in options or user == '':
            print("you can only choose a option from above menu")

def ReadItemsFromTxt():
    "Defining a function to Read data from ItemsTable text File"
    global filteredList
    f = open("ItemTable.txt", "r")
    count = 0
    filteredList = []
    temList1 = []
    temList2 = []
    for line in f:
        count += 1
        if count > 3 and count % 2 == 0: #Reading Data from 4th line
            temList1 = line.split('|')  #Spliting the red Data By targetting Pipe('|') Symbole
        else:
            continue
        for data in range(len(temList1)):
            if data == 0 or data == 8:  #ignoring first '' Empty space and last '\n' newline elements from the temList1
                continue
            else:
                temList2.append(temList1[data]) #appendid all the elements between first and last to temList2
    filteredList.append(temList2) #appending temList2 to filteredList

def finalList():
    global raw, filteredList, finalList, items
    x = ''
    raw = []
    dummyList = []
    finalList = []
    for innerlist in filteredList:
        for data in innerlist:
            txt = data.split() #spliting all the elements of filterdList by space
            for i in txt:
                x += (i + ' ') # concatanation splited elemnts with a space
            raw.append(x)
            x = ''
    for i in raw:
        finalList.append(i[0:-1]) #append elements without the last space
    items = []
    count = 0
    for i in range(len(finalList)):
        count += 1
        dummyList.append(finalList[i])
        if count % 7 == 0:
            items.append(dummyList) #breaking elements 7 by 7 and appending it to items list as nested list
            dummyList = []

def checkItemCode():
    "Function to Check item code is already exist or not"
    global x
    for innerlist in items:
        while True:
            if innerlist[0] == x:
                print('''item code should be uniqe enterd item already exist please Try again : )''')
                x = input('Item Code :')
            else:
                break

def Aid():
    "Function for take item details when user enter AID"
    global x, titles
    record = []
    for inputmsg in titles:
        if titles.index(inputmsg) == 0 or titles.index(inputmsg) == 3 or titles.index(inputmsg) == 4: #checking the item code,price,quantity values with isnumaric
            x = (input(inputmsg + ':'))
            while x.isnumeric() != True:
                print("you can only enter numbers as a "+inputmsg)
                x = (input(inputmsg + ':'))
            checkItemCode()
            record.append(x)
        else:
            x = input(inputmsg + ':')
            while len(x) == 0:
                print("field can't be empty") #checking the enterd value if it is null
                x = input(inputmsg + ':')
            record.append(x)
    items.append(record)

def Did():
    "function for Delete a item"
    global items, x, checklist
    checklist = []
    print("enter the item id to delete")
    x = input('Item Code :') #x is user input
    for i in items:
        checklist.append(i[0]) #appending all the items code to check list
    while x not in checklist:  #checking the user entered item code in check list
        print("entered item code is not exsist on the table")  #if user entered code is not there in check list printing a message
        x = input('Item Code :')
    for i in items:
        if x == i[0]: #if the item code is equal to items list innerlists first element removing the list from items list
            items.remove(i)
    print("Item Deleted Succesfully")

def Uid():
    "Function to update a item"
    global titles, items, checklist
    print("enter the item id to update")
    x = input('Item Code :') #x is user input
    checklist = []
    count = 0
    for i in items:
        checklist.append(i[0]) # appending all the items codes to checklist
    print()
    while x not in checklist: #checking the item code is checklist
        print("entered item code is not exsist on the table")
        x = input('Item Code :')
    else:
        for i in items:
            if x == i[0]:
                for inputmsg in range(0, len(titles)):
                    x = input(titles[inputmsg] + ':') #calling elemnts from from titele list as a prompt message for user
                    count += 1
                    while x == "":  #checking the entered value if it is null
                        print("field can't be empty")
                        x = input(titles[inputmsg] + ':')
                    else:
                        i[count-1] = x
            else:
                continue

def Vid():
    #function to display item details in decening order
    checklist = []
    for i in range(0,len(items)):
        checklist.append(items[i][0])
    descList = []
    maxValue = 0
    if checklist[0] == 'Item Code':
        checklist.remove('Item Code')
    length = len(checklist)
    while len(descList) != length: #desclist for item codes
        for i in range(len(checklist)):
            if int(checklist[i]) > int(maxValue): #finding maxvalue from item code
                maxValue = (checklist[i])
        descList.append(str(maxValue)) # appending the maxvalue to desclist
        checklist.remove(str(maxValue))
        maxValue = 0
    if items[0] != titles:
        items.insert(0, titles)
    length = [0, 0, 0, 0, 0, 0, 0]
    count = 0
    for i in items:  #findin the lenth of each element in each column and taking the highest lenth for column width
        if length[0] < len(i[0]):
            length[0] = len(i[0])
        if length[1] < len(i[1]):
            length[1] = len(i[1])
        if length[2] < len(i[2]):
            length[2] = len(i[2])
        if length[3] < len(i[3]):
            length[3] = len(i[3])
        if length[4] < len(i[4]):
            length[4] = len(i[4])
        if length[5] < len(i[5]):
            length[5] = len(i[5])
        if length[6] < len(i[6]):
            length[6] = len(i[6])
    descItems = [titles]
    for i in descList:
        for j in items:
            if i == j[0]:
                descItems.append(j) #inserting innerlists according to ascending order
    line = ''
    for q in descItems:
        nl = ['', '', '', '', '', '', '']
        nl[0] = q[0].center(length[0], " ")
        nl[1] = q[1].center(length[1], " ")
        nl[2] = q[2].center(length[2], " ")
        nl[3] = q[3].center(length[3], " ")
        nl[4] = q[4].center(length[4], " ")
        nl[5] = q[5].center(length[5], " ")
        nl[6] = q[6].center(length[6], " ")
        # print(nl)

        for i in length:
            if count != len(length): #calculating the borader line size using length list
                line += "+" + "-" * i
                count += 1
        print(line + '+')
        for i in nl:
            if i == nl[-1]: #printing item details
                print("|" + i, end='|')
            else:
                print("|" + i, end='')
        print()
    print(line + "+")
    currentTotal = 0
    for i in range(1,len(items)):
        currentTotal += int(items[i][3]) * int(items[i][4]) #calculating current total
    print("Your current total is :",currentTotal)

def Sid():
    "function to save item details to a text file"
    global f, length
    file = open("ItemTable.txt", "w")
    if items[0] != titles:
        items.insert(0, titles)
    length = [0, 0, 0, 0, 0, 0, 0]
    count = 0
    for i in items:
        if length[0] < len(i[0]):
            length[0] = len(i[0])
        if length[1] < len(i[1]):
            length[1] = len(i[1])
        if length[2] < len(i[2]):
            length[2] = len(i[2])
        if length[3] < len(i[3]):
            length[3] = len(i[3])
        if length[4] < len(i[4]):
            length[4] = len(i[4])
        if length[5] < len(i[5]):
            length[5] = len(i[5])
        if length[6] < len(i[6]):
            length[6] = len(i[6])
    line = ''
    for q in items:
        nl = ['', '', '', '', '', '', '']
        nl[0] = q[0].center(length[0], " ")
        nl[1] = q[1].center(length[1], " ")
        nl[2] = q[2].center(length[2], " ")
        nl[3] = q[3].center(length[3], " ")
        nl[4] = q[4].center(length[4], " ")
        nl[5] = q[5].center(length[5], " ")
        nl[6] = q[6].center(length[6], " ")

        for i in length:
            if count != len(length):
                line += "+" + "-" * i
                count += 1
        file.write(line + "+")
        file.write("\n")
        for i in nl:
            if i == nl[-1]:
                file.write("|" + i + '|')
            else:
                file.write("|" + i + '')
        file.write("")
        file.write("\n")
    file.write(line + "+")

def ReadItemsFromDealers():
    "function to read data from delars table"
    global filteredList
    f = open("Dealers.txt", "r")
    count = 0
    filteredList = []
    temList1 = []
    temList2 = []
    for line in f:
        count += 1
        if count > 3 and count % 2 == 0:
            temList1 = line.split('|')
        else:
            continue
        for data in range(len(temList1)):
            if data == 0 or data == 5:
                continue
            else:
                temList2.append(temList1[data])
    filteredList.append(temList2)

def DealerfinalList():
    "Funtion to fileter delaers detail form delar text file"
    global raw, filteredList, finalList, Dealeritems
    x = ''
    raw = []
    dummyList = []
    finalList = []
    for innerlist in filteredList:
        for data in innerlist:
            txt = data.split()
            for i in txt:
                x += (i + ' ')
            raw.append(x)
            x = ''
    for i in raw:
        finalList.append(i[0:-1]) #filering Datas between " " and "\n" elements
    Dealeritems = []
    count = 0
    for i in range(len(finalList)):
        count += 1
        dummyList.append(finalList[i])
        if count % 4 == 0:
            Dealeritems.append(dummyList)
            dummyList = []

def Sdd():
    #Select 4 Delars Randomly using random function
    global  RandomSelection,DelarsDetails,Check
    DelarsDetails = []
    ReadItemsFromDealers()
    DealerfinalList()
    DelarsDetails = (Dealeritems[0:6])
    DelarsLocations = []
    for i in DelarsDetails:
        DelarsLocations.append(i[2])
    RandomSelection = []

    while len(RandomSelection) != 4:
        rand = (random.choice(DelarsLocations))
        if rand not in RandomSelection:
            RandomSelection.append(rand)
    if len(RandomSelection) == 4:
        print("4 Dealers are Selected Randomly")
    Check = 1

def Vrl():
    #printing Deatails of randomly selected delars
    global DelarsDetails,VrlCheck,DelarNames
    DelarNames = []
    while Check == 0 or len(RandomSelection) == 0 :
        print("Before selecting 'VRL' need to select 'SDD'" )
        UserInput()
        if user.upper() == "SDD":
            Sdd()
    SortedLocation = []
    while RandomSelection:
        low = RandomSelection[0]
        for i in RandomSelection:
            if i < low:
                low = i
        RandomSelection.remove(low)
        SortedLocation.append(low)
    TableLine = ('+' + '-' * 72 + '+')
    print(TableLine)
    print('{}{:20}{}{:15}{}{:15}{}{:15}{}'.format('| ','Name','| ','Contact No','| ','Location','| ','Items','| '))
    print(TableLine)
    for i in SortedLocation:
        for j in DelarsDetails:
            if j[2] == i:
                print('{}{:20}{}{:15}{}{:15}{}{:15}{}'.format('| ',j[0],'| ',j[1],'| ',j[2],'| ',j[3],'| '))
                DelarNames.append(j[0])
    VrlCheck  = 1
    print(TableLine)

def Ldi():
    #printing the items details of a delar from randomly selected delars
    global Check,DelarNames,ItemCodes
    while Check== 0:
        print("Before selecting 'LDI' need to select 'SDD'")
        UserInput()
        if user.upper() == "SDD":
            Sdd()
    while VrlCheck == 0:
        print("Before selecting 'LDI' need to select 'VRL'")
        UserInput()
        if user.upper() == "VRL":
            Vrl()
    print("Randolmly Selcted Delars Are:")
    for i in DelarNames:
        print('*',i)
    print()
    delarname = input("Enter Delar name display the item Details :")
    while delarname not in DelarNames:
        print("Enterd delar name does not excist in the Table")
        delarname = input("Enter Delar name display the item Details :")
    DelarItemsTable = Dealeritems[7:]
    filterDelarItem = []
    for i in DelarItemsTable:
        for j in i:
            if j == '':
                continue
            else:
                filterDelarItem.append(j)

    for delar in Dealeritems:
        if delarname in delar:
            ItemCodes = delar[3].split(',')
            break

    f = open("Dealers.txt", "r")
    DelarsItemList = []
    count = 0
    for line in f:
        count += 1
        if count > 18 and count % 2== 0:
            DelarsItemList += line.split('|')
    while ""  in DelarsItemList and '\n'  in DelarsItemList:
        DelarsItemList.remove("")
        DelarsItemList.remove("\n")
    print("The item Details of selected Delar :",delarname)
    Pipe = "|"
    line = "-"*len(' Item Code '+' Item Name         '+' Item Brand '+' Item Price '+' Item Quantity '+'|'+'|'+'|'+'|'+'|'+'|')
    print(line)
    print('{}{}{}{}{}{}{}{}{}{}{}'.format(Pipe,' Item Code ', Pipe,' Item Name         ', Pipe,' Item Brand ', Pipe,' Item Price ', Pipe,' Item Quantity ', Pipe))
    print(line)
    for j in ItemCodes:
        for i in range(0,len(DelarsItemList),5):
            if j == DelarsItemList[i][1:4]:
                print('{}{}{}{}{}{}{}{}{}{}{}'.format(Pipe,DelarsItemList[i],Pipe,DelarsItemList[i+1],Pipe,DelarsItemList[i+2],Pipe,DelarsItemList[i+3],Pipe,DelarsItemList[i+4],Pipe))
    print(line)

UserInput()
ReadItemsFromTxt()
finalList()
while user.upper() != 'ESC':
    if user.upper() == 'AID':
        Aid()
        UserInput()
    elif user.upper() == "DID":
        Did()
        UserInput()
    elif user.upper() == "UID":
        Uid()
        UserInput()
    elif user.upper() == "VID":
        Vid()
        UserInput()
    elif user.upper() == "SID":
        Sid()
        # table()
        UserInput()
    elif user.upper() == "SDD":
        Sdd()
        UserInput()
    elif user.upper() == "VRL":
        Vrl()
        UserInput()
    elif user.upper() == "LDI":
        Ldi()
        UserInput()

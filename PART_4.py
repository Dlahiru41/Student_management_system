# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1867452----------20210362_lahiru
 
# Date: 06/12/2021

passcount=0
module_trailerCount=0
module_retrieverCount=0
ExcludeCount=0
progress=[]
module_trailer=[]
module_retriever=[]
Exclude=[]
database2={'progress':0,'module trailer':0,'module retriever':0,'Exclude':0}

#predefined function to validate inputs and append them in to respective lists
def TheWholeProcess():
    global database2
    levels=['pass','defer','fail']
    Credits=[0,20,40,60,80,100,120]
    while True:
        FullCredits=[]    #.....values in [0,20,40,60,80,100,120] will append to this list
        
        FullCredits2=[]   #.....if the sum of the elements of list FullCredits is equal 120, those elements will assign to this list
        
        for a in levels:  #.....loop to get input values for 'pass','defer' and 'fail'
            while True:   #.....this loop wil iterate utill the user give a valid input
                try:
                    print('Enter Your Credits at',a,': ',end='')
                    value=int(input())
                    if value not in Credits:
                        print('out of range')
                        continue
                    if value in Credits:
                        FullCredits.append(value)
                    break
                except ValueError:
                    print("Integer Required")
                    continue
        if sum(FullCredits)==120:
            FullCredits2=FullCredits #.......FullCredits2 is the list which contains fully validated inputs
            break
        else:
            print('Total Incorrect')
            continue
    database=dict(zip((levels),(FullCredits2)))#.....database is a dictionary which its key is the grade and value as the input
    global passcount
    global module_trailerCount
    global module_retrieverCount
    global ExcludeCount
    global progress
    global module_trailer
    global module_retriever
    global Exclude
    
    if database['pass']==120:
        passcount+=1 #..............counter to calculate how many time the inputs give 'progress' 
        database2.update({'progress':passcount})#.......updates the value of the key
        progress.append(FullCredits2)
        print('progress')
    elif database['pass']==100:
        module_trailerCount+=1#........counter to calculate how many time the inputs give 'module trailer'
        database2.update({'module trailer':module_trailerCount})#.......updates the value of the key
        module_trailer.append(FullCredits2)
        print('Progress (module trailer)')
    elif (database['pass'] in [0,20,40,60,80]) and (database['fail'] in [0,20,40,60]):
        module_retrieverCount+=1#................counter to calculate how many time the inputs give 'module retriever'
        database2.update({'module retriever':module_retrieverCount})#.......updates the value of the key
        module_retriever.append(FullCredits2)
        print('Do not Progress – module retriever')
    elif database['fail'] in [80,100,120]:
        ExcludeCount+=1#............counter to calculate how many time the inputs give 'Exclude'
        database2.update({'Exclude':ExcludeCount})#.......updates the value of the key
        Exclude.append(FullCredits2)
        print('Exclude')
    return passcount,module_trailerCount,module_retrieverCount,ExcludeCount,database2#......returns all the values of the variables out of the function
        
print('Press "P" to implement the Student Version \n'
      'Press "S" to implement the Staff Version')
while True:#..........iterate to until user inputs a valid inputs 
    possition=input()
    lowerPossition=possition.lower()#..........opening space to user to input either uppercase or lowercase characters
    if lowerPossition not in ['s','p']:
        print('Invalid Respond \n''You must enter "S" or "p"')
        continue
    elif lowerPossition=='p':
        TheWholeProcess() #.........if the user wants to excute the student version the above predefined funtion excute only one time
        break
    elif lowerPossition=='s':
        TheWholeProcess()
        while True:
            print('Would you like to enter another set of data? \n'
            'Enter "y" for yes or "q" to quit and view results:')
            respond=input()
            lowerRespond=respond.lower()
            if lowerRespond not in ['y','q']:
                print('Invalid respond')
                continue
            elif lowerRespond=='y':
                TheWholeProcess()#.........allow user to enter more inputs and validate them if they want to excute the program more time
                continue
            elif lowerRespond=='q':
                break
        break
if lowerPossition=='s':#only works in staff version
    AlphaDict={'Progress':[progress],'Progress(module Trailer)':[module_trailer],
               'Module Retriever':[module_retriever],'Exclude':[Exclude]}

    #write the output into a text file
    import sys
    stdoutOrigin=sys.stdout
    sys.stdout=open("studentDatabase.txt","w")
    for key in AlphaDict:
        for i in AlphaDict[key]:
            for a in i:
                print(key,'-',a)
    sys.stdout.close()
    sys.stdout=stdoutOrigin #allow user to open a the file again and read it, if this line in not keyed the program will not allow user to open the text file and display a error massage

    #read the content on the text file
    print('The Below information is from studentDatabase.txt')
    file = open('studentDatabase.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line,end='')
    file.close()



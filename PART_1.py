# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1867452----------20210362_lahiru
 
# Date: 06/12/2021

passcount=0
module_trailerCount=0
module_retrieverCount=0
ExcludeCount=0
database2={'progress':0,'module trailer':0,'module retriever':0,'Exclude':0}

#predefined function to validate inputs and append them in to respective lists
def TheWholeProcess():
    global database2
    levels=['pass','defer','fail']
    Credits=[0,20,40,60,80,100,120]
    while True:
        FullCredits=[]#.....values in [0,20,40,60,80,100,120] will append to this list
        
        FullCredits2=[]#.....if the sum of the elements of list FullCredits is equal 120, those elements will assign to this list

        for a in levels:#.....loop to get input values for 'pass','defer' and 'fail'
            while True:#.....this loop wil iterate utill the user give a valid input
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
            FullCredits2=FullCredits  #.......FullCredits2 is the list which contains fully validated inputs
            break
        else:
            print('Total Incorrect')
            continue
        
    database=dict(zip((levels),(FullCredits2)))#.....database is a dictionary which its key is the grade and value as the inputs
    global passcount
    global module_trailerCount
    global module_retrieverCount
    global ExcludeCount
    
    if database['pass']==120:
        passcount+=1#..............counter to calculate how many time the inputs give 'progress' 
        database2.update({'progress':passcount})#.......updates the value of the key
        print('progress')
    elif database['pass']==100:
        module_trailerCount+=1#........counter to calculate how many time the inputs give 'module trailer'
        database2.update({'module trailer':module_trailerCount})#.......updates the value of the key
        print('Progress (module trailer)')
    elif (database['pass'] in [0,20,40,60,80]) and (database['fail'] in [0,20,40,60]):
        module_retrieverCount+=1#................counter to calculate how many time the inputs give 'module retriever'
        database2.update({'module retriever':module_retrieverCount})#.......updates the value of the key
        print('Do not Progress – module retriever')
    elif database['fail'] in [80,100,120]:
        ExcludeCount+=1#............counter to calculate how many time the inputs give 'Exclude'
        database2.update({'Exclude':ExcludeCount})#.......updates the value of the key
        print('Exclude')
    return passcount,module_trailerCount,module_retrieverCount,ExcludeCount,database2
        
print('Press "P" to implement the Student Version \n'
      'Press "S" to implement the Staff Version')
while True:#..........iterate to until user inputs a valid inputs 
    possition=input()
    lowerPossition=possition.lower()#..........opening space to user to input either uppercase or lowercase characters
    if lowerPossition not in ['s','p']:
        print('Invalid Respond \n''You must enter "S" or "p"')
        continue
    elif lowerPossition=='p':
        TheWholeProcess()#.........if the user wants to excute the student version the above predefined funtion excute only one time
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
                print('-'*50)
                count=0
                for key in database2:#.......once the user want the quit the program this loop will iterate to print the hoizontal histogram
                    print(key,database2[key],':',(database2[key]*'*'))
                    if database2[key]!=0:
                        count=database2[key]+count
                print(count,' Outcomes in total')
                print('-'*50)
                break
        break



            
            
        
    
    

    


    



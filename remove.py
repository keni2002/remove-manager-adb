#declaring libraies
import os
# necessary variables  and functions


#functions
#Loadin Function
lista = []

#checker;
checker = False
def loadin(word):
    
    if word == 'none':
        os.system("adb shell pm list packages > .list.txt")
    else:
        os.system("adb shell pm list packages | grep " + word + "> .list.txt")
    flow = open(".list.txt", "r")
    

    os.system("clear")
    
    while(True):
        linea = flow.readline()
        if not linea:
            break
        else:
            lista.append(str(linea[8:]))
            
    flow.close()
    if not lista:
        input("Sorry, no found package, press Enter to return: ")
        return False
    else:


        
        flow = open("cache.dat", "a")
        contar = 0
        for x in lista:

            contar += 1
            flow.write(str(contar) + " " + x)
        flow.close()
        os.system("rm .list.txt")
        z = input(chr(27) + "[14;31m" + "Attention, a list will appear,\n Use Up and Down Keys to move\n" +
            "across package names. You MUST Remember ID of the searched package. After..\n" +
            "press <q> key to exit from list\n" +
            "Let's go: "+ chr(27) +"[0;30m")
        os.system("less cache.dat")    
        os.system("rm cache.dat")
        
        return True
#End Loadin Function
#locals
f = open(".device.txt", "r")
linea = ""
os.system("adb devices > .device.txt")
linea = f.readlines()[1]
if len(linea) > 26:
    print("\n **Please, Make sure to connect your phone as File Transfer**\n Exiting...")
    
elif len(linea) > 7 and len(linea) < 26:
    
    
    print("\n"+ chr(27) +"[1;34m" +"Connected Device Successfully :)\n" + chr(27) +"[14;31m" + "PLEASE DONT MOVE THE DATA WIRE")
    print(chr(27) +"[0;30m" + "\n" + linea )
    input("Press Enter to continue:")
        
    option = 0
    #to exit
    exitir = False
    while(exitir == False):
        
        os.system("clear")
        print(chr(27) +"[14;31m" + "<<REMOVE MANAGER ADB>>\n\tWelcome\t")

        try:
            option = int(input("\n" + chr(27) +"[0;30m" + "[Select an option to Load Application Packs]\n" +
                                    " 1 Search a specific package\n" +
                                    " 2 List All packages\n" +
                                    " 3 Exit\n" +
                                    ">> "))
            if option == 3:
                # I close bucle
                os.system("rm .check.dat")
                break
                
                
                os.system("clear")
            elif option == 1:
                cad = str(input("Please insert the searched package: "))
                
                
                #if checker is True then bucle is stoped
                    
                checker = loadin(cad)
               



            elif option == 2:
                checker = loadin('none')
                    
            else:
                input("Invalid selection, TRY again")
                
              
        except ValueError:
            input("Invalid selection, TRY again")
               
        if checker == True:
            
                #to exit
                exitir2 = False
                while(exitir2 == False):
                    os.system("clear")
                    try:
                        value_id  = int(input("Please insert the ID of desired package: "))
                        

                        if value_id > 0 and value_id <= len(lista):
                            while(True):
                                os.system("clear")
                                try:
                                    print(chr(27) +"[14;31m" + "\t\t<<MENU OF TASKS>>\n\t" + chr(27) +"[14;35m"+"Package Selected: "+ lista[value_id-1]+"\t\n\nPROCEED WITH CARE!!\n")
                                    option = int(input("\n" + chr(27) +"[0;30m" + "[Select an option to Manage the Application Pack]\n" +
                                                " 1 Uninstall this Package\n" +
                                                " 2 Uninstall but KEEP the data and cache directories of this Package\n" +
                                                " 3 Return to Load Packages\n" +
                                                " 4 Exit\n" +
                                                ">> "))
                                    if option == 4:
                                        #EXIT
                                        exitir2 = True
                                        exitir = True
                                        os.system("rm .check.dat")
                                        break
                                        
                                    elif option == 1:
                                        #UNINSTALL
                                        os.system("clear")
                                        print(chr(27) +"[1;31m"+"YOU'RE ABOUT TO PERMANENTLY UNINSTALL THE PACKAGE: \n" +
                                                        chr(27) +"[1;34m"+
                                                        lista[value_id-1]+chr(27) +"[0;30m")
                                        z = str(input("Do you want to uninstall this package? (yes/N): "))
                                        if z == 'yes':
                                            #It is important this slicing because there is a hidden \n to the end of the list.
                                            outputs = os.system("adb uninstall " + lista[value_id-1][0:-1]+ "> .check.dat")
                                            flow_output = open(".check.dat", "r")
                                            if_error = flow_output.readline()
                                            flow_output.close()
                                            os.system("clear")
                                            if if_error[0:-1] == "Success":
                                                input(chr(27) +"[1;32m" + "The package: " + 
                                                                            lista[value_id-1] +

                                                                            " was uninstalled successfully :-)" +
                                                                            chr(27) +"[1;34m"+
                                                                            "\nNothing more to do so"+
                                                                            chr(27) +"[0;30m"+
                                                                            "\nPress Enter to return to MAIN MENU >> ")
                                                lista = []
                                                exitir2 = True
                                                break
                                            elif if_error[0:-1] == "Failure [DELETE_FAILED_INTERNAL_ERROR]":
                                                errore = input(chr(27) +"[1;31m" + "INTERNAL ERROR, Maybe " 
                                                            + chr(27) +"[1;34m" + 
                                                            lista[value_id-1][0:-1] +
                                                            chr(27) +"[1;31m\n" + 
                                                            " is a system package and your phone is not Rooted"+
                                                            chr(27) +"[0;30m" +
                                                            "\nPress Enter to return >> ")
                                            else:
                                                input("UNKNOWN FAILURE"+ if_error)
                                            #restart list and return to load
                                            
                                            
                                        else:
                                            input("<<ABORTED>>\nPress Enter to Return to Menu of Task >> ")

                                    elif option == 2:
                                        #SAVE DATA
                                        pass
                                    elif option == 3:
                                        #Select package again
                                        #restart list and exit from task menu
                                        lista = []
                                        exitir2 = True
                                        break

                                    else:
                                        z =  input(chr(27) +"[14;31m"+ "FAILURE!! NO OPTION: "+str(option) +
                                                chr(27) +"[0;30m")
                                except ValueError:
                                    input(chr(27) +"[14;31m"+"FAILURE! INSERT ONLY INTEGER NUMBER"+ chr(27) +"[0;30m" )


                        
                            
                        
                        
                        else:
                            z =  input(chr(27) +"[14;31m"+ "FAILURE: ID out of package range.\n" +
                                        chr(27) +"[0;30m" +
                                        "Range=[1-"+ str(len(lista))+"]")

                    except ValueError:
                        input(chr(27) +"[14;31m"+"FAILURE! INSERT ONLY INTEGER NUMBER"+ chr(27) +"[0;30m" ) 
           # while(True):

            #break # maybe this line was delete in the future
        else:
            pass
    

    








else:
    print("\n  **Please, Make sure to connect your phone to PC in USB 2.0 and Debug USB Mode is activated, **\nExiting...")

f.close()



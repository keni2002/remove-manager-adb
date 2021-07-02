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
    while(True):
        
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
            
            #try:
                while(True):
                    os.system("clear")
                    value_id  = int(input("Please insert the ID of desired package: "))
                    

                    if value_id > 0 and value_id <= len(lista):
                        os.system("clear")
                        
                        print(chr(27) +"[14;31m" + "\t\t<<MENU OF TASKS>>\n\t" + chr(27) +"[14;35m"+"Package Selected: "+ lista[value_id-1]+"\t")
                        option = int(input("\n" + chr(27) +"[0;30m" + "[Select an option to Manage the Application Pack]\n" +
                                    " 1 Uninstall this Package\n" +
                                    " 2 Uninstall but KEEP the data and cache directories of this Package\n" +
                                    " 3 Exit\n" +
                                    ">> "))
                    
                    
                        #restart list
                        lista = []
                    
                    
                    else:
                      z =  input(chr(27) +"[14;31m"+ "FAILURE: ID out of package range.\n" +
                                chr(27) +"[0;30m" +
                                "Range=[1-"+ str(len(lista))+"]")

            #except:
                #pass    
           # while(True):

            #break # maybe this line was delete in the future
        else:
            pass
    

    








else:
    print("\n  **Please, Make sure to connect your phone to PC in USB 2.0 and Debug USB Mode is activated, **\nExiting...")

f.close()



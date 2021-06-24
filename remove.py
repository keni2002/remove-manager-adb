#declaring libraies
import os
# necessary variables 
f = open(".device.txt", "r")
var1 = 0
var2 = 1
option = 0
os.system("adb devices > .device.txt")
linea = f.readlines()[1]
if len(linea) > 26:
    print("\n **Please, Make sure to connect your phone as File Transfer**\n Exiting...")
    
elif len(linea) > 7 and len(linea) < 26:
    
    while(var1 != 3):
        var1 = 0
        print("\n"+ chr(27) +"[1;34m" +"Connected Device Successfully :)")
        print("\n" + linea )
        input("Press Enter to continue:")
        

        while(var2 != 7):
            var2 = 0
            os.system("clear")
            print(chr(27) +"[14;31m" + "<<REMOVE MANAGER ADB>>\n\tWelcome\t")

            try:
                option = int(input("\n" + chr(27) +"[0;30m" + "[Select an option to Load Application Packs]\n" +
                                    " 1 Search a specific package\n" +
                                    " 2 List All packages\n" +
                                    " 3 Exit\n" +
                                    ">> "))
                if option == 3:
                    # I close my own bucle
                    var2 = 7
                    # After I close the main bucle
                    var1 = 3
                    os.system("clear")
                elif option == 1:
                    pass
                elif option ==2:
                    pass
                else:
                    input("Invalid selection, try again: ")
                
                
            except ValueError:
                input("Invalid selection, try again: ")
                
            
    

    








else:
    print("\n  **Please, Make sure to connect your phone to PC and Debug USB Mode is activated**\nExiting...")

f.close()

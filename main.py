#Python program to demonstrate set and dictionary
#Main function starts from here
shop_info = {}
print("____Program to Compare two or more Shops Details____")
while True:
    print("\n\n\n********************************************************")
    print(
        "\tWelcome to CHRIST UNIVERSITY (DEEMED TO BE UNIVERSITY)\n_______________________________________________________\n\t\t\tLAXMAN\tKHATRI\t2048014 "
    )
    print("********************************************************")
    print("\t\t-- COMPARISON OF SHOPS WHICH HAVE MORE ITEMS --")
    print("------------------------------------------------------")
    no_of_shops = input("\tHow manys Shops do you want to compare ('N' to stop): \n=>\t")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    if no_of_shops == 'N' or no_of_shops == 'n':
      print("Have a great Day, Sir/Ma'am!\n\n")
      break
    elif no_of_shops.isnumeric()==False or int(no_of_shops) < 2:
      print("You have enter invalid number of shops, please try to enter 2 or more..\n")
    else:
      #Adding Items to particular shops
      num=int(no_of_shops)
      for i in range(1, num+1):
        msg="Shop_"+str(i)+" Name: "
        shop_name = input(msg)
        shop_info[shop_name] = {}
        msg="How many items does '"+shop_name+"' has: "
        entry=int(input(msg))
        test_set = set() 
        for n in range(0,entry):
          msg="Items "+ str(n+1) +" : "
          test_set.add(input(msg)) 
        shop_info[shop_name]["Items"] = test_set
        print("\n *********** \n")
      #displaying 
      print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\tShop Lists:\n---------------------------------------------------")
      for key in shop_info:
        print(key)
      print("\n*********************************")
      for s_id, s_info in shop_info.items():
        print("Shop Name: ", s_id)
        for key in s_info:
            print(key + ': ', s_info[key])
        print("...............................\n")
      print("\tDIFFERENCE \n*************************")
      for i in range(0, num-1):
        for j in range(i,num-1):
          temp1=list(shop_info)[i]
          temp2=list(shop_info)[j+1]
          print(temp1," - ",temp2 ,"\n-----------------\n")
          print(shop_info[temp1]["Items"]-shop_info[temp2]["Items"])
          print("-----------------\n")
          print(temp2," - ",temp1,"\n-----------------\n" )
          print(shop_info[temp2]["Items"]-shop_info[temp1]["Items"])
          print("-----------------\n")
      print("\n\tSIMILAR (INTERSECTION) \n*************************")
      for i in range(0, num-1):
        for j in range(i,num-1):
          temp1=list(shop_info)[i]
          temp2=list(shop_info)[j+1]
          print(temp1," ^ ",temp2 ,"\n-----------------\n")
          print(shop_info[temp1]["Items"] & shop_info[temp2]["Items"])
          print("\n-----------------\n")
      print("\n\tCOMBINING (UNION) \n*************************")
      for i in range(0, num-1):
        for j in range(i,num-1):
          temp1=list(shop_info)[i]
          temp2=list(shop_info)[j+1]
          print(temp1," U ",temp2 ,"\n-----------------\n")
          print(shop_info[temp1]["Items"] | shop_info[temp2]["Items"])
          print("\n-----------------\n")


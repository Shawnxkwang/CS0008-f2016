
# Xiaokai Wang
# xiw69@pitt.edu
# CS 0008

# assignmnet #1

# ask the user to input prefered unit system/ distance driven/ gas usage
choice = input("Please enter your prefered unit system (USC/Metric): ")
dist = float(input("Please input your distance driven: "))
gas = float(input("Please input your gas usage during this distance: "))

#initialize distance and gas of other unit system
dist_conv = 0.0
gas_conv = 0.0

#check which unit system the user input.
if (choice.lower() == "usc"):
    dist_conv = dist * 1.60934
    gas_conv = gas * 3.78541
elif(choice.lower() == "metric"):
    dist_conv = dist * 0.621371
    gas_conv = gas * 0.264172
else:
    print("Wrong unit system!")

#initialize mpg and liter per 100 kilometers
mpg = 0.0
lpk = 0.0

# compute the mpg and liter per 100 kilometers
if (choice.lower() == "usc"):
    mpg = dist / gas
    lpk = 100 * gas_conv / dist_conv
elif(choice.lower() == "metric"):
    mpg = dist_conv / gas_conv
    lpk = 100 * gas / dist
else:
    print("Wrong unit system!")

# initialize the consumption rating category
rating = ""

#checl status
if (lpk < 0 ):
    print("not valid gas usage per distance")
elif (lpk >= 0 and lpk <= 8):
    rating = "Excellent"
elif (lpk > 8 and lpk <= 10):
    rating = "Good"
elif(lpk > 10 and lpk <= 15):
    rating = "Average"
elif(lpk > 15 and lpk <= 20):
    rating = "Poor"
else:
    rating = "Extremely poor"


#check unit and choose which status we need to use
if (choice.lower() == "usc"):
    # print the final output
    print("\t\t\t\t\t\t\t\t\t" + "USC" + "\t\t\t\t\t\t" + "Metric")
    print("Distance ______________:" + "\t\t   ", format(dist, '.3f'), " miles", "\t\t\t", format(dist_conv, '.3f')," Km")
    print("Gas ___________________:" + "\t\t   ", format(gas, '.3f')," gallons", "\t\t", format(gas_conv, '.3f')," Liters")
    print("Consumption ___________:" + "\t\t   ", format(mpg, '.3f'), " mpg", "\t\t\t\t", format(lpk, '.3f'), " 1/100Km")
    print("")
    print("Gas Consumption Rating : " + rating)


elif(choice.lower() == "metric"):
    # print the final output
    print("\t\t\t\t\t\t\t\t\t" + "USC" + "\t\t\t\t\t\t" + "Metric")
    print("Distance ______________:" + "\t\t   ", format(dist_conv, '.3f'), " miles", "\t\t\t", format(dist, '.3f')," Km")
    print("Gas ___________________:" + "\t\t   ", format(gas_conv, '.3f'), " gallons", "\t\t", format(gas, '.3f')," Liters")
    print("Consumption ___________:" + "\t\t   ", format(mpg, '.3f'), " mpg", "\t\t\t\t", format(lpk, '.3f')," 1/100Km")
    print("")
    print("Gas Consumption Rating : " + rating)


else:
    print("Invalid unit system")







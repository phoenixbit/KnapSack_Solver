



#n is number of objects
n = int(input("Enter number of objects: "))
i = 0
power = ""
#power is the variable to print out the power set

#function to output the power set of a given number of objects
def powerSetPrinter(i,n,power):

    if i == n:
        return

    for p in range(i, n):
        power += chr(p+65)
        print(power)
        powerSetPrinter(p+1,n,power)
        power =power.replace(power[len(power)-1],"")
    return



if __name__ == '__main__':
    powerSetPrinter(i,n,power)



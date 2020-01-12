#!/usr/bin/python
#Author:ketan patel
#created on:13/01/2020

num = """1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 30 40 50 60 70 80 90 """.split(" ")

numText="""One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety """.split(" ")
bigNumbers="Million Billion Trillion Quadrillion Qunitillion Sextillion Septillion Octillion Nonillion Decillion Undecillion DuoDecillion Tredicillion Quattuor-Decillion Quindecillion Sexdecillion Octodecillion Novemdecillion Vigintillion Centillion ".split(" ")
numDict = zip(num,numText)
numDict = dict(numDict)
#print(numDict)
def numberToText(number):
    number =int(number)
    n = str(number)
    global numDict
    global bigNumbers
    strText =""
    while(len(n)>0):    
        if n in numDict:
            strText = strText + numDict[n] 
            
        else:
            if len(n)==2:
                strText = strText + "" + numDict[str((number /10)*10)]+"-" + numDict[n[1]]
            if len(n)==3:
                strText = numDict[n[0]]+ " Hundred "+ numberToText(n[1:])
            if len(n)==4:
                 strText = numDict[n[0]]+ " Thousand "+ numberToText(n[1:])
            if len(n)==5:
                 strText = numberToText(n[0:2])+ " Thousand "+ numberToText(n[2:])
            if len(n)==6:
                 strText = numberToText(n[0])+ " Hundred "+ numberToText(n[1:])
            
            if len(n)>6:
                rem = (len(n)-6)%3
                quot =(len(n)-7)/3
                
                numberWord = bigNumbers[quot]
                if rem == 0:
                    strText = numberToText(n[0:3])+" "+numberWord+" "+ numberToText(n[3:])
                if rem ==1:
                    strText = numberToText(n[0])+ " "+ numberWord+" "+ numberToText(n[1:])
                if rem ==2:
                    strText = numberToText(n[0:2])+ " "+ numberWord+" "+ numberToText(n[2:])   

        return strText



#main program
if __name__ == "__main__":
    response = input("Enter Number to Convert,'Q' or 'q' to Exit: ")
    try:
        while int (response):
            if not len(str(response))>63:
                print ("You entered number with length %d"%(len(str(response))))
            
                print(numberToText(response))
            else:
                print ("To Big Number")
            
        
        
            response = input("Enter Number to Convert,'Q' or 'q' to Exit: ")

    except:
        print("You entered non number ")
        exit
                
            

    


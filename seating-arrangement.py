# seating-arrangement-1 problem

class Test:
    def readData(num):
        inputList = []
        while(num!=0):
            temp = int(input())
            inputList.append(temp)
            num=num-1
        return inputList
            
    def findFacingSeat(seatList):
        resultList = []
        for item in seatList:
            if((item%12==0 or(item+11)%12==0) or (item%6==0 or(item+5)%6==0)):
                seatType = "WS"
                if(item%12 == 0):
                    seatCode = item-11
                elif((item-1)%12 == 0):
                    seatCode = item+11
                elif((item)%6 == 0):
                    seatCode = item+1
                else:
                    seatCode= item-1
                    
            if(((item+1)%12==0 or(item-2)%12==0) or ((item+1)%6==0 or(item-2)%6==0)):
                seatType = "MS"
                if((item+1)%12 == 0):
                    seatCode = item-9
                elif((item-2)%12 == 0):
                    seatCode = item+9
                elif((item+1)%6 == 0):
                    seatCode = item+3
                else:
                    seatCode = item-3
            
            if(((item+2)%12==0 or (item-3)%12==0) or ((item+2)%6==0 or(item-3)%6==0)):
                seatType = "AS"
                if((item+2)%12 == 0):
                    seatCode = item-7
                elif((item-3)%12 == 0):
                    seatCode = item+7
                elif((item+2)%6 == 0):
                    seatCode = item+5
                else:
                    seatCode = item-5
            if(item<=6 and item>=1):
                seatCode = 13-item
                
            if(item<=108 and item>=103):
                seatCode = 205-item
                
                
            if(item<=48 and item>=43):
                seatCode = 85-item
            
            if(item<=49 and item>=54):
                seatCode = 97-item
            print (str(seatCode) + " " + seatType)

newObj = Test
count = int(input())
inputList = newObj.readData(count)
    
newObj.findFacingSeat(inputList)

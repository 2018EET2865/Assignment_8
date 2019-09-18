# reading bit data from user
data=input("Enter bit data   : ")
# initialising parity to 1 as initial parity value
parity=1
# finding parity of data stream
for i in data:
    parity=parity^int(i)
# adding parity bit to data
data+=str(parity)
print("Parity bit data  :",data)
# replacing 010 in data with 0100 to get data to be transmitted
trans=data.replace("010","0100")
# appending 0101 to the data to be transmitted
trans+="0101"
print("Transmitting data:",trans)


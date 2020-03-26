listOfInputs = str(input("please input data: "))
tup = ()
ListOfOutput = []

for i in range(len(listOfInputs)):
   if listOfInputs[i] != " " and listOfInputs[i] != ",":
        ListOfOutput.append(listOfInputs[i])
        
print(ListOfOutput)
print(tuple(ListOfOutput))
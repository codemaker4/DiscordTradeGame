ConfNumDepth = 6

def getConfNum(num, depth):
  if depth <= 0:
    return (num*num)%53
  return ((num*getConfNum(num+depth+7224, depth-1)*533)+(depth+(num*123)+924))%9;

# for i in range(50):
#     print(str(i) + '----' + str(getConfNum(i, ConfNumDepth)))

while True:
    print("0: hout       5: bos")
    print("1: graan      6: weiland")
    print("2: baksteen   7: baksteenfabriek")
    print("3: schaap     8: boederij")
    print("4: ijzer      9: mijn")
    chestID = int(input("id: "))
    itemType = int(input("itemType: "))
    itemCount = int(input("itemCount: "))
    confNum = getConfNum(chestID + itemType + itemCount, ConfNumDepth)
    print(str(chestID)+"."+str(itemType)+"."+str(itemCount)+"."+str(confNum))

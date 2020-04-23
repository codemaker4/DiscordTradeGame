ConfNumDepth = 6

def getConfNum(num, depth):
  if depth <= 0:
    return (num*num)%53
  return ((num*getConfNum(num+depth+7224, depth-1)*533)+(depth+(num*123)+924))%9;

# for i in range(50):
#     print(str(i) + '----' + str(getConfNum(i, ConfNumDepth)))

nextID = int(input("nextID > "))

while True:
    chestID = nextID
    print("0: hout       5: bossen")
    print("1: graan      6: weilanden")
    print("2: baksteen   7: baksteenfabrieken")
    print("3: schapen    8: boederijen")
    print("4: ijzer      9: mijnen")
    itemType = int(input("itemType > "))
    itemCount = int(input("itemCount > "))
    confNum = getConfNum(chestID + itemType + itemCount, ConfNumDepth)
    print(str(chestID)+"."+str(itemType)+"."+str(itemCount)+"."+str(confNum))
    nextID += 1

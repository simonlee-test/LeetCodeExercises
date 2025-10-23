class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    mergedList=[]
    index1 =0
    index2=0
    if not(list1):
        return list2
    
    elif not(list2):
        return list1

    else:
        while (index1 < len(list1)) and (index2< len(list2)) :
            if list1[index1] == list2[index2]:
                mergedList.append(list1[index1])
                mergedList.append(list2[index2])
                index1+=1
                index2+=1

            elif list1[index1] < list2[index2]:
                mergedList.append(list1[index1])
                index1+=1
            
            else:
                mergedList.append(list2[index2])
                index2+=1

        if index1 < len(list1):
            for i in range(index1, len(list1)):
                mergedList.append(list1[i])

        elif index2 < len(list2):
            for i in range(index2, len(list2)):
                mergedList.append(list2[i])
    
    return mergedList


list1 = [2,2,2,3,5,6,8,9,12] 
list2 = [0,1,1,2,3,7,10,10,11]

print(mergeTwoLists(list1,list2))



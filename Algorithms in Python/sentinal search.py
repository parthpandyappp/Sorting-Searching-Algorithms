def sentinal_search(array,value):       #function for searching 
    n=len(array)
    last=array[n-1]
    array[n-1]=value
    i=0
    while(array[i]!=value):
        i+=1
    array[n-1]=last
    if(i!=n-1 or array[n-1]==value):   
        return i
    return -1

def input_array():                       #function for taking input of array
    attended=[]
    number_of_attendee=int(input("Enter number of attendee : "))
    for i in range(number_of_attendee):
        tep=int(input("Enter roll number of attendee:"))
        attended.append(tep)
    return attended

if __name__=="__main__":
    arr=input_array()
    num=int(input("Enter number you want to search in array : "))
    ind=sentinal_search(arr,num)
    if(ind==-1):
        print("Element not found!!")
    else:
        print("Element found at",str(ind)," index !!")

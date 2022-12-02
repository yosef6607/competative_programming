#User function Template for python3

def reverseWord(s):
    list1 = list()
    for i in s:
        list1.append(i)
    for i in range(len(list1)//2):
        start_element =list1[i]
        last_element = list1[(len(list1)-1) - i]
        temp = start_element
        start_element = last_element
        last_element = temp
        list1[i] = start_element
        list1[(len(list1)-1) - i] = last_element
    reverse_string = "".join(str(x) for x in list1)
    return reverse_string


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends
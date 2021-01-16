def main():
    x = input("Enter the first number to compare : ")
    y = input("Enter the second number to compare : ")

    #conditional flow uses if, elif , else

    if(x<y):
        st= "x is less than y"
    elif(x == y):
        st =" x equal y"
    else:
        st ="x is greater than y"
    print(st)
   #conditional
if __name__ == "__main__":
    main()
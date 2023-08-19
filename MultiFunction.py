class multipleFunction():
    def subfields():
        print("Subfields in AI are:")
        lists=['Machine Learning','Neutral Networks','Vision','Robotics','Speech Processing','Natural Language processing']
        for temp in lists:
            print(temp)
    def oddeven():
        num=int(input("Enter the number:"))
        if(num%2)==1:
            print("{0} is odd number".format(num))
        else:
            print("{0} is Even number".format(num))
    def eligible():
        Gender=input("Your Gender:")
        if(Gender=="Male"):
            Age=int(input("Your Age:"))
            if(Age<21):
                print("Not Eligible")
            else:
                print("Eligible")
        if(Gender=="Female"):
            Age=int(input("Your Age:"))
            if(Age<18):
                print("Not Eligible")
            else:
                print("Eligible")      
    def percentage():
        sub1=int(input("subject1="))
        sub2=int(input("subject2="))
        sub3=int(input("subject3="))
        sub4=int(input("subject4="))
        sub5=int(input("subject5="))
        print("Total:",sub1+sub2+sub3+sub4+sub5)
        Total=sub1+sub2+sub3+sub4+sub5
        percent=(Total/500)*100
        print("Percentage:",percent)
    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+breadth)
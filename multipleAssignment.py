class multipleAssignment():
    def oddEven():
        num=int(input("enter the number:"))
        if((num%2)==1):
            print(num,"is odd number")
            message="odd number"
        else:
            print(num,"is even number")
            message="even number"
        return message
    def percentage():
        subject1=int(input("subject1:"))
        subject2=int(input("subject2:"))
        subject3=int(input("subject3:"))
        subject4=int(input("subject4:"))
        subject5=int(input("subject5:"))
        total=subject1+subject2+subject3+subject4+subject5
        print("total:",total)
        percentage=total/5
        print("percentage:",percentage)
    def elegible():
        gender=input("your gender:")
        age=int(input("your age"))
        if(gender in "male"):
            if(age<21):
                print("not eligible")
                message="not eligible"
            else:
                print("eligible")
                message="eligible"
        elif(gender in "female"):
             if(age<18):
                 print("not eligible")
                 message="not eligible"
             else:
                 print("eligible")
        else:
            print("invalid gender")
            message="invalid gender"
        return message
    def subfieldsInAI():
        lists=("machine lerning","neural learning","vision","robotics","speech processing","natural language processing")
        field="sub-field in ai are:"
        print(field)
        for field in lists:
            print(field)
    def triangle():
        height=int(input("height:"))
        breath=int(input("breath:"))
        print("area of formula:(breath*height)/2")
        area=(breath*height)/2
        print("area of triangle:",area)
        height1=int(input("height1:"))
        height2=int(input("height2:"))
        breath1=int(input("breath1:"))
        print("perimeter of triangle=height1+height2+breath1")
        perimeter=height1+height2+breath1
        print("perimeter of triangle:",perimeter)
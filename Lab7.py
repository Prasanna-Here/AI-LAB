from kanren import Relation,facts,var,conde,run

people=Relation()
likes=Relation()

facts(people,("alice",),("bob",))
facts(likes,("alice","Maths"),("bob","Physics"))

def intelligent_rule(x):
    subject=var()
    return conde((people(x),likes(x,subject)))

print("Queries:")
print("1. Who is intelligent?")
print("2. Is Alice intelligent?")
print("3. Is Bob intelligent?")

choice = int(input("Enter your query choice (1/2/3): "))

x=var()

if choice==1:
    result=run(2,x,intelligent_rule(x))
    print("Intelligent people:", result)
elif choice==2:
    result=run(1,x,intelligent_rule('alice'))
    print("Is Alice intelligent? ",bool(result))
elif choice==3:
    result=run(1,x,intelligent_rule('bob'))
    print("Is Bob intelligent? ",bool(result))
else:
    print("Invalid input")
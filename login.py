def signup():
    def validate(pw):
        flags=[0,0,0,0,0]
        for i in range(len(pw)):
            if(pw[i].isalpha() and pw[i].islower() and flags[0]!=1):
                flags[0]=1
            if(pw[i].isdigit() and flags[1]!=1):
                flags[1]=1
            if(pw[i].isalpha() and pw[i].isupper() and flags[2]!=1):
                flags[2]=1
            if((pw[i]=='$' or pw[i]=='#' or pw[i]=='@') and flags[3]!=1):
                flags[3]=1
            if(len(pw)>=8 and len(pw)<=15):
                flags[4]=1
        if(0 not in flags):
            return pw
    username=input('Please enter the username\n')
    passwords=input('Please enter the passwords to check\n').split(',')
    verified=[]
    for pw in passwords:
        v=validate(pw)
        if v:
            verified.append(v)
    print(verified,sep=',')
    print('Please select one of the following:')
    for j in range(len(verified)):
        print(j+1,")",verified[j])
    i=int(input())
    users.append(username)
    pwords.append(verified[i-1])

def signin():
    f=0
    unm=input('Enter Username :\n')
    psw=input('Enter Password :\n')
    for i in range(len(users)):
        if (users[i]==unm) and (pwords[i]==psw):
            f=1
    if(f==1):
        print('Sign in Successful !')
    else:
        print('Something went wrong.Try again.')
    
def choice():
    r=int(input("Please choose an option:\n1)Signup\n2)Sign in"))
    if(r==1):
        signup()
    elif(r==2):
        signin()
    else:
        print('INVALID CHOICE!')
        choice()

users=[]
pwords=[]
g=1
while (g==1):
    while (1):
        choice()
        g=int(input("Enter 1 to continue.\n"))
        if(g!=1):
            break
    if(g!=1):
        break
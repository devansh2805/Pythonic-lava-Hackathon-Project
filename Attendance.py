import os
import pandas as pd
os.chdir("C:\\Users\\Devansh Shah\\Desktop\\Pythonic_lava\\hackathon")
df=pd.read_csv("TestCopy.csv")
def choice():
    print("Choose an option : ")
    c=int(input())
    if(c>6 or c<1):
        print("Enter a valid option.\n Press 1 to try again.")
        n=int(input())
        if(n==1):
            choice()
    if(c==1):
        view()
    elif(c==2):
        searchByRoll()
    elif(c==3):
        searchByLecture()
    elif(c==4):
        allAbsent()
    elif(c==5):
        allPresent()
    else:
        edit()
def view():
    print(df)
def searchByRoll():
    count=0
    print("Enter the roll number : ")
    roll=int(input())
    num=df[df['Roll No.']==roll]
    print(num)
    if(num['LECTURE 1']=='P').bool():
        count=count+1
    if(num['LECTURE 2']=='P').bool():
        count=count+1
    if(num['LECTURE 3']=='P').bool():
        count=count+1
    if(num['LECTURE 4']=='P').bool():
        count=count+1
    print("Number of lectures present : ",count)
    print("Number of lectures absent : ",4-count)
def searchByLecture():
    print("Enter the lecture number : ")
    lec=int(input())
    l=object
    if(lec==1):
        l='LECTURE 1'
        print(df.drop(['LECTURE 4','LECTURE 2','LECTURE 3'],axis=1))
    elif(lec==2):
        l='LECTURE 2'
        print(df.drop(['LECTURE 4','LECTURE 1','LECTURE 3'],axis=1))
    elif(lec==3):
        l='LECTURE 3'
        print(df.drop(['LECTURE 4','LECTURE 2','LECTURE 1'],axis=1))
    elif(lec==4):
        l='LECTURE 4'
        print(df.drop(['LECTURE 1','LECTURE 2','LECTURE 3'],axis=1))
    present=list(df[l])
    print("Number of students present : ",present.count('P'))
    print("Number of students absent : ",present.count('A'))
def allPresent():
    print(df[(df['LECTURE 1']=='P') & (df['LECTURE 2']=='P') & (df['LECTURE 3']=='P') & (df['LECTURE 4']=='P')])
def allAbsent():
    print(df[(df['LECTURE 1']=='A') & (df['LECTURE 2']=='A') & (df['LECTURE 3']=='A') & (df['LECTURE 4']=='A')])
def edit():
    print("Enter the student roll number : ")
    roll=int(input())
    print("Enter the lecture number : ")
    j=int(input())
    if(j==1):
        l='LECTURE 1'
    if(j==2):
        l='LECTURE 2'
    if(j==3):
        l='LECTURE 3'
    if(j==4):
        l='LECTURE 4'
    asf=df.loc[0]
    list(asf)
    ni=asf[1]
    roll-ni
    df[roll-ni:roll-ni+1][l].replace(to_replace=['P','A'],value='A',inplace=True)
    print(df[roll-ni:roll-ni+1])
choice()   
df.to_csv('TestCopy.csv',index=False) 
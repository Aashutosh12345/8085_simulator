import re
import sys
import settings
from error_store import Error_Store
from execute import execute
print '*****WELCOME TO 8085 EMULATOR*****'
correct=1
while(correct==1):
    try:
        PC=raw_input('Enter the starting address : ')
        if(len(PC)>4 or re.findall('[^A-F0-9]',PC)):
            print 'PC value out of range'
        elif(PC[0]=='0' or len(PC)<4):
            print 'Minimum PC value you can take is 1000'
        else:
            correct=0
        PC1=PC
    except:
        pass
while(1):
    st=PC+': '
    inp=raw_input(st)
    if(inp=='QUIT'):
        break
    ob1=Error_Store()
    PC=ob1.check(inp,PC)
    PC=PC.upper()
    if(len(PC)>4):
        print 'PC value has gone out of range'
        sys.exit(0)
print(".......COMPILED SUCCESSFULLY.......")
for PC in settings.sub:
     print 'Write subroutine for starting address',PC
     while(1):
        st=PC+': '
        inp=raw_input(st)
        if(inp=='QUIT'):
            break
        ob1=Error_Store()
        PC=ob1.check(inp,PC)
        PC=PC.upper()
        if(len(PC)>4):
            print 'PC value has gone out of range'
            quit()
while(1):
    for i in settings.input1: 
        while(1):
            II="ENTER VALUE AT MEM. ADDRESS "+i+" : "
            I=raw_input(II)
            if(len(I)!=2 or re.findall('[^A-F0-9]',I)):
                print 'INVALID INPUT'
            else:
                settings.h[i]=I
                break          
    if(PC1!=PC):
        print("...........EXECUTING..........")
        ob2=execute()
        ob2.execute1(PC1) 
    temp=str(settings.S)+str(settings.Z)+'0'+str(settings.AC)+'0'+str(settings.P)+'0'+str(settings.CY)
    settings.F=hex(int(temp,2)).upper()
    if(len(settings.F)==4):
        settings.F=settings.F[2:]
    else:
        settings.F='0'+settings.F[2]
    print '\nVALUES OF REGISTERS :\n'    
    print 'A =',settings.A
    print 'B =',settings.B
    print 'C =',settings.C
    print 'D =',settings.D
    print 'E =',settings.E
    print 'H =',settings.H
    print 'L =',settings.L
    print 'F =',settings.F
    print '\nVALUE OF EACH FLAG REGISTER :\n' 
    print 'SIGN FLAG =',settings.S
    print 'ZERO FLAG =',settings.Z
    print 'AUXILARY CARRY FLAG =',settings.AC
    print 'PARITY FLAG =',settings.P
    print 'CARRY FLAG =',settings.CY
    for i in settings.output: 
        print "VALUE AT MEM. ADDRESS",i,":",settings.h[i]
    if(len(settings.input1)==0):
        break
    else:
        I2=raw_input("WANT TO EXECUTE FOR MORE INPUT VALUES y/n")
        if(I2!='y' and I2!='Y'):
            break
print 'GOOD BYE!'

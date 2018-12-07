import re
import settings
class Error_Store:
    def check(self,opcode,PC):
        if opcode[0:4]=='LDA ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER LDA...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='3A'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.input1).append(opcode[4:])
                #A=h[opcode[4:8]]
            return PC
        elif opcode=='XCHG':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='EB'
            return PC
        elif opcode[0:3]=='HLT':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='76'
            return PC
        elif opcode=='MOV A,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7F'
            return PC
        elif opcode=='MOV A,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='78'
            return PC
        elif opcode=='MOV A,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='79'
            return PC
        elif opcode=='MOV A,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7A'
            return PC
        elif opcode=='MOV A,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7B'
            return PC
        elif opcode=='MOV A,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7C'
            return PC
        elif opcode=='MOV A,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7D'
            return PC
        elif opcode=='MOV A,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='7E'
            return PC
        elif opcode=='MOV B,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='47'
            return PC
        elif opcode=='MOV B,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='40'
            return PC
        elif opcode=='MOV B,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='41'
            return PC
        elif opcode=='MOV B,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='42'
            return PC
        elif opcode=='MOV B,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='43'
            return PC
        elif opcode=='MOV B,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='43'
            return PC
        elif opcode=='MOV B,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='44'
            return PC
        elif opcode=='MOV B,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='45'
            return PC
        elif opcode=='MOV B,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='46'
            return PC
        elif opcode=='MOV C,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4F'
            return PC
        elif opcode=='MOV C,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='48'
            return PC
        elif opcode=='MOV C,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='49'
            return PC
        elif opcode=='MOV C,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4A'
            return PC
        elif opcode=='MOV C,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4B'
            return PC
        elif opcode=='MOV C,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4C'
            return PC
        elif opcode=='MOV C,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4D'
            return PC
        elif opcode=='MOV C,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='4E'
            return PC
        elif opcode=='MOV D,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='57'
            return PC
        elif opcode=='MOV D,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='57'
            return PC
        elif opcode=='MOV D,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='50'
            return PC
        elif opcode=='MOV D,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='51'
            return PC
        elif opcode=='MOV D,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='52'
            return PC
        elif opcode=='MOV D,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='53'
            return PC
        elif opcode=='MOV D,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='54'
            return PC
        elif opcode=='MOV D,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='55'
            return PC
        elif opcode=='MOV D,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='56'
            return PC
        elif opcode=='MOV E,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5F'
            return PC
        elif opcode=='MOV E,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='58'
            return PC
        elif opcode=='MOV E,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='59'
            return PC
        elif opcode=='MOV E,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5A'
            return PC
        elif opcode=='MOV E,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5B'
            return PC
        elif opcode=='MOV E,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5C'
            return PC
        elif opcode=='MOV E,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5D'
            return PC
        elif opcode=='MOV E,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='5E'
            return PC
        elif opcode=='MOV H,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='67'
            return PC
        elif opcode=='MOV H,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='60'
            return PC
        elif opcode=='MOV H,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='61'
            return PC
        elif opcode=='MOV H,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='62'
            return PC
        elif opcode=='MOV H,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='63'
            return PC
        elif opcode=='MOV H,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='64'
            return PC
        elif opcode=='MOV H,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='65'
            return PC
        elif opcode=='MOV H,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='66'
            return PC
        elif opcode=='MOV L,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6F'
            return PC
        elif opcode=='MOV L,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='68'
            return PC
        elif opcode=='MOV L,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='69'
            return PC
        elif opcode=='MOV L,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6A'
            return PC
        elif opcode=='MOV L,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6B'
            return PC
        elif opcode=='MOV L,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6C'
            return PC
        elif opcode=='MOV L,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6D'
            return PC
        elif opcode=='MOV L,M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='6E'
            return PC
        elif opcode=='MOV M,A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='77'
            return PC
        elif opcode=='MOV M,B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='70'
            return PC
        elif opcode=='MOV M,C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='71'
            return PC
        elif opcode=='MOV M,D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='72'
            return PC
        elif opcode=='MOV M,E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='73'
            return PC
        elif opcode=='MOV M,H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='74'
            return PC
        elif opcode=='MOV M,L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='75'
            return PC
        elif opcode[0:6]=='MVI A ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI A ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='3E'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI B ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI B ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='06'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI C ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI C ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='0E'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI D ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI D ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='16'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI E ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI E ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='1E'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI H ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI H ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='26'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI L ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI L ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='2E'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode[0:6]=='MVI M ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI M ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='36'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
            return PC
        elif opcode=='LDAX B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='0A'
            return PC
        elif opcode=='LDAX D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='1A'
            return PC
        elif opcode[0:5]=='LHLD ':
            if(len(opcode)!=9 or re.findall('[^0-9A-F]',opcode[5:])):
                print 'INVALID ADDRESS AFTER LHLD...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='2A'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[7:9]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.input1).append(opcode[5:])
                tt=hex(int(opcode[5:],16)+1).upper()
                tt=tt[2:]
                if(len(tt)==1):
                    tt='000'+tt
                elif(len(tt)==2):
                    tt='00'+tt
                elif(len(tt)==3):
                    tt='0'+tt
                (settings.input1).append(tt)
            return PC
        elif opcode[0:6]=='LXI B ':
            if(len(opcode)!=10 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER LXI B ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='01'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[8:10]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.input1).append(opcode[6:])
            return PC
        elif opcode[0:6]=='LXI D ':
            if(len(opcode)!=10 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER MVI D ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='11'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[8:10]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.input1).append(opcode[6:])
            return PC
        elif opcode[0:6]=='LXI H ':
            if(len(opcode)!=10 or re.findall('[^0-9A-F]',opcode[6:])):
                print 'INVALID ADDRESS AFTER LXI H ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='21'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[8:10]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.input1).append(opcode[6:])
                settings.count_in=settings.count_in+1
            return PC
        elif opcode[0:4]=='STA ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER STA...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='32'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.output).append(opcode[4:])
            return PC
        elif opcode=='STAX B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='02'
            return PC
        elif opcode=='STAX D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='12'
            return PC
        elif opcode[0:5]=='SHLD ':
            if(len(opcode)!=9 or re.findall('[^0-9A-F]',opcode[5:])):
                print 'INVALID ADDRESS AFTER SHLD...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='22'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[7:9]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.output[settings.count_out]=opcode[5:]
                settings.count_out=settings.count_out+1
                tt=hex(int(opcode[5:],16)+1).upper()
                tt=tt[2:]
                if(len(tt)==1):
                    tt='000'+tt
                elif(len(tt)==2):
                    tt='00'+tt
                elif(len(tt)==3):
                    tt='0'+tt
                (settings.output).append(tt)
            return PC
        elif opcode=='ADD A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='87'
            return PC
        elif opcode=='ADD B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='80'
            return PC
        elif opcode=='ADD C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='81'
            return PC
        elif opcode=='ADD D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='82'
            return PC
        elif opcode=='ADD E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='83'
            return PC
        elif opcode=='ADD H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='84'
            return PC
        elif opcode=='ADD L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='85'
            return PC
        elif opcode=='ADD M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='86'
            return PC
        elif opcode[0:4]=='ADI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER ADI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='C6'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode[0:4]=='ACI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER ACI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='CE'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='ADC A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8F'
            return PC
        elif opcode=='ADC B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='88'
            return PC
        elif opcode=='ADC C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='89'
            return PC
        elif opcode=='ADC D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8A'
            return PC
        elif opcode=='ADC E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8B'
            return PC
        elif opcode=='ADC H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8C'
            return PC
        elif opcode=='ADC L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8D'
            return PC
        elif opcode=='ADC M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='8E'
            return PC
        elif opcode=='SUB B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='90'
            return PC
        elif opcode=='SUB C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='91'
            return PC
        elif opcode=='SUB D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='92'
            return PC
        elif opcode=='SUB E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='93'
            return PC
        elif opcode=='SUB H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='94'
            return PC
        elif opcode=='SUB L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='95'
            return PC
        elif opcode=='SUB M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='96'
            return PC
        elif opcode=='SUB A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='97'
            return PC
        elif opcode[0:4]=='SUI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER SUI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='D6'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode[0:4]=='SBI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER MVI B ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='DE'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='SBB B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='98'
            return PC
        elif opcode=='SBB C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='99'
            return PC
        elif opcode=='SBB D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9A'
            return PC
        elif opcode=='SBB E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9B'
            return PC
        elif opcode=='SBB H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9C'
            return PC
        elif opcode=='SBB L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9D'
            return PC
        elif opcode=='SBB M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9E'
            return PC
        elif opcode=='SBB A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='9F'
            return PC
        elif opcode=='INR A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='3C'
            return PC
        elif opcode=='INR B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='04'
            return PC
        elif opcode=='INR C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='0C'
            return PC
        elif opcode=='INR D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='14'
            return PC
        elif opcode=='INR E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='1C'
            return PC
        elif opcode=='INR H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='24'
            return PC
        elif opcode=='INR L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='2C'
            return PC
        elif opcode=='INR M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='34'
            return PC
        elif opcode=='INX B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='03'
            return PC
        elif opcode=='INX D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='13'
            return PC
        elif opcode=='INX H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='23'
            return PC
        elif opcode=='DCR A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='3D'
            return PC
        elif opcode=='DCR B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='05'
            return PC
        elif opcode=='DCR C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='0D'
            return PC
        elif opcode=='DCR D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='15'
            return PC
        elif opcode=='DCR E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='1D'
            return PC
        elif opcode=='DCR H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='25'
            return PC
        elif opcode=='DCR L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='2D'
            return PC
        elif opcode=='DCR M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='35'
            return PC
        elif opcode=='DCX B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='0B'
            return PC
        elif opcode=='DCX D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='1B'
            return PC
        elif opcode=='DCX H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='2B'
            return PC
        elif opcode=='DAA':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='27'
            return PC
        elif opcode[0:4]=='JMP ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER JMP ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='C3'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:3]=='JC ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER JC ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='DA'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:3]=='JZ ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER JZ ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='CA'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:3]=='JP ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER JP ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='F2'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:3]=='JM ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER JM ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='FA'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:4]=='JNC ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER JNC ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='D2'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:4]=='JNZ ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER JNZ ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='C2'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:4]=='JPE ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER JPE ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='EA'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode[0:4]=='JPO ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER JPO ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='E2'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode=='DAD B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='09'
            return PC
        elif opcode=='DAD D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='19'
            return PC
        elif opcode=='DAD H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='29'
            return PC
        elif opcode=='ANA A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A7'
            return PC
        elif opcode=='ANA B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A0'
            return PC
        elif opcode=='ANA C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A1'
            return PC
        elif opcode=='ANA D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A2'
            return PC
        elif opcode=='ANA E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A3'
            return PC
        elif opcode=='ANA H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A4'
            return PC
        elif opcode=='ANA L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A5'
            return PC
        elif opcode=='ANA M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A6'
            return PC
        elif opcode[0:4]=='ANI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER ANI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='E6'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='ORA A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B7'
            return PC
        elif opcode=='ORA B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B0'
            return PC
        elif opcode=='ORA C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B1'
            return PC
        elif opcode=='ORA D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B2'
            return PC
        elif opcode=='ORA E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B3'
            return PC
        elif opcode=='ORA H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B4'
            return PC
        elif opcode=='ORA L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B5'
            return PC
        elif opcode=='ORA M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B6'
            return PC
        elif opcode[0:4]=='ORI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER ORI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='F6'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='XRA A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AF'
            return PC
        elif opcode=='XRA B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A8'
            return PC
        elif opcode=='XRA C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='A9'
            return PC
        elif opcode=='XRA D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AA'
            return PC
        elif opcode=='XRA E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AB'
            return PC
        elif opcode=='XRA H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AC'
            return PC
        elif opcode=='XRA L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AD'
            return PC
        elif opcode=='XRA M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='AE'
            return PC
        elif opcode[0:4]=='XRI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER XRI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='EE'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='CMC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='3F'
            return PC
        elif opcode=='STC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='37'
            return PC
        elif opcode=='NOP':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='00'
            return PC
        elif opcode=='CMA':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='2F'
            return PC
        elif opcode=='CMP A':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BF'
            return PC
        elif opcode=='CMP B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B8'
            return PC
        elif opcode=='CMP C':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='B9'
            return PC
        elif opcode=='CMP D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BA'
            return PC
        elif opcode=='CMP E':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BB'
            return PC
        elif opcode=='CMP H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BC'
            return PC
        elif opcode=='CMP L':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BD'
            return PC
        elif opcode=='CMP M':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='BE'
            return PC
        elif opcode[0:4]=='CPI ':
            if(len(opcode)!=6 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER CPI ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+2)
                PC=PC[2:len(PC)]
                settings.h[temp]='FE'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
            return PC
        elif opcode=='RRC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='0F'
            return PC
        elif opcode=='RAR':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='1F'
            return PC
        elif opcode=='RLC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='07'
            return PC
        elif opcode=='RAL':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='17'
            return PC
        elif opcode[0:7]=='LXI SP ':
            if(len(opcode)!=11 or re.findall('[^0-9A-F]',opcode[7:])):
                print 'INVALID ADDRESS AFTER LXI SP ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='31'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[7:9]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[9:11]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
            return PC
        elif opcode=='SPHL':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='F9'
            return PC
        elif opcode=='PCHL':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E9'
            return PC
        elif opcode=='XTHL':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E3'
            return PC
        elif opcode=='PUSH B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='C5'
            return PC
        elif opcode=='PUSH D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='D5'
            return PC
        elif opcode=='PUSH H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E5'
            return PC
        elif opcode=='PUSH PSW':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='F5'
            return PC
        elif opcode=='POP B':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='C1'
            return PC
        elif opcode=='POP D':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='D1'
            return PC
        elif opcode=='POP H':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E1'
            return PC
        elif opcode=='POP PSW':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='F1'
            return PC
        elif opcode=='INX SP':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='33'
            return PC
        elif opcode=='DCX SP':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='3B'
            return PC
        elif opcode=='DAD SP':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='39'
            return PC
        elif opcode[0:5]=='CALL ':
            if(len(opcode)!=9 or re.findall('[^0-9A-F]',opcode[5:])):
                print 'INVALID ADDRESS AFTER CALL ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='CD'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[7:9]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[5:])
            return PC
        elif opcode[0:3]=='CC ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER CC ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='DC'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[3:])
            return PC
        elif opcode[0:3]=='CZ ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER CZ ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='CC'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[3:])
            return PC
        elif opcode[0:3]=='CM ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER CM ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='FC'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[3:])
            return PC
        elif opcode[0:3]=='CP ':
            if(len(opcode)!=7 or re.findall('[^0-9A-F]',opcode[3:])):
                print 'INVALID ADDRESS AFTER CP ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='F4'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[3:5]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[5:7]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[3:])
            return PC
        elif opcode[0:4]=='CNC ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER CNC ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='D4'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[4:])
            return PC
        elif opcode[0:4]=='CNZ ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER CNZ ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='C4'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[4:])
            return PC
        elif opcode[0:4]=='CPE ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER CPE ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='EC'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[4:])
            return PC
        elif opcode[0:4]=='CPO ':
            if(len(opcode)!=8 or re.findall('[^0-9A-F]',opcode[4:])):
                print 'INVALID ADDRESS AFTER CPO ...RE-TYPE THE INSTRUCTION'
            else:
                temp=PC
                PC=hex(int(PC,16)+3)
                PC=PC[2:len(PC)]
                settings.h[temp]='E4'
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[4:6]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                settings.h[temp]=opcode[6:8]
                temp=hex(int(temp,16)+1)
                temp=(temp[2:len(temp)]).upper()
                (settings.sub).append(opcode[4:])
            return PC
        elif opcode=='RC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='D8'
            return PC
        elif opcode=='RNC':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='D0'
            return PC
        elif opcode=='RZ':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='C8'
            return PC
        elif opcode=='RNZ':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='C0'
            return PC
        elif opcode=='RPE':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E8'
            return PC
        elif opcode=='RPO':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='E0'
            return PC
        elif opcode=='RM':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='F8'
            return PC
        elif opcode=='RP':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='F0'
            return PC
        elif opcode=='RET':
            temp=PC
            PC=hex(int(PC,16)+1)
            PC=PC[2:len(PC)]
            settings.h[temp]='C9'
            return PC
        else:
            print 'INVALID INSTRUCTION...RE-TYPE YOUR INSTRUCTION'
            return PC
            
        
            
            
            
            
        
            
            
            
        
        
            
            
            
        
        
            
        
        
    


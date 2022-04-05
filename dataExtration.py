
import os
import re

from pathlib import Path

# print(os.getcwd())
# print(os.listdir())


def fun1(path):
    str1="Init -> Rotating"
    str2="actual"
    str3="ASYN"
    lst=[]
    compiled=re.compile(r"[\w]{6}.(\d{1,3}\.\d{3})")
    compiled2=re.compile(r"Spin\s(\-?\d{1,2}\.\d{3})")
    # with open(path+"summery.txt","w") as wf:
    with open(path,"r") as f :
            ctr=0
            temp=f.readline()
            while temp:            
                if temp.find(str1)>-1 :
                    print(temp)
                    for i in range(5):
                        temp=f.readline()
                        matches2=compiled2.findall(temp)
                        if matches2:
                            break

                    if not (temp.find(str3)>-1) and matches2 :
                    
                        
                        print(matches2)
                        print("---------------------")
                        # if False:
                        if float(matches2[0])>0.000 or float(matches2[0])<0.000:
                            if float(matches2[0])>0.000: sign=1
                            else : sign=-1
                            print("        *********************          "+str(sign))
                        
                            ctr=ctr+1
                            while not temp.find(str2)>-1 and temp:
                                temp=f.readline()
                            if temp:    
                                matches=compiled.findall(temp) 
                                print(matches)
                                if float(matches[1])==0 and float(matches[0])>10 :
                                    matches[1]="360"
                                if sign==-1:
                                    val=round(float(matches[0])-float(matches[1]),3)
                                elif sign==1:
                                    val=round(float(matches[1])-float(matches[0]),3)
                                lst.append(val)
                            # wf.write(f"{ctr}st Rotating -> Checking :       {str(val)}\n")
                            # for words in temp.split("            "): 
                            #     print(words,end=" ")
                        # print(ctr)    
                temp=f.readline()    
        # temp=f.readlines()
        
        # for line in temp: 
        #     if line.find(str2)>-1 : 
        #             print(f.tell())
        #             print(line)
        #     # if str1 in line:
        #             ctr=ctr+1
    return lst

if __name__=="__main__" :
    # print(f'the counter is {fun1()}')
    botLogFolder_Path=os.path.join(os.getcwd(),"BOT_065")
    with open(botLogFolder_Path+"\summery.txt","w") as wf:
        lst=[]
        botLog_fileNames=os.listdir(botLogFolder_Path)
        for fileName in botLog_fileNames :
            botLogFile_Path=os.path.join(botLogFolder_Path,fileName)
            lst=lst+fun1(botLogFile_Path)
        
        for item in lst :
            wf.write(str(item)+"\n")
        wf.write(f"max of error=  {max(lst)}\n")
        wf.write(f"min of error=  {min(lst)}\n")
        wf.write(f"avrage of error=  {sum(lst) / len(lst)}\n")


        print("Done ! ")

    
import matplotlib.pyplot as plt
import numpy as np

f=open("Final.txt","r")

color1 = '#1f77b4'   #blue
color2 = '#ff7f0e'   #orange
color3 = '#2ca02c'   #green

#Analyze Student ---------------------------------------------------------------
def analyze_student(Roll):
    marks=Get_Marks(Roll)
    info=Get_Stu_Info(Roll)
    overAll=get_overall_avg()
    avg=sum(marks)/4
    marks.append(avg)

    n=5
    bar=np.arange(n)
    width=0.25

    x=["PS","FSD","DE","FCSP","Average"]

    bar1=plt.bar(bar, marks, width, color=color1, label=info[-1])
    bar2=plt.bar(bar+width, overAll, width, color=color2, label="Overall Average")

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),(info[-1],"Overall Average"))
    plt.title(info[-1]+" Marks Analysis")
    plt.show()
    


#Compare Students ---------------------------------------------------------------
def compare_students(Roll_1,Roll_2):
    marks_1=Get_Marks(Roll_1)
    marks_2=Get_Marks(Roll_2)
    info_1=Get_Stu_Info(Roll_1)
    info_2=Get_Stu_Info(Roll_2)

    n=4
    bar=np.arange(n)
    width=0.25

    x=["PS","FSD","DE","FCSP"]

    bar1=plt.bar(bar, marks_1, width,color=color1, label=info_1[-1])
    bar2=plt.bar(bar+width, marks_2, width, color=color2, label=info_2[-1])

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),(info_1[-1],info_2[-1]))
    plt.title(info_1[-1]+"  vs  "+info_2[-1]+"  Marks Comparison")
    plt.show()

#Analyze Batch ---------------------------------------------------------------
def analyze_batch(Batch):

    toppers=Get_Toppers(Batch)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    marks=Get_batch_marks(Batch)
    overAll=get_overall_avg()

    width=0.25

    plt.subplot(2,1,1) #first Plot
    
    x=["PS","FSD","DE","FCSP","Average"]
    n=5
    bar=np.arange(n)

    avg=sum(marks)/4
    marks.append(avg)    

    bar1=plt.bar(bar, marks, width, color=color1, label=Batch)
    bar2=plt.bar(bar+width, overAll, width, color=color2, label="Overall Average")

    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),(Batch,"Overall Average"))
    plt.title("Average Marks Analysis")

    plt.subplot(2,1,2) #Second Plot

    x=["PS","FSD","DE","FCSP"]
    n=4
    bar=np.arange(n)

    bar1=plt.bar(bar, topper_1_marks, width, color=color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color=color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color=color1 ,label=topper_3[-1])

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title("Topper Analysis")

    plt.suptitle(Batch+" Analysis")
    plt.show()


#Compare Batch ---------------------------------------------------------------
def compare_batch(Batch_1,Batch_2):

    n=4
    bar=np.arange(n)
    width=0.25
    x=["PS","FSD","DE","FCSP"]

    plt.subplot(2,2,1)  #First Plot
    marks_1=Get_batch_marks(Batch_1)
    marks_2=Get_batch_marks(Batch_2)

    bar1=plt.bar(bar, marks_1, width,color =color1, label="Batch "+Batch_1)
    bar2=plt.bar(bar+width, marks_2, width, color =color2, label="Batch "+Batch_2)

    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),("Batch "+Batch_1,"Batch "+Batch_2))
    plt.title("Avg Marks Comparison")


    plt.subplot(2,2,2)      #Second Plot


    highest_1=Get_Toppers(Batch_1)
    highest_2=Get_Toppers(Batch_2)
    # highest_mark_1=[highest_1[3],highest_1[4],highest_1[5],highest_1[6]]
    # highest_mark_2=[highest_2[3],highest_2[4],highest_2[5],highest_2[6]]

    bar1=plt.bar(bar, [highest_1[3],highest_1[4],highest_1[5],highest_1[6]], width,color =color1, label="Batch "+Batch_1)
    bar2=plt.bar(bar+width, [highest_2[3],highest_2[4],highest_2[5],highest_2[6]], width, color =color2, label="Batch "+Batch_2)

    plt.ylabel("Highest Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),("Batch "+Batch_1,"Batch "+Batch_2))
    plt.title("Highest Marks in Specific Subjects")

    plt.subplot(2,2,3)      #Third Plot

    toppers=Get_Toppers(Batch_1)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    bar1=plt.bar(bar, topper_1_marks, width,color =color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color =color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color =color1, label=topper_3[-1])

    plt.ylabel("Marks")
    plt.xlabel("Subjects")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title(Batch_1+" Topper Analysis")

    plt.subplot(2,2,4)      #Fourth Plot
    
    toppers=Get_Toppers(Batch_2)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    bar1=plt.bar(bar, topper_1_marks, width,color =color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color =color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color =color1, label=topper_3[-1])

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title(Batch_2+" Topper Analysis")


    plt.suptitle(Batch_1+"  vs  "+Batch_2+" Analysis")
    plt.show()



#Analyze Branch ---------------------------------------------------------------
def analyze_branch(Branch):
    marks=Get_Branch_Subject_Avg(Branch)
    overAll=get_overall_avg()

    toppers=Get_Toppers(Branch)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    plt.subplot(2,1,1) #first Plot
    n=5
    bar=np.arange(n)
    width=0.25

    avg=sum(marks)/4
    marks.append(avg)   

    x=["PS","FSD","DE","FCSP","Average"]

    bar1=plt.bar(bar, marks, width,color =color1, label=Branch)
    bar2=plt.bar(bar+width, overAll, width, color =color2, label="Overall Average")

    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),(Branch,"Overall Average"))
    plt.title("Average Marks Analysis")
    

    plt.subplot(2,1,2) #Second Plot

    n=4
    bar=np.arange(n)
    x=["PS","FSD","DE","FCSP"]

    bar1=plt.bar(bar, topper_1_marks, width,color =color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color =color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color =color1, label=topper_3[-1])

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title("Topper Analysis")

    plt.suptitle(Branch+" Analysis")
    plt.show()


#Compare Branch ---------------------------------------------------------------
def compare_branch(Branch_1,Branch_2):
    marks_1=Get_Branch_Subject_Avg(Branch_1)
    marks_2=Get_Branch_Subject_Avg(Branch_2)

    avg_1=Get_Branch_Total_Avg(Branch_1)
    avg_2=Get_Branch_Total_Avg(Branch_2)

    n=4
    bar=np.arange(n)
    width=0.25
    x=["PS","FSD","DE","FCSP"]

    plt.subplot(2,2,1)      #First Plot

    bar1=plt.bar(bar, marks_1, width,color =color1, label="Branch "+Branch_1)
    bar2=plt.bar(bar+width, marks_2, width, color =color2, label="Branch "+Branch_2)

    plt.ylabel("Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),("Branch "+Branch_1,"Branch "+Branch_2))
    plt.title("Branch "+Branch_1+"  vs  "+"Branch "+Branch_2+"  Subject Avg Marks Comparison")

    plt.subplot(2,2,2)      #Second Plot

    highest_1=Get_Toppers(Branch_1)
    highest_2=Get_Toppers(Branch_2)
    # highest_mark_1=[highest_1[3],highest_1[4],highest_1[5],highest_1[6]]
    # highest_mark_2=[highest_2[3],highest_2[4],highest_2[5],highest_2[6]]

    bar1=plt.bar(bar, [highest_1[3],highest_1[4],highest_1[5],highest_1[6]], width,color =color1, label="Batch "+Branch_1)
    bar2=plt.bar(bar+width, [highest_2[3],highest_2[4],highest_2[5],highest_2[6]], width, color =color2, label="Batch "+Branch_2)

    plt.ylabel("Highest Marks")

    plt.xticks(bar+0.12,x)
    plt.legend((bar1,bar2),("Batch "+Branch_1,"Batch "+Branch_2))
    plt.title("Highest Marks in Specific Subjects")

    plt.subplot(2,2,3)      #Third Plot

    toppers=Get_Toppers(Branch_1)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    bar1=plt.bar(bar, topper_1_marks, width,color =color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color =color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color =color1, label=topper_3[-1])

    plt.ylabel("Marks")
    plt.xlabel("Subjects")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title(Branch_1+" Topper Analysis")
    
    plt.subplot(2,2,4)      #Fourth Plot
    
    toppers=Get_Toppers(Branch_2)
    topper_1=Get_Stu_Info(toppers[0])
    topper_2=Get_Stu_Info(toppers[1])
    topper_3=Get_Stu_Info(toppers[2])

    topper_1_marks=Get_Marks(toppers[0])
    topper_2_marks=Get_Marks(toppers[1])
    topper_3_marks=Get_Marks(toppers[2])

    bar1=plt.bar(bar, topper_1_marks, width,color =color3, label=topper_1[-1])
    bar2=plt.bar(bar+width, topper_2_marks, width, color =color2, label=topper_2[-1])
    bar3=plt.bar(bar+2*width, topper_3_marks, width, color =color1, label=topper_3[-1])

    plt.xlabel("Subjects")
    plt.ylabel("Marks")

    plt.xticks(bar+0.24,x)
    plt.legend((bar1,bar2,bar3),("1st "+topper_1[-1],"2nd "+topper_2[-1],"3rd "+topper_3[-1]))
    plt.title(Branch_2+" Topper Analysis")

    plt.suptitle(Branch_1+"  vs  "+Branch_2+" Analysis")
    plt.show()



#-------------------------------------------------Functions-------------------------------------------------
def Get_Marks(Roll):
    f.seek(0)
    for line in f:
        search_str1 = str(Roll)+" CSE"
        search_str2 = str(Roll)+" CEA"
        search_str3 = str(Roll)+" CST"
        search_str4 = str(Roll)+" IT"
        if (search_str1 in line) or (search_str2 in line) or (search_str3 in line) or (search_str4 in line):
            marks=line.split()

            ps=float(marks[-4])
            fsd=float(marks[-3])
            de=float(marks[-2])
            fcsp=float(marks[-1])

            return [ps,fsd,de,fcsp]
# print(Get_Marks(Roll))

def Get_Stu_Info(Roll):
    f.seek(0)
    for line in f:
        search_str1 = str(Roll)+" CSE"
        search_str2 = str(Roll)+" CEA"
        search_str3 = str(Roll)+" CST"
        search_str4 = str(Roll)+" IT"
        if (search_str1 in line) or (search_str2 in line) or (search_str3 in line) or (search_str4 in line):
            details=line.split()
            l=len(details)-7
            roll=details[0]
            branch=details[1]
            batch=details[2]
            name=""
            if l==1:
                name=str(details[3])
            elif l==2:
                name=str(details[3])+" "+str(details[4])
            elif l==3:
                name=str(details[3])+" "+str(details[4])+" "+str(details[5])
            return [roll,branch,batch,name]
        # print(list([roll,branch,batch,name]))
# Get_Stu_Info(Roll)

def Get_batch_marks(Batch):
    f.seek(0)
    count=0
    ps_avg=0.0
    fsd_avg=0.0
    de_avg=0.0
    fcsp_avg=0.0
    
    for line in f:
        if str(Batch).upper() in line:
            count+=1
            ps_avg+=float(line.split()[-4])
            fsd_avg+=float(line.split()[-3])
            de_avg+=float(line.split()[-2])
            fcsp_avg+=float(line.split()[-1])
    ps_avg=round(ps_avg/count,2)
    fsd_avg=round(fsd_avg/count,2)
    de_avg=round(de_avg/count,2)
    fcsp_avg=round(fcsp_avg/count,2)
    return [ps_avg,fsd_avg,de_avg,fcsp_avg]
# print(Get_batch_marks())
                
def Get_Branch_Subject_Avg(Branch):
    f.seek(0)
    count=0
    ps_avg=0.0
    fsd_avg=0.0
    de_avg=0.0
    fcsp_avg=0.0
    for line in f:
        if str(Branch).upper() in line:
            count+=1
            ps_avg+=float(line.split()[-4])
            fsd_avg+=float(line.split()[-3])
            de_avg+=float(line.split()[-2])
            fcsp_avg+=float(line.split()[-1])
    ps_avg=round(ps_avg/count,2)
    fsd_avg=round(fsd_avg/count,2)
    de_avg=round(de_avg/count,2)
    fcsp_avg=round(fcsp_avg/count,2)
    return [ps_avg,fsd_avg,de_avg,fcsp_avg]

def Get_Branch_Total_Avg(Branch):
    f.seek(0)
    count=0
    avg=0.0
    for line in f:
        if str(Branch).upper() in line:
            count+=1
            avg+=float(line.split()[-4])+float(line.split()[-3])+float(line.split()[-2])+float(line.split()[-1])
    avg=round(avg/(count*4),2)
    return avg

def get_overall_avg():
    f.seek(0)
    count=0
    total_avg=0.0

    ps_avg=0.0
    fsd_avg=0.0
    de_avg=0.0
    fcsp_avg=0.0

    for line in f:
        if line[0].isdigit():
            count+=1
            ps_avg+=float(line.split()[-4])
            fsd_avg+=float(line.split()[-3])
            de_avg+=float(line.split()[-2])
            fcsp_avg+=float(line.split()[-1])
            total_avg=(ps_avg+fsd_avg+de_avg+fcsp_avg)/4

    ps_avg=round(ps_avg/count,2)
    fsd_avg=round(fsd_avg/count,2)
    de_avg=round(de_avg/count,2)
    fcsp_avg=round(fcsp_avg/count,2)
    total_avg=round(total_avg/count,2)

    return [ps_avg,fsd_avg,de_avg,fcsp_avg,total_avg]

def Get_Toppers(arg):
    f.seek(0)

    topper_1, topper_2, topper_3=0.0,0.0,0.0
    max_ps,max_fsd,max_de,max_fcsp=0.0,0.0,0.0,0.0
    topper_1_roll,topper_2_roll,topper_3_roll="","",""

    for line in f:
        
        if arg in line:
            total_marks=float(line.split()[-4])+float(line.split()[-3])+float(line.split()[-2])+float(line.split()[-1])
            roll=line.split()[0]

            if max_ps<float(line.split()[-4]):
                max_ps=float(line.split()[-4])
            if max_fsd<float(line.split()[-3]):
                max_fsd=float(line.split()[-3])
            if max_de<float(line.split()[-2]):
                max_de=float(line.split()[-2])
            if max_fcsp<float(line.split()[-1]):
                max_fcsp=float(line.split()[-1])

            if total_marks>topper_1:
                topper_3=topper_2
                topper_2=topper_1
                topper_1=total_marks
                topper_1_roll=roll

            elif total_marks>topper_2:
                topper_3=topper_2
                topper_2=total_marks
                topper_2_roll=roll
            elif total_marks>topper_3:
                topper_3=total_marks
                topper_3_roll=roll

            max_ps=round(max_ps,2)
            max_fsd=round(max_fsd,2)
            max_de=round(max_de,2)
            max_fcsp=round(max_fcsp,2)
    return [topper_1_roll,topper_2_roll,topper_3_roll,max_ps,max_fsd,max_de,max_fcsp]
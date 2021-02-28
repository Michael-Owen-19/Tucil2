# Nama : Michael Owen
# NIM  : 13519055

# mencetak nama aplikasi
print("Course Planning")

# input nama file
file = str(input("Masukkan nama File : "))

#pembacaan dan pembersihan file
with open(file, 'r') as f:
    lines = f.readlines()
    lines = [line.replace(' ', '') for line in lines]
    lines = [line.replace('\n', '') for line in lines]
    lines = [line.replace('.', '') for line in lines]
for i in range(len(lines)):
    lines[i]=lines[i].split(',')

# memasukkan data input ke dalam array graf
graph=[]
for i in range(len(lines)):
    graph.append([lines[i],len(lines[i])-1])

#fungsi yang berfungsi untuk mengecek apakah list memiliki mata kuliah yang tidak memiliki prereq ataupun semua prereqnya telah dipetakan
def isDAG(list):
    for i in range(len(list)):
        if list[i][1]==0:
            return True
    return False

#fungsi yang mengecek apakah array kosong
def isEmpty(list):
    for i in range (len(list)):
        if list[i][1]!=-1:
            return False
    return True

# fungsi yang mengembalikan array yang berisi course dari array inputan yang tidak memiliki prereq atau semua prereqnya telah dipetakan
def getCourse(list):
    temp=[]
    for i in range(len(list)):
        if list[i][1]==0:
            temp.append(graph[i])
    return temp

#main program
loop=False
semester=1          #inisialisasi semester
CourseDict={}       #dictionary yang menampung course yang diambil setiap semester
while(isEmpty(graph)==False):       #melakukan perulangan jika graf belum kosong atau dipetakan semua
    courseList=getCourse(graph)
    local=[]
    for i in range(len(courseList)):
        local.append(courseList[i][0][0])
    CourseDict.update({semester:local})     #melakukan pemetaan course ke dictionary
    if isDAG(graph)==True:

        for idx in range(len(courseList)):
            graph.remove(courseList[idx])       #menghapus course yang tidak memiliki prereq atau prereqnnya telah dipetakan semua
        for i in range(len(graph)):
            for j in range(len(courseList)):
                if courseList[j][0][0] in graph[i][0][1:]:
                    graph[i][0].remove(courseList[j][0][0])     #menghapus course prereq
                    graph[i][1]-=1
    else:
        loop=True
        break       # jika graf bukan DAG maka menghentikan perulangan
    semester+=1     # bergerak ke semester berikutnya


if loop==True:
    print("Bukan DAG, Loop detected")

else:   #loop == False
    #melakukan pencetakan semester beserta course yang diambil pada semester tersebut
    for i in range(len(CourseDict)):
        for j in range(len(CourseDict[i+1])):
            if len(CourseDict[i+1])>1:
                if j==0:
                    print("Semester ",i+1," : ",CourseDict[i+1][j],end=" ")
                else:
                    print(", ",CourseDict[i+1][j])
            else:
                print("Semester ",i+1," : ",CourseDict[i+1][j])




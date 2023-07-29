try:
    with open('./Classroom/Exception_File/qwerty.txt','r') as fin, open('./Classroom/Exception_File/out.txt','w') as fout:
    # fin = open('./Classroom/Exception_File/qwerty.txt','a')
    # fin.write("errror")
    # f2 = open('./Classroom/Exception_File/qwerty.txt','r')
    # print(f2.read())
        f = fin.readlines()
        fout = open('./Classroom/Exception_File/out.txt','w')
        fout.writelines(f)
    # for line in fin:
    #     fout.write(line)
    #     fout.write(line)
    # f = fin.readline()
    # print (f)
    # f = fin.readline()
    # print (f)
    # f = fin.readline()
    # print (f)
    # list2 = f.split('\n')
    # print(list2)
except:
    print('Error open file\n Close')
finally:
    fin.close()
    # fout.close()

input()
fin=open('list.txt','r')
fout=open('list.js','r+')
for line in fin:
    fout.write('\"')
    fout.write(line.strip())
    fout.write('\",')
fin.close()

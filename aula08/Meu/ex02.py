with open(r'C:\Users\ruifa\OneDrive - Universidade de Aveiro\FP\aula08\Meu', 'r') as f:
    names = {}
    f.readline()
    for line in f:
        name = line.split(" ")
        name[-1] = name[-1].strip()
        names[name[-1]] = set()
        names[name[-1]].add(name[0])

for e in names:
    print(e, ":", names[e])




       

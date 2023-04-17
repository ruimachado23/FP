Un = 100
c = 0

while Un > 0:
    print(Un)
    Un = 1.01*Un - 1.01
    c += 1

print("Foram mostrados", str(c), "termos de Un")
    
        
        

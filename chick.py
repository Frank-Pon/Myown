for x in range(0,20):
    for y in range (0,33):
        z=100-x-y
        if 5*x+3*y+z/3==100:
            print("公雞:%d隻,母雞:%d隻,雛雞:%d隻"%(x,y,z))





for i in range(20):
    for j in range (33):
        k = 100 - i - j 
        if i*5+j*3+k/3 ==100:
            print(f"可買公雞:{i}隻,母雞:{j}隻,雛雞:{k}隻")
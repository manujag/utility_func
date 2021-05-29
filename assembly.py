import dis
def sem(a,b,c,d,e):
    return (a-b)/(c+(d*e))

def sem1(a,b,c,d,e):
    return 0/0

print(dis.dis(sem1))
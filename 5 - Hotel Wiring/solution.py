T = int(input().strip())

for t in range(T):
    M,N,K = (int(x) for x in input().strip().split())
    
    total_on = 0
    delta = []
    for m in range(M):
        on = int(input().strip())
        diff = 2*on - N
        delta.append(diff)
        total_on += on
    
    delta.sort()
    total_on -= sum(delta[:K])
    print(total_on)
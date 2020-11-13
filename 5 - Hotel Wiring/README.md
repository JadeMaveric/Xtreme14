This one's really simply, from a certain perspective.  
We've got to flip K switches to maximise the number of lights that are on. We only need to worry about the value for the K switches, specifically the change in the value. Once we know the change it's as simple as sorting the list and choosing the K entries with the most change.

```python
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
```

Question: https://csacademy.com/contest/ieeextreme-practice/task/hotel-wiring
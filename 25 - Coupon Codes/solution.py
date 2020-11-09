# A Naive solution would compare all codes against each other to find
# pairs with a hamming distance == 1. Even optimised versions of this become
# O(n^2). The input constrains go all the way up to 10^5, and the server will
# omae wa mo shindeiru our code before it even goes through half of them

# We can reduce runtime here to O(n) by using a hashmap,
# at the expense of more memory. But we've got 256MB of that so... meh!
# Here we can find out exactly how many code have the same hamming distance
# in constant time. Instead of iterating and comparing with all of them

N = int(input().strip())
table = dict()

for n in range(N):
    code = input().strip().replace('-', '')
    for keyword in [code[:i]+'?'+code[i+1:] for i in range(len(code))]:
        if keyword in table:
            table[keyword] += 1
        else:
            table[keyword] = 1

ans = 0
for entry in table:
    n = table[entry]
    ans += n * (n-1) / 2
    
ans = int(ans)
print(ans)
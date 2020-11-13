from math import ceil

N,Cb,Cp = (int(x) for x in input().strip().split(' '))

blue_tiles_needed = 0
pink_tiles_needed = 0

for n in range(N):
    Bi,Pi = (int(x) for x in input().strip().split(' '))
    blue_tiles_needed += Bi
    pink_tiles_needed += Pi
  

blue_tiles_cost = Cb * ceil(blue_tiles_needed/10)
pink_tiles_cost = Cp * ceil(pink_tiles_needed/10)

print(blue_tiles_cost + pink_tiles_cost)
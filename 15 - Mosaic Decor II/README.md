This in some way a lot like [Mosaic Decor I](). We've got to place rectangular tiles, on a rectangular wall. No ratations allowed. The dimensions of the tiles won't always align with the wall, so we'll need to cut a good chuck off. For cut that we make, we've got to pay some fellow, so we got to keep that in mind.

Our goal is to minimise the costs. There's two factors here, the number of tiles and the number of cuts. We can't really do anything about the tiles, that's a constant surface area we need to buy. But we can do something about the cuts. Namely, we can 'cut' the cost by 2.

We've got cut off every area which exceeds the wall boundaries. This could mean shaving off 4 sides of tiled area. But, if our tiles are aligned with 2 edges (so start placing them from a corner) then the number of edges we need to shave off reduces to 2.

```python
from math import ceil

wall_width, wall_height, tile_width, tile_height, tile_cost, cut_cost \
= (int(x) for x in input().strip().split())

tiles_required = ceil(wall_width/tile_width) \
                 * ceil(wall_height/tile_height)
cuts_required = (wall_width if wall_height%tile_height else 0) \
                + (wall_height if wall_width%tile_width else 0)
bundles_required = ceil(tiles_required/10)

tiles_cost = max(100, bundles_required * tile_cost)
cuts_cost  = cuts_required * cut_cost

print(tiles_cost + cuts_cost)
```

Question: https://csacademy.com/contest/ieeextreme-practice/task/mosaic2
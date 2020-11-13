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
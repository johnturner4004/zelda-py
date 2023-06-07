from csv import reader

def import_csv_layout(path):
  
  with open(path) as level_map:
    terrain_map = []
    layout = reader(level_map, delimiter=',')
    for row in layout:
      terrain_map.append(list(row))
    return terrain_map

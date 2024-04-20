def read_file(path:str) -> dict:
    with open(path,'r', encoding='UTF-8') as file:
        data = file.readlines()
        symbols = [ch.strip() for ch in data[::2]]
        coords = [i.strip().replace('_', ' ').split(' ') for i in data[1::2]]
        coords_int = [[int(j) for j in l] for l in coords]
        result = {}
        for j, value in enumerate(coords_int):
            value_x = value[::2]
            value_y = value[1::2]
            coords_result = [(coord, value_y[i]) for i, coord in enumerate(value_x)]
            result[symbols[j]] = coords_result
        return result

def save_pict_to_file(symbols:dict, textfile:str):
    matrix = []
    coords_used = set()
    for i in symbols.values():
        coords_used.update(i)
    coords = [int(l) for i in symbols.values() for j in i for l in j]
    max_coords_x = max(coords[::2])
    max_coords_y = max(coords[1::2])
    for x_coord in range(max_coords_x+1):
        matrix.append([' ']*(max_coords_y+1))
        for i in symbols:
            for coord in symbols[i]:
                if coord[0] == x_coord:
                    matrix[x_coord][coord[1]] = i
                elif coord not in coords_used:
                    coords_used.add(coord)
                    break

    with open(textfile, 'w', encoding='UTF-8') as file:
        for j in matrix:
            line = ''.join(j)
            file.write(line + '\n')
        return None

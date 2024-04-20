"""
imported tempfile for doctest in second func
"""
def read_file(path:str) -> dict:
    """
    This is function that reads file and returns dictionary to decode picture
    Args:
        path (str): path to file which must be read

    Returns:
        dict: dictionary of symbol and list of its coordinates
    """
    with open(path,'r', encoding='UTF-8') as file:
        data = file.readlines()
        symbols = [ch.strip() for ch in data[::2]]
        coords = [i.strip().replace('_', ' ').split(' ') for i in data[1::2]]
        coords_int = []
        for l in coords:
            coords_int.append([int(j) for j in l])
        result = {}
        # inputing all symbols and their coords to dictionary
        for j, value in enumerate(coords_int):
            value_x = value[::2]
            value_y = value[1::2]
            coords_result = []
            for i, coord in enumerate(value_x):
                coords_result_symb = (coord, value_y[i])
                coords_result.append(coords_result_symb)
            result[symbols[j]] = coords_result
        return result

def save_pict_to_file(symbols:dict, textfile:str):
    """
    func to write picture to file
    Args:
        symbols (dict): symbol and its coords dictionary
        textfile (str): file where this programm writes picture
    """
    matrix = []
    coords = []
    coords_used = []
    for i in symbols:
        coords_used += symbols[i]
    for i in symbols:
        for j in range(len(symbols[i])):
            for l in symbols[i][j]:
                coords.append(int(l))
    max_coords_x = max(coords[::2])
    max_coords_y = max(coords[1::2])
    for x_coord in range(max_coords_x+1):
        matrix.append([])
        for y_coord in range(max_coords_y+1):
            for i in symbols:
                if (x_coord,y_coord) in symbols[i]:
                    matrix[x_coord].append(i)
                elif (x_coord,y_coord) not in coords_used:
                    matrix[x_coord].append(' ')
                    coords_used.append((x_coord, y_coord))

    with open(textfile, 'w', encoding='UTF-8') as file:
        for j in matrix:
            if j != matrix[-1]:
                line = ''.join(j)
                file.write(line + '\n')
            else:
                line = ''.join(j)
                file.write(line)
        return None

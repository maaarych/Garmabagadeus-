def read_file(path:str) -> dict:
    """
    This is function that reads file and returns dictionary to decode picture
    Args:
        path (str): path to file which must be read

    Returns:
        dict: dictionary of symbol and list of its coordinates
    """
    result = {}
    with open(path,'r', encoding='UTF-8') as file:
        symbols = []
        for line_num, line in enumerate(file):
            if line_num % 2 == 0:
                symbols.append(line.strip())
            else:
                coords = line.strip().replace('_', ' ').split(' ')
                coords_int = [int(coord) for coord in coords]
                coords_result = [(coords_int[i], coords_int[i+1]) for i in range(0, len(coords_int), 2)]
                result[symbols[-1]] = coords_result
    return result

def save_pict_to_file(symbols:dict, textfile:str):
    """
    func to write picture to file
    Args:
        symbols (dict): symbol and its coords dictionary
        textfile (str): file where this programm writes picture
    """
    matrix = []
    coords_used = set()
    max_coords_x = 0
    max_coords_y = 0
    for coords in symbols.values():
        for coord in coords:
            x_coord, y_coord = coord
            coords_used.add((x_coord, y_coord))
            max_coords_x = max(max_coords_x, x_coord)
            max_coords_y = max(max_coords_y, y_coord)

    for x_coord in range(max_coords_x+1):
        matrix.append([])
        for y_coord in range(max_coords_y+1):
            found_symbol = False
            for symbol, coords in symbols.items():
                if (x_coord, y_coord) in coords:
                    matrix[x_coord].append(symbol)
                    found_symbol = True
                    break
            if not found_symbol:
                matrix[x_coord].append(' ')
                coords_used.add((x_coord, y_coord))

    with open(textfile, 'w', encoding='UTF-8') as file:
        for j in matrix:
            line = ''.join(j)
            file.write(line + '\n')

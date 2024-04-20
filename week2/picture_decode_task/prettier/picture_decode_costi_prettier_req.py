def read_file(path: str) -> dict:
    """
    This function reads a file and returns a dictionary to decode a picture.
    Args:
        path (str): Path to the file that needs to be read.

    Returns:
        dict: Dictionary of symbols and their coordinates.
    """
    with open(path, 'r', encoding='UTF-8') as file:
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


def save_pict_to_file(symbols: dict, textfile: str):
    """
    Function to write a picture to a file.
    Args:
        symbols (dict): Dictionary of symbols and their coordinates.
        textfile (str): File where the picture will be written.
    """
    matrix = []
    coords_used = [coord for coords in symbols.values() for coord in coords]
    coords = [int(l) for symbol_coords in symbols.values() for coord in symbol_coords for l in coord]
    max_coords_x = max(coords[::2])
    max_coords_y = max(coords[1::2])
    for x_coord in range(max_coords_x + 1):
        matrix.append([])
        for y_coord in range(max_coords_y + 1):
            for i in symbols:
                if (x_coord, y_coord) in symbols[i]:
                    matrix[x_coord].append(i)
                elif (x_coord, y_coord) not in coords_used:
                    matrix[x_coord].append(' ')
                    coords_used.append((x_coord, y_coord))

    with open(textfile, 'w', encoding='UTF-8') as file:
        for j in matrix:
            line = ''.join(j)
            file.write(line + '\n' if j != matrix[-1] else line)
        return None

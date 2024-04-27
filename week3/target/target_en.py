"""target"""
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    # >>> generate_grid()
    # [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    vowels = ['A', 'E', 'I', 'O', 'U']

    def generate():
        lst, out = [], []
        while len(out)!=3:
            if len(lst)<3:
                lst.append(random.choice(alphabet))
            else:
                out.append(lst)
                lst = []
        if len([j for i in out for j in i if j in vowels]) !=3:
            return generate()
        return out
    return generate()

# print(generate_grid())

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt',['h', 'r', 'i', 'd', 't', 'd', 'x', 'x', 'm'])
    ['dirt', 'mirth', 'thir', 'third', 'trim', 'trix']
    """
    lst = []
    letters = [i.lower() for i in letters]
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            line_ = line.strip().lower()
            counter = 0
            let2 = letters.copy()
            if len(line_)>=4 and letters[4] in line_:
                for i in line_:
                    if i in let2:
                        counter+=1
                        let2.remove(i)
            if counter==len(line_):
                if line_ not in lst:
                    lst.append(line_)
    return lst

# print(get_words('en.txt',[el for el in 'jniarnoah']))

def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    try:
        lst = []
        while True:
            input_ = input()
            lst.append(input_)
    except EOFError:
        return lst

def get_pure_user_words(
        user_words: list[str], letters: list[str],
        words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(['dirt'], ['h', 'r', 'i', 'd', 't', 'd', 'x', 'x', 'm'], \
['dirt', 'mirth', 'thir', 'third', 'trim'])
    []
    """
    letters_ = [x.lower() for x in letters]
    kanaut, out = [], []
    for i in user_words:
        let_ = letters_.copy()
        counter = 0
        if 4<=len(i):
            if letters[4] in i:
                for j in i:
                    if j in let_:
                        let_.remove(j)
                        counter+=1
                if len(i) == counter:
                    kanaut.append(i)
    for k in kanaut:
        if k not in words_from_dict:
            out.append(k)
    return out

def main():
    grid = generate_grid()
    print(f'Your board is {grid}')
    lst = []
    for i in grid:
        for k in i:
            lst.append(k.lower)
    print('Please, suggest your words here:')
    us_ = get_user_words()
    new = list(grid[0] + grid[1] + grid[2])
    for j, element in enumerate(new):
        new[j] = element.lower()
    words = get_words('en.txt', new)
    num = len(words) - len(get_pure_user_words(us_, new, words))
    print(f'Number of the right words: {num}')
    print('All possible words:')
    print(words)
    print('You missed the following words:')
    print(get_pure_user_words(us_, new, words))
    no = []
    for k in us_:
        if 4<=len(k)<=9:
            if new[4] in k:
                if k not in words:
                    no.append(k)
    print(f"You suggest, but we don't have them in the dictionary: {no}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

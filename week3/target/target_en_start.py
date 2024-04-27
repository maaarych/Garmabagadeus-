"""target"""
import random
def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    >>> generate_grid()
    [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lst1, lst2, lst3, main_lst = [], [], [], []
    for i in range(3):
        i = random.choice(alphabet)
        lst1.append(i)
    for j in range(3):
        j = random.choice(alphabet)
        lst2.append(j)
    for k in range(3):
        k = random.choice(alphabet)
        lst3.append(k)
    main_lst.append(lst1)
    main_lst.append(lst2)
    main_lst.append(lst3)
    return main_lst

def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt',['h', 'r', 'i', 'd', 't', 'd', 'x', 'x', 'm'])
    ['dirt', 'mirth', 'thir', 'third', 'trim']
    """
    lst = []
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            line_ = line.strip().lower()
            counter = 0
            let2 = letters.copy()
            if 9>=len(line_)>=4:
                for i in line_:
                    if letters[4] in line:
                        if i in let2:
                            counter+=1
                            let2.remove(i)
            if counter==len(line_):
                if line_ not in lst:
                    lst.append(line_)
    return lst
def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    try:
        lst =[]
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
    ['mirth', 'thir', 'third', 'trim']
    """
    letters_ = [x.lower() for x in letters]
    kanaut = []
    for i in user_words:
        let_ = letters_.copy()
        if 4<=len(i)<=9:
            if letters[4] in i:
                for j in i:
                    if j in let_:
                        let_.remove(j)
                kanaut.append(i)
    for k in kanaut:
        if k in words_from_dict:
            words_from_dict.remove(k)
    return words_from_dict

def main():
    '''
    Starts a game.
    '''
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

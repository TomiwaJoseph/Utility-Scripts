import sys
from itertools import permutations
   

def find_words():
    ''' Accept scrambled letters and word length '''
    try:
        scrambled_letters = sys.argv[1]
        if scrambled_letters == '--help':
            print()
            print('#--------------------------------------------------#')
            print()
            print('You have to enter both your letters and word length')
            print('Eg. python word_finder.py pnhoty 6')
            print("Results -> ['phyton', 'python', 'typhon']")
            print()
            print('#--------------------------------------------------#')
            print()
            return
        word_length = int(sys.argv[2])
        
        with open("./better_dictionary.txt") as file_content:
            contents = file_content.readlines()
            contents = [word.rstrip() for word in contents]

        final_search_results = []
        all_possible_combinations = sorted(["".join(word) for word in list(permutations(scrambled_letters, word_length))])
        for word in all_possible_combinations:
            if word in contents:
                final_search_results.append(word)
        print()
        print('#--------------------------------------------------#')
        print()
        print(sorted(list(set(final_search_results))))
        print()
        print('#--------------------------------------------------#')
        print()
    except (IndexError, ValueError):
        print()
        print('#--------------------------------------------------#')
        print()
        print('INPUT ERROR')
        print('You have to enter both your letters and word length')
        print('Eg. python word_finder.py pnhoty 6')
        print("Results -> ['phyton', 'python', 'typhon']")
        print()
        print('#--------------------------------------------------#')
        print()


if __name__ == "__main__":
    find_words()

class TrieNode:
    '''
    Represents each node in the trie
    Data:
    children - to denote the children of each trie node
    end_of_word - boolean value to denote the end of word at a node
    '''
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    '''
    ========================================================
    METHOD:
    insert_word - Method to insert  words in Trie.

    PARAMETERS:
    word - input of string type for words in Trie.

    RETURN:
    None
    ========================================================
    '''
   
    def insert_word(self, word : str) -> None:
        current_node = self.root
        
        for i in word:
            if i not in current_node.children:
                current_node.children[i] = TrieNode()
            current_node = current_node.children[i]
        current_node.end_of_word = True

    '''
    ========================================================
    METHOD:
    depth_first_search_trie - Method to traverse through a trie using DFS

    PARAMETERS:
    current_node - Represents particular node of the trie
    current_word - String value to keep track of word processed through DFS
    words - Contains list of all the words traversed

    RETURN:
    None
    ========================================================
    '''
       
    def depth_first_search_trie(self, current_node, current_word, words):
        if current_node.end_of_word:
            words.append(current_word)

        for character, child_node in current_node.children.items():
            self.depth_first_search_trie(
                child_node, current_word + character, words)

    '''
    ========================================================
    METHOD:
    find_words_with_substring - Method to traverse the Trie and find
        all posible words matching substring.

    PARAMETERS:
    substring - String type to hold the users input choice of substring.

    RETURN:
    found_words - Returns a list of words.
    ========================================================
    '''

    def find_words_with_substring(self, substring):
        words = []
        found_words = []
        self.depth_first_search_trie(self.root, "", words)
        for word in words:
            if substring in word:
                found_words.append(word)
        return found_words

    '''
    ========================================================
    METHOD:
    print_trie - Method to print all the words in the trie

    PARAMETERS:
    None

    RETURN:
    words - list
    ========================================================
    '''

    def print_trie(self):
        words = []
        self.depth_first_search_trie(self.root, "", words)
        words.sort()
        return words

 
# Create trie object
new_trie = Trie()


display_menu = 1
while (display_menu):
    print('\n')
    print("####################### MENU #######################")
    print("1. Insert a new word")
    print("2. Print all the words")
    print("3. Print words containing the substring")
    print("4. Exit")

    # To get the user choice from the menu
    user_choice = int(input())

    match user_choice:
        case 1:
            # to insert words into trie
            number_of_words = int(input("Enter the number of words: "))
            print("Number of words: ", number_of_words)

            words = []
            for i in range(0, number_of_words):
                word = str(input(f"Enter {i+1} word: "))
                words.append(word.lower().strip())

            for word in words:
                new_trie.insert_word(word)

        case 2:
            # to print all words in the trie
            print("All words in the trie: ", new_trie.print_trie())

        case 3:
            # to print all words matching with the substring
            substring = str(input("Enter the substring to be matched with: "))
            print("Found words with substring: ",
                  new_trie.find_words_with_substring(substring))

        case 4:
            # to exit the program
            print("End of Program :) Bye!")
            display_menu = 0
        case _:
            # The default case to ask the correct choice from user
            print("Please enter a number from the above choices!")

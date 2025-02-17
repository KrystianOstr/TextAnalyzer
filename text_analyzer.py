import os

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def analyze(self):
        self.count_words()
        self.count_characters()
        self.most_common_words()
        self.save_to_file()


    def count_words(self):
        count_words = len(self.text.split())

        return count_words

    def count_characters(self):
        count_chars_with_whitespace = len(self.text)
        count_chars_without_whitespace = len(self.text.replace(" ", ""))

        return count_chars_with_whitespace, count_chars_without_whitespace

    def most_common_words(self, n=5):
        from collections import Counter
        words = self.text.split()
        most_common_words = Counter(words)
        
        return most_common_words.most_common(n)
    


def get_text_input():
    get_input_from_user = input('\nProvide the text to analyze: \n')
    return get_input_from_user

def load_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f'\n{content}\n')
            return TextAnalyzer(content)
    except FileNotFoundError:
         print('File doesn`t exist')
         return None

def save_to_file(analyzer, filename='text_analyzer.txt'):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(analyzer.text)

def save_statistics_to_file(analyzer, filename='text_analyzer_statistics.txt'):
        word_count = analyzer.count_words()
        total_characters, characters_without_spaces = analyzer.count_characters()
        common_words = analyzer.most_common_words()

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Words in text: {word_count}.\n')
            file.write(f'Chars WITH whitespaces in text: {total_characters}.\n')
            file.write(f'Chars WITHOUT whitespaces in text: {characters_without_spaces}.\n')
            file.write('Most common words in text:\n')
            for word, count in common_words:
                file.write(f'{word} : {count}\n')


def display_statistics(analyzer):
        word_count = analyzer.count_words()
        total_characters, characters_without_spaces = analyzer.count_characters()
        common_words = analyzer.most_common_words()

        print(f'\nWords in text: {word_count}.')
        print(f'\nChars WITH whitespaces in text: {total_characters}.')
        print(f'\nChars WITHOUT whitespaces in text: {characters_without_spaces}.')
        print('\nMost common words in text:')
        for word, count in common_words:
            print(f'{word} : {count}')
        print('\n')

def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} deleted.')
    except FileNotFoundError:
        print(f'{filename} doesn`t exist.')



def delete_all_files():
    files = ['text_analyzer.txt', 'text_analyzer_statistics.txt']
    for file in files:
        delete_file(file)

while True:
    print('1. Input  the text')
    print('2. Load the text from file')
    print('3. Show statistics')
    print('4. Save the text to file')
    print('5. Save the statistics to file')
    print('6. Delete all files')
    print('7. Exit')

    try:
        user_choose = int(input('\nChoose 1 - 7:\n'))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.\n")
        continue


    if user_choose == 1:
        text_to_analyze = get_text_input()
        analyzer = TextAnalyzer(text_to_analyze)
    elif user_choose == 2:
        analyzer = load_from_file('text_analyzer.txt')
        if analyzer is None:
            print('Loading failed.\n')
    elif user_choose == 3:
        display_statistics(analyzer)
    elif user_choose == 4:
        if analyzer:
            save_to_file(analyzer, 'text_analyzer.txt')
        else:
            print('Nothing to save.')
    elif user_choose == 5:
        if analyzer:
            save_statistics_to_file(analyzer, 'text_analyzer_statistics.txt')
        else:
            print('Nothing to save.')
    elif user_choose == 6:
        delete_all_files()
    elif user_choose == 7:
        print('\nGoodbye!\n')
        break
    else:
        print('Wrong. Do it again.')




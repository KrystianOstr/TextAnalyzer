
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
    # get_input_from_user = input('\nProvide the text to analyze: \n')
    get_input_from_user = 'Świetnie Świetnie Świetnie Świetnie Świetnie, projekt Analizator Tekstu to doskonały wybór. Pozwoli Ci rozwijać umiejętności pracy z tekstem, obsługą plików oraz wykorzystaniem klas i obiektów.'
    return get_input_from_user

def load_from_file(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f'\n{content}\n')

def save_to_file(analyzer, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(analyzer.text)

def save_statistics_to_file(analyzer, filename):
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

while True:
    print('1. Input  the text')
    print('2. Load the text from file')
    print('3. Show statistics')
    print('4. Save the text to file')
    print('5. Save the statistics to file')
    print('6. Exit')

    user_choose = int(input('\nChoose 1 - 5:\n'))

    if user_choose == 1:
        text_to_analyze = get_text_input()
        analyzer = TextAnalyzer(text_to_analyze)
    elif user_choose == 2:
        load_from_file('text_analyzer.txt')
    elif user_choose == 3:
        display_statistics(analyzer)
    elif user_choose == 4:
        save_to_file(analyzer, 'text_analyzer.txt')
    elif user_choose == 5:
        save_statistics_to_file(analyzer, 'text_analyzer_statistics.txt')
    elif user_choose == 6:
        print('\nGoodbye!\n')
        break




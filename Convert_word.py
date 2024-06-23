def main():
    input_file = 'Personal project/Wordle/Word_data.txt'
    output_file = 'Personal project/Wordle/Word_data_converted.txt'
    Five_letter_word = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == 5:
                Five_letter_word.append(word)

    with open(output_file, 'w') as f:
        for word in Five_letter_word:
            f.write(word+ '\n')

    print(len(Five_letter_word))

if __name__ == '__main__':
    main()
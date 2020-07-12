phone_book = {
    "1": [],
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'pqrs',
    "8": 'tuv',
    "9": 'wxyz'
}

output_arr = []


def all_possible_words(digits, output):
    if len(digits) == 0:
        output_arr.append(output)
        return

    for elm in phone_book[digits[0]]:
        all_possible_words(digits[1:], output + elm)


all_possible_words("234", "")
print(output_arr)
# ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']

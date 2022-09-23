text = 'абв  Как хорошо абв летом на море! абв'
def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

text = del_some_words(text)
print(text)
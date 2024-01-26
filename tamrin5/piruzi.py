import re

def remove_persian(text):
    persian_special_chars_pattern = re.compile(r'[،:؛.؟!٬٫]+')
    cleaned_text = persian_special_chars_pattern.sub('', text)
    return cleaned_text

def find_similar_words(n, sentence, target_word):
    sentence = remove_persian(sentence)
    words = sentence.split(" ")
    result = [word for word in words if calc_distance(word, target_word) <= n]
    return result

def calc_distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    if len1 < len2:
        word1 += '_' * (len2 - len1)
    elif len1 > len2:
        word2 += '_' * (len1 - len2)

    distance = sum(ch1 != ch2 for ch1, ch2 in zip(word1, word2))
    return distance

def main():
    k = int(input())
    sentence = input()
    target_word = input()

    result = find_similar_words(k, sentence, target_word)

    for word in result:
        print(word)

if __name__ == "__main__":
    main()

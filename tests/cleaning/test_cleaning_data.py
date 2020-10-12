import pytest

from cleaning.cleaning_data import has_character, remove_pattern, count_words, generate_list, classify_domain

class TestHasCharacter(object):
    def test_with_character(self):
        test_string = "Aegon Targaryen (son of Rhaegar)"
        test_character = "("
        expected = 1
        actual = has_character(test_string, test_character)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    
    def test_without_character(self):
        test_string = "Aegon Targaryen"
        test_character = "("
        expected = 0
        actual = has_character(test_string, test_character)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

class TestRemovePattern(object):
    def test_with_parentheses(self):
        test_string = "Aegon Targaryen (son of Rhaegar)"
        test_pattern = r".*?(\s\(.*?\))"
        expected = "Aegon Targaryen"
        actual = remove_pattern(test_string, test_pattern)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_without_parentheses(self):
        test_string = "Aegon Targaryen"
        test_pattern = r".*?(\s\(.*?\))"
        expected = "Aegon Targaryen"
        actual = remove_pattern(test_string, test_pattern)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

class TestCountWords(object):
    def test_three_words(self):
        test_string = "abc def ghi"
        expected = 3
        actual = count_words(test_string)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_one_words(self):
        test_string = "abc"
        expected = 1
        actual = count_words(test_string)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_trailing_space(self):
        test_string = "abc def ghi "
        expected = 3
        actual = count_words(test_string)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_leading_space(self):
        test_string = " abc"
        expected = 1
        actual = count_words(test_string)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_empty(self):
        test_string = ''
        expected = 0
        actual = count_words(test_string)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"


class TestGenerateList(object):
    def test_count_words(self):
        test_function = count_words
        test_list = ["abc def", "ghi"]
        expected = [2, 1]
        actual = generate_list(test_function, test_list)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_has_character(self):
        test_function = has_character
        test_list = ['abc','ef(','hij']
        test_arg = '('
        expected = [0, 1, 0]
        actual = generate_list(test_function, test_list, test_arg)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_classify_domain(self):
        test_function = classify_domain
        test_list = ["aegon.v.targaryen@goldmansacs.com", "aegor.rivers@gmail.com"]
        test_domain = "professional"
        expected = [1, 0]
        actual = generate_list(test_function, test_list, test_domain)
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

class TestClassifyDomain(object):
    def test_professional(self):
        test_email = "aegon.v.targaryen@goldmansacs.com"
        test_domain = "professional"
        expected = 1
        actual = classify_domain(test_email, test_domain)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_not_professional(self):
        test_email = "aegor.rivers@gmail.com"
        test_domain = "professional"
        expected = 0
        actual = classify_domain(test_email, test_domain)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_junk(self):
        test_email = "anders.yronwood@hotmail.com"
        test_domain = "junk"
        expected = 1
        actual = classify_domain(test_email, test_domain)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def test_personal(self):
        test_email = "aegor.rivers@gmail.com"
        test_domain = "personal"
        expected = 1
        actual = classify_domain(test_email, test_domain)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

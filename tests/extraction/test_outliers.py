import pytest
import pandas as pd

from extraction.outliers import scatter_outliers, scatter, threshold, outliers

class TestThreshold(object):
    def testNoneAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "None".
        monkeypatch.setattr('builtins.input', lambda _: "None")

        expected = ""
        actual = threshold(lower = True)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"
    
    def testNoAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "".
        monkeypatch.setattr('builtins.input', lambda _: "")

        expected = "blank"
        actual = threshold(lower = True)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def testFloatAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "1.2".
        monkeypatch.setattr('builtins.input', lambda _: "1.2")

        expected = 1.2
        actual = threshold(lower = True)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def testIntAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "2".
        monkeypatch.setattr('builtins.input', lambda _: "2")

        expected = 2.0
        actual = threshold(lower = True)
        assert actual == expected, f"Expected: {expected}, Actual {actual}" 

    def testHelloAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "Hello".
        monkeypatch.setattr('builtins.input', lambda _: "Hello")

        expected = "blank"
        actual = threshold(lower = True)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def testUpperNoneAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "None".
        monkeypatch.setattr('builtins.input', lambda _: "None")

        expected = ""
        actual = threshold(lower = False)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"
    
    def testUpperNoAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "".
        monkeypatch.setattr('builtins.input', lambda _: "")

        expected = "blank"
        actual = threshold(lower = False)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def testUpperFloatAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "1.2".
        monkeypatch.setattr('builtins.input', lambda _: "1.2")

        expected = 1.2
        actual = threshold(lower = False)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

    def testUpperIntAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "2".
        monkeypatch.setattr('builtins.input', lambda _: "2")

        expected = 2.0
        actual = threshold(lower = False)
        assert actual == expected, f"Expected: {expected}, Actual {actual}" 

    def testUpperHelloAnswer(self, monkeypatch):
        # monkeypatch the "input" function, so that it returns "Hello".
        monkeypatch.setattr('builtins.input', lambda _: "Hello")

        expected = "blank"
        actual = threshold(lower = False)
        assert actual == expected, f"Expected: {expected}, Actual {actual}"

testDF = pd.DataFrame(
            {
            "col1": [0,1,2,3,4,5,6,7,8,9],
            "col2": [0,1,2,3,4,5,6,7,8,9],
            "col3": [0,1,2,3,4,5,6,7,8,9],
            "col4": [0,1,2,3,4,5,6,7,8,9],
            "col5": [0,1,2,3,4,5,6,7,8,9]
            })
class TestOutliers(object):
    
    def testLower1(self):
        actual = outliers(testDF.copy(), series="col1", min=1.0)
        expected = pd.DataFrame({
            "col1": [0,1,2,3,4,5,6,7,8,9],
            "col2": [0,1,2,3,4,5,6,7,8,9],
            "col3": [0,1,2,3,4,5,6,7,8,9],
            "col4": [0,1,2,3,4,5,6,7,8,9],
            "col5": [0,1,2,3,4,5,6,7,8,9],
            "lower_outlier_col1": [1,1,0,0,0,0,0,0,0,0]
            })
        assert actual.equals(expected), f"Expected: {expected}, Actual {actual}"

    def testUpper5(self):
        actual = outliers(testDF.copy(), series="col5", max=5.0)
        expected = pd.DataFrame({
            "col1": [0,1,2,3,4,5,6,7,8,9],
            "col2": [0,1,2,3,4,5,6,7,8,9],
            "col3": [0,1,2,3,4,5,6,7,8,9],
            "col4": [0,1,2,3,4,5,6,7,8,9],
            "col5": [0,1,2,3,4,5,6,7,8,9],
            "upper_outlier_col5": [0,0,0,0,0,1,1,1,1,1]
            })
        assert actual.equals(expected), f"Expected: {expected}, Actual {actual}"

    def testLower1Upper5(self):
        actual = outliers(testDF.copy(), series="col1", min=1.0, max=5.0)
        expected = pd.DataFrame({
            "col1": [0,1,2,3,4,5,6,7,8,9],
            "col2": [0,1,2,3,4,5,6,7,8,9],
            "col3": [0,1,2,3,4,5,6,7,8,9],
            "col4": [0,1,2,3,4,5,6,7,8,9],
            "col5": [0,1,2,3,4,5,6,7,8,9],
            "lower_outlier_col1": [1,1,0,0,0,0,0,0,0,0],
            "upper_outlier_col1": [0,0,0,0,0,1,1,1,1,1]
            })
        assert actual.equals(expected), f"Expected: {expected}, Actual {actual}"

    def testNoThreshold(self):
        actual = outliers(testDF.copy(), series="col1")
        expected = pd.DataFrame({
            "col1": [0,1,2,3,4,5,6,7,8,9],
            "col2": [0,1,2,3,4,5,6,7,8,9],
            "col3": [0,1,2,3,4,5,6,7,8,9],
            "col4": [0,1,2,3,4,5,6,7,8,9],
            "col5": [0,1,2,3,4,5,6,7,8,9]
            })
        assert actual.equals(expected), f"Expected: {expected}, Actual {actual}"

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union, Tuple

def scatter_outliers(dataset: pd.DataFrame, target: str, x: str, outlierDictionary: dict) -> Tuple[pd.DataFrame, dict]:
    """Take in a dataframe and the name of two series, show a scatterplot of the two,
    and then append a series of outliers to the DataFrame.

    :param dataset: A dataframe to take the series and append the outliers to
    :param target: Name of the target variable
    :param x: Name of the second series to check
    :param outlierDictionary: Dictionary with outlier values

    :return dataset: The dataset with outliers appended
    :return outlierDictionary: Updated Dictionary with new outliers
    """
    print(x)
    scatter(dataset[x], dataset[target])
    minThreshold = threshold(True)
    maxThreshold = threshold(False)
    outlierDictionary[x]['Lower'] = minThreshold
    outlierDictionary[x]['Upper'] = maxThreshold

    dataset = outliers(dataset, series=x, min=minThreshold, max=maxThreshold)
    return dataset, outlierDictionary

def scatter(x: pd.Series, y: pd.Series) -> None:
    """Takes in two series and shows a scatterplot
    
    :param x: The x-axis of the scatterplot
    :param y: The y-axis of the scatterplot
    """
    plt.scatter(x=x,y=y)
    plt.title(label = x.name)
    plt.show()
    return

def threshold(lower: bool) -> Union[float, str]:
    """Takes user input to create thresholds values
    
    :param lower: Boolean if it is the lower threshold or the upper threshold
    
    :return threshold: a float value of the theshold, or a blank string if there is no threshold"""

    if lower == True: thresholdType = "Lower"
    elif lower == False: thresholdType = "Upper"
    else: return "Please use a boolean value"

    threshold = "blank"
    for i in range(3):
        thresholdString = input(f'What is the {thresholdType.upper()} threshold for outliers? Enter None if there is no {thresholdType.upper()} threshold.')
        if thresholdString.lower() == "none": 
            threshold = ""
            break
        else:
            try: 
                threshold = float(thresholdString)
                break
            except:
                print("Please enter a valid value (int, float, or 'None')")
                i += 1
    return threshold


def outliers(dataset: pd.DataFrame, series: str, min='', max='') -> pd.DataFrame:
    """Returns a list of outliers based on min and max thresholds
    
    :param dataset: Dataframe with the series
    :param series: Name of the series to make outlies of
    :param min: lower threshold for outliers
    :param max: upper threshold for outliers
    
    :return dataset: Dataset with outlier flags"""

    if min != '':
        dataset["lower_outlier_"+series] = [1 if value <= min else 0 for value in dataset[series]]

    if max != '':
        dataset["upper_outlier_"+series] = [1 if value >= max else 0 for value in dataset[series]]

    return dataset

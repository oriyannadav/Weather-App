import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit):
    temp_in_celcius = float((float(temp_in_farenheit) - 32) * (5/9))
    temp_in_celcius = round(temp_in_celcius, 1)
    return temp_in_celcius
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass


def calculate_mean(weather_data):
    total = 0
    for temp in weather_data:
        total = total + float(temp)
    number_of_items = len(weather_data)
    mean_value = total / number_of_items
    return mean_value

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    # if len(weather_data) > 0:
    #     min_value = float(min(weather_data))
    #     list_indices = []
    #     list_len = len(weather_data)
    #     sequence = range(list_len)
    #     for index in sequence:
    #         if weather_data[index] == min_value:
    #             list_indices.append(index)
    #     if len(list_indices) > 0:
    #         max_index = max(list_indices)
    #     else:
    #         max_index = weather_data.index(min(weather_data))
    #     return (min_value, max_index)
    # else:
    #     return ()

    weather_data_new = []
    for temp in weather_data:
        weather_data_new.append(float(temp))
    if len(weather_data_new) > 0:
        min_value = float(min(weather_data_new))
        list_indices = []
        list_len = len(weather_data_new)
        sequence = range(list_len)
        for index in sequence:
            if weather_data_new[index] == min_value:
                list_indices.append(index)
        if len(list_indices) > 0:
            max_index = max(list_indices)
        else:
            max_index = weather_data_new.index(min(weather_data_new))
        return (min_value, max_index)
    else:
        return ()


    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    # if len(weather_data) > 0:
    #     max_value = float(max(weather_data))
    #     list_indices = []
    #     list_len = len(weather_data)
    #     sequence = range(list_len)
    #     for index_position in sequence:
    #         if weather_data[index_position] == max_value:
    #             return list_indices.append(index_position)
    #     if len(list_indices) > 0:
    #         max_index = max(list_indices)
    #     else:
    #         max_index = weather_data.index(max(weather_data))
    #     return (max_value, max_index)
    # else:
    #     return ()


    weather_data_new = []
    for temp in weather_data:
        weather_data_new.append(float(temp))
    if len(weather_data_new) > 0:
        max_value = float(max(weather_data_new))
        list_indices = []
        list_len = len(weather_data_new)
        sequence = range(list_len)
        for index in sequence:
            if weather_data_new[index] == max_value:
                list_indices.append(index)
        if len(list_indices) > 0:
            max_index = max(list_indices)
        else:
            max_index = weather_data_new.index(max(weather_data_new))
        return (max_value, max_index)
    else:
        return ()


    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

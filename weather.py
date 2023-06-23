import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    temp = str(temp)
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    import datetime as dt
    date_string = dt.datetime.strptime(iso_string, '%Y-%m-%dT07:00:00+08:00')
    date_object = date_string.strftime("%A %d %B %Y")
    return date_object
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
    with open(csv_file) as file:
        reader = csv.reader(file, delimiter = ",")
        next(reader)
        big_list = []
        for row in reader:
            if row:
                str1 = str(row[0])
                int1 = int(row[1]) 
                int2 = int(row[2])
                small_list = [str1, int1, int2]
                big_list.append(small_list)
        return big_list

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
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
    import datetime as dt
    min_temp = []
    max_temp = []
    days = len(weather_data)
    for summary in weather_data:
        min_temp.append(float(summary[1]))
        lowest_temp = float(min(min_temp))
        lowest_temp_c = float((float(lowest_temp) - 32) * (5/9))
        lowest_temp_c = round(lowest_temp_c, 1)
        if lowest_temp in summary:
            date_string = dt.datetime.strptime(summary[0], '%Y-%m-%dT07:00:00+08:00')
            lowest_temp_date = date_string.strftime("%A %d %B %Y")
        max_temp.append(float(summary[2]))
        highest_temp = float(max(max_temp))
        highest_temp_c = float((float(highest_temp) - 32) * (5/9))
        highest_temp_c = round(highest_temp_c, 1)
        if highest_temp in summary:
            date_string = dt.datetime.strptime(summary[0], '%Y-%m-%dT07:00:00+08:00')
            highest_temp_date = date_string.strftime("%A %d %B %Y")
        min_total = 0
        for temp in min_temp:
            min_total = min_total + float(temp)
        number_of_items = len(min_temp)
        average_lowest_temp = min_total / number_of_items
        average_lowest_temp_c = float((float(average_lowest_temp) - 32) * (5/9))
        average_lowest_temp_c = round(average_lowest_temp_c, 1)
        max_total = 0
        for temp in max_temp:
            max_total = max_total + float(temp)
        number_of_items = len(max_temp)
        average_highest_temp = max_total / number_of_items
        average_highest_temp_c = float((float(average_highest_temp) - 32) * (5/9))
        average_highest_temp_c = round(average_highest_temp_c, 1)
    return f"{days} Day Overview\n  The lowest temperature will be {lowest_temp_c}{DEGREE_SYBMOL}, and will occur on {lowest_temp_date}.\n  The highest temperature will be {highest_temp_c}{DEGREE_SYBMOL}, and will occur on {highest_temp_date}.\n  The average low this week is {average_lowest_temp_c}{DEGREE_SYBMOL}.\n  The average high this week is {average_highest_temp_c}{DEGREE_SYBMOL}.\n"

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    import datetime as dt
    daily_summaries = []
    for daily_summary in weather_data:
        if daily_summary:
            date_string = dt.datetime.strptime(daily_summary[0], '%Y-%m-%dT07:00:00+08:00')
            date = date_string.strftime("%A %d %B %Y")
            low_temp = float(daily_summary[1])
            low_temp_c = float((float(low_temp) - 32) * (5/9))
            low_temp_c = round(low_temp_c, 1)
            high_temp = float(daily_summary[2])
            high_temp_c = float((float(high_temp) - 32) * (5/9))
            high_temp_c = round(high_temp_c, 1)
            daily_summary_str = f"---- {date} ----\n  Minimum Temperature: {low_temp_c}{DEGREE_SYBMOL}\n  Maximum Temperature: {high_temp_c}{DEGREE_SYBMOL}\n\n"
            daily_summaries.append(daily_summary_str)
        else:
            daily_summaries.append("\n")
    return ''.join(daily_summaries)
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

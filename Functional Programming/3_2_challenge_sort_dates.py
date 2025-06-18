def sort_dates(dates):
    return sorted(dates, key=format_date) #creates a new sorted list

def format_date(date):
    month, day, year = date.split("-") # split into three values at the hyphen
    return year + month + day # concatenate back into a single value starting with the year

"""    
The sort_dates function uses Python's built-in sorted() function rather than the .sort() method. The important difference is sorted() creates a new sorted list rather than modifying the original list in place.

The key parameter in sorted(dates, key=format_date) is where the magic happens. This tells Python to use the format_date function to transform each date into a value that can be used for comparison during sorting.
The format_date function:
Takes a date string like "07-21-2023" (in month-day-year format)
Splits it at the hyphens into three parts using split("-")
Returns these parts concatenated in year-month-day order: "20230721"
By rearranging the dates into "YYYYMMDD" format, the dates can be sorted correctly when compared as strings.

How this works:
Python creates a temporary list of tuples, where each tuple contains:
The transformed value (what format_date returns)
The original value (the date string)
For example, with the date "07-21-2023", Python would create: ("20230721", "07-21-2023")
Python sorts this list of tuples based on the first element (the transformed value)
After sorting, Python extracts just the second elements (the original dates) to create the final result
"""
# time calculator
# if you spent this many minutes taking action daily
# at the end of the year, how much time you'll spend.... 1

def calculate_time():
    minutes = int(input("Enter the number of minutes you spend on this habit every day: "))
    total_minutes = minutes * 365
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
    print(f"You have spent a total amount of daily: {hours} hours and {remaining_minutes} minutes.")

calculate_time()

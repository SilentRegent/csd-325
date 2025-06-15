import csv
from datetime import datetime
#adding sys to aid in exiting the program
import sys
from matplotlib import pyplot as plt

#added absolute path was the only way I could get it to run
filename = r'C:\Users\theve\Mod 4.2 Assignment\sitka_weather_2018_simple.csv'


dates, highs, lows = [], [], []
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    for row in reader:
        # added try/except to improve user-friendliness by managing data issues
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            
            high = int(row[5])
            low = int(row[6])
        except ValueError:

            print(f"Missing or invalid data for {row}")
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)
#added define function to apply formatting        
def plot_temps(dates,temps,label,color):
    fig, ax = plt.subplots()
    #changed to plot by temp and not just high temp
    ax.plot(dates, temps, c=color)

# Format plot.
    #added dynamically change graph label based on temperature
    plt.title(f"Daily {label} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
# added intro to program for user
print("Welcome to My Temperature Plotter!")
print("Choose high or low daily temperatures.")
print("Use the provided menu to select an option.\n")



# added While loop to loop program until user chooses to exit
while True:
    print(" Temperature Plotter Menu")
    print("1. View HIGH temperatures")
    print("2. View LOW temperatures")
    print("3. Exit")

    choice = input("Select an option (1-3): ").strip()

    if choice == '1':
        print("Plotting high temperatures...")
        plot_temps(dates, highs, "High", "red")
    elif choice == '2':
        print("Plotting low temperatures...")
        plot_temps(dates,lows, "Low", "blue")
    elif choice == '3':
        print("Exiting program!")
        sys.exit()
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
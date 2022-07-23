import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import missingno as ms

data = pd.read_csv(r'nyc_taxis.csv')


def show_complete_data():
    print(data)  # to print the complete data


def show_brief_data():
    data.info()  # to see the information of data


def show_missing_values():  # use to see if any data has null value
    plt.figure(figsize=(10, 10))
    ms.bar(data)
    plt.show()


def show_pickups_in_hours():
    category = pd.crosstab(index=data['pickup_time'], columns='Count of PickUps as per Time')
    category.plot(kind='bar', color='b', alpha=0.8)
    plt.show()


def show_most_drop_location():
    plt.figure(figsize=(15, 15))
    pd.Series(data['dropoff_location_code']).value_counts()[:25].plot(kind="pie")
    plt.title("Cab Rides Ends at")
    plt.xticks(rotation=70)
    plt.show()


def show_total_amount():
    a = sb.catplot(x='trip_length', y='total_amount', hue='mode', data=data,
                   height=15, kind='bar', palette='muted')
    a.fig.suptitle('total amount paid on trip length in different mode', fontsize=15)
    a.fig.set_size_inches(15, 15)
    a.set_xlabels('trip_length', fontsize=20)
    a.set_ylabels('total_amount', fontsize=20)
    plt.show()


def show_mean_trip_length():
    plt.figure(figsize=(12, 7))
    sb.countplot(data['trip_length'], order=data['trip_length'].value_counts().index, palette='deep')
    plt.axhline(data['trip_length'].value_counts().mean(), linestyle='dotted', color='blue',
                label='Means trip Length across month')
    plt.show()


choice = 0
while (choice < 8):
    print("\n\n\n<!----------Welcome To Mini Project (Data Analysis)----------!>")
    print("\n\t\t\t#----------by Yagya Solanki----------#")
    print("\n\nChoose any option:")

    print("\n1. Show Data \t2. Show Brief Data\t3. Check Null Value")
    print("\n4. Pickup in hours\t5. Show Most drop location")
    print("\n6. Show Total Amount\t7. Show Mean Trip Length\n")

    choice = int(input("Enter Your Choice: "))
    if (choice == 1):
        show_complete_data()
    elif (choice == 2):
        show_brief_data()
    elif(choice == 3):
        show_missing_values()
    elif(choice == 4):
        show_pickups_in_hours()
    elif(choice == 5):
        show_most_drop_location()
    elif(choice == 6):
        show_total_amount()
    elif(choice == 7):
        show_mean_trip_length()
    else:
        print("Sorry, I can't help You Right Now")

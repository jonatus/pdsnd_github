import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


Cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    print('\nHello! Let\'s explore some US bikeshare data!')

    while True :
        city =input('\nchoose from chicago, new york city or washington to filter\n').lower()
        if city in Cities:
            break
        else:
            print('\nWrong city selected, Select from the cities above, thank you')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month do you want to filter? january, february,..., june\n').lower()
        if month in months:
            break
        else:
            print('\nIncorrect selection of month, Select from the months above, thank you')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day do you want to explore?. enter number for day like 1.sunday, 2. monday,..,7.saturday.\n')



    show = [0]
    start_loc = 0
    df = pd.DataFrame()
    view = input("Do you want to filter the first 7 rows of stats, if yes then  select 1 for YES, 0 for NO or None to exit\n")

    while True:
        if view not in show:
            result = df.iloc[0:7]
            print(f"\nThe first 7 filtered rows are {result} ")
            start_loc =+ 7

            nue_filtering = input("Do yo want to continue filtering another 7 rows\n").lower()
            break






    print("Thank you for your response, see you later. Goodbye")
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])          # load data file into a dataframe

    df['Start Time'] = pd.to_datetime(df['Start Time'])         # convert the Start Time column to datetime



    df['month'] = df['Start Time'].dt.month             # extract month and day of week and hour from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':      # filter by month if applicable
        month = months.index(month) + 1
        df = df[ df['month'] == month ]


     # filter by day of week if applicable
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]       # filter by day of week to create the new dataframe

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print(f"\nThe most common month form a particlar city bikeshare data is: {most_common_month}")


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print(f"\nThe most common month in the selected city bikeshare data is: {most_common_day_of_week}")


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print(f"\nThe most common hour in  the choosen city bikeshare data is: {most_common_start_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nwhat is the most common used start station?')
    most_start_station =  df['Start Station'].value_counts().idxmax()
    print(f"\nThe most common station used as starting point for many users is: {most_start_station}")


    # display most commonly used end station
    print('\nIs there a particular station that frequently ends motivate bikeshare activities in a day?')
    most_end_station =  df['End Station'].value_counts().idxmax()
    print(f"\nFrequent ending station of motivate bikeshare for many users is: {most_end_station}")


    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].value_counts().idxmax()
    print(f"\nThe most commonly used start station and end station: {most_common_start_end_station}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # display total travel time
    total_travel_time = df['Total Duration'].sum()
    minute, second = divmod(total_travel_time, 60)     #Finds out the duration in minutes and seconds format
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 360)
    #Finds out the duration in hour and minutes format
    print(f"The total_travel_time is {year} years, {day} days, {hour} hours, {minute} minutes and {second} seconds.")


    # display mean travel time
    print('what is the average Travel time from a city selected')
    print('The mean travel time is: ',df(total_travel_time).mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('what are the type of users in the bikeshare')
    User_type = df['User Type'].value_counts()
    for index, user_type in enumerate(user_type):
        print("  {}: {}".format(user_counts.index[index], user_type))




    # Display counts of gender
    print('what types gender use motivatebikeshare')
    gender_type = df['Gender'].value_counts()
    for index,gender_type   in enumerate(gender_type):
        print("  {}: {}".format(gender_counts.index[index], gender_type))

    # Display earliest, most recent, and most common year of birth
    most_earliest_year_of_birth = int(df['Birth Year']).min()
    print('The most earliest year of birth is: ', most_earliest_year_of_birth)

    most_recent_year_of_birth = int(df['Birth Year']).max()
    print('The most recent year of birth from motivate bikeshare is: ',most_recent_year_of_birth)

    Most_common_year_of_birth =int(df['Birth Year']).value_counts().idxmax()
    print('The Most common year of birth from motivate bikeshare is: ', Most_common_year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

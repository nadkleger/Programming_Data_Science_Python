import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select one city to explore the data of bike share. ' +
                     'Chicago, New York City, Washington?\n')
        if city.lower() in CITY.DATA.keys():
            break
        else:
            print("\nTry again with a new city!")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True: 
        month = input('n\Which month do you want to choose from: All, January ' +
                      'February, March, April, May, June\n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april',
                             'may', 'june']:
            break
        else:
            print("\nTry again with a new month!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\Which weekday do you want to use to filter data?' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', +
                           'friday', 'saturday', 'sunday\n')
             break
        else:
            print("\nTry again with a new day!")

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nMost common month of travel:')
    print(df['month']mode()[0]
             
    # TO DO: display the most common day of week
    print('\nMost common week day of travel:')
    print(df['day_of_week']mode()[0]

    # TO DO: display the most common start hour
    print('\nMost common start hour of travel:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("The most common start station with this filter is: " +
          most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = str(df['End Station'].mode()[0])
    print("The most common end station with this filter is: " +
          most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent Start and End Combination')
    print(df.groupby(['Start Station', 'End Station']).size()nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time:')
    print)datetime.timedelta(seconds=int/df['Trip Duration'].sum())))


    # TO DO: display mean travel time
    print('\nMean Travel Time:')
    print)datetime.timedelta(seconds=int/df['Trip Duration'].mean())))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value.counts().to_string()
    print("User type distribution:")
    print(user_types)                       

    # TO DO: Display counts of gender
    print('\nCounts of Gender:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include gender')                       


    # TO DO: Display earliest, most recent, and most common year of birth
    try: 
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nThe oldest person riding a bike with this filter "
              "was born in: " + earliest_birth_year)
                           
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("\nThe youngest person riding a bike with this filter +
              "was born in: " + most_recent_birth_year)
                           
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("\nThe most common birth year amongst the bikers "
              "with this filter is: " + most_common_birth_year)
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                           
def raw_data(df):
    """Display 5 lines of data entries
    
    Return: 
        Print five data entry rows"""
                           
    show_more = 'YES'
    while show_more == 'YES':
        for i in df.iterrows():
               count = 0
               while count < 5:
                    print(i)      
                    count += 1
               response = input('\nDo you want to keep seeing 5 more data entries? YES or NO?\n')
               if response.lower() == 'no':
                    show_more = 'no'
                    break       

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

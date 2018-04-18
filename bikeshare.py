import time
import pandas as pd
import numpy as np
import datetime
import glob
global city
global month
global day
global df
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """


    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Which city would you like to analyze?').lower()
        if city in ('chicago', 'new york city', 'washington', 'all'):
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to analyze?').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all'):
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to analyze?').lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break

    print('-'*40)
    return city, month, day


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


    df = pd.DataFrame()
    if city == "new york city":
        df = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/new_york_city.csv")

    elif city == "chicago":
        df = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/chicago.csv")

    elif city == "washington":
        df = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/washington.csv")

    elif city == "all":
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/new_york_city.csv")
        df1 = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/chicago.csv")
        df2 = pd.read_csv("C:/Users/yappa/OneDrive/Udacity/DataAnalyst/Project 2/Udacity/washington.csv")
        df.append(df1)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day'] = df['Start Time'].dt.strftime('%A')
    df['Hour'] = df['Start Time'].dt.strftime('%I %p')
    df['Trip'] = df[['Start Station', 'End Station']].apply(lambda x: ' - '.join(x), axis =1)
    if month == "all":
        df = df
    else:
        df = df[df['Month'] == month.title()]

    if day == "all":
        df = df
    else:
        df = df[df['Day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month

    common_month = df['Month'].mode()
    print("The usage month with the highest frequency is {}.".format(common_month))

    # display the most common day of week

    common_day = df['Day'].mode()
    print("The day with the highest frequency is {}.".format(common_day))

    # display the most common start hour
    common_hour = df['Hour'].mode()
    print("The hour with the highest frequency is {}.".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()
    print("Most trips commenced from {}.".format(common_start))

    # display most commonly used end station
    common_end = df['End Station'].mode()
    print("Most trips ended at {}.".format(common_end))

    # display most frequent combination of start station and end station trip
    common_trip = df['Trip'].mode()
    print("The most common journey was between {}.".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print ("Total travel time was {} minutes.".format(total_travel))
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print ("Mean travel time was {} minutes.".format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User by type:")
    df['User Type'].value_counts()

    # Display counts of gender
    print("Users by gender:")
    df['Gender'].value_counts()

    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].unique()
    earliest = min(birth_year)
    recent = max(birth_year)
    common_year = df['Birth Year'].mode()
    print("The oldest user was born in {}.".format(earliest))
    print("The youngest user was born in {}".format(recent))
    print("Most users were born in {}".format(common_year))
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

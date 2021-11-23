import time 
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago' : 'chicago.csv',
              'new york' : 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january' , 'february', 'march' ,'april' , 'may' , 'june']

Days = ['monday' , 'tuesday' , 'wendesday' , 'thurasday' , 'friday' , 'saturday' , 'sunday']

Cities = ['chicago' , 'new york' , 'washington']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    for city in Cities :
        print(" ",city , end ="  /n")
        
    while True:
        city = input("which city would you like to explore  :  ").lower()
        
        if city not in Cities :
            print ("sorry your option not inculded in city list , try again!")
 
        else :
            break
           
    # get user input for month (all, january, february, ... , june)
    for month in Months :
        print(" ",month , end ="  /n")
    
    while True: 
        month = input("which month would you like to explore or type all to display months from junuary to june : ").lower()
        if month != "all" and month not in Months :
             print ("sorry your option is not included ,try again")  
        else :
             break
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    for day in Days :
        print(" ",day, end ="  /")
    
    while True: 
        day = input("which day would you like to explore or type all to display all days of week : ").lower()
        if day != "all" and day not in Days :
            print ("sorry your option is not included ,try again")
        else :
            break                  
                      
    print('-'*40)
    return city, month, day

def load_data(city, month, day) :
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """""
    #to read datafram import pandas 
       
    df = pd.read_csv(CITY_DATA[city])
    
    #convert time column from string type to datetime 
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    #to extract months from start time
    
    df["month"] = df["Start Time"].dt.month

    #to extract day name from start time
    df["day_of_week"] = df['Start Time'].dt.weekday_name
    
    #to extract hour from timedata and make separate column for hour
    df["hour"] = df["Start Time"].dt.hour
    
   
    # make sure not to use zeroindex 
   
    if month != 'all':
        month = Months.index(month)+1
        df = df[df["month"] == month]
    
     
    if day != 'all':

       df = df[df["day_of_week"] == day.title()]
   
       
    return df
    print("_"*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nElapsed time...\n')    
    start_time = time.time()
   
    
    # display the most common month

    most_common_month = df["month"].mode()[0]
    print("the most common month is :  {} ".format(most_common_month))


    # display the most common day of week
    most_common_day = df["day_of_week" ].mode()[0]
    print("the most common month is :  {}".format(most_common_day))

    # display the most common start hour

    most_common_hour = df["hour"].mode()[0]
    print("the most common month is : {} ".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start = df["Start Station"].mode()[0]
    print("the most commonly used as start station is : {} " .format(most_common_start))
    # display most commonly used end station

    most_common_end = df["End Station"].mode()[0]
    print("the most commonly used as end station is : {}" .format(most_common_end))
    # display most frequent combination of start station and end station trip
    df["station_combined"] = df["Start Station"] + df["End Station"]
    most_common_station = df["station_combined"].mode()[0]
    print("the most commonly used as end and start station is : {} " .format(most_common_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    total_travel = df["Trip Duration"].sum() 
    d=total_travel/(3600*24)
    h=total_travel/3600
    m=total_travel/60
    
    print(f'Total time travel:  {str(d)}+day(s)b+{str(h)}+ hour(s) +{str(m)}+ minute(s)')





    # display mean travel time
    total_travel = df["Trip Duration"].mean() 
    d=total_travel/(3600*24)
    h=total_travel/3600
    m=total_travel/60
    
    print("Total time travel: "+ str(d)+"day(s)b"+str(h)+ "hour(s) "+str(m)+ "minute(s).")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df["User Type"].value_counts()
    print("user type count is :{}".format(user_counts) )


    # Display counts of gender
    if input == 'washington' or input =="new york" :
        try :
            gender_count = df["Gender"].value_counts()
            print("number of gender :  {}".format(gender_count) )
        except KeyError :
            print("sorry no information about this ")   
            
    # Display earliest, most recent, and most common year of birth
    # to earliest year of birth 
    while input == ("chicago" , "new_york") :
        try : 
            earliest_year= df["Birth Year"].min()
            print("The most earliest birth year:{}" . format(earliest_year))
            most_recent = df["Birth Year"] .max()
            print("The most recent birth year:{}".format(most_recent))
            common_year =df["Birth Year"].value_counts().idxmax()
            print("The most common birth year: {}".format(common_year))
        except KeyError :
            print ("sorry this information not available ")
        else :
            break
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df) :
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    while True :
        print(df.iloc[0:5])
        if input != "yes" :
            break
    
    print('-'*40)                  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
                      

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)           

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
                          break
if __name__ == "__main__":
    main()


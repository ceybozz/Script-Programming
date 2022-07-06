import numpy, csv, pandas, matplotlib.pyplot, seaborn
from numpy import float64, multiply, percentile, row_stack
from glob import glob
from pandas.io.parsers import read_csv

def program():
    def button():
        button = 0
        while button !=10:
            button = menu()
            if button == 1: # Button 1 
                drop_rows_csv()
            if button == 2: # Button 2 
                read_csv()
            if button == 3: # Button 3
                new_colum_csv()
            if button == 4: # Button 4
                multiple_csv()
            if button == 5: # Button 5
                rename_colum_csv()
            if button == 6: # Button 6
                drop_null_csv()
            if button == 7: # Button 6
                number_summary_csv()
            if button == 8: # Button 6
                outliers()
            if button == 9: # Button 6
                scatter()
            if button == 10: # Button 6
                print('Program has ended!')
                quit()

    def menu():   # Meny
        print('\n*******************************************************')
        print('--------------- Welcome to the CSV-Meny ---------------')
        print('*******************************************************\n')
        print('1. Dropp columns')
        print('2. Basic overview')
        print('3. Qualitative data to quantitative data')
        print('4. Joining/Merging multiple CSV:s together to create DataFrame') 
        print('5. Renaming columns.')
        print('6. Dropping missing/NaN or null values')
        print('7. Number summary')
        print('8. Dropp duplicate rows')
        print('9. Plot different features')
        print('10. End program')
        print('*******************************************************\n')

        button = int(input('Please choose a number between 1 - 10: '))   # Enter number (int)
        while button < 1 or button > 10:
            button = int(input('Number must be between 1 - 10.\nPlease try again: '))
        return button

    def drop_rows_csv():    # Button 1
        print('The the dropped rows are:')
        print('Engine Fuel Type, Engine Cylinders, Engine Cylinders, Market Category, Driven_Wheels, Number of Doors,',
        'Transmission Type, Vehicle Size, Vehicle Style, highway MPG, city mpg')

    def read_csv(): # Button 2
        print('Shows the 5 first rows...')
        print(drop_null_CSV.head())
        print('Shows the 5 last rows...')
        print(drop_null_CSV.tail())
        print('Shows amout of rows and colums...')
        print(drop_null_CSV.shape)
        print('Shows count, mean, std, min, 25%, 50%, 75%, max...')
        print(drop_null_CSV.describe())
        button()

    def new_colum_csv():    # Button 3
        print('\nThe new column is ID and it transform/convert from qualitative data to quantitative data...(Brand)')
        print(drop_rows_CSV)

    def multiple_csv(): # Button 4
        print('Added colum is ID')
        print('\nDropping duplicate rows...')
        print(drop_dup_CSV)
        multiply_CSV =  pandas.concat((pandas.read_csv(file).assign(filename=file)
                        for file in sorted_CSV), ignore_index=True)
        print('\nJoining/Merging/concatenating multiple CSV:s together to create a new DataFrame...')
        print(multiply_CSV)

    def rename_colum_csv(): # Button 5
        print('The renamed names are: \nMake --> Brand \nMSRP --> Price')

    def drop_null_csv():    # Button 6
        print('\nDropping missing/NaN/null values...')
        print(drop_null_CSV)
        button()
    
    def number_summary_csv():   # Button 7
        year = drop_null_CSV['Year']
        price = drop_null_CSV['Price']

        # Count
        print('\nCount')
        print(f'Year:', year.count().tolist(),
                '| Price:', price.count().tolist())
        # Mean
        print('\nMean')
        print(f'Year:', round(year.mean().tolist()),
                '| Price:', round(price.mean().tolist(),2))
        # Std
        print('\nStd')
        print(f'Year:', year.median().tolist(),
                '| Price:', price.median().tolist())
        #Min
        print('\nMin')
        print(f'Year:', numpy.percentile(year, 0),
                '| Price:', numpy.percentile(price, 0))
        #25%
        print('\n25% quartile')
        print(f'Year:', numpy.percentile(year, 25),
                '| Price:', numpy.percentile(price, 25))
        #50%
        print('\n50% quartile')
        print(f'Year:', numpy.percentile(year, 50),
                '| Price:', numpy.percentile(price, 50))
        #75%
        print('\n75% quartile')
        print(f'Year:', numpy.percentile(year, 75),
                '| Price:', numpy.percentile(price, 75))
        #Max
        print('\nMax')
        print(f'Year:', numpy.percentile(year, 100),
                '| Price:', numpy.percentile(price, 100))
    
    def outliers(): # Button 8
        print('Remove all cars from year', round(max_thresold), 'and up.')
        print('Remove all cars from year', round(min_thresold), 'and down.')
        print(df0)

    def scatter(): #Button 9
        sorted_np = filterd_CSV.sort_values(by='Price', ascending=False)
        print(sorted_np)
        engine_hp_data = filterd_CSV['Engine HP']
        price_data = filterd_CSV['Price']

        # Scatter
        matplotlib.pyplot.scatter(engine_hp_data, price_data)
        matplotlib.pyplot.ylabel('Price')
        matplotlib.pyplot.xlabel('Engine HP')
        matplotlib.pyplot.title('Scatter for Engine HP and Price')
        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.show()

        # Histogram
        matplotlib.pyplot.hist(engine_hp_data, bins=7, edgecolor='black', log=True)
        matplotlib.pyplot.title('Histogram for Engine HP and Price')
        matplotlib.pyplot.xlabel('Engine HP')
        matplotlib.pyplot.ylabel('Price')
        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.show()

        # Heatmap
        matplotlib.pyplot.figure(figsize=(10,5))
        c = filterd_CSV.corr()
        seaborn.heatmap(c, cmap='BrBG', annot=True)
        matplotlib.pyplot.title('Heatmap Engine HP and Price')
        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.show()
    button()

# READ CSV
original_CSV = pandas.read_csv('cars_data.csv')
# REMOVE COLIMS
drop_rows_CSV = original_CSV.drop(['Engine Fuel Type', 'Engine Cylinders', 'Market Category', 
                                    'Driven_Wheels', 'Number of Doors', 'Transmission Type', 
                                    'Vehicle Size', 'Vehicle Style', 'highway MPG', 'city mpg', 
                                    'Popularity'], axis=1)
# RENAME
drop_rows_CSV.rename(columns={'Make' : 'Brand', 'MSRP' : 'Price'}, inplace = True)   # Changing index colum, "rename"-method
# ADD COLUM/TRANSFORM FROM QUALITATIVETO QUANTITATIVE
drop_rows_CSV['ID'] = pandas.factorize(drop_rows_CSV.Brand)[0]
# DATAFRAME
dataframe_CSV = pandas.DataFrame(drop_rows_CSV)
# DROP DUB
drop_dup_CSV = dataframe_CSV.drop_duplicates()
#DROP NULL
drop_null_CSV = drop_dup_CSV.dropna()
# MULTIPLE CSV CREATE DATAFRAME
sorted_CSV = sorted(glob('cars_dat*.csv'))
# OUTLIERS DETECTION AND REMOVAL, WITH PERCENTILE
max_thresold = drop_null_CSV['Year'].quantile(0.95)
min_thresold = drop_null_CSV['Year'].quantile(0.05)
df0 = drop_null_CSV[(drop_null_CSV['Year']<max_thresold) & (drop_null_CSV['Year']>min_thresold)]
# GROUP BY
group_by_CSV = drop_null_CSV.groupby('Brand')
filterd_CSV = group_by_CSV[['Model', 'Price','Engine HP']].max()
filterd_CSV.to_csv('cars_data_copy_2.csv')

program()
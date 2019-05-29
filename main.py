import csv
import pandas
import matplotlib.pyplot as plt


# filename = 'KSI.csv'
def get_column_names():
    raise NotImplementedError


def load_data(filename='KSI.csv'):
    """loads the data set"""
    d = []
    with open(filename) as csv_file:
        # csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line_count, row in enumerate(csv_reader):
            if line_count == 0:
                print(f'Column names are \n{", ".join(row)}')
                # column_names = row
            else:
                d.append(row)
    # print(f'Processed {line_count} lines.')
    return d


def get_accidents_by_hour(d, year=2017):
    """Gets the accidents per hour from the data set and writes it to a csv file"""
    years = {}
    # accidents_by_hour = {}
    for row in d:
        time_of_accident = row['Hour']
        year = row['YEAR']
        hour = time_of_accident
        if year not in years:
            years[year] = {}
        years[year][hour] = years[year].get(hour, 0) + 1
        # time_interval = time_of_accident[:2]+'00'
        # accidents_by_hour[hour] = accidents_by_hour.get(hour, 0) + 1
        # accidents_by_hour
        # [time_interval] = accidents_by_hour
        # .get(time_interval, 0) + 1

    # with open('hourly accidents.csv', 'w') as f:
    #     f.write('HOUR,ACCIDENTS\n')
    #     for hour, number in accidents_by_hour:
    #         f.write(f'{hour},{number}\n')
    years = sorted(years.items(), key=lambda u: u[0])
    # for year in years:
    #     for hour, accidents in sorted(year[1].items(), key=lambda x: int(x[0])):
    #             print(hour, accidents)
    a = [0 for _ in range(24)]
    for year in years:
        for x in year[1].items():
            a[int(x[0])] += x[1]

    with open('accidents_by_hour.csv', 'w') as f:
        f.write('YEAR,')
        for i in range(24):
            if i != 0:
                f.write(',')
            f.write(str(i))
        f.write('\n')
        for year in years:
            f.write(year[0])
            for hour, accidents in sorted(year[1].items(), key=lambda u: int(u[0])):
                f.write(',')
                f.write(str(accidents))
            f.write('\n')
    # with open('single_var.csv', 'w') as f:
    #     f.write('HOUR,ACCIDENTS\n')
    #     for i, n in enumerate(a):
    #         f.write(f'{i},{n}\n')


def output_to_csv(filename, d, column_names):
    with open(filename, 'w') as f:
        for i, name in enumerate(column_names):
            if i != 0:
                f.write(',')
            f.write(name)
        f.write('\n')
        for row in d:
            for i, item in enumerate(row):
                if i != 0:
                    f.write(',')
                f.write(str(item))
            f.write('\n')


def visualizations():
    """
    Visualizations were just immensely easier to do in google sheets. See excel sheet, or report, or presentation.
    :return:
    """
    raise NotImplementedError
    # df = pandas.read_csv('accidents_by_hour.csv', index_col=0, header=0)
    # plt.plot(0, 0, data=df)
    # plt.show()


data = load_data()
get_accidents_by_hour(data)
print('Visualizations were just immensely easier to do in google sheets. See excel sheet, or report, or presentation.')
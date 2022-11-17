import csv

all_input_list = []
speed_list = []


class UserInput:

    def append_to_list(time_dist_list):
        if len(all_input_list) < 10:
            if len(time_dist_list) == 2:
                all_input_list.append(time_dist_list)
        else:
            print("List crossed the limit")
        return (all_input_list)


class Measure:
    def measure_speed():

        for x, y in all_input_list:
            speed = x/y
            speed_list.append([x, y, speed])
        return speed_list


class DataSet:
    def save_input():
        distance = float(input("Enter Distance in Km:"))
        time = float(input("Enter Time in hrs:"))
        input_list = [distance, time]
        UserInput.append_to_list(input_list)


class showResults:
    def makeresult(speedlist_updated):
        header = ['Distance in Km', 'Time in hrs', 'Speed in Km/h']
        with open('C:/Users/Nandhini/Documents/speed.csv', 'w', encoding='UTF8')as f:
            # create the csv writer
            writer = csv.writer(f)
        # write a row to the csv file
            writer.writerow(header)
            for x in speedlist_updated:
                writer.writerow(x)


class main():
    DataSet.save_input()
    DataSet.save_input()
    speedlist_updated = Measure.measure_speed()
    showResults.makeresult(speedlist_updated)

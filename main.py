import csv
import datetime
from pprint import pprint

class A:    

  def create_csv_list(self, argument2, filename=False):
    if not filename:
      filename = testOutput + '.csv'
    self.point_counter = 0
    self.csv_header = ['header1', 'header2', 'header3']

    self.write_csv(csv_list=output, filename=filename)

  def write_csv(self, csv_columns=None, csv_list=None, filename=None):
    with open(filename, 'w+', encoding='UTF8', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(self.csv_header)
      writer.writerows(csv_list)

  def main():

    data_files = ['SalesJan2009.csv']

    work_obj = WorkData(file_list=data_files)

    work_obj.create_csv_list(filename='test.csv')

    blah = work_obj.connect_stuff()

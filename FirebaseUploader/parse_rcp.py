__author__ = 'EliFinkelshteyn'
import csv
rcp_file = open('../Data/realclearpolitics.txt')
csv_output = open('../Data/realclearpolitics.csv', 'w')
with open('../Data/realclearpolitics.csv', 'w') as csv_output:
    csv_writer = csv.writer(csv_output, delimiter=',', quotechar='"')
    line_list = []
    for counter, item in enumerate(rcp_file.readlines()):
        print item
        line_list.append(item.rstrip())
        print line_list
        if (counter + 1) % 7 == 0:
            csv_writer.writerow(line_list)
            line_list = []



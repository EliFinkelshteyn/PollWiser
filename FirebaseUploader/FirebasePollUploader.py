__author__ = 'EliFinkelshteyn'
from firebase import Firebase
import simplejson as json
import csv, argparse, re, datetime
parser = argparse.ArgumentParser(description='Upload some polling data.')
parser.add_argument('--data_type', dest='data_type', action='store',\
    help='what you want to upload', type=str)
#parser.add_argument('--output-dir', dest='output_dir', action='store',\
#    help='directory you\'d like to save to', type=str)
args = parser.parse_args()
if args.data_type == 'approval':
    data_file = '../Data/approval.csv'
    schema = ['Date',"% Approve","% Disapprove"]
if args.data_type == 'electoral_vote':
    data_file = '../Data/electoral_vote.csv'
    schema = ['Day','Len','State','EV','Dem','GOP','Ind','Date','','','','',
              '','','','Pollster']
if args.data_type == 'rcp1':
    data_file = '../Data/realclearpolitics.csv'
    schema = ['Poll',"Date","Sample","MoE","Obama","Romney","Spread"]
f = Firebase("http://demo.firebase.com/seifeet/%s" % args.data_type)

def generate_dates(start_date, end_date):
    td = datetime.timedelta(hours=24)
    current_date = start_date
    dates = []
    while current_date <= end_date:
        current_date += td
        dates.append(current_date)
    return dates

def getDates(date_range):
    dates = re.findall('\d+/\d+ - \d+/\d+',date_range)
    dates = dates[0].split(' - ')
    new_dates = []
    for date in dates:
        date +='/2012'
        new_dates.append(datetime.datetime.strptime(date, '%m/%d/%Y'))
    dates = generate_dates(new_dates[0], new_dates[1])
    new_dates = []
    for date in dates:
        new_dates.append(date.strftime('%s'))
    return new_dates

with open(data_file, 'rb') as polls_csv:
    polls_reader = csv.reader(polls_csv, delimiter=',')
    for row in polls_reader:
        row_dict = {}
        for counter, item in enumerate(row):
            row_dict[schema[counter]] = item
        dates = getDates(row_dict['Date'])
        for date in dates:
            row_dict['Date'] = date
            print row_dict
            print 'about to push!'
            f.push(row_dict)
            print 'done!'


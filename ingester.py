"""
Push new data to sqlite database.
"""
import dateutil.parser
import datetime

from peewee import *

from models import File, Contribution

from app import db

def parse_fec_file(infile):
    with open(infile) as f:
        res = [parse_line(line) for line in f]
        return [line_to_dict(val) for val in res]

def parse_line(l):
    vals = l.split('|')
    vals = map(lambda x: None if x=='' else x,vals)
    int_cols = [18-1,21-1] #file num and sub id
    for i in int_cols:
        if vals[i] is not None:
            vals[i] = int(vals[i])
    float_cols = [15-1] #transaction amount
    for i in float_cols:
        if vals[i] is not None:
            vals[i] = float(vals[i])
    date_cols = [14-1] #date
    for i in date_cols:
        vl = vals[i]
        if vl is not None:
            vals[i] = datetime.datetime(month=int(vl[0:2]), day=int(vl[2:4]), year=int(vl[4:8]))
    return vals

def row_to_dict(row):
    return {
        "comittee_id" : row[0],
        "ammendment_id" : row[1],
        "report_type" : row[2],
        "transaction_pgi" : row[3],
        "image_num" : row[4],
        "transaction_tp" : row[5],
        "entity_tp" : row[6],
        "name" : row[7],
        "city" : row[8],
        "state" : row[9],
        "zip_code" : row[10],
        "employer" : row[11],
        "occupation" : row[12],
        "transaction_date" : row[13],
        "transaction_amount" : str(row[14]),
        "other_id" : row[15],
        "transaction_id" : row[16],
        "file_num" : row[17],
        "memo_cd" : row[18],
        "memo_text" : row[19],
        "sub_id" : row[20]
    }

def ingested(filepath):
    '''Return true if file is already ingested, false otherwise'''
    # TODO: implement better (just checks if file in table right now)
    try:
        myfile = File.get(name=filepath)
        print "%s already in database." % filepath
        return True
    except:
        return False

def ingest(filepath):
    '''Ingest file into database'''

    print "Ingesting %s" % filepath
    rows_in_file = parse_fec_file(filepath)
    myfile = File.get_or_create(name=filepath)
    myfile_id = myfile.id

    with db.transaction(): # TODO: More sane error handling
        for idx in range(0, len(rows_in_file), 500):

            # Ingest 500 rows at a time
            print "Inserting row %d of %s" % (idx, filepath)
            rows_subset = rows_in_file[idx:idx+500]
            rows_to_insert = []

            for row in rows_subset:
                unsaved_new_contribution = Contribution(**row_to_dict(row))
                import pdb; pdb.set_trace()
                # If the row isn't already there, insert it
                if :
                    pass
                # If the row is there, check for modifications
                elif:
                    # If it has not been modified, simply add a ContributionHistory object
                    if:
                    # If it has been modified, create a new object and give the new object a contribution history
                    else:
                        pass

            Contribution.insert_many(rows_subset).execute()

if __name__ == '__main__':
    filepaths = [
        "data/FEC 2014 2.17.2014/itcont.txt",
        "data/FEC 2014 3.22.2015/itcont.txt",
        "data/FEC 2014 9.14.2014/itcont.txt"
    ]

    for filepath in filepaths:
        if not ingested(filepath):
            ingest(filepath)
   

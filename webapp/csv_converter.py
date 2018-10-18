'''
    Paul Butterfield and Conor Gormally
    Script for converting csv to format that is usable for our api
'''

import sys
import csv
import re

def load_industries_from_codes(tsv_file_name):
    tsv_file = open(tsv_file_name, encoding='utf-8')
    reader = csv.reader(tsv_file, delimiter = '\t')

    industries = []
    for row in reader:
        if(row[0] != 'Catcode'):
            assert len(row) == 6
            industry_id = row[0]
            industry_name = row[1]
            industry = {'industry_id': industry_id, 'industry_name': industry_name}
            industries.append(industry)
    csv_file.close()
    return industries

def load_pacs_from_csv(csv_file_name):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    pacs = []
    for row in reader:
        assert len(row) == 14
        id = depipe(row[1])
        name = depipe(row[2])
        party = depipe(row[8])
        industry_id = depipe(row[9])
        sensitive = depipe(row[11]) in ['Y', 'y']
        foreign = bool(depipe(row[12]))
        pac = {'id': id, 'name': name, 'pary':party, 'industry_id': industry_id, 'sensitive': sensitive, 'foreign': foreign}
        pacs.append(pac)
    csv_file.close()
    return pacs

def load_candidates_from_csv(csv_file_name):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    candidates = []
    for row in reader:
        assert len(row) == 12
        id = depipe(row[1])
        lastname_firstname_party = depipe(row[3])
        name_party_list = lastname_firstname_party.split(' ')
        party = depipe(name_party_list[-1])
        last_name = name_party_list[-2]
        first_name = name_party_list[:-2] 
        industry_id = depipe(row[9])
        sensitive = depipe(row[11]) in ['Y', 'y']
        foreign = bool(depipe(row[12]))
        pac = {'id': id, 'name': name, 'pary':party, 'industry_id': industry_id, 'sensitive': sensitive, 'foreign': foreign}
        pacs.append(pac)
    csv_file.close()
    return candidates

def depipe(piped_string):
    return piped_string[1:-1]

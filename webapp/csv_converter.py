'''
    Paul Butterfield and Conor Gormally
    Script for converting csv to format that is usable for our api
'''

import sys
import csv
import re

def creat_transactions():
    return transactions[]

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
        pac = {'id': id, 'name': name, 'party':party, 'industry_id': industry_id, 'sensitive': sensitive, 'foreign': foreign}
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
        state = depipe(row[5])[0:1]
        seat = depipe(row[5])[2:3]
        candidate = {'id': id, 'first_name': first_name, 'last_name': last_name, 'party':party,
                     'state': state, 'seat': seat}
        candidates.append(candidate)
    csv_file.close()
    return candidates

def load_individuals_and_individual_transactions_from_csv(csv_file_name, transactions):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    individual_donors = []
    transactions = []
    for row in reader:
        assert len(row) == 23
        id = depipe(row[2])
        name = depipe(row[3])
        state = depipe(row[12])
        gender = depipe(row[18])
        industry_id = depipe(row[7])
        date = depipe(row[8])
        amount = depipe(row[9])
        contributor_id = depipe(row[2])
        contributor_type = 'individual',
        recipient_id = depipe(row[4])
        if(depipe(row[14])[0] == 'P'):
            recipient_type = 'PAC'
        else:
            recipient_type = 'Candidate'
        individual_donor = {'id': id, 'name': name, 'state':state,
                     'gender': gender, 'industry_id': industry_id}
        transaction = {'date': date, 'amount': amount, 'contributor_id': contributor_id, 'contributor_type': contributor_type,
                        'recipient_id': recipient_id, 'recipient_type': recipient_type}
        individual_donors.append(individual_donor)
        transactions.append(transaction)
    csv_file.close()
    return candidates

def load_pac_to_candidate_transactions_from_csv(csv_file_name, transactions):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    for row in reader:
        date = depipe(row[5])
        amount = depipe(row[4])
        contributor_id = depipe(row[2])
        contributor_type = 'individual',
        recipient_id = depipe(row[3])
        recipient_type = 'Candidate'
        transaction = {'date': date, 'amount': amount, 'contributor_id': contributor_id, 'contributor_type': contributor_type,
                        'recipient_id': recipient_id, 'recipient_type': recipient_type}
        transactions.append(transaction)
    csv_file.close()


def load_pac_to_pac_transactions_from_csv(csv_file_name, transactions):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    for row in reader:
        date = depipe(row[5])
        amount = depipe(row[4])
        contributor_id = depipe(row[2])
        contributor_type = 'individual',
        recipient_id = depipe(row[3])
        recipient_type = 'Candidate'
        transaction = {'date': date, 'amount': amount, 'contributor_id': contributor_id, 'contributor_type': contributor_type,
                        'recipient_id': recipient_id, 'recipient_type': recipient_type}
        transactions.append(transaction)
    csv_file.close()

def depipe(piped_string):
    return piped_string[1:-1]

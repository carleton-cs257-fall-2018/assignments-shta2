'''
    Paul Butterfield and Conor Gormally
    Script for converting csv to format that is usable for our api
'''

import sys
import csv
import re

def create_transactions():
    transactions = []
    return transactions

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
    tsv_file.close()
    return industries

def load_pacs_from_csv(csv_file_name):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    pacs = []
    for row in reader:
        if not(len(row) == 14)
            print(row)
        #assert len(row) == 14
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
        if(depipe(row[5])[0] == 'P'):
            continue
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

def load_individuals_and_individual_transactions_from_csv(csv_file_name):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    individual_donors = []
    for row in reader:
        assert len(row) == 23
        id = depipe(row[2])
        name = depipe(row[3])
        state = depipe(row[12])
        gender = depipe(row[18])
        if(gender == 'N'):
            gender = 'U'
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

def load_pac_to_candidate_transactions_from_csv(csv_file_name):
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

def load_pac_to_pac_transactions_from_csv(csv_file_name):
    csv_file = open(csv_file_name, encoding='utf-8')
    reader = csv.reader(csv_file)

    for row in reader:
        date = depipe(row[5])
        amount = depipe(row[4])
        if(depipe(row[21])[0] == 1):
            contributor_id = depipe(row[14])
            recipient_id = depipe(row[2])
        else:
            contributor_id = depipe(row[2])
            recipient_id = depipe(row[14])
        contributor_type = 'PAC',
        recipient_type = 'PAC'
        transaction = {'date': date, 'amount': amount, 'contributor_id': contributor_id, 'contributor_type': contributor_type,
                        'recipient_id': recipient_id, 'recipient_type': recipient_type}
        transactions.append(transaction)
    csv_file.close()

def depipe(piped_string):
    return piped_string[1:-1]

def save_industries_table(industries, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for industry in industries:
        industry_row = [industry['industry_id'], industry['industry_name']]
        writer.writerow(industry_row)
    output_file.close()

def save_pacs_table(pacs, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for pac in pacs:
        pac_row = [pac['id'], pac['name'], pac['party'], pac['industry_id'], pac['sensitive'], pac['foreign'] ]
        writer.writerow(pac_row)
    output_file.close()

def save_candidates_table(candidates, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for candidate in candidates:
        candidate_row = [candidate['id'], candidate['first_name'], candidate['last_name'], candidate['party'],
                         candidate['state'], candidate['seat']]
        writer.writerow(candidate_row)
    output_file.close()

def save_individuals_table(individual_donors, csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for individual in individual_donors:
        indidvidual_row = [individual['id'], individual['name'], individual['state'], individual['gender'],
                         individual['industry_id']]
        writer.writerow(indidvidual_row)
    output_file.close()

def save_transactions_table(csv_file_name):
    ''' Save the books in CSV form, with each row containing
        (id, title, publication year). '''
    output_file = open(csv_file_name, 'w', encoding='utf-8')
    writer = csv.writer(output_file)
    for transaction in transactions:
        transaction_row = [transaction['date'], transaction['amount'], transaction['contributor_id'], transaction['contributor_type'],
                           transaction['recipient_id'], transaction['recipient_type']]
        writer.writerow(transaction_row)
    output_file.close()

if __name__ == '__main__':
    save_industries_table(load_industries_from_codes('doc/codes.txt'), 'industries.csv')
    save_pacs_table(load_pacs_from_csv('/Users/ConorGormally/Documents/Fall18/CS/Original_CSV_Files/cmtes18.txt'), 'pacs.csv')
    save_candidates_table(load_candidates_from_csv('/Users/ConorGormally/Documents/Fall18/CS/Original_CSV_Files/cands18.txt'), 'candidates.csv')
    create_transactions();
    save_individuals_table(load_individuals_and_individual_transactions_from_csv('/Users/ConorGormally/Documents/Fall18/CS/Original_CSV_Files/indivs18.txt'), 'individual_donors.csv')
    load_pac_to_candidate_transactions_from_csv('/Users/ConorGormally/Documents/Fall18/CS/Original_CSV_Files/pacs18.txt')
    load_pac_to_pac_transactions_from_csv('/Users/ConorGormally/Documents/Fall18/CS/Original_CSV_Files/pacs_other18.txt')
    save_transactions_table('transactions.csv')

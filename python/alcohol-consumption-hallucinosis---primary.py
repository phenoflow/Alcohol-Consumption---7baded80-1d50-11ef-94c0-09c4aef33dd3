# Rosa Parisi, Roger T. Webb, Mathew J. Carr, Kieran J. Moriarty, Elise Kleyn, Christopher E. M. Griffiths, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"E250.11","system":"readv2"},{"code":"SM00z00","system":"readv2"},{"code":"E23z.00","system":"readv2"},{"code":"E011z00","system":"readv2"},{"code":"Eu10514","system":"readv2"},{"code":"E012.11","system":"readv2"},{"code":"Eu10711","system":"readv2"},{"code":"E01z.00","system":"readv2"},{"code":"E01yz00","system":"readv2"},{"code":"SM0z.00","system":"readv2"},{"code":"Eu10511","system":"readv2"},{"code":"E250.13","system":"readv2"},{"code":"136Z.00","system":"readv2"},{"code":"E250z00","system":"readv2"},{"code":"E013.00","system":"readv2"},{"code":"E230z00","system":"readv2"},{"code":"E231z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-consumption-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-consumption-hallucinosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-consumption-hallucinosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-consumption-hallucinosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

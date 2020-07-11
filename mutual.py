from sklearn.metrics import mutual_info_score
from collections import OrderedDict as OD
import csv

def sim(a,b):
    return 1 - mutual_info_score(a,b)

result = OD()

drug_to_list = OD()

with open('result.csv', 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        drug_to_list[row[0]] = map(float ,row[1:])

    drugs = drug_to_list.keys()

    for i in xrange(len(drugs)):
        result[drugs[i]] = OD()

    for i in xrange(len(drugs)):
        result[drugs[i]][drugs[i]] = 1
        for j in xrange(i+1, len(drugs), 1):
            result[drugs[i]][drugs[j]] = sim(drug_to_list[drugs[i]], drug_to_list[drugs[j]])

            result[drugs[j]][drugs[i]] = result[drugs[i]][drugs[j]]

with open("mutual_info_score_output.txt","w") as f:
    f.write("     ")
    for drA in drugs:
        f.write(drA + ' ')
    f.write('\n')
    for drA in drugs:
        f.write(drA + ' ')
        for drB in drugs:
            f.write(str(result[drA][drB]) + ' ')
        f.write('\n')
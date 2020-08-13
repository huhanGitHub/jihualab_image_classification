path_predicted = 'D:\Machine_Learning\projects\pytorch_classification-master\pytorch_classification-master\data\\resnext101_32x16d_submission.csv'
path_reference = 'D:\Machine_Learning\projects\pytorch_classification-master\pytorch_classification-master\data\\test_results.txt'

y_predicted = open(path_predicted).readlines()
y_reference = open(path_reference).readlines()

# print(y_predicted)
# print(y_reference)
# print('\n')

y_predicted = sorted(y_predicted, key=lambda x: x[:x.index(',')])
y_reference = sorted(y_reference, key=lambda y: y[:y.index(',')])

# print(y_predicted)
# print(y_reference)

y_pre = []
y_ref = []

for i in y_predicted:
    #print(i.index(','))
    y_pre.append(int(i[i.index(',')+1: i.index(',')+2]))

for j in y_reference:
    y_ref.append(int(j[j.index(',')+1: j.index(',')+2]))

print(y_pre)
print(y_ref)
print('\n')

print('total test cases: '+str(len(y_pre)))
print('\n')

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve

print('accuracy:'+str(accuracy_score(y_pre, y_ref)))
print('accuracy without normalize:'+str(accuracy_score(y_pre, y_ref, normalize=False)))
print('\n')

print('precision (macro):'+str(precision_score(y_pre, y_ref, average='macro')))
print('precision (micro):'+str(precision_score(y_pre, y_ref, average='micro')))
print('precision (weighted):'+str(precision_score(y_pre, y_ref, average='weighted')))
print('precision (none):'+str(precision_score(y_pre, y_ref, average=None)))
print('\n')

print('recall (macro):'+str(recall_score(y_pre, y_ref, average='macro')))
print('recall (micro):'+str(recall_score(y_pre, y_ref, average='micro')))
print('recall (weighted):'+str(recall_score(y_pre, y_ref, average='weighted')))
print('recall (none):'+str(recall_score(y_pre, y_ref, average=None)))
print('\n')

print('f1 (macro):'+str(f1_score(y_pre, y_ref, average='macro')))
print('f1 (micro):'+str(f1_score(y_pre, y_ref, average='micro')))
print('f1 (weighted):'+str(f1_score(y_pre, y_ref, average='weighted')))
print('f1 (none):'+str(f1_score(y_pre, y_ref, average=None)))

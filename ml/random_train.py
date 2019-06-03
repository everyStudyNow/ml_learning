from process_file import *
from sklearn import metrics, ensemble
from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB

source_path = 'random_train.txt'
model_path = 'random_forest.model'
vocab_path = 'vocab.txt'

x_train, train_target = build_vocab(source_path, vocab_path)

train_feature = train_feature(vocab_path, x_train)

# 随即森林
# model = ensemble.RandomForestClassifier(n_estimators=10)
# 多项式贝叶斯分类器
model = MultinomialNB(alpha=0.001)
count = int(len(train_feature) * 0.9)

model.fit(np.array(train_feature[:count]), np.array(train_target[:count]))

joblib.dump(model, model_path)

test_predict = model.predict(train_feature[count:])
test_target = train_target[count:]
true_false = (test_predict == test_target)
accuracy = np.count_nonzero(true_false) / float(len(test_target))
print("accuracy is %f" % accuracy)

print(metrics.classification_report(test_target, test_predict, target_names=['0', '1']))

# 混淆矩阵
print("Confusion Matrix...")
print(metrics.confusion_matrix(test_target, test_predict))






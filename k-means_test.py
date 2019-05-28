from process_file import *
from sklearn import metrics, ensemble
from sklearn.externals import joblib
from sklearn.cluster import KMeans

source_path = 'random_train.txt'
model_path = 'k-means.model'
vocab_path = 'vocab.txt'

x_train, train_target = build_vocab(source_path, vocab_path)

train_feature = train_feature(vocab_path, x_train)

model = KMeans(n_clusters=2, random_state=0)

model.fit(np.array(train_feature))

joblib.dump(model, model_path)


print(model.predict([train_feature[0]]))  # 预测簇id
print(model.cluster_centers_)  # 聚类中心
print(model.labels_)  # 返回所有簇id
print(metrics.calinski_harabaz_score(train_feature, model.predict(train_feature)))  # Calinski-Harabasz分数可以用来评估聚类效果，它内部使用簇内的稠密程度和簇间的离散程度的比值，所以数值越大效果越好





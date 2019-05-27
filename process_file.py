import os
import jieba
import random
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer


def _read_file(file):
    with open(file, encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def _write_file(file, content):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)


stop_path = 'stopword.txt'
stop_words = _read_file(stop_path)


def build_vocab(source_path, save_path):
    x_train = list()
    y_train = list()
    temp = _read_file(source_path)
    random.shuffle(temp)
    for line in temp:
        t = line.split(' ')
        if len(t) == 2:
            words = [w for w in jieba.cut(t[1])]
            x_train.append(' '.join(words))
            y_train.append(t[0])
    count_vec = CountVectorizer(stop_words=None)
    count_vec.fit_transform(x_train)
    vocab = count_vec.get_feature_names()
    vocab = [w for w in vocab if w not in stop_words]
    _write_file(save_path, '\n'.join(vocab))
    return x_train, y_train


def read_vocab(vocab_path):
    return _read_file(vocab_path)


def train_feature(vocab_path, x_train):
    vocab = read_vocab(vocab_path)
    word_to_id = dict(zip(vocab, range(0, len(vocab))))
    vocab_size = len(word_to_id)
    data = np.zeros((len(x_train), vocab_size)).tolist()
    for i in range(len(x_train)):
        dd = [word_to_id[x] for x in x_train[i].split(' ') if x in word_to_id]
        counter = Counter(dd)
        for k, v in counter.items():
            data[i][k] = v
    return data

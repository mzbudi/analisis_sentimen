import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
import joblib
from json import dump
from tqdm import tqdm
import pandas as pd
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn
vectorizer = TfidfVectorizer(min_df=0.01, max_df=3.0)

def str2bool(s):
    return s.lower() in ('true', '1')

parser = argparse.ArgumentParser()
parser.add_argument("--load", default=True, type=str2bool)
args = parser.parse_args()
print(args)
trained = args.load

files = ["kpu"]
datasets = {k:{l:[] for l in ["Train", "Test"]} for k in files}

for _fn in files:
    last_accs = 0.0
    print("Start Training for %s"%_fn)
    for _ in tqdm(range(500)):
        fn = "stemmed_%s_no_jutsu.csv"%_fn
        df = pd.read_csv(fn)
        tweets_features = vectorizer.fit_transform(raw_documents=df["Stemmed"].values)
        x_train, x_test, y_train, y_test = train_test_split(tweets_features, df["Sentimen"],
                                                            test_size=0.2, shuffle=True)
        if trained:
            model = joblib.load("%s_classifier.svm"%_fn)
        else:
            model = GridSearchCV(SVC(), {'gamma':[1, 0.1, 0.001, 0.0001, 0.00001],
                                         'kernel':['linear', 'rbf']},
                                 refit=True, verbose=0)
            model.fit(x_train, y_train)
            model = model.best_estimator_
        train_tweets = [df["Stemmed"][i] for i in y_train.index]
        test_tweets = [df["Stemmed"][i] for i in y_test.index]
        datasets[_fn]["Test"] = {
            "Tweet": [df["Tweet"][i] for i in y_test.index],
            "Stemmed": test_tweets,
            "TFIDF": x_test,
            "Sentimen": y_test.values
        }
        datasets[_fn]["Train"] = {
            "Tweet": [df["Tweet"][i] for i in y_train.index],
            "Stemmed": train_tweets,
            "TFIDF":x_train,
            "Sentimen":y_train.values
        }
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        modes = ["Train", "Test"]
        if report['accuracy'] > last_accs:
            last_accs = report["accuracy"]

            with open("%s_result.json"%fn, 'w') as f:
                dump(report, f)
            print(report['accuracy'])
            if not trained:
                joblib.dump(model, "%s_classifier.svm"%_fn)
            for mode in modes:
                print("Saving %s data for %s"%(mode, _fn))
                joblib.dump(
                    datasets[_fn][mode],
                    "%s_%s_datas.data"%(_fn, mode)
                )

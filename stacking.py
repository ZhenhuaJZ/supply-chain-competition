from tqdm import tqdm
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

def stack_split(feature, labels, number_of_model):
    # Define number of sizes per model
    fold_size = int(labels.size/number_of_model)

    # Iterate number of models to get different fold, feature and label data
    fold_split = {}
    feature_split = {}
    label_split = {}
    fold_split_label = {}

    for i in range(number_of_model):
        # define starting and end rows of the fold data
        start_row = fold_size * i
        end_row = fold_size * (i+1)

        if i == number_of_model - 1:

            print("\nfold_{}".format(i+1) + " starting between row:{}".format(start_row) + " and row:{}".format(end_row))
            fold_split["fold_{}".format(i+1)] = feature[start_row:,:]
            fold_split_label["fold_label_{}".format(i+1)] = labels[start_row:]
            # Delete the extrated data from feature and label data
            feature_split["feature_{}".format(i+1)] = np.delete(feature, np.s_[start_row:], axis = 0)
            label_split["label_{}".format(i+1)] = np.delete(labels, np.s_[start_row:], axis = 0)

        else:

            print("\nfold_{}".format(i+1) + " starting between row:{}".format(start_row) + " and row:{}".format(end_row))
            # Store extrated fold data from feature
            fold_split["fold_{}".format(i+1)] = feature[start_row:end_row,:]
            fold_split_label["fold_label_{}".format(i+1)] = labels[start_row:end_row]
            # Delete the extrated data from feature and label data
            feature_split["feature_{}".format(i+1)] = np.delete(feature, np.s_[start_row:(start_row + fold_size)], axis = 0)
            label_split["label_{}".format(i+1)] = np.delete(labels, np.s_[start_row:(start_row + fold_size)], axis = 0)

    return fold_split, fold_split_label, feature_split, label_split



def stack_layer(names, classifiers, feature, labels, test_feature):

        # progress_log(names, classifiers, layer_name)
        fold_split, fold_split_label, feature_split, label_split = stack_split(feature,labels,5)
        layer_transform_train = []
        layer_transform_test = []
        weighted_avg_roc = []
        for name, clf in zip(names, classifiers):
            fold_score = []
            test_score = []

            for i in tqdm(range(len(fold_split))):
                # print("\nProcessing model :{} fold {}".format(name, i+1))
                clf.fit(feature_split["feature_{}".format(i+1)], label_split["label_{}".format(i+1)])
                # print("Training complete")
                stack_score = clf.predict(fold_split["fold_{}".format(i+1)])
                # print("fold score predicted")
                test_prediction = clf.predict(test_feature)
                print(test_prediction.shape)
                print(stack_score)
                # print("test score predicted")
                test_score.append(test_prediction.tolist())
                fold_score += stack_score.tolist()
                # print("model {}".format(name) + " complete")

            #Averaging stacked
            stack_test_layer1_preds = np.stack(test_score, 1)
            #averaging stacked data
            avged_test_preds = []

            for row in stack_test_layer1_preds:
                avg = np.mean(row)
                avged_test_preds.append(avg)

            print("\nAveraging test score done ......")
            layer_transform_train.append(fold_score)
            layer_transform_test.append(avged_test_preds)

        layer_transform_train = np.array(layer_transform_train).transpose()
        layer_transform_test = np.array(layer_transform_test).transpose()
        print("layer_transform_train : \n" , layer_transform_train)
        # np.savetxt(log_file + "{}_train_{}:{}.csv".format(layer_name, now.hour, now.minute) ,layer_transform_train , fmt = '%.9f', delimiter = ',')
        # np.savetxt(log_file + "{}_test_{}:{}.csv".format(layer_name, now.hour, now.minute) ,layer_transform_test ,fmt = '%.9f', delimiter = ',')
        return layer_transform_train, layer_transform_test

def two_layer_stack(train_x, train_y, test, mode = "full", save_path = "", save_name = ""):
    if mode == "full":
        clf_names = ["XGBRegressor", "LGBMRegressor", "Lasso", "Ridge"]
        classifiers = [
            XGBRegressor(max_depth = 3, learning_rate = 0.1, n_eatimators = 100),
            LGBMRegressor(num_leaves = 31, max_depth = 4, learning_rate = 0.1, n_estimators = 100),
            Lasso(alpha = 0.1),
            Ridge(alpha = 0.5)
        ]
        layer_1_train, layer_1_test = stack_layer(clf_names, classifiers, train_x, train_y, test)

    if mode == "save":
        clf_names = ["XGBRegressor", "LGBMRegressor", "Lasso", "Ridge"]
        classifiers = [
            XGBRegressor(max_depth = 3, learning_rate = 0.1, n_eatimators = 100, n_jobs = -1),
            LGBMRegressor(num_leaves = 31, max_depth = 4, learning_rate = 0.1, n_estimators = 100, n_jobs = -1),
            Lasso(alpha = 0.1),
            Ridge(alpha = 0.5)
        ]
        layer_1_train, layer_1_test = stack_layer(clf_names, classifiers, train_x, train_y, test)
        pd.to_csv(layer_1_train, save_path + save_name)
        pd.to_csv(layer_1_test, save_path + save_name)

    if mode == "read":
        layer_1_train = pd.read_csv(save_path + save_name)
        layer_1_test = pd.read_csv(save_path + save_name)

    clf_names = ["XGBRegressor", "LGBMRegressor", "Lasso", "Ridge"]
    classifiers = [
        XGBRegressor(max_depth = 3, learning_rate = 0.1, n_eatimators = 100),
        Lasso(alpha = 0.1)]
    _, layer_2_test = stack_layer(clf_names, classifiers, layer_1_train, train_y, layer_1_test)

    layer_2_test = np.average(layer_2_test,axis = 1)

    return layer_2_test


def main():
    size = 2000
    dataset = pd.read_csv("/home/stirfryrabbit/Documents/train_w1.csv")
    train = dataset.drop(["data_date", "goods_id", "sku_id", "label"], axis = 1).loc[:size].values
    label = dataset.label.loc[:size].values
    test = dataset.drop(["data_date", "goods_id", "sku_id", "label"], axis = 1).loc[size+1:size+500].values
    pred = two_layer_stack(train, label, test)
    print(type(pred))

main()

import matplotlib.pyplot as plt
import pandas as pd

def split_input_data(data):
    # Your code goes here
    return X_train, X_test, y_train, y_test


def display_contours(classifier, number_of_neighbors):
    #Your code goes here

    plt.show()


def knn(nneighbors, X_train, y_train, X_test):
    #Your code goes here

    display_contours(clf, nneighbors)
    return predicted_y


def evaluateknn(y_predicted, y_test):



if __name__ == "__main__":
    input_data = pd.read_csv("inputData.csv")
    X_train, X_test, y_train, y_test = split_input_data(input_data)

    predicted_y = knn(3, X_train, y_train, X_test)
    evaluateknn(predicted_y, y_test)

import csv
from random import shuffle
from sklearn import tree
import time

# read csv files
with open('longontsteking_data.csv', 'r') as DataFile:
    csvList = list(csv.reader(DataFile))[1:]
    shuffle(csvList)
    trainDataCount = round(len(csvList) * 7 / 10) + 1
    print("Using " + str(trainDataCount) + " rows for training")
    print("Using " + str(len(csvList) - trainDataCount) + " rows for testing")
    trainData = csvList[0:trainDataCount].copy()
    testData = csvList[trainDataCount:].copy()

# datasets
test_features = []
test_labels = []

features = []
labels = []

# split labels from features
for item in testData:
    test_labels.append(item[-1])
    test_features.append(item[:-1].copy())

for item in trainData:
    labels.append(item[-1])
    features.append(item[:-1].copy())


# create a decision tree classifier
DT_clf = tree.DecisionTreeClassifier()
# train the classifier with the trainingsdata
DT_clf = DT_clf.fit(features, labels)

print("\nHello, I am Fruity. \nI can predict what kind of fruit you have. \nFor this I only need to know the height, width and weight.")

while True:
    print("\nGeslacht? (0 voor VROUW, 1 voor MAN)")
    # get height value from user
    geslacht = int(input(""))
    print("\nLeeftijd?")
    # get width value from user
    leeftijd = int(input(""))
    print("\nHoesten?")
    # get weight value from user
    hoesten = int(input(""))

    print("\nZere keel?")
    # get weight value from user
    zere_keel = int(input(""))

    print("\nPijn op de borst?")
    # get weight value from user
    pijn_op_de_borst = int(input(""))

    print("\nKortademigheid?")
    # get weight value from user
    kortademigheid = int(input(""))

    print("\nDruk op de borstkas?")
    # get weight value from user
    druk_op_de_borstkas = int(input(""))
    print("\nKoorts?")
    # get weight value from user
    koorts = int(input(""))
    print("\nSnelle ademhaling?")
    # get weight value from user
    snelle_ademhaling = int(input(""))

    # predict fruit type on the basis of data entered by the user
    prediction = int(DT_clf.predict([[geslacht, leeftijd, hoesten, zere_keel, pijn_op_de_borst,
                                      kortademigheid, druk_op_de_borstkas, koorts, snelle_ademhaling]])[0])
    # link correct fruitname to predicted value
    print("\n\nI think you have a:")
    if prediction == 1:
        print("Longontsteking")
    elif prediction == 2:
        print("Hooikoorts")
    else:
        print("Helemaal niets")

    print(prediction)

    print("\n\n\nDo you want me to predict YOUR ZIEKTE again? (Y/N)")
    again = input("")
    if again.upper() != "Y":
        break

print("\nOkay you see the next time!")

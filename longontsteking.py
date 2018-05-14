import csv
from random import shuffle
from sklearn import tree

# read csv files
with open('longontsteking_data.csv', 'r') as DataFile:
    csvList = list(csv.reader(DataFile))[1:]
    shuffle(csvList)
    trainDataCount = round(len(csvList) * 7 / 10) + 1
    print("Er worden " + str(trainDataCount) +
          " rijen gebruikt om de applicatie te trainen.")
    print("Er worden " + str(len(csvList) - trainDataCount) +
          " rijen gebruikt om de applicatie te testen.")
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

print("\nDeze applicatie kan bekijken of je longontsteking, hooikoorts of geen ziekte hebt. Hiervoor worden er een aantal vragen gesteld.")

while True:
    print("\nWat is jouw geslacht? (0 voor VROUW, 1 voor MAN)")
    geslacht = int(input(""))

    print("\nWat is jouw leeftijd?")
    leeftijd = int(input(""))

    print("\nMerk je dat je veel moet hoesten?")
    hoesten = int(input(""))

    print("\nHeeft u een zere keel?")
    zere_keel = int(input(""))

    print("\nHeeft u pijn op de borst?")
    pijn_op_de_borst = int(input(""))

    print("\nHeeft u last van kortademigheid?")
    kortademigheid = int(input(""))

    print("\nVoelt u druk op de borstkas?")
    druk_op_de_borstkas = int(input(""))

    print("\nHeeft u last van koorts?")
    koorts = int(input(""))

    print("\nHeeft u last van een snelle ademhaling?")
    snelle_ademhaling = int(input(""))

    prediction = int(DT_clf.predict([[geslacht, leeftijd, hoesten, zere_keel, pijn_op_de_borst,
                                      kortademigheid, druk_op_de_borstkas, koorts, snelle_ademhaling]])[0])

    print("\n\nDe applicatie geeft aan dat u de volgende ziekte heeft:")
    if prediction == 1:
        print("Longontsteking")
    elif prediction == 2:
        print("Hooikoorts")
    else:
        print("Helemaal niets")

    print("\nUw ziekte is bepaald. Druk op 'j' om de applicatie te herstarten.")
    again = input("")
    if again.upper() != "J":
        break

print("\nU heeft aangegeven dat u geen behoefte meer heeft om de applicatie te herstarten. Fijne dag.")

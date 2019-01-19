from sklearn import tree

#[height, weight, shoe size]
X = [
  [119, 855, 129], [102,813,116], [143,895,153], [127,920,142], [146,930,144],
  [105,838,119], [114,852,134], [127,898,156], [143,907,153], [114,884,133]
]

Y=[
  'male', 'male', 'male', 'male', 'male',
  'female', 'female', 'female', 'female', 'female'
]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[207,1061,168], [144,899,145]]) #['male', 'female']

print(prediction)
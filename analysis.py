# feature column list
features = ['likes', 'view_count', 'comment_count']

import turicreate as tc

# load data
data=tc.SFrame("data_c/joined_all.csv")

# split data into training and testing sets
train_data_set,test_data=data.random_split(.9,seed=1)

# split test data into dev and test sets
test_data_set,dev_set=test_data.random_split(.5,seed=1)

# create model
model=tc.regression.create(train_data_set, target='dislikes', features=features)

# save predictions
predictions = model.predict(test_data_set[1])
print(predictions)

# evaluate predictions
# results = model.evaluate(test_data)


# select feature columns

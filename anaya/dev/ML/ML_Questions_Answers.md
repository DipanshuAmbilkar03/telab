# Machine Learning: Questions and Answers

## Experiment 1: PCA on the Wine Dataset

**Q1. What is PCA and why is it used here?**
PCA (Principal Component Analysis) is a dimensionality reduction technique. It converts the original features into a smaller set of new features called principal components. Here it reduces 13 wine measurements to 2 components so the data can be plotted and the wine groups inspected.

**Q2. Why do we standardize the data before applying PCA?**
PCA is based on variance, so a feature measured in large units would dominate the components. StandardScaler gives every feature mean 0 and standard deviation 1. This puts all features on the same scale so each one contributes fairly.

**Q3. What does the explained variance ratio tell us?**
It tells what fraction of the total variance each principal component captures. In this experiment the first two components together keep about 55% of the variance. A higher value means less information is lost in the reduction.

**Q4. What is a principal component?**
A principal component is a linear combination of the original features. The first component points in the direction of maximum variance in the data. Each next component is perpendicular to the previous ones and captures the most remaining variance.

**Q5. Is PCA a supervised or unsupervised technique?**
PCA is unsupervised because it does not use the class labels while computing the components. In this experiment the segment labels are used only afterwards, to colour the scatter plot and check the separation.

**Q6. What did the scatter plot of PC1 vs PC2 show?**
The three wine segments formed clearly separated groups in the 2D plot. This means the two components retained enough information to distinguish the groups. It confirms that PCA preserved the useful structure of the data.

## Experiment 2: Uber Fare Prediction with Linear, Ridge and Lasso Regression

**Q1. What is regression and what are we predicting here?**
Regression is a supervised learning task that predicts a continuous value. Here the target is the Uber fare, predicted from distance, duration and number of passengers. The model learns the relationship between these features and the fare from past trips.

**Q2. What is an outlier and how was it detected here?**
An outlier is a value that is far away from the rest of the data. It was detected with the IQR rule: fares below Q1 minus 1.5 times IQR or above Q3 plus 1.5 times IQR are outliers. Such rows were removed because they can pull the regression line away from the general pattern.

**Q3. What does correlation with fare tell us?**
Correlation measures how strongly a feature moves together with the fare, from -1 to +1. Distance (about 0.99) and duration (about 0.95) are strongly related to fare, while passengers has almost no relation. Strong features usually make better predictors.

**Q4. What is the difference between Ridge and Lasso regression?**
Both add a penalty on the size of the coefficients to plain linear regression. Ridge uses the sum of squared coefficients (L2 penalty) and shrinks them towards zero. Lasso uses the sum of absolute values (L1 penalty) and can shrink some coefficients exactly to zero, which also does feature selection.

**Q5. Why is regularization needed at all?**
Without regularization a model can overfit, meaning it fits the training data too closely and performs poorly on new data. The penalty keeps the coefficients small and the model simpler. This usually improves accuracy on unseen test data.

**Q6. What do R2 and RMSE mean in the results?**
R2 tells how much of the variation in fare the model explains; 1.0 is perfect and all three models scored about 0.986. RMSE is the average prediction error in fare units, about 14 rupees here. Lower RMSE and higher R2 mean a better model.

## Experiment 3: SVM Classification of Handwritten Digits

**Q1. What is a Support Vector Machine?**
SVM is a supervised classification algorithm that finds the best boundary, called a hyperplane, between classes. It chooses the hyperplane with the maximum margin, that is the largest distance to the nearest points of each class. Those nearest points are the support vectors.

**Q2. What data does the digits dataset contain?**
It has 1797 images of handwritten digits, each image is 8 by 8 pixels. Flattened, each image becomes 64 numeric features. The label is the digit from 0 to 9, so it is a 10 class classification problem.

**Q3. Why do we split the data into train and test sets?**
The model is trained on the training set and evaluated on a separate test set it has never seen. This gives an honest estimate of how the model will perform on new data. Here 80% was used for training and 20% for testing.

**Q4. What is a confusion matrix?**
It is a table that compares actual classes with predicted classes for the test set. Correct predictions lie on the diagonal. Off diagonal entries show exactly which digits were confused with each other, for example a 8 predicted as a 1.

**Q5. What do precision, recall and F1 score mean?**
Precision is the fraction of predicted positives that are actually correct. Recall is the fraction of actual positives that the model found. F1 score is the harmonic mean of precision and recall and balances both in one number.

**Q6. The accuracy is about 98.9%. What does that mean and is it good?**
It means about 98.9% of the test images were classified into the correct digit. For a 10 class problem where random guessing gives 10%, this is a very strong result. It shows SVM works well on this kind of image data.

## Experiment 4: K-Means Clustering on the Iris Dataset

**Q1. What is K-Means clustering?**
K-Means is an unsupervised algorithm that groups data into k clusters. Each point is assigned to the nearest cluster centre (centroid), then the centroids are recomputed as the mean of their points. These two steps repeat until the clusters stop changing.

**Q2. What is inertia in K-Means?**
Inertia is the sum of squared distances of every point to its assigned cluster centre. Smaller inertia means tighter, more compact clusters. It is the quantity that K-Means tries to minimize.

**Q3. What is the elbow method and what did it show here?**
We run K-Means for k from 1 to 10 and plot inertia against k. Inertia falls fast at first and then slows down; the bend or elbow is the suggested number of clusters. Here the elbow is at k = 3, which matches the three iris species.

**Q4. Why can we not just keep increasing k to reduce inertia?**
Inertia always decreases as k grows, and with one cluster per point it becomes zero. But too many clusters lose the useful grouping and overfit the data. The elbow point balances compact clusters against a sensible number of groups.

**Q5. K-Means is unsupervised, so how did we check the result?**
The true species labels were hidden during clustering and used only for checking afterwards. One cluster contained all 50 setosa flowers, and the other two matched versicolor and virginica with only a few mixes. This purity check shows the clusters are meaningful.

**Q6. Why is the choice of the initial centroids important?**
K-Means starts from randomly placed centroids, and a poor start can end in a weak local solution. That is why the code uses n_init=10, running the algorithm 10 times from different starts. It keeps the run with the lowest inertia.

## Experiment 5: Random Forest for Car Safety Prediction

**Q1. What is a Random Forest?**
Random Forest is an ensemble classifier made of many decision trees. Each tree is trained on a random subset of the data and a random subset of features. For prediction, all trees vote and the majority class is the final answer.

**Q2. Why does a forest work better than a single decision tree?**
A single tree can overfit and change a lot with small changes in data. Averaging the votes of many different trees cancels out individual errors. This reduces variance and usually gives higher and more stable accuracy.

**Q3. The car dataset is all text categories. Why did we encode it?**
Machine learning models work with numbers, not text labels like low, med or high. OrdinalEncoder converts each category into a number while keeping the natural order of values such as low < med < high < vhigh. The encoded matrix can then be given to the model.

**Q4. What features and classes does the car dataset have?**
It has 1728 cars described by 6 features: buying price, maintenance cost, doors, persons, luggage boot size and safety. The target has 4 classes: unacc, acc, good and vgood. The model predicts the acceptability class of a car from its features.

**Q5. What does n_estimators=100 mean?**
It is the number of decision trees in the forest, here 100 trees. More trees usually make the prediction more stable, up to a point. After enough trees the accuracy stops improving while training time keeps increasing.

**Q6. The accuracy is about 98.8%. How do we read the classification report alongside it?**
Accuracy is the overall fraction of correct predictions. The report gives precision, recall and F1 for every class separately, so a weak class cannot hide behind a good overall score. Here all four classes score high, so the model is reliable across classes.

## Experiment 6: Maze Exploration with Q-Learning

**Q1. What is reinforcement learning?**
In reinforcement learning an agent learns by interacting with an environment through trial and error. It takes actions, receives rewards or penalties, and learns which actions lead to the highest total reward. Unlike supervised learning, no correct answers are given in advance.

**Q2. What is Q-Learning and what is stored in the Q-table?**
Q-Learning is a reinforcement learning algorithm that learns the value of every action in every state. These values are stored in a Q-table, here Q[row][col][action]. After training, the best action in a state is simply the one with the highest Q-value.

**Q3. Explain the reward design used in the maze.**
Each normal step gives -1, which pushes the agent to find a short path. Hitting a wall gives -5, which teaches the agent to avoid walls. Reaching the goal gives +20 and ends the episode, which is the main positive signal the agent works towards.

**Q4. What is the epsilon-greedy policy?**
With probability epsilon (0.15 here) the agent takes a random action to explore new possibilities. Otherwise it exploits, taking the action with the highest Q-value known so far. This balances learning new things against using what is already learned.

**Q5. What roles do alpha and gamma play in the Q update?**
Alpha (0.2) is the learning rate: how much a new experience changes the old Q-value. Gamma (0.95) is the discount factor: how much future rewards matter compared to immediate ones. A gamma close to 1 makes the agent value the final goal strongly.

**Q6. How do we know the agent actually learned?**
After 1500 training episodes the agent was run greedily, always picking the best known action. It reached the goal in 14 steps without any random moves. The printed maze shows the learned path from S to G avoiding all walls, which proves the Q-table captured a correct route.

## Experiment 7: Emotion Detection from Text

**Q1. What is the goal of this experiment?**
The goal is to classify short text messages into one of three emotions: happy, sad or angry. It is a text classification task, so the text must first be converted into numbers that a classifier can use. Two classifiers are trained and compared.

**Q2. What preprocessing is done on the text and why?**
Each message is lowercased, URLs and mentions are removed, and punctuation is stripped. This reduces noise so that the same word in different forms, like Happy and happy, is treated as one feature. Cleaner text gives the model a smaller and more useful vocabulary.

**Q3. What is TF-IDF?**
TF-IDF converts text into numeric features. Term frequency counts how often a word appears in a message, and inverse document frequency lowers the weight of words that appear in almost every message. The result highlights words that are characteristic of a message, and using unigrams plus bigrams also captures word pairs.

**Q4. What is the difference between Logistic Regression and Naive Bayes here?**
Logistic Regression learns a weighted decision boundary between the classes and generally handles overlapping features well. Multinomial Naive Bayes uses word probabilities and assumes features are independent of each other given the class. That assumption is simple but often too strong for text, one reason it scored lower here.

**Q5. What were the results and which model was better?**
Logistic Regression reached about 0.87 accuracy and Naive Bayes about 0.80 on the test set. So Logistic Regression was the better model and was used for the confusion matrix and the demo. The confusion matrix shows most errors are a few messages mixed between emotion classes.

**Q6. How was the better model tested on new sentences?**
Three brand new sentences, never seen in training, were cleaned and converted with the same TF-IDF vectorizer. The model predicted happy, sad and angry correctly for the three demo sentences. This shows the model generalizes to unseen text instead of only memorizing the training data.

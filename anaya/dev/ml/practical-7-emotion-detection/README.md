# Practical 7: Emotion Detection from Text (simple version)

## Aim
Detect emotions (happy, sad, angry) in short text messages and compare two classifiers.

## Problem Statement
Preprocess short text messages, convert them to TF-IDF features (unigrams + bigrams), train Logistic Regression and Multinomial Naive Bayes, compare them on accuracy, show a confusion matrix, and test the better model on new unseen sentences.

## Steps followed
1. Build a labelled dataset (180 messages, 60 per emotion) from emotion word lists with message templates, seeded so it is reproducible.
2. Preprocess: lowercase, remove URLs, mentions and punctuation.
3. TF-IDF vectorization with unigrams + bigrams.
4. Train Logistic Regression and Naive Bayes; compare accuracy.
5. Confusion matrix of the better model; predict 3 brand-new sentences.

## Output
- Logistic Regression reaches ~0.87 accuracy and beats Naive Bayes (~0.80); the confusion matrix and the new-sentence demo use the Logistic Regression model.

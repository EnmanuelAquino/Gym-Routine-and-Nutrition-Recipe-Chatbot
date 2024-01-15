# Gym Routine and Nutrition Recipe Chatbot

## Introduction

Happy to share my latest project: Gym routine and nutrition recipe recommendation chatbot. Inspired by the new year resolution "NEW YEAR NEW ME."

The chatbot is designed for user interaction to address follow-up questions, focusing on two main features:

1. **Gym Routines:**
   - Choose from a selection of 420 exercises targeting specific body parts.
   - Specify intensity level, number of exercises, and receive step-by-step instructions for each exercise.

2. **Nutrition Recipes:**
   - Access a database of 1,925 recipes.
   - Request recipes based on attributes such as calories, carbohydrates, protein, fat, and total preparation time.
   - Receive recipes containing specific ingredients or items.

All information was preprocessed using web scraping procedures from the famous website [Bodybuilding.com](https://www.bodybuilding.com/).

## Framework and Architecture

- **Framework Used:** [Rasa](https://rasa.com/)
- **Model:** [DIET Classifier](https://rasa.com/docs/rasa/nlu/components/#dietclassifier)

## How it Works

The chatbot operates as a dialogue system where users interact with an automated system in a two-way conversation. Users provide text input, and the chatbot responds with relevant actions or questions.

### DIET Classifier

- **Intent Classification:**
  - Predicts the intent class with high accuracy for further action or response.
- **Entity Recognition:**
  - Identifies predefined words within user input to predict intent or serve as input for future actions.

## Results

- **Intent Classification:**
  - Accuracy: 0.99
  - F1-score: 0.99

- **Entity Extractor Classification:**
  - Accuracy: 0.95
  - F1-score: 0.92

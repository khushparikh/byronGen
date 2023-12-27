# Sentiment-Driven Lord Byron Poem Generator
Based on a user's real-time diary input, recommends a poem by Lord Byron to help explore their emotions with a literary companion.

## Usage
Simply clone the repo or go to https://huggingface.co/spaces/kparikh/APCSPBYRON to access the fully running model.

## Functionality
Created a json data file of all Lord Byron poems and their assigned sentiment score (generated through NLTK tools). Then, uses the same library to assign sentiment scores to input text and uses a match algorithm to output the closest match.

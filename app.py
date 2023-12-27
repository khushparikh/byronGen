import poetpy
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import gradio as gr
import json

def getPoem(userInput):
    # Access all poetry by Lord Byron- One Time Process
    # byronPoems = poetpy.get_poetry('author', 'Lord Byron')

    # Create a .json of all Byron Poems
    poemTable = {}
    getScore = SentimentIntensityAnalyzer()
    '''
    for poem in byronPoems:
        lines = poem['lines']
        fullText = ""
        for line in lines:
            fullText = fullText + line
        textSentiment = getScore.polarity_scores(fullText)["compound"]
        poemTable[poem["title"]] = textSentiment
    with open("poemTable.json", "w") as outfile:
        json.dump(poemTable, outfile)
    '''
    # Uploads .json file with all poem titles and sentiments included
    with open('poemTable.json') as json_file:
        poemTable = json.load(json_file)
    
    userSentiment = getScore.polarity_scores(userInput)["compound"]
    print("USER SENTIMENT IS: " + str(userSentiment))
    closestSentiment = 0
    closestPoem = ""
    for pName, pSentiment in poemTable.items():
        if abs(pSentiment - userSentiment) < abs(closestSentiment - userSentiment):
            closestPoem = pName
            closestSentiment = pSentiment
            
    return ("\"" + closestPoem + "\"" + " by Lord Byron")

# Creation of Gradio Interface
with gr.Blocks() as interface:
    with gr.Row():
        with gr.Column():
            input = gr.Textbox()
        with gr.Column():
            poemName = gr.Textbox()
    btn = gr.Button("Find Me a Poem")
    btn.click(getPoem, inputs=input, outputs= poemName)

interface.launch()

from __future__ import unicode_literals, print_function
import json
import os
import nltk
import tensorflow as tf
import tensorflow_hub as hub
from nltk.tokenize import word_tokenize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import pipeline
from spacy.lang.en import English
nltk.download('punkt')

MAX_TOKENS = 880
MIN_WORD_PER_SENTENCE = 15
SUMMARY_MAX_LENGTH = 240
SUMMARY_MIN_LENGTH = 30

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class Bullet:
    text = ""
    publisher = "NewsBroInc."
    def __init__(self, text, publisher):
        self.text = text
        self.publisher = publisher
    def __str__(self):
        return f"""{self.publisher}: {self.text}"""

class Summary:
    text = ""
    publisher = "NewsBroInc."
    def __init__(self, text, publisher):
        self.text = text
        self.publisher = publisher


def getNumTokens(article):
    return len(word_tokenize(article))

def lexRank(article, sentenceCount):
    # Create a parser for the article text
    parser = PlaintextParser.from_string(article, Tokenizer("english"))

    # Create a LexRank summarizer
    summarizer = LexRankSummarizer()

    # Get the summary
    summary = summarizer(parser.document, sentenceCount)

    summaryText = []
    for sentence in summary:
        summaryText.append(str(sentence))
    return " ".join(summaryText)


def bart(article, maxLength=SUMMARY_MAX_LENGTH, minLength=SUMMARY_MIN_LENGTH):
    return summarizer(article, max_length=maxLength, min_length=minLength, do_sample=False)


def getArticles():
    folder_path = "articles"

    # Get the list of all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Filter out only the txt files
    txt_files = [f for f in files if f.endswith(".txt")]

    # Create a dictionary to store the content of each text file
    file_contents = {}

    # Loop through each txt file and read its content
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            publisher = txt_file[:-4]
            file_contents[publisher] = content

    return file_contents

def summarizeArticle(article):
    numTokens = getNumTokens(article)
    lexRankedArticle = article
    i = 0
    while numTokens > MAX_TOKENS:
        numSentences = MAX_TOKENS / (MIN_WORD_PER_SENTENCE + i)
        lexRankedArticle = lexRank(article, numSentences)
        numTokens = getNumTokens(lexRankedArticle)
        i += 1
    return bart(lexRankedArticle)
    
def getSummarizedArticles():
    articles = getArticles()
    summaries = []
    for article in articles:
        cur = Summary(summarizeArticle(articles[article])[0]['summary_text'], article)
        summaries.append(cur)
    return summaries

def areBulletsSimilar(sentence1, sentence2):

    embeddings1 = embed([sentence1])
    embeddings2 = embed([sentence2])

    similarity = tf.reduce_sum(tf.multiply(embeddings1, embeddings2)).numpy()

    # print(similarity)
    return similarity > 0.5

def getSentencesFromRawText(input_text):
    # Load the English NLP model from spacy
    nlp = English()

    # Process the text using spacy
    doc = nlp(input_text)
    nlp.add_pipe('sentencizer')

    doc = nlp(input_text)
    sentences = [sent.text.strip() for sent in doc.sents]

    return sentences
    
def getAllBullets(summaries):
    allBullets = []
    for summary in summaries:
        publisher = summary.publisher
        curBullets = getSentencesFromRawText(summary.text)
        for bulletText in curBullets:
            allBullets.append(Bullet(bulletText, publisher)) 
    return allBullets


def getFinalClusters(allBullets):
    output = [[allBullets[0]]]
    for i in range(1, len(allBullets)):
        cur = allBullets[i]
        foundSimilarInstance = False
        for i in range (len(output)):
            if areBulletsSimilar(cur.text, output[i][0].text):
                foundSimilarInstance = True
                output[i].append(cur)
                break
        if foundSimilarInstance == False:
            output.append([cur])

    return output

def getFinalOutput(clusters):
    sortedList = sorted(clusters, key=len)
    sortedList.reverse()
    return sortedList[:5]

def getData():
    allSummaries = getSummarizedArticles()
    allBullets =  getAllBullets(allSummaries)
    clusters = getFinalClusters(allBullets)
    finalOutput = (getFinalOutput(clusters))
    data = []
    for element in finalOutput:
        publishers = []
        for subElement in element:
            publishers.append(subElement.publisher)
        headline = {
            'score' : f"""{round((len(set(publishers)) / 31) * 100, 1)}%""",
            'text' : element[0].text,
            'publishers' : list(set(publishers)),
        }
        data.append(headline)
    return data

def sendData():
    data = getData()
    jsonString = json.dumps(data, indent=2)
    print(jsonString)



    
    file_name = 'output.json'
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

sendData()







    
# News Article Scraper and NLP Analysis Pipeline

This project is a data pipeline for scraping news articles, performing Natural Language Processing (NLP) tasks, and generating insights from the text data. The tasks covered include web scraping, data preprocessing, text analysis, and summarization using state-of-the-art NLP techniques. It also used a Large Language Model from Hugging Face to do sentiment analysis on the data.

## Project Structure

The project is divided into three main sub-tasks:

1. **Data Collection and Web Scraping**
2. **Data Preprocessing using NLP & Information Retrieval Techniques**
3. **Text Analysis and Summarization**

## Sub Tasks Breakdown

### Sub Task 1: Data Collection and Web Scraping

In this part, I have used "Scrapy" web scraping tool to gather text data from a news website. I have extracted article text along with relevant metadata such as the article title, paragraphs, links etc.

- **Tools Used**:  `Scrapy`
- **Output**: A `.csv` file containing scraped news.

#### Steps:
1. Use web scraping libraries to crawl a news website.
2. Parse the HTML content to extract the article text and metadata.
3. Save the data into a CSV format with columns like:
   - `title`: Title of the news article
   - `paragraph`: Paragraph from the article
   - `links`: Links contained in the article
   - `headings`: Headings from the article

### Sub Task 2: Data Preprocessing using NLP & Information Retrieval Techniques

This part focuses on preparing the scraped data for analysis by cleaning and normalizing it. NLP techniques such as tokenization ,lemmatization etc., are applied.

- **Tools Used**:  `pandas`, `re`, `NLTK`, `spacy`,`transformers`

#### Steps:
1. **Handling Missing Values**: Replace any missing values in the dataset.
2. **Standardizing Features**: Convert text to lower case, remove stop words, and perform lemmatization.
3. **Removing Outliers**: Detect and remove text paragraph having too short or too long length.
4. **Text Preprocessing**:
   - Tokenization
   - Lemmatization
   - Removal of punctuations, and special characters.

### Sub Task 3: Text Analysis and Summarization

In this final stage, we perform deeper text analysis by extracting key insights such as word frequencies, sentiment, and summarizing articles.

- **Tools Used**: `NLTK`, `spaCy`, Hugging Face models (e.g., `transformers`)

#### Steps:
1. **Word Frequency Analysis**: Analyze the most common words in each article.
2. **Text Summarization**: Use pre-trained transformer models (e.g., from Hugging Face) to generate summaries of the articles.
3. **Sentiment Analysis**: Perform sentiment analysis on the articles to detect emotions like joy, sadness, or anger.

## Installation

To run this project, follow the steps below:

### Clone the Repository

```bash
git clone https://github.com/yourusername/news-scraper-nlp.git
cd news-scraper-nlp

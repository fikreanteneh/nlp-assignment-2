# Amharic News Classification

This project focuses on classifying Amharic news articles into six distinct categories.

- ሀገር አቀፍ ዜና (National News)
- መዝናኛ (Entertainment)
- ስፖርት (Sports)
- ቢዝነስ (Business)
- አለም አቀፍ ዜና (World News)
- ፖለቲካ (Politics)

### Resources

- [Site For Testing Esaily](https://nlp-assignment-2-1.onrender.com/)
- [The News Dataset on Hugging Face](https://huggingface.co/datasets/fikreanteneh/Amharic-News-Classification)
- [Finetuned Classifier Model on Hugging Face](https://huggingface.co/fikreanteneh/AmharicNewsClassifier/tree/main)
- [GitHub Repository](https://github.com/fikreanteneh/nlp-assignment-2)

## Inspiration

This Amharic News Classifier draws inspiration from the research paper, "[An Amharic News Text Classification Dataset](https://arxiv.org/pdf/2103.05639)" by Israel Abebe Azime and Nebil Mohammed. The paper emphasizes the challenges of performing text classification in low-resource languages like Amharic due to the lack of labeled data. It introduces a dataset of over 50,000 news articles categorized into six classes, offering a baseline for classification tasks using simple models such as Naive Bayes with Count Vectorizer and TF-IDF.

We used the same dataset for our classification task and finetuned XLM RoBERTa, a Transformer model, for Amharic news classification. XLM RoBERTa is the only model we found that is trained on Amharic language. The model was pretrained on 100 different languages, including Amharic, and has over 200 million parameters.

Unlike traditional models like Naive Bayes, which rely on simple text features such as word counts or TF-IDF, XLM RoBERTa leverages deep learning and contextual embeddings to deliver superior performance on sequence classification tasks. This makes it an ideal choice for Amharic, where labeled datasets are scarce, and more robust models are needed.

In this project, we deployed three models, with XLM RoBERTa and the Naive Baye models from the paper.

- XLM RoBERTa (Finetuned for Classification on Amharic News)
- Naive Bayes with Count Vectorizer
- Naive Bayes with TF-IDF

## Dataset

Dataset is Available at: [Amharic News Dataset on Hugging Face](https://huggingface.co/datasets/fikreanteneh/Amharic-News-Classification)

The dataset consists of 50,706 news articles in the Amharic language, categorized into six classes:

- ሀገር አቀፍ ዜና (National News): 20,564 articles
- መዝናኛ (Entertainment): 3,873 articles
- ስፖርት (Sports): 9,812 articles
- ቢዝነስ (Business): 9,307 articles
- አለም አቀፍ ዜና (World News): 6,515 articles
- ፖለቲካ (Politics): 6,635 articles

It was collected from the following sources:

- Addis Admas: 1839 articles
- Addis Maleda: 847 articles
- Al-Ain Amharic: 887 articles
- Amhara MM: 2438 articles
- BBC Amharic: 816 articles
- Ethiopian Press: 5597 articles
- Ethiopian Reporter: 6280 articles
- Fana Broadcasting: 7700 articles
- Soccer Ethiopia: 8595 articles
- VOA Amharic: 6943 articles
- Walta: 8764 articles

### Preprocessing

**Normalization**: Applied character-level normalization to correct inconsistencies in the Amharic script (e.g., ጸሀይ and ፀሐይ). These characters represent the same word, but the Amharic language does not enforce a strict rule on which character to use. Therefore, we normalized them to a consistent character representation.

**Filtering**: Removed rows with missing values in the category column.

**Splitting**: Used an 80-20 split for training and testing, ensuring a diverse representation of categories in both subsets.

**Sample Data**

| headline                            | category | date              | views | link                                |
| :---------------------------------- | :------- | :---------------- | ----: | :---------------------------------- |
| የኦሊምፒክ ማጣሪያ ተሳታፊዎች የሚለዩበት ቻምፒዮና ... | ስፖርት     | January 14, 2021  |     2 | <https://www.press.et/Ama/?p=39481> |
| አዲስ ዘመን ድሮ...                       | መዝናኛ     | December 28, 2020 |     4 | <https://www.press.et/Ama/?p=38334> |

## Implementation Overview

We have implemented the following models:

1. [XLM RoBERTa (Pretrained and Finetuned)](#1-xlm-roberta-pretrained-and-finetuned)
2. [Count Vectorizer + Naive Bayes](#2-count-vectorizer)
3. [TF-IDF + Naive Bayes](#3-tf-idf)

### 1. XLM RoBERTa (Pretrained and Finetuned)

We fine-tuned the XLM-RoBERTa model developed by Facebook to classify Amharic news articles into six distinct categories. XLM-RoBERTa, a pre-trained multilingual language model supporting 100 languages, including Amharic, was chosen for its strong performance on multilingual text classification tasks.

To adapt the model to our task, we added a classification layer on top of the pre-trained XLM-RoBERTa model. The fine-tuning process was conducted on the Amharic news dataset.

During training, we used a batch size of 16, a learning rate of 5e-5, and a maximum sequence length of 512 tokens. Gradient accumulation with 4 steps was employed to handle memory constraints, and the model was trained for 5 epochs. Dynamic padding was implemented using a data collator to ensure efficient processing of variable-length input sequences.

The entire training and fine-tuning process utilized the Transformers library from hugging face. Once fine-tuned, the model was deployed on Hugging Face's model hub for easy access and integration into applications. We developed a API to serve the model, enabling real-time predictions on Amharic news articles.

### Evaluation Results

| Category                   | Precision  | Recall     | F1 Score   |
| -------------------------- | ---------- | ---------- | ---------- |
| ሀገር አቀፍ ዜና (National News) | 0.9113     | 0.8849     | 0.8979     |
| መዝናኛ (Entertainment)       | 0.8681     | 0.7315     | 0.7940     |
| ስፖርት (Sports)              | 0.9732     | 0.9932     | 0.9831     |
| ቢዝነስ (Business)            | 0.7129     | 0.7631     | 0.7372     |
| አለም አቀፍ ዜና (World News)    | 0.8984     | 0.9192     | 0.9087     |
| ፖለቲካ (Politics)            | 0.8378     | 0.8427     | 0.8402     |
| **Average**                | **0.8670** | **0.8557** | **0.8602** |

### 2. Count Vectorizer

### Evaluation Results

| Category                   | Precision | Recall   | F1 Score |
| -------------------------- | --------- | -------- | -------- |
| ፖለቲካ (Politics)            | 0.67      | 0.58     | 0.62     |
| ሀገር አቀፍ ዜና (National News) | 0.88      | 0.48     | 0.62     |
| ስፖርት (Sports)              | 0.96      | 0.94     | 0.95     |
| ዓለም አቀፍ ዜና (World News)    | 0.45      | 0.89     | 0.60     |
| ቢዝነስ (Business)            | 0.40      | 0.75     | 0.52     |
| መዝናኛ (Entertainment)       | 0.26      | 0.80     | 0.39     |
| **Average**                | **0.60**  | **0.74** | **0.62** |

### 3. TF-IDF

### Evaluation Results

| Category                   | Precision | Recall   | F1 Score |
| -------------------------- | --------- | -------- | -------- |
| ፖለቲካ (Politics)            | 0.55      | 0.75     | 0.63     |
| ሀገር አቀፍ ዜና (National News) | 0.93      | 0.47     | 0.63     |
| ስፖርት (Sports)              | 0.97      | 0.94     | 0.96     |
| ዓለም አቀፍ ዜና (World News)    | 0.66      | 0.73     | 0.69     |
| ቢዝነስ (Business)            | 0.37      | 0.83     | 0.52     |
| መዝናኛ (Entertainment)       | 0.23      | 0.84     | 0.36     |
| **Average**                | **0.62**  | **0.76** | **0.63** |

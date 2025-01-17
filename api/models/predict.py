import os
import re
import joblib

base_dir = os.path.dirname(os.path.abspath(__file__))
count_vectorizer_model = joblib.load(
    os.path.join(base_dir, 'count_vectorizer_nb_model.pkl'))
count_vectorizer = joblib.load(os.path.join(base_dir, 'count_vectorizer.pkl'))
tf_idf_vectorizer_model = joblib.load(
    os.path.join(base_dir, 'tf_idf_nb_model.pkl'))
tf_idf_vectorizer = joblib.load(
    os.path.join(base_dir, 'tf_idf_vectorizer.pkl'))

unique_label = ['ፖለቲካ', 'ሀገር አቀፍ ዜና', 'ስፖርት', 'ዓለም አቀፍ ዜና', 'ቢዝነስ', 'መዝናኛ']


def normalize_char_level_missmatch(input_token):
    rep1 = re.sub('[ሃኅኃሐሓኻ]', 'ሀ', input_token)
    rep2 = re.sub('[ሑኁዅ]', 'ሁ', rep1)
    rep3 = re.sub('[ኂሒኺ]', 'ሂ', rep2)
    rep4 = re.sub('[ኌሔዄ]', 'ሄ', rep3)
    rep5 = re.sub('[ሕኅ]', 'ህ', rep4)
    rep6 = re.sub('[ኆሖኾ]', 'ሆ', rep5)
    rep7 = re.sub('[ሠ]', 'ሰ', rep6)
    rep8 = re.sub('[ሡ]', 'ሱ', rep7)
    rep9 = re.sub('[ሢ]', 'ሲ', rep8)
    rep10 = re.sub('[ሣ]', 'ሳ', rep9)
    rep11 = re.sub('[ሤ]', 'ሴ', rep10)
    rep12 = re.sub('[ሥ]', 'ስ', rep11)
    rep13 = re.sub('[ሦ]', 'ሶ', rep12)
    rep14 = re.sub('[ዓኣዐ]', 'አ', rep13)
    rep15 = re.sub('[ዑ]', 'ኡ', rep14)
    rep16 = re.sub('[ዒ]', 'ኢ', rep15)
    rep17 = re.sub('[ዔ]', 'ኤ', rep16)
    rep18 = re.sub('[ዕ]', 'እ', rep17)
    rep19 = re.sub('[ዖ]', 'ኦ', rep18)
    rep20 = re.sub('[ጸ]', 'ፀ', rep19)
    rep21 = re.sub('[ጹ]', 'ፁ', rep20)
    rep22 = re.sub('[ጺ]', 'ፂ', rep21)
    rep23 = re.sub('[ጻ]', 'ፃ', rep22)
    rep24 = re.sub('[ጼ]', 'ፄ', rep23)
    rep25 = re.sub('[ጽ]', 'ፅ', rep24)
    rep26 = re.sub('[ጾ]', 'ፆ', rep25)
    # Normalizing words with Labialized Amharic characters such as በልቱዋል or  በልቱአል to  በልቷል
    rep27 = re.sub('(ሉ[ዋአ])', 'ሏ', rep26)
    rep28 = re.sub('(ሙ[ዋአ])', 'ሟ', rep27)
    rep29 = re.sub('(ቱ[ዋአ])', 'ቷ', rep28)
    rep30 = re.sub('(ሩ[ዋአ])', 'ሯ', rep29)
    rep31 = re.sub('(ሱ[ዋአ])', 'ሷ', rep30)
    rep32 = re.sub('(ሹ[ዋአ])', 'ሿ', rep31)
    rep33 = re.sub('(ቁ[ዋአ])', 'ቋ', rep32)
    rep34 = re.sub('(ቡ[ዋአ])', 'ቧ', rep33)
    rep35 = re.sub('(ቹ[ዋአ])', 'ቿ', rep34)
    rep36 = re.sub('(ሁ[ዋአ])', 'ኋ', rep35)
    rep37 = re.sub('(ኑ[ዋአ])', 'ኗ', rep36)
    rep38 = re.sub('(ኙ[ዋአ])', 'ኟ', rep37)
    rep39 = re.sub('(ኩ[ዋአ])', 'ኳ', rep38)
    rep40 = re.sub('(ዙ[ዋአ])', 'ዟ', rep39)
    rep41 = re.sub('(ጉ[ዋአ])', 'ጓ', rep40)
    rep42 = re.sub('(ደ[ዋአ])', 'ዷ', rep41)
    rep43 = re.sub('(ጡ[ዋአ])', 'ጧ', rep42)
    rep44 = re.sub('(ጩ[ዋአ])', 'ጯ', rep43)
    rep45 = re.sub('(ጹ[ዋአ])', 'ጿ', rep44)
    rep46 = re.sub('(ፉ[ዋአ])', 'ፏ', rep45)
    rep47 = re.sub('[ቊ]', 'ቁ', rep46)  # ቁ can be written as ቊ
    rep48 = re.sub('[ኵ]', 'ኩ', rep47)  # ኩ can be also written as ኵ
    return rep48


def preprocess_text(text):
    text = re.sub('[^\w\s]', '', text)  # Remove punctuation
    # Normalize character-level mismatches
    text = normalize_char_level_missmatch(text)
    return text


def count_vectorizer_predict(new_article):
    # Preprocess the input text
    preprocessed_article = preprocess_text(new_article)

    # Transform the text using the same CountVectorizer
    transformed_article = count_vectorizer.transform(
        [preprocessed_article]).toarray()

    predicted_class = count_vectorizer_model.predict(transformed_article)
    predicted_label = unique_label[predicted_class[0]]

    return predicted_label


def tf_idf_predict(new_article):
    # Preprocess the input text
    preprocessed_article = preprocess_text(new_article)

    # Transform the text using the same TF-IDF Vectorizer
    transformed_article = tf_idf_vectorizer.transform(
        [preprocessed_article]).toarray()

    predicted_class = tf_idf_vectorizer_model.predict(transformed_article)
    predicted_label = unique_label[predicted_class[0]]

    return predicted_label

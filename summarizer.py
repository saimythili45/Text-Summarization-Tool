import string


def summarize_article(text, num_sentences=3):
    """
    Summarizes an article by selecting the most important sentences
    based on word frequency.

    Parameters:
        text (str): The full article text.
        num_sentences (int): Number of top sentences to include in the summary.

    Returns:
        str: Summary of the article.
    """
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    sentence_scores = {}
    for sentence in sentences:
        sentence_words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
        score = sum(freq.get(word, 0) for word in sentence_words)
        sentence_scores[sentence] = score
      
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

  
    return '. '.join(top_sentences) + '.'


# Example usage
if __name__ == "__main__":
    article = """
    Artificial intelligence (AI) is transforming industries by automating tasks, enhancing decision-making,
    and enabling new capabilities. One of the major fields in AI is Natural Language Processing (NLP),
    which focuses on the interaction between computers and human language. NLP is used in applications
    such as chatbots, machine translation, sentiment analysis, and text summarization. With advances in
    machine learning and deep learning, NLP models are becoming increasingly sophisticated and capable of
    understanding context, tone, and intent. These developments promise to make communication between
    humans and machines more seamless than ever.
    """
    print("Original Length:", len(article), "characters")
    summary = summarize_article(article, num_sentences=3)
    print("Summary:\n", summary)

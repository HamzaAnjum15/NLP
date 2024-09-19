import spacy

print("\nHamza Anjum B20102048 Section B")

nlp = spacy.load("en_core_web_sm")

# Sample text
text = """
Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976. 
The company, headquartered in Cupertino, California, revolutionized personal computing with the Macintosh in 1984. 
As of 2024, Apple is one of the most valuable companies in the world, with a market capitalization of over $2 trillion.
"""

doc = nlp(text)

tokens = [token.text for token in doc]
sentences = list(doc.sents)
print("Tokens:", tokens)
print("\nSentences:")
for sent in sentences:
    print(sent)

lemmas = [token.lemma_ for token in doc]
print("\nLemmas:", lemmas)

print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

print("\nPOS Tags:")
for token in doc:
    print(f"{token.text}: {token.pos_} ({token.tag_})")

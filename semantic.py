import spacy



nlp = spacy.load("en_core_web_md")

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print("\nCat vs Monkey vs Banana")
# Cat vs Monkey - model noted that they were both animals and hence had the highest level of similarity
print(word1.similarity(word2)) 
# Banana vs Monkey - model must know that monkeys are fond of bananas and therefore a correlation shown 
print(word3.similarity(word2))
# Banana vs cat - very little correlation here and therefore lowest similarity level of all 3 of the comparisons 
print(word3.similarity(word1))


#My own example 
print("\nOwn Example")
item1 = nlp("rock")
item2 = nlp("stone")
item3 = nlp("music")
print(item1.similarity(item2)) 
print(item3.similarity(item2))
print(item3.similarity(item1))

# Run using en_core_web_sm
#   Userwarning given saying that model getting used has no word vectors loaded and so the similarity method will not necessarily compare the results against the correct thing and suggests using one of the larger models instead 
# The similarities provided are also much higher vs the en_core_web_md model




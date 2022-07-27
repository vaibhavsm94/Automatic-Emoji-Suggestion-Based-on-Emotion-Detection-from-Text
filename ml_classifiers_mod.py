# coding: utf-8
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify.naivebayes import NaiveBayesClassifier
import thread

documents_f = open("both_documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()


word_features_f = open("word_features_complete_train_bigrams.pickle", "rb")
word_features_bigrams = pickle.load(word_features_f)
word_features_f.close()


word_features_f = open("word_features_bothgrams.pickle", "rb")
word_features_hybrid = pickle.load(word_features_f)
word_features_f.close()


classifier_f = open("classifier_bothgrams.pickle", "rb")
hybrid_classifier = pickle.load(classifier_f)
classifier_f.close()

classifier_f = open("nb_complete_trained_bigrams.pickle", "rb")
bigram_classifier = pickle.load(classifier_f)
classifier_f.close()


def removal(sentence):
    sentence_list = []
    words = nltk.word_tokenize(sentence)
    characters = ["á", "\n", ",", "."]
    for w in words:
      for c in characters:
        if c in w: 
          break
      sentence_list.append(w)
    #new = ' '.join([i for i in s if not [e for e in characters if e in i]])
    #sentence_list.append(new)
    return sentence_list

# POS-TAGGER, returns NAVA words

def pos_tag(sentences):
    tags = [] # have the pos tag included
    nava_sen = []
    for s in sentences:
        s_token = nltk.word_tokenize(s)
        pt = nltk.pos_tag(s_token)
        nava = []
        nava_words = []
        for t in pt:
            if t[1].startswith('NN') or t[1].startswith('JJ') or t[1].startswith('VB') or t[1].startswith('RB') or t[1].startswith('CC') or t[1].startswith('IN') or t[1].startswith('UH') :
                nava.append(t)
                nava_words.append(t[0])
        tags.append(nava)
        nava_sen.append(nava_words)
    return tags, nava_sen
    
    
def find_features_hybrid(document):    
    words_single = word_tokenize(document)
    words_double = list(nltk.bigrams(words_single))
    words = words_single + words_double 
    features = {}
    for w in word_features_hybrid:
        features[w] = (w in words)
    return features
    
def find_features_bigrams(document):    
    words_single = word_tokenize(document)
    words_double = list(nltk.bigrams(words_single))
    words = words_single + words_double
    features = {}
    for w in word_features_bigrams:
        features[w] = (w in words_double)
    return features

   
def update(text,category):
                print text,"Update classifier"
                additional_words = word_tokenize(text) 
                #sent = removal(text)
		nava, sent_pt = pos_tag(text)               
                req_words_f = open("req_words_bothgrams.pickle","rb")
                req_words = pickle.load(req_words_f)
                req_words_f.close()
                for sen in sent_pt:
		 for s in sen:
 		  req_words.append(s)
		#req_words.extend(additional_words)
		all_words = nltk.FreqDist(req_words)
		word_features = all_words.keys()
		#data.append((word_tokenize(text),category))
		additional_feature = [(find_features_hybrid(text), category)]
		'''
		featuresets_f = open("","rb")
		featuresets = pickle.load(featuresets_f)
		featuresets_f.close()
		'''
		featuresets = [(find_features_hybrid(rev), category) for (rev, category) in documents]
		training_set = featuresets[:6000]
		training_set.extend(additional_feature)
		# Train it again
		classifier = NaiveBayesClassifier.train(training_set)
		save_classifier = open("nb_updated_classifier.pickle","wb")
                pickle.dump(classifier, save_classifier)
                save_classifier.close()
                
                


def categorise(text):
  words = word_tokenize(text)          
  bi = nltk.bigrams(words)
  needed_bigrams = [('not','happy'),('with','accident')]
  flag = 0
  for word in bi:
     for b in needed_bigrams:
         if b == word:
              flag = 1
              break
              
  if flag == 0:
         feats = find_features_hybrid(text)
         result = hybrid_classifier.classify(feats) 
         dist = hybrid_classifier.prob_classify(feats) 
  else:
         feats = find_features_bigrams(text)
         result = bigram_classifier.classify(feats)
         dist = bigram_classifier.prob_classify(feats)
  classes = ['joy', 'sadness', 'anger', 'shame', 'guilt', 'fear', 'disgust']
  prob = {}
  for cls in classes:
        prob[cls] = '%0.4f' % round(dist.prob(cls), 4)       
  return result,prob


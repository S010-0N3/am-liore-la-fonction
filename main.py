def tokenize(text_string, special_character, replacement_string,clean = False):
  cleaned_text = text_string
  for test_string in special_character:
    cleaned_text = cleaned_text.replace(test_string, replacement_string)
  cleaned_text = cleaned_text.lower()
  text_tokens = cleaned_text.split(" ")

  return text_tokens


def spell_check(vocabulary_file, text_file, special_characters=[",","!","'",".","\n"], replacement_string= ""):
  misspelled_words =[]
  vocabulary = open(vocabulary_file,"r",encoding="utf-8").read()
  text = open(text_file,"r",encoding="utf-8").read()

  print(vocabulary_file)
  print(text_file)

  tokenized_vocabulary = tokenize(vocabulary,special_characters,replacement_string)
  tokenized_text = tokenize(text,special_characters,replacement_string,True)

  for token in tokenized_text:
    if token not in tokenized_vocabulary and token != "":
      misspelled_words.append(token)

  return misspelled_words


###Tokenization du vocabulaire :
vocabulary = open("dico.txt","r",encoding="utf-8").read()

### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")

###tokenize
f = open("text.txt","r",encoding="utf-8")
text_string = f.read()

###Trouver les mot mal orthographier.
clean_characters = [".",",","'","\n"]
replacement = ""
tokenize_text = tokenize(text_string,clean_characters,replacement)

print(tokenize_text[0:10])

final_misspelled_words = spell_check(vocabulary_file="dico.txt",text_file ="text.txt")

print(final_misspelled_words)
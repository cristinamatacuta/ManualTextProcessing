import re

#function to read the chapter of the book
def read_book():
  #open and read the chapter
  with open("Sapir1921_chapter1.txt","r") as file_read:
    #save thechapter in a variable
    #return the variable
    my_file=file_read.read()
    return my_file

#function to read the stop words
def read_stop_words():
  #open and read the stop words
    with open("stopwordlist.txt", "r") as file_read2:
      #read the words and strip them of white space
        stop_words = [line.strip() for line in file_read2.readlines()]
      #return the stop words
        return stop_words


# fragment the sentences:

def get_sentences(text):
  #used regex to fragment the sentence, at punctuation mark
  #and spaces
  sentences = re.split(r'(?<=[.!?])\s+', text)
  # returned the fragmented sentences
  return sentences

#tookenize the words
#remove punctuation
def get_words(text):
  #reused the function for the sentences
  sentences=get_sentences(text)
  #initilized list to store the words
  words=[]
  
  #iterate through each sentence
  for sentence in sentences:
    #sentence words are obtained by breaking the sentence into word using re
    #the result is a list of lists
      sentence_words = re.findall(r'\b\w+(?:[-]\w+)*\b', sentence)
    #add the words in the words list that was initialized initially
      words.extend(sentence_words)
  #return the list of words
  return words


#customize a key to use in sorting the sentences

def count_words(sentence):
  #reused word tokenization
  words=get_words(sentence)
  #returned the lenght of the list words
  return len(words)

#function to get the longest sentence
def longest_sentence(text):
  #reused sentence fragmentation function
  sentences=get_sentences(text)

  #sort the sentences based on their lenght 
  #using the customzed key
  sentences.sort(key=count_words, reverse=True)

  #get the longest sentence using indexing 
  longest_sentence_in_text=sentences[0]

  return longest_sentence_in_text
  
#function to get the shortest sentence
#longest word
def longest_word(text):
  #reused the word tokenization function
  words=get_words(text)
  #sort the list based on lenght
  words.sort(key=len, reverse=True)
  #get the longest word using indexing
  longest_word_in_text=words[0]
  #returned the longest word
  return longest_word_in_text
  
def stop_words_removed(text):
  #saved the stop words in a list
    stop_words = read_stop_words()
  #reused the get words function to get the words
  #saved them in a list
    words=get_words(text)
  #list comprehension
  #used to remove the stop words from the list of words
    clean_words = [word for word in words if word.lower() not in stop_words]
  #returned the a list with words with stop words removed
    return clean_words
def named_entities_a_l(text):
  stop_words=read_stop_words()
  # Define a regular expression pattern to match named entities from A to L
  pattern = r'(?<!\n\n)(?<![.!?]\s)[A-L][a-z]\w*(?: [A-Z][a-z]\w*)*'

  #initialized an empty list
  matches = []
  #used re.findall to save in a list all words 
  #that match the pattern from the text
  matches1 = re.findall(pattern, text)

   #for each word that matches the pattern if the 
   #word is not a stop word append it to the list matches
  for match in matches1:
    if match.lower() not in stop_words:
        matches.append(match)


  # convert the list to a set to remove duplicates
  matches_set = set(matches)
  #convert the new set to a list
  matches_lst = list(matches_set)
  #sort the list alphabetically
  matches_lst.sort()

  #return the sorted list of matches
  return matches_lst


def named_entities_m_z(text):
  stop_words=read_stop_words()
  # Define a regular expression pattern to match named entities from A to L
  pattern = r'(?<!\n\n)(?<![.!?]\s)[M-Z][a-z]\w*(?: [A-Z][a-z]\w*)*'
  
  #initialized an empty list
  matches = []
  #used re.findall to save in a list all words 
  #that match the pattern from the text
  matches1 =re.findall(pattern, text)

  #for each word that matches the pattern if the 
  #word is not a stop word append it to the list matches
  for match in matches1:
    if match.lower() not in stop_words:
        matches.append(match)


  # convert the list to a set to remove duplicates
  matches_set = set(matches)
  #convert the new set to a list
  matches_lst = list(matches_set)
  #sort the list alphabetically
  matches_lst.sort()

  #return the sorted list of matches
  return matches_lst


#function to find out the 10 most used words
def ten_most_used_words(text):
  #saved the clean words in a variable
    words = stop_words_removed(text)
  #initialize a dictionary
    word_frequency = {}
  # iterating through each word from words
    for word in words:
        word_lower = word.lower()  # convert word to lowercase for case-insensitive counting
      #check if the word is in the dictionary
        if word_lower in word_frequency:
          #if yes value incremets with one
            word_frequency[word_lower] += 1
        else:#else the key is added to the dictionary
            word_frequency[word_lower] = 1
#sort the dictionary by value
    word_frequency_order = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
  #get the top 10 by taking the first 10 elements of the sorted dictionary
    top_ten_words = dict(word_frequency_order[:10])

  #iterate throuh the keys and values of the new created dictionary and print them
    for key, value in top_ten_words.items():
        print(key + " : " + str(value))


#main function for printing 
def main():
  #save in a variable the text
  text=read_book()

  #aestetics space
  print("\n"*3)
  
  #longest sentence in the text
  longest_sentence_in_text=longest_sentence(text)
  print("The longest sentence in the text is: \n")
  print(longest_sentence_in_text)

  print("\n"*2)
  
  #longest word in the text
  longest_word_in_text=longest_word(text)
  print("Longest Word in the text is \n")
  print(longest_word_in_text)

  print("\n"*2)

  #printing A-L named entities
  print("A-L Named Entities")
  names_a_to_l=named_entities_a_l(text)
  #unpack the elements of the list and print them
  #used as a separator the new line character
  print(*names_a_to_l, sep='\n')


  print("\n"*2)

  #printing M-Z named entities
  print("M-Z Named Entities")
  names_m_to_z=named_entities_m_z(text)
  #unpack the elements of the list and print them
  #used as a separator the new line character
  print(*names_m_to_z, sep="\n")

  print("\n"*2)#aestetics
  
  #print 10 most used words
  print("The top 10 most used words in the text based on their frequency are:", sep="\n") 
  ten_most_used_words(text)

#calling the main
if __name__ == "__main__":
 main() 

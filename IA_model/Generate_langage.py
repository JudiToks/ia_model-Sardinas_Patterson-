import random


def generate_word():
   length = random.randint(1, 7)
   word = ""
   for _ in range(length):
      bit = str(random.randint(0, 1))
      word += bit
   return word


def generate_language():
   num_words = random.randint(1, 10)
   language = "["
   for _ in range(num_words):
      word = generate_word()
      language += word + ", "
      language.strip()
   language = language[0:language.__len__()-2]
   language = language + "]"
   return language


def create_data():
   file = open('data.txt', 'w')
   for i in range(8000):
      file.write(generate_language() + "\n")
   file.close()
   
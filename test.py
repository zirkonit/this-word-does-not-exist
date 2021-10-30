from title_maker_pro.word_generator import WordGenerator
word_generator = WordGenerator(
  device="cpu",
  forward_model_path="<somepath1>",
  inverse_model_path="<somepath2>",
  blacklist_path="<blacklist>",
  quantize=False,
)

# a word from scratch:
print(word_generator.generate_word())

# definition for a word you make up
print(word_generator.generate_definition("rockerboy")) 

# new word made up from a definition
print(word_generator.generate_word_from_definition("a word that does not exist")) 
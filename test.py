from title_maker_pro.word_generator import WordGenerator
word_generator = WordGenerator(
  device="cpu",
  forward_model_path="forward-dictionary-model-v1",
  inverse_model_path="inverse-dictionary-model-v1",
  blacklist_path="blacklist.pickle",
  quantize=False,
)

# a word from scratch:
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())
print(word_generator.generate_word())

# definition for a word you make up
# print(word_generator.generate_definition("rockerboy")) 

# new word made up from a definition
print(word_generator.generate_word_from_definition("a word that does not exist")) 
print(word_generator.generate_word_from_definition("relating to or denoting the current geological age, viewed as the period during which human activity has been the dominant influence on climate and the environment")) 
print(word_generator.generate_word_from_definition("avid or frequent users of the social media application Twitter")) 
print(word_generator.generate_word_from_definition("(on the social media application Twitter) repost or forward (a message posted by another user)")) 
print(word_generator.generate_word_from_definition("remove (someone) from a list of friends or contacts on a social networking website:")) 
print(word_generator.generate_word_from_definition("the action or practice of sending sexually explicit photographs or messages via mobile phone")) 
print(word_generator.generate_word_from_definition("a word or phrase preceded by a hash sign (#), used on social media websites and applications, especially Twitter, to identify digital content on a specific topic")) 
print(word_generator.generate_word_from_definition("a person who uploads, produces, or appears in videos on the video-sharing website YouTube")) 
print(word_generator.generate_word_from_definition("a digital audio file made available on the internet for downloading to a computer or mobile device, typically available as a series, new instalments of which can be received by subscribers automatically.")) 
print(word_generator.generate_word_from_definition("a personal website or social media account where a person regularly posts short videos")) 

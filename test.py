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

# definition for a word you make up
# print(word_generator.generate_definition("rockerboy")) 

# new word made up from a definition
print(word_generator.generate_word_from_definition("spoil a photograph of (a person or thing) by unexpectedly appearing in the camera's field of view as the picture is taken, typically as a prank or practical joke"))
print(word_generator.generate_word_from_definition("the activity or sport of moving rapidly through an area, typically in an urban environment, negotiating obstacles by running, jumping, and climbing."))
print(word_generator.generate_word_from_definition("an exceptionally skilled and celebrated soccer player."))
print(word_generator.generate_word_from_definition("(on a website) an arrangement whereby access is restricted to users who have paid to subscribe to the site."))
print(word_generator.generate_word_from_definition("a person who makes jokes; a joker"))
print(word_generator.generate_word_from_definition("a type of cricket match in which each team has a single innings consisting of a maximum of twenty overs."))
print(word_generator.generate_word_from_definition("a way of paying for goods by debit or credit card whereby one enters one's personal identification number in an electronic device rather than signing a slip."))
print(word_generator.generate_word_from_definition("a shopping facility whereby a customer can buy or order goods from a store's website and collect them from a local branch"))
print(word_generator.generate_word_from_definition("remove unnecessary items from (an untidy or overcrowded place)"))
print(word_generator.generate_word_from_definition("a person who approaches passers-by in the street asking for subscriptions or donations to a particular charity"))

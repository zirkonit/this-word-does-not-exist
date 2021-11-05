from title_maker_pro.word_generator import WordGenerator
word_generator = WordGenerator(
  device="cpu",
  forward_model_path="forward-dictionary-model-v1",
  inverse_model_path="inverse-dictionary-model-v1",
  blacklist_path="blacklist.pickle",
  quantize=False,
)

# a word from scratch:
# print(word_generator.generate_word())

# definition for a word you make up
# print(word_generator.generate_definition("rockerboy")) 

# new word made up from a definition
phrases = ["basinogenal",
"twitterbot",
"friendedit",
"phonecams",
"hashtagline",
"tvrenturfers",
"microdisc",
"filthstream",
"backover",
"HDMI 3.0",
"assage",
"fovetail",
"referfleur",
"zaptown",
"rowdfund",
"fumblebombing",
"styledolusto",
"pedimento skiing",
"eighteen-strand puzzle",
"campsan",
"jerdy",
"subscription opt-in",
"nycch",
"short <|bd|> short",
"drawup",
"tendervert",
"pychous berry",
"sinkerfish",
"Rvibsoriasis",
"Orcinomella",
"smokeball",
"familiar.commee.",
"soprancy",
"bleinade",
"accompanyingly",
"fleshfold",
"mid-triftifties",
"Eurozonegate",
"Reopening <|bd|> Ireland",
"Euro-Atlantic International",
"Europeanist",
"Euro euro!",
"dialecticalitarianism",
"Bourbonanistism",
"rightsholdering",
"reforms <|bd|> realsession",
"nonappointed",
"Clintonian",
"floucher",
"baby boomersan",
"jobster",
"saleshay",
"tabline",
"chairoverstep",
"Ecstasyhead",
"grapeberry",
"groggasm",
"order <|bd|> declaration",
"snackfish",
"hairgloss day",
"infomercialist",
"echelp",
"webset",
"cornerpage",
"Goveray",
"azzis",
"war, intimidation, and sabotage",
"smasse",
"monetative",
"myguebio",
"dateproblem"]

for phrase in phrases:
  try:
    print(word_generator.generate_definition(phrase))
    # print(word_generator.generate_word_from_definition(phrase))
  except UnicodeEncodeError:
    continue

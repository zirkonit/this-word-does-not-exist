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
print(word_generator.generate_word_from_definition("a bright red edible berry widely cultivated in China, supposed to contain high levels of certain vitamins."))
print(word_generator.generate_word_from_definition("a very large mass of solid waste in a sewerage system, consisting especially of congealed fat and personal hygiene products that have been flushed down toilets"))
print(word_generator.generate_word_from_definition("an acute infectious disease caused by a coronavirus, with initial symptoms including fever and cough and in some cases progressing to pneumonia and respiratory failure. It was first recognized as an epidemic that began in China in 2002."))
print(word_generator.generate_word_from_definition("any of various single-stranded RNA viruses including the Norwalk virus and closely related viruses."))
print(word_generator.generate_word_from_definition("a cigarette-shaped device containing a nicotine-based liquid that is vaporized and inhaled, used to simulate the experience of smoking tobacco"))
print(word_generator.generate_word_from_definition("a close but non-sexual relationship between two men."))
print(word_generator.generate_word_from_definition("the explanation of something by a man, typically to a woman, in a manner regarded as condescending or patronizing"))
print(word_generator.generate_word_from_definition("a pale yellow edible fatty substance made by churning cream and used as a spread or in cooking"))
print(word_generator.generate_word_from_definition("excellent or impressive (used as a general term of approval)"))
print(word_generator.generate_word_from_definition("totally"))
print(word_generator.generate_word_from_definition("the decade from 2000 to 2009"))
print(word_generator.generate_word_from_definition("a term for the potential withdrawal of Greece from the eurozone (the economic region formed by those countries in the European Union that use the euro as their national currency)"))
print(word_generator.generate_word_from_definition("the withdrawal of the United Kingdom from the European Union:"))
print(word_generator.generate_word_from_definition("an economic and political association of certain European countries as a unit with internal free trade and common external tariffs."))
print(word_generator.generate_word_from_definition("an economic and political association of certain European countries as a unit with internal free trade and common external tariffs."))
print(word_generator.generate_word_from_definition("a person who is opposed to increasing the powers of the European Union."))
print(word_generator.generate_word_from_definition("the single European currency, which replaced the national currencies of France, Germany, Spain, Italy, Greece, Portugal, Luxembourg, Austria, Finland, the Republic of Ireland, Belgium, and the Netherlands in 2002. Nineteen member states of the European Union now use the euro."))
print(word_generator.generate_word_from_definition("any option regarded as an alternative to two extremes, especially a political agenda which is centrist and consensus-based rather than left- or right-wing"))
print(word_generator.generate_word_from_definition("the policies and principles advocated by former British Prime Minister Tony Blair"))
print(word_generator.generate_word_from_definition("a government policy of encouraging unemployed people and others receiving state benefits to find a job, for example by providing job training or paying a fee to employers"))
print(word_generator.generate_word_from_definition("promotion of a person's welfare, especially that of an addict, child, or criminal, by enforcing certain constraints on them, or requiring them to take responsibility for their actions."))
print(word_generator.generate_word_from_definition("(of a politician) departing from the official party line."))
print(word_generator.generate_word_from_definition("relating to or characteristic of the former US president Bill Clinton or his policies"))
print(word_generator.generate_word_from_definition("a brash, materialistic young woman of a type supposedly found in Essex or surrounding areas in the south-east of England."))
print(word_generator.generate_word_from_definition("the generation born after that of the baby boomers (roughly from the early 1960s to late 1970s), typically perceived to be disaffected and directionless:"))
print(word_generator.generate_word_from_definition("a person who is unemployed and looking for work."))
print(word_generator.generate_word_from_definition("a documentary following people in a particular occupation or location over a period of time"))
print(word_generator.generate_word_from_definition("a tabloid newspaper"))
print(word_generator.generate_word_from_definition("the practice in an office of allocating desks to workers when they are required or on a rota system, rather than giving each worker their own desk."))
print(word_generator.generate_word_from_definition("under the influence of the drug Ecstasy, typically with the result of feeling euphoric and affectionate"))
print(word_generator.generate_word_from_definition("a ready-mixed drink that resembles a soft drink but contains alcohol."))
print(word_generator.generate_word_from_definition("a pub that specializes in serving high-quality food"))
print(word_generator.generate_word_from_definition("a court order which can be obtained by local authorities in order to restrict the behaviour of a person likely to cause harm or distress to the public."))
print(word_generator.generate_word_from_definition("any of various chiefly marine fish that are widely caught for food."))
print(word_generator.generate_word_from_definition("a day on which everything seems to go wrong, characterized as a day on which one's hair is particularly unmanageable."))
print(word_generator.generate_word_from_definition("an expert or habitual user of the internet."))
print(word_generator.generate_word_from_definition("a toilet, especially an earth closet"))
print(word_generator.generate_word_from_definition("an information system on the internet which allows documents to be connected to other documents by hypertext links, enabling the user to search for information by moving from one document to another."))
print(word_generator.generate_word_from_definition("a set of related web pages located under a single domain name, typically produced by a single person or organization"))
print(word_generator.generate_word_from_definition("the introductory page of a website, typically serving as a table of contents for the site."))
print(word_generator.generate_word_from_definition("a regularly updated website or web page, typically one run by an individual or small group, that is written in an informal or conversational style."))
print(word_generator.generate_word_from_definition("Short Message (or Messaging) Service, a system that enables mobile phone users to send and receive text messages."))
print(word_generator.generate_word_from_definition("criminal activities carried out by means of computers or the internet."))
print(word_generator.generate_word_from_definition("sexual arousal using computer technology, especially by wearing virtual reality equipment or by exchanging messages with another person via the internet"))
print(word_generator.generate_word_from_definition("the use of computer technology to disrupt the activities of a state or organization, especially the deliberate attacking of information systems for strategic or military purposes"))
print(word_generator.generate_word_from_definition("irrelevant or unsolicited messages sent over the internet, typically to a large number of users, for the purposes of advertising, phishing, spreading malware, etc."))
print(word_generator.generate_word_from_definition("an overwhelming quantity of email messages sent to one address"))
print(word_generator.generate_word_from_definition("a simple cafe in which customers pay to use computer terminals to access the internet."))
print(word_generator.generate_word_from_definition("a problem with some computers arising from an inability of the software to deal correctly with dates of 1 January 2000 or later."))
print(word_generator.generate_word_from_definition("an electronic toy displaying a digital image of a creature, which has to be looked after and responded to by the ‘owner’ as if it were a pet."))

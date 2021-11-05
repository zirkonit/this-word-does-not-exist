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
phrases = ["a cigarette-shaped device containing a nicotine-based liquid that is vaporized and inhaled, used to simulate the experience of smoking tobacco", 
"a close but non-sexual relationship between two men.", 
"the explanation of something by a man, typically to a woman, in a manner regarded as condescending or patronizing", 
"a pale yellow edible fatty substance made by churning cream and used as a spread or in cooking", 
"excellent or impressive (used as a general term of approval)", 
"totally", 
"the decade from 2000 to 2009", 
"a term for the potential withdrawal of Greece from the eurozone (the economic region formed by those countries in the European Union that use the euro as their national currency)", 
"the withdrawal of the United Kingdom from the European Union:", 
"an economic and political association of certain European countries as a unit with internal free trade and common external tariffs.", 
"an economic and political association of certain European countries as a unit with internal free trade and common external tariffs.", 
"a person who is opposed to increasing the powers of the European Union.", 
"the single European currency, which replaced the national currencies of France, Germany, Spain, Italy, Greece, Portugal, Luxembourg, Austria, Finland, the Republic of Ireland, Belgium, and the Netherlands in 2002. Nineteen member states of the European Union now use the euro.", 
"any option regarded as an alternative to two extremes, especially a political agenda which is centrist and consensus-based rather than left- or right-wing", 
"the policies and principles advocated by former British Prime Minister Tony Blair", 
"a government policy of encouraging unemployed people and others receiving state benefits to find a job, for example by providing job training or paying a fee to employers", 
"promotion of a person's welfare, especially that of an addict, child, or criminal, by enforcing certain constraints on them, or requiring them to take responsibility for their actions.", 
"(of a politician) departing from the official party line.", 
"relating to or characteristic of the former US president Bill Clinton or his policies", 
"a brash, materialistic young woman of a type supposedly found in Essex or surrounding areas in the south-east of England.", 
"the generation born after that of the baby boomers (roughly from the early 1960s to late 1970s), typically perceived to be disaffected and directionless:", 
"a person who is unemployed and looking for work.", 
"a documentary following people in a particular occupation or location over a period of time", 
"a tabloid newspaper", 
"the practice in an office of allocating desks to workers when they are required or on a rota system, rather than giving each worker their own desk.", 
"under the influence of the drug Ecstasy, typically with the result of feeling euphoric and affectionate", 
"a ready-mixed drink that resembles a soft drink but contains alcohol.", 
"a pub that specializes in serving high-quality food", 
"a court order which can be obtained by local authorities in order to restrict the behaviour of a person likely to cause harm or distress to the public.", 
"any of various chiefly marine fish that are widely caught for food.", 
"a day on which everything seems to go wrong, characterized as a day on which one's hair is particularly unmanageable.", 
"an expert or habitual user of the internet.", 
"a toilet, especially an earth closet", 
"an information system on the internet which allows documents to be connected to other documents by hypertext links, enabling the user to search for information by moving from one document to another.", 
"a set of related web pages located under a single domain name, typically produced by a single person or organization", 
"the introductory page of a website, typically serving as a table of contents for the site.", 
"a regularly updated website or web page, typically one run by an individual or small group, that is written in an informal or conversational style.", 
"Short Message (or Messaging) Service, a system that enables mobile phone users to send and receive text messages.", 
"criminal activities carried out by means of computers or the internet.", 
"sexual arousal using computer technology, especially by wearing virtual reality equipment or by exchanging messages with another person via the internet", 
"the use of computer technology to disrupt the activities of a state or organization, especially the deliberate attacking of information systems for strategic or military purposes", 
"irrelevant or unsolicited messages sent over the internet, typically to a large number of users, for the purposes of advertising, phishing, spreading malware, etc.", 
"an overwhelming quantity of email messages sent to one address", 
"a simple cafe in which customers pay to use computer terminals to access the internet.", 
"a problem with some computers arising from an inability of the software to deal correctly with dates of 1 January 2000 or later.", 
"an electronic toy displaying a digital image of a creature, which has to be looked after and responded to by the ‘owner’ as if it were a pet."]

for phrase in phrases:
  try:
    print(word_generator.generate_word_from_definition(phrase))
  except UnicodeEncodeError:
    continue

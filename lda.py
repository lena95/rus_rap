import json
from gensim import corpora, models

with open('for_lda_pymorphy2.json', 'r', encoding='utf-8') as file:
    texts = json.load(file)

dictionary = corpora.Dictionary(texts)
dictionary.filter_extremes(no_below=1, no_above=0.7)
corpus = [dictionary.doc2bow(text) for text in texts]

lda = models.LdaModel(corpus, num_topics=10,
                      id2word=dictionary,
                      update_every=5,
                      chunksize=10000,
                      passes=100)
lda.show_topics()
lda.save('lda_pymorphy2.model')

topics_matrix = lda.show_topics(formatted=False, num_words=20)
print("Topics:")
for item in topics_matrix:
    print(item)

# Результаты обработки файла for_lda.json:

# Topics:
# (0,
#  [('жизн', 0.007569376), ('сво', 0.006806156), ('мир', 0.0060578203), ('люд', 0.0059849625), ('вер', 0.0058179046),
#   ('наш', 0.0042834077), ('кажд', 0.004246467), ('пок', 0.0038917342), ('все', 0.00387356), ('сил', 0.003390165),
#   ('бог', 0.0033693174), ('нам', 0.0031815032), ('стал', 0.0031753213), ('свет', 0.0031492333),
#   ('брат', 0.0029872076), ('пут', 0.0029515475), ('рук', 0.0028291084), ('одн', 0.0028127462),
#   ('глаз', 0.002788241), ('душ', 0.0027598834)])
# (1, [('че', 0.016046572), ('i', 0.010510571), ('yo', 0.0078255255), ('the', 0.006536205), ('a', 0.0061505055),
#      ('on', 0.0049407114), ('дава', 0.004653976), ('э', 0.0043100915), ('my', 0.004097153), ('me', 0.004057307),
#      ('it', 0.0038767348), ('and', 0.0036471877), ('говор', 0.0036002144), ('to', 0.003565932), ('s', 0.0034318552),
#      ('m', 0.0033739947), ('ху', 0.0031222678), ('is', 0.0029849822), ('in', 0.0027481962), ('ид', 0.0027099175)])
# (2, [('тво', 0.012271334), ('все', 0.010460019), ('прост', 0.010247782), ('мо', 0.009249248), ('теб', 0.0075250743),
#      ('глаз', 0.0062158415), ('тоб', 0.005926064), ('буд', 0.0058406373), ('зна', 0.005617251),
#      ('одн', 0.0055989777), ('сво', 0.0055766203), ('жизн', 0.0053042867), ('сердц', 0.0051787044),
#      ('друг', 0.0051345457), ('лиш', 0.0047756704), ('люб', 0.0046680206), ('ноч', 0.0046352306),
#      ('слов', 0.004559042), ('нам', 0.0045412625), ('любов', 0.0043149334)])
# (3, [('мо', 0.009818013), ('рэп', 0.00849791), ('все', 0.008285733), ('слов', 0.0046530548), ('пок', 0.004291819),
#      ('нам', 0.004188155), ('прост', 0.0040306947), ('ещ', 0.0038254077), ('сво', 0.003768059),
#      ('буд', 0.003716336), ('жизн', 0.0037093356), ('песн', 0.0034829006), ('наш', 0.0032918511),
#      ('кажд', 0.003175574), ('так', 0.0031666828), ('ваш', 0.0030745266), ('музык', 0.0030394709),
#      ('люд', 0.00282136), ('перв', 0.0027565693), ('сам', 0.002753199)])
# (4,
#  [('дела', 0.012998416), ('наш', 0.00737576), ('сво', 0.0062531857), ('кажд', 0.005656418), ('дава', 0.005136786),
#   ('нам', 0.0050817993), ('двига', 0.004902778), ('всем', 0.004784577), ('танц', 0.004295346), ('бит', 0.004224436),
#   ('кача', 0.0038990478), ('ак', 0.003734639), ('э', 0.003411792), ('рэп', 0.0033284705), ('ваш', 0.0030877197),
#   ('пок', 0.0030299681), ('голов', 0.0028115255), ('тем', 0.0026174474), ('клуб', 0.0025396813),
#   ('выш', 0.0025314004)])
# (5, [('волн', 0.0066411295), ('им', 0.005699862), ('город', 0.00547547), ('привет', 0.004935737),
#      ('паца', 0.004689538), ('ввид', 0.0045570075), ('наш', 0.0044905776), ('ак', 0.003984469),
#      ('дом', 0.0032997057), ('мод', 0.0032075294), ('ро', 0.0031478025), ('стенк', 0.0031333484),
#      ('ват', 0.0023620524), ('трит', 0.0023339055), ('лял', 0.0021042507), ('поня', 0.0019580326),
#      ('солнц', 0.0019026482), ('куб', 0.0017816088), ('чемода', 0.0017237044), ('шаг', 0.0016819149)])
# (6,
#  [('хоп', 0.010514767), ('хип', 0.010282907), ('рэп', 0.0057334406), ('любл', 0.005031193), ('люб', 0.0046099564),
#   ('город', 0.0036879058), ('ногга', 0.0031546715), ('клуб', 0.0029306023), ('бит', 0.0028293012),
#   ('москв', 0.0028071855), ('крут', 0.0027908785), ('крич', 0.0027231604), ('тво', 0.0025644551),
#   ('наш', 0.0025466473), ('дава', 0.0025267547), ('стил', 0.002500509), ('go', 0.002491202), ('сам', 0.0023811597),
#   ('ваш', 0.0023307311), ('мно', 0.0020927743)])
# (7, [('дом', 0.0063220104), ('мо', 0.00594932), ('так', 0.004535566), ('че', 0.0044897), ('нам', 0.0043744356),
#      ('район', 0.004060315), ('дел', 0.0037398015), ('пар', 0.003549353), ('кур', 0.0033047262),
#      ('дава', 0.0032642994), ('сво', 0.002909181), ('утр', 0.0029073337), ('все', 0.0028744193),
#      ('мам', 0.0028477663), ('паца', 0.002793178), ('помн', 0.0027703983), ('москв', 0.0027305789),
#      ('наш', 0.0026055158), ('рук', 0.0024227584), ('одн', 0.0024190333)])
# (8,
#  [('тво', 0.01692999), ('теб', 0.009351816), ('рэп', 0.007350007), ('баттл', 0.0045784838), ('пар', 0.0039088624),
#   ('сук', 0.0038567258), ('трек', 0.003719616), ('ваш', 0.0032790354), ('буд', 0.0031615451),
#   ('парен', 0.0030902743), ('прост', 0.0029534495), ('е', 0.0028721197), ('мо', 0.002848247), ('сво', 0.0027473432),
#   ('нужн', 0.002636237), ('дела', 0.0024973573), ('перв', 0.0024064395), ('так', 0.0023552983),
#   ('пок', 0.0023094139), ('раунд', 0.0022668224)])
# (9, [('рэп', 0.0161417), ('тво', 0.015193637), ('сво', 0.0081357425), ('мо', 0.0064990795), ('ваш', 0.0051548895),
#      ('сук', 0.00505446), ('теб', 0.0050508855), ('люб', 0.004474324), ('говор', 0.004439613),
#      ('прост', 0.003975548), ('ху', 0.003695244), ('нах', 0.0035016106), ('чита', 0.003495981),
#      ('дела', 0.0034210547), ('пох', 0.0034104201), ('русск', 0.003341228), ('зна', 0.0033246563),
#      ('так', 0.0033209021), ('че', 0.0032139292), ('всем', 0.0031731024)])


# Результаты обработки файла for_lda_pymorphy2.json

# Topics:
# (0, [('дым', 0.008040588), ('наш', 0.004300883), ('злой', 0.0028625159), ('рука', 0.0027046825), ('дать', 0.0025401495), ('пока', 0.0025305978), ('игра', 0.0024065967), ('рэп', 0.0023944115), ('битый', 0.002381483), ('go', 0.0021224583), ('сидеть', 0.0020569349), ('город', 0.0020124156), ('ум', 0.0019346322), ('слово', 0.0018032762), ('я', 0.0017695323), ('нога', 0.0017081), ('один', 0.0017050557), ('звезда', 0.0016519522), ('тони', 0.0015985807), ('вокруг', 0.0015900517)])
# (1, [('город', 0.005743424), ('наш', 0.004886588), ('весь', 0.0048688683), ('свой', 0.0037141286), ('рэп', 0.002959832), ('мир', 0.0029477025), ('мы', 0.0027434702), ('ваш', 0.002702564), ('каждый', 0.0026603895), ('новый', 0.0025305292), ('ещё', 0.0024280145), ('стиль', 0.0022813666), ('тот', 0.0021832718), ('хип', 0.002154288), ('рука', 0.0021147688), ('место', 0.0021049038), ('хоп', 0.0020902639), ('пока', 0.0019864198), ('самый', 0.0019608464), ('хуй', 0.0019289247)])
# (2, [('иметь', 0.005592974), ('наш', 0.0048232125), ('ввиду', 0.004211554), ('пам', 0.0036454727), ('пара', 0.0035975613), ('е', 0.003312414), ('оу', 0.0028129134), ('соня', 0.0026658417), ('продолжать', 0.0025221026), ('свой', 0.002501949), ('ау', 0.0023730625), ('никто', 0.0022867967), ('мой', 0.001873824), ('делать', 0.0018380746), ('двигать', 0.0018178495), ('рыжий', 0.0017875588), ('жить', 0.0016264165), ('давать', 0.0016118942), ('путь', 0.0015722254), ('стоять', 0.0015451204)])
# (3, [('весь', 0.010390155), ('ты', 0.009733516), ('твой', 0.009406942), ('мой', 0.0081019355), ('один', 0.00686717), ('знать', 0.0059006168), ('быть', 0.005806712), ('глаз', 0.0056293164), ('свой', 0.0054395334), ('просто', 0.0053968676), ('жизнь', 0.0052580703), ('день', 0.0050612073), ('время', 0.0048799594), ('хотеть', 0.00478417), ('мир', 0.004766569), ('тот', 0.004749181), ('любовь', 0.0047059916), ('небо', 0.0045387554), ('сердце', 0.0043530944), ('мы', 0.0043345504)])
# (4, [('—', 0.014862558), ('эй', 0.010142327), ('любить', 0.007874739), ('грязь', 0.0046048327), ('ноггано', 0.00427272), ('рука', 0.003943183), ('слышать', 0.0031017505), ('пом', 0.0029561825), ('зал', 0.0029136345), ('ди', 0.0028089862), ('понять', 0.0024997515), ('должный', 0.0024001186), ('заткнуться', 0.002220201), ('ощутить', 0.0020541542), ('кутуз', 0.0020397282), ('погнать', 0.0020069876), ('куб', 0.0019740998), ('наркотик', 0.0018954182), ('проклятый', 0.0018909929), ('вибрация', 0.001883225)])
# (5, [('i', 0.013990224), ('you', 0.010467823), ('a', 0.0094817085), ('ак', 0.009156804), ('the', 0.008275206), ('ла', 0.005403087), ('it', 0.005356414), ('my', 0.005197965), ('me', 0.0050998526), ('m', 0.005015557), ('s', 0.0049861763), ('and', 0.0046274285), ('to', 0.004272254), ('is', 0.00390435), ('витя', 0.0038195977), ('on', 0.003705931), ('don', 0.0036588842), ('чё', 0.0036065113), ('t', 0.0033932168), ('стиль', 0.0033660165)])
# (6, [('весь', 0.01492256), ('человек', 0.01147631), ('жизнь', 0.010023405), ('свой', 0.009120153), ('знать', 0.007921699), ('тот', 0.0076941727), ('каждый', 0.0057857344), ('жить', 0.00571937), ('хотеть', 0.005370407), ('мой', 0.0053616096), ('наш', 0.0053292136), ('стать', 0.0053021866), ('верить', 0.005247878), ('деньга', 0.005040776), ('видеть', 0.0048222137), ('быть', 0.0044583105), ('бог', 0.004373515), ('мир', 0.0041864766), ('делать', 0.0040609986), ('такой', 0.0039202822)])
# (7, [('ты', 0.014949786), ('хотеть', 0.008349294), ('твой', 0.0076499265), ('делать', 0.0072781616), ('любить', 0.0072620884), ('её', 0.006038281), ('такой', 0.0056387666), ('секс', 0.0049334927), ('девочка', 0.0046288343), ('детка', 0.004576624), ('клуб', 0.0045340075), ('милый', 0.00407936), ('просто', 0.0039993073), ('танцевать', 0.003944722), ('любовь', 0.0039055885), ('эй', 0.003780719), ('мы', 0.003777811), ('быть', 0.0037687293), ('друг', 0.003472763), ('один', 0.0032800203)])
# (8, [('рэп', 0.017638875), ('твой', 0.016830921), ('ты', 0.007792209), ('мой', 0.0069034006), ('весь', 0.0065035434), ('ваш', 0.0061230245), ('свой', 0.005955002), ('хотеть', 0.005520118), ('быть', 0.0054876534), ('трек', 0.0048711547), ('делать', 0.0041873353), ('знать', 0.004163761), ('хип', 0.004150117), ('просто', 0.004124902), ('хоп', 0.004037263), ('читать', 0.00373443), ('слово', 0.003590964), ('дать', 0.0035215488), ('пока', 0.003469197), ('парень', 0.0034242426)])
# (9, [('весь', 0.00880593), ('че', 0.0050386568), ('дом', 0.004658386), ('пацан', 0.0044206157), ('давать', 0.004099592), ('район', 0.0039157798), ('такой', 0.0034785138), ('мы', 0.0034441215), ('курить', 0.0033048561), ('дело', 0.0032217018), ('свой', 0.0031054777), ('наш', 0.0030471215), ('быть', 0.0029866216), ('тот', 0.0028908995), ('москва', 0.0028771919), ('один', 0.002846709), ('чё', 0.0026745435), ('пока', 0.0026068895), ('делать', 0.0025612828), ('идти', 0.002280078)])


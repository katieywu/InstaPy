#!/usr/local/bin/python
from instapy import InstaPy

# if you don't provide arguments, the script will look for INSTA_USER and INSTA_PW in the environment
session = InstaPy(username='katslaundry', password='cmykLTNBT95.')
session.login()

"""Comment util"""
# default enabled=False, ~ every  image will be commented on
session.set_do_comment(enabled=True, percentage=30)
session.set_comments(['Beautiful shot!', u"I really love the tones in this shot :black_heart:",
                      'Awesome - keep making cool work'])
session.set_dont_like(['#adulting', '#alone', '#americangirl', '#ariefmirna2015', '#armparty', '#asia', '#asiandick',
                       '#attractive', '#babyrp', '#bacak', '#badbitcztwerk', '#baddie', '#balenciaga', '#balls',
                       '#bang', '#bangbang', '#batikate', '#beaty', '#beautyblogger', '#belfie', '#bi', '#bigdickboy',
                       '#bikinibody',
                       '#bombshell', '#bootay', '#bootybounce', '#bra', '#brain', '#breast', '#buns', '#butt',
                       '#butts', '#cam', '#carving', '#catsau', '#cesitone', '#cheeky', '#citycentre',
                       '#commentschivettes', '#costumes', '#cph', '#cpr', '#csun', '#cumfession', '#curvesfordays',
                       '#curvy', '#damngirl', '#datass', '#date', '#dating', '#desk', '#direct', '#dm', '#dominant',
                       '#dripping', '#dutchgirl', '#dxb', '#easter', '#ebonyandivory', '#edm', '#edmbabes',
                       '#eggplant', '#eggplants', '#eggporn', '#elevator', '#escilepernatale', '#estellaseraphim',
                       '#everybodyisbeautiful', '#excitada', '#expose', '#fapstagram', '#feetofatlanta', '#fishnets',
                       '#foreplay', '#freakshow', '#freethenipple', '#gays', '#gilofashion', '#girlsonly', '#gloves',
                       '#goddess', '#hamishnadine', '#happythanksgiving', '#hardsummer', '#hijabiba', '#hooters',
                       '#hornyyyyyyasf', '#hotgirls', '#hotguy', '#hots', '#hottie', '#humpday', '#iamgay',
                       '#instagirl', '#instamood', '#istanbulgay#italiano', '#jugs', '#kansas', '#kickoff', '#kik',
                       '#kikgirl', '#kikmessenger', '#killingit', '#kissing', '#lesbian', '#lesbiansofinstagram',
                       '#lilmandingo', '#lingerie', '#lust', '#marcoreus', '#master', '#mebelim', '#medicina',
                       '#mexicangirl', '#mirrorphoto', '#mixedgirls', '#models', '#mr40club', '#mrsandmrsbordeaux',
                       '#mrtox', '#nacket', '#nasty', '#newyears', '#newyearsday', '#ngento', '#oovoo', '#petite',
                       '#piroka', '#pixie', '#poop', '#pornfood', '#printic', '#publicrelations', '#pushups', '#rack',
                       '#ravebabes', '#roleplay', '#russiangirl', '#russianmilf', '#saltwater', '#sexlife', '#shebad',
                       '#shesquats', '#shit', '#shower', '#single', '#singlelife', '#skype', '#slimthick', '#snap',
                       '#snapback', '#snapchat', '#snapchatgay', '#snapme', '#sokus', '#sopretty', '#spanishgirl',
                       '#sparklingnudes', '#stopdropandyoga', '#stranger', '#streetphoto', '#stud', '#submission',
                       '#sultry', '#sunbathing', '#swole', '#tag4like', '#takeitoff', '#teens', '#tgif', '#thatasstho',
                       '#thick', '#thought', '#todayimwearing', '#treviso', '#twerk', '#twerker', '#undies',
                       '#valentinesday', '#vatine', '#weed', '#weedstagram', '#weezmoney', '#wet', '#whitegirl',
                       '#woman', '#womancrushwednesday', '#women', '#workflow'])

"""Follow util"""
# default enabled=False, follows ~ every 10th user from the images
session.set_dont_include(['sydneywilsonnn','netalirich','thestylestatus','natalie.alysa','andreaxagain','danielledijkers','hanadp','akheiss','lejardintricote','caroberrylove','afterabby','lindseyalouie', 'simply.sami', 'browneyedtoast', 'eggcanvas', 'trulylaur', 'zoras_daughter', 'baileymbc', 'miiamata', 'misstarabelle', 'cookiecat.herine', 'livblankson', 'blackarrowblog', 'figtny', '_hollyt', 'thebrittkit', 'zhours', 'minimalist.aesthetics', 'krischerie', 'neonblush', 'dylanasuarez', 'reemkanj', 'vonvogue', 'cheraleelyle', 'moreelistyle', 'fig.1a', 'missannatai', 'andyheart', 'mypetitedilemma', 'icingandglitter', 'westelm', 'dromelot', 'city_fashion_blogger', 'stylish_stories_', 'xoxotsumi', 'lizaherlands_', 'irists', 'fashionfeaturesocial', 'cityinstills', 'the.ivory.fawn', 'nycbambi', 'the7pm', 'kiraamaa', 'beauxmondes', 'harperandharley', 'joanneeleanore', 'kristauffer', 'styledbyjackie', 'lillehoang', 'katherrinetaylor', 'her_editorial', 'cassiemasangkay', 'lydiajanetomlinson', 'oliviabynature', 'mija_mija', 'bardot', 'msbeltempo', 'julesdenby', 'bangbangnyc', 'jlisabethl', 'margasalomc', 'kaity_modern', 'viennawedekind', 'ozma_of_california', 'stephweizman', 'veganeatsnyc', 'jeannedamas', 't_canvas', 'glossier', 'melissaorons', 'jordanrisa', 'erica.maltz', 'kristywho', 'nettxyer13', 'flobreezyy', 'taylranne', 'honeynsilk', 'noanoir_', 'elisaschenke', 'imjennim', 'tiffwang_', 'thelustlistt', 'alyssa.lenore', 'rice_ink', 'itsdayslikethis', 'newyork_act', 'teale_talbot', 'bandier', 'hellowhitney', 'senseforstylebyina', 'emrata', 'joannahalpin', 'allanaramaa', 'thefashioncuisine', 'theglowedit', 'creativeecho', 'howdoyouwearthat', 'chrisellelim', 'seenbyhanna', 'cityhobbit', 'brittfabello', 'angrybaker', 'diannnnneee', 'tania_sarin', 'thetrottergirl', 'melissamale', 'alyssalyncholiviaculpo', 'emily_luciano', 'anaiseleni', 'songofstyle', 'cerealmag', 'kinfolk', 'alice_gao'])
session.set_upper_follower_count(limit=100000)
session.set_lower_follower_count(limit=500)
session.set_do_follow(enabled=False, percentage=11, times=1)

"""Like util"""
# # completely ignore liking images from certain users
# session.set_ignore_users(['random_user', 'another_username'])
# # searches the description and owner comments for the given words
# # and won't like the image if one of the words are in there
# session.set_dont_like(['food', 'eat', 'meal'])
# # will ignore the don't like if the description contains
# # one of the given words
# session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])

"""Unfollow util"""
# will prevent commenting and unfollowing your good friends
# session.set_dont_include(['friend1', 'friend2', 'friend3'])

"""Different tasks"""


# you can put in as much tags as you want, likes 100 of each tag
session.like_by_tags(["#seeyourcity", "#loves_nyc",
                      "#seekthesimplicity", "#liveunscripted",
                      "#darlingescapes", "#thatsdarling", "#thehappynow", "#theartofslowliving", "#aquietstyle",
                      "#verilymoment", "#postitfortheaesthetic", "#foreveryoung", "#visualsoflife", "#nycblogger",
                      '#ootdfash', '#outfitinspo', '#whatiwore', '#currentlywearing', '#fashiongram', '#fashionaddict',
                      '#nycblogger', '#nycstyle', '#fblogger', '#fashionblogger', '#asseenonme', '#todaysoutfit',
                      '#igstyle', '#fwis', '#pursuepretty', '#ootdshare', '#ootdwatch', '#outfitideas', '#styleblogger',
                      '#minimalove', '#bloggerfashion', '#stylediaries', '#fashioninspo', '#aboutalook',
                      '#wearthisnext', '#streetstyle', '#styleguide', '#womensweardaily', '#portraitmode',
                      '#fashionstatement', '#ootdmagazine', '#ootdsubmit', '#inspocafe', '#worldfashionstyles',
                      '#streetstyleluxe', '#minimalstreetstyle', '#fashionvoyage', '#classicoutfit', '#classiclook',
                      '#ootdstyle'], amount=15)


# session.like_by_tags(["#ootdfash", "#outfitinspo", "#whatiwore", "#currentlywearing", "#fashiongram",
#                       "#todaysoutfit", "#igstyle", "#fromwhereistand", "#pursuepretty", "#chasinglight", "#fashionista",
#                       "#ootdshare", "#ootdwatch", "#outfitideas", "#styleblogger", "#fblogger",
#                       "#minimalove", "#bloggerfashion", "#outfitinspiration", "#stylediaries", "#fashioninspo",
#                       "#aboutalook", '#wearthisnext', '#thatsdarling', '#styleguide', '#womensweardaily', '#portraitmode',
#                       '#fashionstatement', '#ootdmagazine', '#ootdsubmit', '#inspocafe', '#worldfashionstyles',
#                       '#streetstyleluxe', '#minimalstreetstyle', '#fashionvoyage', '#classicoutfit', '#classiclook',
#                       '#ootdstyle', '#personalstyle', '#minimalstyle', '#minimalfashion', '#bloggerlife',
#                       '#bloggerstyle', '#fashiondetails', '#fashiongoals', '#nycblogger', '#nycfashionblogger',
#                       '#streetfashion', '#streetstyleluxe', '#styleinspo', '#fashioninspo', '#styleinspiration',
#                       '#fashioninspiration', '#ootdsubmit', '#stylediary', '#detailsoftheday'],
#                      amount=15)

# For 50% of the 30 newly followed, move to their profile
# and randomly choose 5 pictures to be liked.
# Take into account the other set options like the comment rate
# and the filtering for inappropriate words or users

# session.set_user_interact(amount=2, random=False, percentage=65, media='Photo')
#
# session.unfollow_users(amount=90, onlyInstapyFollowed=True)
#
# session.follow_user_followers(["lindseyalouie",'kristengracelam',"caitlinmiyako"], amount=30,
#                               random=True, interact=True)

# session.like_by_feed(amount=100)

# unfollows 10 of the accounts your following -> instagram will only unfollow 10 before you'll be 'blocked
#  for 10 minutes' (if you enter a higher number than 10 it will unfollow 10, then wait 10 minutes and will continue then)

"""Ending the script"""
# clears all the cookies, deleting you password and all information from this session
session.end()

logo = print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = [
    "build",
    "baboon", 
    "camel", 
    "shark", 
    "banana",
    "deserve", 
    "absurd", 
    'structure', 
    'axiom', 
    'google', 
    'abstract', 
    'three', 
    'relation', 
    'faking', 
    'launch', 
    'random',
    'flopping',
    'galaxy', 
    'funny', 
    'exodus',
    "tailspin",
    "upset",
    "cardsharp",
    "tabletop",
    "jetport",
    "footlights",
    "backslap",
    "timeshare",
    "superscript",
    "sidewalk",
    "herself",
    "bookend",
    "eyesight",
    "thunderbolt",
    "takeoff",
    "fishpond",
    "allspice",
    "however",
    "underexpose",
    "superpower",
    "superhero",
    "throwaway",
    "supergiant",
    "watercraft",
    "daisywheel",
    "anytime",
    "standoff",
    "bellhop",
    "upward",
    "someplace",
    "bluebird",
    "eyeballs",
    "afterglow",
    "upstate",
    "also",
    "butterball",
    "racquetball",
    "foreshadow",
    "bookworm",
    "toolbox",
    "showoff",
    "airmen",
    "below",
    "weatherproof",
    "peppermint",
    "mainline",
    "moonbeam",
    "itself",
    "nowhere",
    "silversmith",
    "daybook",
    "shipbottom",
    "jumpshot",
    "pickup",
    "upstroke",
    "hamburger",
    "newsprint",
    "throwback",
    "wayward",
    "upturn",
    "ponytail",
    "alongside",
    "warehouse",
    "whitecap",
    "soybean",
    "bookkeeper",
    "intake",
    "weekday",
    "duckbill",
    "earring",
    "carsick",
    "turncoat",
    "faded",
    "right",
    "boundless",
    "obtainable",
    "flawless",
    "sleepy",
    "soft",
    "vague",
    "muddled",
    "extralarge",
    "giddy",
    "busy",
    "slim",
    "burly",
    "rural",
    "level",
    "delicious",
    "confused",
    "hesitant",
    "terrific",
    "combative",
    "ahead",
    "exciting",
    "acid",
    "guiltless",
    "prickly",
    "penitent",
    "quiet",
    "small",
    "petite",
    "selective",
    "abashed",
    "pale",
    "zippy",
    "flimsy",
    "free",
    "squeamish",
    "capricious",
    "aboard",
    "eminent",
    "teeny",
    "wealthy",
    "ritzy",
    "adhoc",
    "pleasant",
    "left",
    "large",
    "nice",
    "knotty",
    "oafish",
    "blue",
    "tense",
    "itchy",
    "scarce",
    "material",
    "yummy",
    "tacky",
    "educated",
    "dependent",
    "secondhand",
    "cuddly",
    "sharp",
    "past",
    "satisfying",
    "general",
    "average",
    "violet",
    "deeply",
    "wise",
    "exuberant",
    "trite",
    "temporary",
    "jumbled",
    "domineering",
    "rare",
    "historical",
    "useless",
    "grouchy",
    "narrow",
    "annoyed",
    "longing",
    "profuse",
    "lean",
    "truthful",
    "attractive",
    "closed",
    "cheerful",
    "male",
    "naughty",
    "huge",
    "chubby",
    "momentous",
    "receptive",
    "zonked",
    "melted",
    "hideous",
    "possessive",
    "squealing",
    "grateful",
    "crowded",
    "quizzical",
    "tangy",
    "zesty",
    "thoughtless",
    "innate",
    "thankful",
    "boiling",
    "gorgeous",
    "broken",
    "brief",
    "unique",
    "anxious",
    "nonchalant",
    "plastic",
    "chunky",
    "apathetic",
    "brainy",
    "sedate",
    "tawdry",
    "cynical",
    "beneficial",
    "different",
    "bumpy",
    "auspicious",
    "perfect",
    "righteous",
    "half",
    "wholesale",
    "recondite",
    "macho",
    "premium",
    "gullible",
    "forgetful",
    "overwrought",
    "previous",
    "vengeful",
    "spotless",
    "wanting",
    "enchanted",
    "abhorrent",
    "bizarre",
    "embarrassed",
    "direful",
    "hard",
    "obnoxious",
    "tense",
    "flippant",
    "ubiquitous",
    "shut",
    "disgusted",
    "hulking",
    "tranquil",
    "useful",
    "axiomatic",
    "delicate",
    "tasty",
    "alcoholic",
    "cool",
    "yellow",
    "moldy",
    "coherent",
    "faulty",
    "evanescent",
    "makeshift",
    "standing",
    "windy",
    "late",
    "good",
    "maniacal",
    "silly",
    "caring",
    "omniscient",
    "ugly",
    "parallel",
    "neat",
    "languid",
    "determined",
    "thick",
    "statuesque",
    "shocking",
    "exclusive",
    "futuristic",
    "steady",
    "fast",
    "draconian",
    "nimble",
    "legal",
    "drab",
    "violent",
    "safe",
    "threatening",
    "adventurous",
    "dispensable",
    "obscene",
    "entertaining"
    ]
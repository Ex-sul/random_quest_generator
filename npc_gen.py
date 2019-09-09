# MODULES IMPORTED
import random
from random import choice as rc

# LISTS - CHARACTER AND PERSONALITY
# CHARACTER TRAITS
# Good
traits1_char_is_good = ["angelic", "good-natured", "high-minded", "incorruptible", "magnanimous", "upright",
                        "upstanding", "saintly", "virtuous", "beneficent", "righteous", "blameless", "ethical",
                        "moral", "morally exemplary"]
traits1_char_not_good = ["demonic", "amoral", "barbaric", "brutal", "corrupt", "decadent", "destructive", "hateful",
                         "malicious", "sadistic", "sordid", "superficial", "vacuous", "venal", "nefarious", "vicious",
                         "wicked", "bad", "villainous"]

# Honorable, receiving or worthy of honor
traits2_char_is_honor = ["admirable", "dignified", "honorable", "noble", "praiseworthy", "laudable", "respected"]
traits2_char_not_honor = ["contemptible", "ignoble", "ignominious", "contemptible", "disgraceful", "dishonorable",
                          "infamous", "shameful"]

# Benevolent, Kind, Considerate
traits3_char_is_bene = ["benevolent", "caring", "compassionate", "conscientious", "considerate", "empathetic", "kind",
                        "protective", "respectful", "sensitive", "sweet", "sympathetic", "tolerant", "understanding",
                        "warm", "warm-hearted", "appreciative", "gracious"]
traits3_char_not_bene = ["cliquish", "malevolent", "insensitive", "cold", "cold-hearted", "callous", "cruel", "envious",
                         "jealous", "impudent", "inconsiderate", "insensitive", "mocking", "predatory",
                         "unappreciative", "uncaring", "ungrateful", "venomous", "tyrannical", "despotic", "imperious",
                         "authoritarian", "domineering", "high-handed", "possessive", "power-hungry", "suspicious",
                         "bossy", "paternalistic"]

# Humble
traits4_char_is_humble = ["humble", "modest", "self-critical", "self-effacing", "unpretentious"]
traits4_char_not_humble = ["immodest", "snobbish", "proud", "arrogant", "conceited", "egocentric", "haughty",
                           "narcissistic", "petty", "prideful", "self-righteous", "moralistic", "sanctimonious",
                           "pharisaical", "un-self critical", ]

# Chaste, Pure
traits5_char_is_pure = ["chaste", "prudish", "celibate", "pure"]
traits5_char_not_pure = ["lustful", "lewd", "lascivious", "unchaste", "sensual", "dissolute", "hedonistic",
                         "libidinous", "perverse", "licentious", "profligate", "provocative", "vile"]

# Just
traits6_char_is_just = ["fair", "just", "impartial", "equitable", "evenhanded", "fair-minded"]
traits6_char_not_just = ["unfair", "unjust", "sectarian", "biased", "partisan", "prejudiced", "fanatical"]

# Honest, Sincere
traits7_char_is_honest = ["genuine", "honest", "guileless", "forthright", "open", "direct", "transparent", "blunt",
                          "authentic", "sincere"]
traits7_char_not_honest = ["disingenuous", "dishonest", "beguiling", "deceptive", "artificial", "deceitful", "devious",
                           "false", "fraudulent", "insincere", "scheming", "sly", "crafty", "subtle"]

# Faithful, Loyal; Constant, Dependable
traits8_char_is_const = ["constant", "dedicated", "dutiful", "faithful", "loyal", "reliable", "responsible", "solid",
                         "stable", "steadfast", "steady", "trustworthy", "devoted", "unchanging"]
traits8_char_not_const = ["unfaithful", "faithless", "fickle", "arbitrary", "disloyal", "erratic", "irresponsible",
                          "lazy", "neglectful", "treacherous", "unreliable", "unstable", ]

# Merciful, Forgiving; Patient, Thick-skinned
traits9_char_is_forgive = ["forgiving", "patient", "uncomplaining", "thick-skinned", "merciful", ]
traits9_char_not_forgive = ["unforgiving", "vengeful", "angry", "pugnacious", "oversensitive", "whiny", "impatient",
                            "reactionary", "reactive", "resentful", "vindictive", ]

# Selfless, Self-Denying; Charitable, Helpful, Generous
traits10_char_is_charit = ["self-denying", "selfless", "ascetic", "generous", "helpful", "sharing", ]
traits10_char_not_charit = ["ungenerous", "unhelpful", "stingy", "miserly", "close-fisted", "greedy", "money-minded",
                            "opportunistic", "self-indulgent", "selfish", "thievish", "uncharitable", ]

# Brave
traits11_char_is_brave = ["heroic", "brave", "courageous", "daring", "fearless", "gallant", "gutsy", "stout"]
traits11_char_not_brave = ["cowardly", "dastardly", "anxious", "apprehensive", "base", "cowering", "caitiff",
                           "gutless", "jittery", "craven", "pusillanimous", "fainthearted", "nervous", "panicky"]

# Pious, Reverent
traits12_char_is_pious = ["pious", "reverential", "religious", "devout", "godly", "reverent", "god-fearing",
                          "churchgoing"]
traits12_char_not_pious = ["impious", "irreligious", "irreverent", "iconoclastic", "sanctimonious", "ungodly",
                           "godless"]

# Industrious, Hard-working
traits13_char_is_indust = ["punctual", "self-reliant", "focused", "hardworking", "busy", "diligent", "assiduous",
                           "laborious", "active", "attentive", "industrious", "productive", "eager", "studious",
                           "dutiful"]
traits13_char_not_indust = ["negligent", "procrastinating", "lazy", "apathetic", "inattentive", "indifferent",
                            "lackadaisical", "lethargic", "passive"]

# Compliant, Flexible; Obedient
traits14_char_is_flex = []
traits14_char_not_flex = []

# Self-Controlled
traits15_char_is_contr = ["restrained", "frugal", "disciplined", "self-controlled", "composed", "controlled",
                          "deliberate", "ordered"]
traits15_char_not_contr = ["unrestrained", "uninhibited", "undisciplined", "compulsive", "indiscreet", "unruly"]

char_traits_pos = []
char_traits_pos.extend(traits1_char_is_good)
char_traits_pos.extend(traits2_char_is_honor)
char_traits_pos.extend(traits3_char_is_bene)
char_traits_pos.extend(traits4_char_is_humble)
char_traits_pos.extend(traits5_char_is_pure)
char_traits_pos.extend(traits6_char_is_just)
char_traits_pos.extend(traits7_char_is_honest)
char_traits_pos.extend(traits8_char_is_const)
char_traits_pos.extend(traits9_char_is_forgive)
char_traits_pos.extend(traits10_char_is_charit)
char_traits_pos.extend(traits11_char_is_brave)
char_traits_pos.extend(traits12_char_is_pious)
char_traits_pos.extend(traits13_char_is_indust)
char_traits_pos.extend(traits14_char_is_flex)
char_traits_pos.extend(traits15_char_is_contr)

char_traits_neg = []
char_traits_neg.extend(traits1_char_not_good)
char_traits_neg.extend(traits2_char_not_honor)
char_traits_neg.extend(traits3_char_not_bene)
char_traits_neg.extend(traits4_char_not_humble)
char_traits_neg.extend(traits5_char_not_pure)
char_traits_neg.extend(traits6_char_not_just)
char_traits_neg.extend(traits7_char_not_honest)
char_traits_neg.extend(traits8_char_not_const)
char_traits_neg.extend(traits9_char_not_forgive)
char_traits_neg.extend(traits10_char_not_charit)
char_traits_neg.extend(traits11_char_not_brave)
char_traits_neg.extend(traits12_char_not_pious)
char_traits_neg.extend(traits13_char_not_indust)
char_traits_neg.extend(traits14_char_not_flex)
char_traits_neg.extend(traits15_char_not_contr)

# PERSONALITY TRAITS
# Social, Friendly, Extroverted; Charismatic
traits16_pers_is_social = ["leaderly", "charismatic", "persuasive", "teacherly", "accessible", "agreeable", "amiable",
                           "charming", "cheerful", "lively", "colorful", "companionable", "conciliatory", "cooperative",
                           "courteous", "discreet", "cultured", "ebullient", "elegant", "eloquent", "enthusiastic",
                           "exciting", "friendly", "fun-loving", "hearty", "humorous", "inoffensive", "lovable",
                           "mature", "personable", "polished", "popular", "sociable", "tasteful", "urbane", "vivacious",
                           "well-bred", "winning", "youthful", "amusing", "artful", "chummy", "formal", "glamorous",
                           "smooth", "stylish", "suave", "grand", "trendy", "gallant", "responsive", ]
traits16_pers_not_social = ["antagonistic", "inaccessible", "standoffish", "shy", "solitary", "gossiping", "defensive",
                            "creepy", "melodramatic", "flippant", "uncultured", "humorless", "rude", "unlovable",
                            "immature", "severe", "aloof", "bizarre", "bland", "contrary", "critical", "difficult",
                            "dry", "dull", "earthy", "enigmatic", "escapist", "extravagant", "freewheeling",
                            "inconspicuous", "individualistic", "private", "quiet", "quirky", "reserved", "retiring",
                            "sarcastic", "unceremonious", "abrasive", "abrupt", "always the victim", "antisocial",
                            "argumentative", "cantankerous", "charmless", "childish", "clumsy", "coarse", "complaining",
                            "condemnatory", "contemptuous", "crass", "crude", "cynical", "discouraging", "discourteous",
                            "disputatious", "disrespectful", "disruptive", "disturbing", "frightening", "gloomy",
                            "graceless", "grim", "hostile", "ill-mannered", "impish", "insulting", "intolerant",
                            "irascible", "irritable", "loquacious", "mannerless", "mawkish", "mealy-mouthed",
                            "meddlesome", "melancholic", "mischievous", "miserable", "moody", "morbid", "obnoxious",
                            "offhand", "pompous", "presumptuous", "pretentious", "prim", "scornful", "secretive",
                            "sedentary", "stiff", "tactless", "tasteless", "tense", "thin-skinned", "troublesome",
                            "unfriendly", "unimpressive", "unlovable", "unpolished", "odd", "ridiculous", ]

# Detail-oriented, Tidy, Alert
traits17_pers_is_detailed = ["scrupulous", "alert", "meticulous", "observant", "organized", "painstaking", "orderly",
                             "perfectionist", "planful", "pedantic", "clean", "neat", "tidy", ]
traits17_pers_not_detailed = ["thoughtless", "disorderly", "bewildered", "disorganized", "confused", "preoccupied",
                              "forgetful", "single-minded", "sloppy", "vague", "dirty", "messy", ]

# Forceful, Strong-Willed, Confident
traits18_pers_is_forceful = ["strong-willed", "assertive", "forceful", "competitive", "strong", "aggressive",
                             "demanding", "dominating", "stern", "strict", "courageous", "daring", "decisive",
                             "dynamic", "firm", "unflappable", "dauntless", "independent", "tough", "secure",
                             "confident", "outspoken", "physical", "masculine", "stubborn", "disobedient", "willful",
                             "unyielding", "uncooperative", "inflexible", "rigid", "dogmatic", "narrow-minded",
                             "adamant", "pigheaded", "obstinate"]
traits18_pers_not_forceful = ["gentle", "peaceful", "weak-willed", "wormy", "noncompetitive", "soft", "submissive",
                              "unaggressive", "undemanding", "vulnerable", "weak", "insecure", "overly repentant",
                              "conformist", "conventional", "mellow", "ordinary", "placid", "fawning", "flattering",
                              "self-effacing", "self-conscious", "timid", "panicky", "delicate", "dependent",
                              "desperate", "fearful", "anxious", "hesitant", "indecisive", "inert", "passive",
                              "inhibited", "neurotic", "effeminate", "twitchy", "casual", "subservient", "docile",
                              "tractable", "obedient", "flexible", "undogmatic", "compliant", "deferential",
                              "respectful", "amenable", "acquiescent", "governable", "obliging", "obeisant"]

# Ambitious
traits19_pers_is_ambit = ["self-improvement minded", "well-rounded", "ambitious", "purposeful", "hurried",
                          "self-sufficient", ]
traits19_pers_not_ambit = ["unambitious", "aimless", "complacent", "self-destructive", ]

# Trusting, Gullible, Not Guarded
traits20_pers_is_trusting = ["trusting", "impressionable", "gullible", "naive", "credulous", "naive", "unquestioning",
                             "unsuspicious"]
traits20_pers_not_trusting = ["cautious", "circumspect", "skeptical", "calculating", "paranoid", "questioning",
                              "doubtful", "mistrustful", "incredulous", "unconvinced", "suspicious"]

# Intelligent, Capable
traits21_pers_is_int = ["resourceful", "brilliant", "capable", "clever", "contemplative", "creative", "curious", "deep",
                        "educated", "efficient", "farsighted", "imaginative", "incisive", "innovative", "insightful",
                        "intuitive", "knowledgeable", "logical", "methodical", "objective", "perceptive", "precise",
                        "profound", "rational", "realistic", "reflective", "sage", "sane", "scholarly", "shrewd",
                        "skillful", "sober", "sophisticated", "studious", "systematic", "thorough", "well-read", "wise",
                        "witty", "cerebral", "complex", "articulate", "intelligent", "many-sided", "unfathomable",
                        "unfoolable", "open-minded"]
traits21_pers_not_int = ["shallow", "uneducated", "shallow-minded", "obtuse", "dim-witted", "simple",
                         "constantly mistaken", "foolish", "ignorant", "incurious", "irrational", "muddle-headed",
                         "one-dimensional", "one-sided", "opinionated", "shortsighted", "small-minded", "softheaded",
                         "stupid", "superstitious", "uncreative", "uncritical", "unimaginative", "unreflective", ]

# Energetic, Lively, Carefree; Idealistic, Impractial, Unserious
traits22_pers_is_liv = ["boisterous", "breezy", "adventurous", "venturesome", "very active", "careless", "energetic",
                        "optimistic", "passionate", "playful", "relaxed", "romantic", "idealistic", "imprudent",
                        "reckless", "obsessive", "absentminded", "frivolous", "silly", "indulgent", "noncommittal",
                        "fanciful", "easily distracted", "impractical", "unrealistic", "sentimental", "spontaneous",
                        "sporting", "dreamy", "daydreaming", "fiery", "flamboyant", "high-spirited", "idiosyncratic",
                        "intense", "modern", "emotional", "unpredictable", "whimsical", "zany", "excitable", "extreme",
                        "impulsive", "rowdy", ]
traits22_pers_not_liv = ["calm", "stolid", "unhurried", "discontented", "discouraged", "enervated", "pessimistic",
                         "plodding", "slow", "prudent", "adaptable", "anticipative", "clear-headed", "balanced",
                         "practical", "earnest", "serious", "stoic", "businesslike", "joyless", "impassive",
                         "impersonal", "predictable", "solemn", "unsentimental", "apathetic", ]

# Miscellaneous
traits23_pers_is_misc = ["patriotic", "family-oriented", "rustic", "political", "luddite", "old-fashioned", ]
traits23_pers_not_misc = ["unpatriotic", ]

pers_traits_pos = []
pers_traits_pos.extend(traits16_pers_is_social)
pers_traits_pos.extend(traits17_pers_is_detailed)
pers_traits_pos.extend(traits18_pers_is_forceful)
pers_traits_pos.extend(traits19_pers_is_ambit)
pers_traits_pos.extend(traits20_pers_is_trusting)
pers_traits_pos.extend(traits21_pers_is_int)
pers_traits_pos.extend(traits22_pers_is_liv)
pers_traits_pos.extend(traits23_pers_is_misc)

pers_traits_neg = []
pers_traits_neg.extend(traits16_pers_not_social)
pers_traits_neg.extend(traits17_pers_not_detailed)
pers_traits_neg.extend(traits18_pers_not_forceful)
pers_traits_neg.extend(traits19_pers_not_ambit)
pers_traits_neg.extend(traits20_pers_not_trusting)
pers_traits_neg.extend(traits21_pers_not_int)
pers_traits_neg.extend(traits22_pers_not_liv)
pers_traits_neg.extend(traits23_pers_not_misc)

all_traits_pos = []
all_traits_pos.extend(char_traits_pos)
all_traits_pos.extend(pers_traits_pos)

all_traits_neg = []
all_traits_neg.extend(char_traits_neg)
all_traits_neg.extend(pers_traits_neg)

all_traits = []
all_traits.extend(all_traits_pos)
all_traits.extend(all_traits_neg)

# LISTS - PROFESSIONS
prof_com = ["architect", "astrologer", "baker", "banker", "barber", "bee keeper", "brewer", "bell maker",
            "blacksmith", "bodyguard", "bookbinder", "butcher", "candlemaker", "carpenter", "cartographer", "cook",
            "courier", "dog trainer", "falconer", "farmer", "fletcher", "glassblower", "gravedigger", "grocer",
            "guard", "guild master", "harness maker", "herbalist", "horse trainer", "hunter", "innkeeper", "jeweler",
            "librarian", "locksmith", "lumberjack", "merchant", "messenger", "pilgrim", "sailor",
            "ship builder", "shipwright", "shoemaker", "soldier", "spinner", "stonemason", "tailor", "tavern keeper", "town crier",
            "weaver", "wine merchant", "cowherd", "swineherd", "gardener", "goatherd", "hawker", "peasant", "reaper",
            "serf", "hostler", "sheep-shearer", "thresher", "woodcutter", "lumberjack", "vintner", "woolcomber",
            "yeoman", "forester", "fowler", "gamekeeper", "master of hounds", "molecatcher", "rat catcher", "trapper",
            "leech-collector", "seaweed harvester", "oysterer", "pastrycook", "cooper", "scabbard maker", "hatter",
            "saddler", "chicken butcher", "purse maker", "buckle maker", "roofer", "rope maker", "tanner", "rug maker",
            "town's guard", "bleacher", "cutler", "knife sharpener", "glover", "bottler", "cobbler", "girdler",
            "armorsmith", "arrowsmith", "bladesmith", "bowyer", "merchant tailor", "miner", "swordsmith", "smelter",
            "blacksmith's striker", "arcane smith", "silversmith", "goldbeater", "spooner", "tinker", "alabasterer",
            "stabler", "basketmaker", "bonecarver", "book printer", "bricklayer", "builder", "buttonmaker",
            "cabinetmaker", "cartwright", "chainmaker", "charcoalburner", "cheesemaker", "clockmaker", "clothier",
            "coiner", "combmaker", "compass-smith", "confectioner", "corsetier", "ditch digger", "dog catcher", "dyer",
            "embroiderer", "engraver", "feltmaker", "furniture maker", "gemcutter", "gilder", "horner", "lacemaker",
            "lampwright", "lanternmaker", "leadworker", "linenspinner", "lutemaker", "mapmaker", "master builder",
            "miller", "miniaturist", "mint maker", "moneyer", "nailmaker", "netmaker", "oilmaker", "papermaker",
            "parchmenter", "perfumer", "pewterer", "pinmaker", "plasterer", "pot mender", "quarrier", "quilter",
            "reedmaker", "sailmaker", "saltboiler", "sawyer", "shingler", "siever", "sin-eater", "silk-dyer", "stonecarver",
            "stonecutter", "tapestrymaker", "tenter", "threadmaker", "tile maker", "wheelwright", "typefounder",
            "haberdasher", "hay merchant", "ironmonger", "oil merchant", "spice merchant", "pie seller", "stationer",
            "taverner", "archer", "bowman", "captain", "crossbowman", "guardsman", "pikeman", "scout", "sergeant",
            "sergeant-at-arms", "spearman", "siege engineer", "camp cook", "hermit", "pardoner", "bargeman", "mariner",
            "sea captain", "ship's captain", "navigator", "riverboat pilot", "courtier", "ship provisioner", "mathematician",
            "philosopher", "professor", "scribe", "tutor", "theologian", "restaurateur", "copyist", "bather", "porter",
            "attendant", "lawyer", "attorney", "dog trainer", "privy cleaner", "procurator", "quartermaster", "riveter",
            "royal food taster", "scullion", "stable hand", "valet", "wagoner", "water carrier", "weeper", "beggar",
            "transient", "squatter", "vagabond", "acolyte", "ale house keeper", "almsman", "anchorsmith",
            "ballast master", "blast furnace slagger", "boatswain", "bondman", "broker", "cane seller", "castrator"]
prof_com_m = ["barman", "ferryman", "fisherman", "monk", "priest", "plowman", "shepherd", "tillerman", "huntsman",
              "foundryman", "silk-dresser", "friar", "boatman", "waterman", "manservant", "butler", "groom",
              "groom of the stool", "potboy", "rag and bone man", "whipping boy"]
prof_com_f = ["bartender", "ferrywoman", "fisherwoman", "milkmaid", "nun", "priestess", "quilter", "seamstress",
              "wet-nurse", "dairymaid", "plowwoman", "shepherdess", "tillerwoman", "huntswoman", "foundrywoman",
              "silkmaid", "maid", "maidservant", "laundress", "scullery maid", "housewife", "alewife", "brewster"]
prof_gov = ["bailiff", "captain of the guard", "chamberlain", "chancellor", "chancery clerk", "coin stamper",
            "executioner", "jailer", "judge", "landlord", "royal treasurer", "sheriff", "steward", "tax collector",
            "toll keeper", "lancer", "diplomat", "constable", "exchequer", "herald", "keeper of the privy seal",
            "marshal", "master of the revels", "seneschal", "admiral", "solicitor", "alderman"]
prof_gov_m = ["host for foreign diplomats, ambassadors, and important travelers", "lord high steward", "watchman",
              "almanac man"]
prof_gov_f = ["hostess for foreign diplomats, ambassadors, and important travelers"]
prof_crime = ["arsonist", "assassin", "bandit", "blackmailer", "briber", "burglar", "con artist", "fence", "forger",
              "grave robber", "highway robber", "hired thug", "impostor", "kidnapper for ransom", "mercenary",
              "pickpocket", "poacher", "saboteur", "seller of contraband (drugs, weapons, cursed or magical objects)",
              "slaver", "spy", "temple robber", "thief", "unlawful dueler", "usurer (loan shark)", "vandal",
              "cutpurse", "murderer"]
prof_crime_m = ["warlock who curses people, places, or objects for money or worse compensation", "conman"]
prof_crime_f = ["courtesan", "prostitute", "harlot",
                "witch who curses people, places, or objects for money or worse compensation"]
prof_med = ["alchemist", "apothecary", "healer", "physician", "surgeon", "doctor", "leech", "sawbones", "herbalist"]
prof_med_f = ["midwife", "wise woman", "nurse"]
prof_art = ["bard", "calligrapher", "dancer", "glasspainter", "manuscript illuminator", "painter", "playwright",
            "poet", "sculptor", "storyteller", "tumbler", "artist's model", "fresco painter", "composer", "fiddler",
            "harper", "lutenist", "minstrel", "musician", "piper", "singer", "actor", "fool", "juggler", "jester",
            "troubadour"]
prof_high = ["aristocrat", "general", "royal adviser", ]
prof_high_m = ["baron", "bishop", "count", "duke", "king", "knight", "nobleman", "prince", "squire", "emperor",
               "archduke", "abbot", "cardinal"]
prof_high_f = ["baroness", "countess", "duchess", "high priestess", "lady", "noblewoman", "princess", "queen", "abbess",
               "empress", "archduchess", "dame",]

# CONSTITUTION AND APPEARANCE #
# -2 illnesses that do not disfigure #
con_2_ill = ["ague (malaria)", "bad blood (syphilis)", "biliousness (jaundice from liver disease)", "black fever",
             "blindness", "brain fever (meningitis)", "breakbone (dengue fever)", "canine madness (rabies)", "cholera",
             "cold plague", "consumption (tuberculosis)", "deafness", "diphtheria",
             "ecstasy (catalepsy marked by loss of reason)",
             "grocer's itch (skin disease caused by mites in sugar or flour)", "horrors (delirium tremens)",
             "jail fever (typhus)", "King's evil (tuberculosis of neck and lymph glands)", "lockjaw (tetanus)",
             "mania (insanity)", "mortification or mormal (gangrene)", "palsy", "paroxysms (convulsions)", "plague",
             "rickets", "scarlet fever", "severe dehydration", "St. Anthony's Fire (ergotism)",
             "St. Vitus' Dance or Viper's Dance (chorea)", "the flux (dysentry)", "the red plague (smallpox)",
             "the sacred disease or falling sickness (epilepsy)", "the shakes (Parkinson's)",
             "the sweating sickness (influenza)", "typhoid fever", "whooping cough", "winter fever (pneumonia)"]
con_2_ill_mag = ["curse", ]
con_2_ill_poor = ["brink of starvation", ]
con_2_ill_f = ["childbed fever (puerperal fever)"]
# -2 injuries that do not disfigure #
con_2_inj = ["fatal, non-magical wounds", "fatal, non-magical burns", ]
con_2_inj_mag = ["fatal magical wounds", "fatal magical burns", ]
# -2 illnesses that disfigure #
con_2_ill_disfig = ["apoplexy (paralysis due to stroke)", "leprosy", ]
# -2 injuries that disfigure #
con_2_inj_disfig = ["loss of arm", "loss of foot", "loss of hand", "loss of leg", ]
# -1 illnesses that do not disfigure #
con_1_ill = ["fatigue", "muteness", "mild dehydration", "light-headedness", "food poisoning", "eye infection",
             "joint aches", "chicken pox", "barrel fever (hangover)", "green fever (anemia)", "quincy (tonsillitis)",
             "screws (arthritis)"]
con_1_ill_poor = ["lice", "fleas", "bedbugs"]
# -1 injuries that do not disfigure #
con_1_inj = ["broken bone", "sprained ankle", "sprained wrist", "bruising", "lacerations", "loss of fingers",
             "loss of toes", "loss of tongue", "scarring from wounds", "scarring from burns",
             "scarring from skin infections", "minor, non-magical wounds", "minor, non-magical burns", "concussion",
             "animal bite", "dislocated shoulder", "sterility or infertility"]
con_1_inj_mag = ["minor magical wounds", "minor magical burns"]
# -1 illnesses that disfigure #
con_1_ill_disfig = ["skin infection", "scurvy"]
# -1 injuries that disfigure #
con_1_inj_disfig = ["loss of ear", "loss of an eye", "loss of teeth"]


# LISTS - QUIRKS


def q_jewel():
    jewelry_types = ["a ring", "a bracelet", "a necklace", "a locket", "an amulet", "an earring"]
    return random.choice(jewelry_types)


def q_obj():
    objects = ['trinket', 'artifact', 'ring', 'bracelet', 'necklace', 'locket', 'amulet', 'earring', 'coin',
               'coin purse',
               'pair of greaves', 'pair of gauntlets', 'pair of boots', 'helmet', 'breastplate', 'shield', 'sword',
               'dagger', 'knife',
               'cup', 'plate', 'spoon', 'needle', 'thread', 'thimble', 'spinning wheel', 'hatchet', 'staff',
               'spell focus',
               'vial', 'quiver', 'crystal', 'orb', 'rod', 'wand', 'blanket', 'cloak', 'bell', 'candle', 'book',
               'bottle',
               'map', 'scroll', 'chain', 'chalk', 'rope', 'shirt', 'pair of trousers', 'belt', 'button', 'hat',
               'reliquary',
               'emblem', 'hourglass', 'flask', 'hunting trap', 'leash', 'collar', 'ink well', 'quill', 'lamp', 'ladder',
               'magnifying glass', 'set of manacles', 'hand mirror', 'mirror', 'sheet of parchment',
               'bottle of perfume',
               'cooking pot', 'healing potion', 'robe', 'sack', 'whistle', 'pouch of powdered soap', 'spellbook',
               'spyglass',
               'tent', 'torch', 'tinderbox', 'mess kit', 'waterskin', 'whetstone', 'bow', 'rapier', 'abacus',
               'deck of cards',
               'set of dice', 'chess piece', 'letter', 'bone', 'tooth', 'tusk', 'antler', 'shard of glass',
               'mirror shard',
               'pebble', 'stone', 'nail', 'leaf', 'marble']
    return random.choice(objects)


def quirks_people(n):
    # Lists of people by relational proximity
    people_closest = []
    people_close = ["father", "mother", "brother", "sister", "son", "daughter"]
    people_less_close = ["grandfather", "grandmother", "cousin", "mentor", "benefactor", "benefactress", "enemy",
                         "rival", "friend", "childhood friend", "guardian", "patron", "patroness", "step father",
                         "step mother", "step brother", "step sister", "uncle", "aunt", "nephew", "niece", "nanny",
                         "ward",
                         "father-in-law", "mother-in-law", "brother-in-law", "sister-in-law"]
    people_least_close = ["traveler", "creditor", "lender", "employer", "superior", "employee", "subordinate",
                          "correspondent", "liason", "peer", "teacher", "student", "flatterer", "lackey",
                          "acquaintance", "colleague"]
    # Sorting closest people by gender
    if n.sex == "male":
        people_closest.extend(["wife", "beloved", "fiancée"])
    else:
        people_closest.extend(["husband", "lover", "suitor", "fiancé"])
    # Pool of people, weighted by relational proximity
    people_pool = []
    people_lists = [people_closest, people_close, people_less_close, people_least_close]
    people_pool.extend(random.choices(people_lists, weights=[40, 30, 20, 10])[0])
    random.shuffle(people_pool)
    p1 = people_pool.pop()
    # Making sure p1 and p2 aren't the same person
    if p1 in people_closest:
        people_pool.clear()
        people_lists = [people_close, people_less_close, people_least_close]
        people_pool.extend(random.choices(people_lists, weights=[40, 40, 20])[0])
        random.shuffle(people_pool)
        p2 = people_pool.pop()
    else:
        p2 = people_pool.pop()
    # Determining gender of p1
    if p1 in ["wife", "beloved", "fiancée", "mother", "sister", "daughter", "grandmother", "benefactress", "patroness",
              "step mother",
              "step sister", "aunt", "niece", "nanny"]:
        p1_subj = "she"
        p1_poss = "her"
        p1_obj = "her"
        p1_reflex = "herself"
    elif p1 in ["husband", "lover", "suitor", "fiancé", "father", "brother", "son", "grandfather", "benefactor",
                "patron",
                "step father", "step brother", "uncle", "nephew"]:
        p1_subj = "he"
        p1_poss = "his"
        p1_obj = "him"
        p1_reflex = "himself"
    else:
        p1_sex = random.choice(["male", "female"])
        if p1_sex == "male":
            p1_subj = "he"
            p1_poss = "his"
            p1_obj = "him"
            p1_reflex = "himself"
        else:
            p1_subj = "she"
            p1_poss = "her"
            p1_obj = "her"
            p1_reflex = "herself"

    return p1, p2, p1_subj, p1_poss, p1_obj, p1_reflex


def q_circ():
    circumstance_types = ["dead", "dying", "lost", "estranged", "much loved", "hated", "imprisoned", "falsely accused",
                          "banished", "distant", "nearby", "close", "indebted", "dangerous",
                          "troubled", "misunderstood", "erring", "concerned", "distressed", "wounded", "enchanted",
                          "enthralled", "spellbound", "cursed", "metamorphosed", "avenged", "vindicated", "acquitted",
                          "deceived", "disregarded", "neglected", "famous", "believed-to-be-dead", "drunken",
                          "believed-to-be-lost", "captured", "kidnapped", "insane", "mad", "homicidal", "murdered",
                          "self-destructive", "financially ruined", "returned", "found", "new", "undead", "cornered",
                          "desperate", "loving", "wonderful", "trustful", "loyal", "trusting", "gullible",
                          "happy", "newly resurrected", "recovering", "ailing", "convalescing", "penitent", "pious",
                          "reverent", "longsuffering", "persevering", "relentless", "frustrated", "patient", "prudent",
                          "scheming", "thoughtful", "selfless", "selfish", "intelligent", "foolish", "wise", "shrewd",
                          "delusional", "all-seeing", "vigilant", "callous", "infallible", "innocent", "magic-endowed",
                          "famous", "infamous", "well known", "little known", "secret", "stalwart", "sensitive",
                          "much maligned"]
    return random.choice(circumstance_types)


def q_orgs():
    organization_types = ["a guild of craftsmen", "a bard's college", "a college of magic", "a secret society",
                          "a school", "the royal guard", "the town's guard", "an army", "a team of legal experts",
                          "a royal court", "an acting troupe", "a society of magicians or jesters", "a gang of bandits",
                          "an enemy army", "a coven of witches", "a clan of vampires", "a cabal of usurpers",
                          "a group of conspirators", "a group of conspiracy theorists", "a group of assassins",
                          "a well-known spy network", "a rumored spy network", "a prostitution ring", "a church",
                          "a temple", "an order of priests and priestesses", "an order of monks and hermits",
                          "a group of royal advisers of an enemy", "a group of ambassadors and diplomats from an enemy",
                          "a foreign intelligence service", "an enemy intelligence service",
                          "the nation's intelligence ministry", "a merchants' guild", "a caravan of merchants",
                          "a group of missionaries", "a secret society of printers who hide ciphers in their books",
                          "an association of book-lovers", "the aristocracy", "a clan of gypsies",
                          "a group of street urchin and pickpockets", "a high-minded society of barbers",
                          "a secret school", "a fight club", "an association of doctors", "a charitable organization",
                          "an association of bankers and money-lenders", "a posse of bounty-hunters",
                          "a mercenary guild", "a society of librarians", "an association of scholars",
                          "a bards' college", "a group of scholars who study magic",
                          "a group of scholars who predict and prevent crimes involving magic",
                          "a group dedicated to eradicating magic and those who use it",
                          "an elitist group of educators who insist that everyone must learn magic",
                          "a traveling carnival", "a traveling circus", "a group of farmers",
                          "an association of horse-breeders",
                          "a group dedicated to the conservation or recovery of magic"]
    return random.choice(organization_types)


def q_magic():
    actions_toward_magic = ["detect", "identify", "dispel"]
    return random.choice(actions_toward_magic)


def q_familiar():
    familiars = ['bat', 'cat', 'crab', 'toad', 'frog', 'hawk', 'lizard', 'owl', 'snake', 'fish', 'rat', 'raven',
                 'spider', 'weasel']
    return random.choice(familiars)


def q_thinks():
    thinks_words = ["has discovered", "will soon discover", "is discovering", "is afraid", "fears", "was afraid",
                    "thinks", "knows", "suspects", "doesn't know", "has been told", "hopes", "is secretly relieved",
                    "has long suspected", "believes", "received a letter saying", "has been deceived to think",
                    "assumes"]
    return random.choice(thinks_words)


def q_places():
    places = ["place of birth", "home", "hometown", "native land", "village", "city", "kingdom", "country", "island",
              "ship", "nation",
              "land", "empire", "realm", "continent", "plane of existence"]
    return random.choice(places)


def q_places_lite():
    places = ['village', 'city', 'land', 'kingdom', 'empire', 'country', 'nation', 'army', 'island', 'continent',
              'plane of existence']
    return random.choice(places)


def quirk_gen(n):
    # VARIABLES
    subj = n.subj.capitalize()
    subj_l = n.subj
    poss = n.poss
    obj = n.obj
    reflex = n.reflex
    gender = n.gender
    org = q_orgs()
    isnt = "isn't"
    p1, p2, p1_subj, p1_poss, p1_obj, p1_reflex = quirks_people(n)
    circ = q_circ()
    circ_spc25 = random.choices([f" {circ} ", " "], weights=[75, 25])[0]
    circ_spc50 = random.choice([f" {circ} ", " "])
    circ_spc75 = random.choices([f" {circ} ", " "], weights=[25, 75])[0]
    circ_spc90 = random.choices([f" {circ} ", " "], weights=[10, 90])[0]

    ##################### but [    ] say ##############
    cannot_ = random.choice(['cannot', 'is unable to', 'refuses to', 'is afraid to', 'dares not', 'does not at first',
                             'is reluctant to', 'will not clearly', 'will not'])
    # VARIABLES CONT'D
    reaction_types = ["breaks out in hives", "has feelings of dread", "has feelings of unease", "experiences itching",
                      "experiences swelling of throat and difficulty breathing",
                      "experiences lightheadedness or confusion", "is inexplicably giddy", "is oddly euphoric",
                      "experiences temporary amnesia", "experiences permanent amnesia", "experiences aches and pains",
                      "has a heightened sense of smell", "has a hypersensitive nose", "starts crying uncontrollably",
                      "starts laughing uncontrollably", "experiences blindsight",
                      "experiences tickling sensations", f"hears ringing in {poss} ears", "experiences hallucinations",
                      "has visions", "sleepwalks or has night terrors", f"compulsively cleans {poss} body",
                      "has suicidal thoughts", "is catatonic or unresponsive", "has strange and vivid dreams",
                      f"experiences rapid weight {rc(['gain', 'loss'])}", "cannot sleep",
                      "experiences cold-stimulus headache (brain freeze)", "experiences rapid hair loss and recovery",
                      "is instantly awake, sober, and alert", "becomes suddenly disoriented", "is flammable",
                      "cannot speak without shouting", f"shocks everyone {subj_l} touches with static electricity",
                      "becomes frightened and doesn't recognize anyone", "cannot see people", "cannot see objects",
                      "becomes invulverable and harmless", "glows dimly in a wide radius",
                      f"magically and involuntarily changes {rc(['size', 'shape', 'hue', 'age'])}", "grows pale",
                      "has nosebleeds", "experiences a consistent magical effect",
                      "experiences a random magical effect",
                      f"involuntarily casts a {rc(['random', 'specific'])} spell", "becomes amorous",
                      f"is compelled to tell {rc(['the truth', 'lies'])}", "has seizures",
                      "experiences an aura with no accompanying seizure", "has sensations of drowning",
                      "experiences vertigo or sensations of falling", "looks obscured by shadow",
                      "is shinier and reflects light more intensely", "faints", "loses consciousness",
                      "grows increasingly tired", "loses every desire, appetite, purpose, and goal",
                      f"{rc(['ravenously hungry', 'has an unquenchable thirst', 'cannot eat or drink'])}",
                      "experiences racing thoughts, elevated mood, difficulty maintaining attention, and becomes hyperactively goal-directed",
                      "experiences synesthesia, seeing sounds as swirls of colored light"]
    reacts = random.choice(reaction_types)
    # ALONE
    quirks_1 = [f"{subj} wears too much jewelry",
                f"{subj} is always chewing",
                f"{subj} always has unkempt or disheveled hair",
                f"{subj} sneezes when nervous",
                f"{subj} is prone to correct people's grammar or spelling",
                f"{subj} has a nervous twitch",
                f"{subj} is able to {q_magic()} magic",
                f"{subj} {reacts} in the presence of magic",
                f"{subj} {reacts} in the presence of {rc(['mages', 'magic-users', 'people who can use magic'])}",
                f"{subj} {reacts} in the presence of invisible or undetected magic",
                f"{subj} {reacts} in the presence of magical beasts, races, or deities",
                f"{subj} {reacts} in places where magic has been done {rc(['recently', 'before'])}",
                f"{subj} {reacts} in places where magic {rc(['has never been done', 'has not been done recently', 'cannot be done'])}",
                f"{subj} {reacts} in the presence of death",
                f"{subj} {reacts} in ancient ruins, temples, and graveyards",
                f"{subj} {reacts} when near the followers of a certain {rc(['god', 'powerful being'])}",
                f"{subj} {reacts} near aberrations, fey folk, fiends, elementals, giants, shapechangers, and magical beasts",
                f"{subj} {reacts} when travelling over ground on which people have died",
                f"{subj} {reacts} when on ground in which people have been buried",
                f"{subj} {reacts} in {poss} own {q_places()}",
                f"{subj} {reacts} when {subj_l} casts spells",
                f"{subj} {reacts} when spells are cast on {obj}",
                f"{subj} {reacts} if {subj_l} maintains eye contact with anyone for more than a few seconds",
                f"{subj} {reacts} when the name of someone from {poss} past is spoken aloud",
                f"{subj} {reacts} in the presence of a particular member of the party",
                f"{subj} {reacts} when {rc(['indoors', 'outdoors'])}",
                f"{subj} {reacts} in the presence of {rc(['children', 'pets and familiars'])}",
                f"{subj} {reacts} if {subj_l} attempts to ride {rc(['a horse or other beast of burden', 'in a cart or wagon drawn by any type of beast of burden'])}",
                f"{subj} {reacts} {rc(['at dawn', 'at midday', 'at dusk', 'in the night'])}",
                f"{subj} {rc(['often', 'frequently', 'occasionally', 'sometimes'])} {reacts} {rc(['in summertime', 'in autumn', 'at wintertime', 'in the spring'])}",
                f"{subj} has two different-colored eyes",
                f"{subj} has a single lock of white hair (or a contrasting color)",
                f"{subj} stands and sits oddly erect",
                f"{subj} slouches and has poor posture",
                f"{subj} wears glasses or a monocle",
                f"{subj} is strangely agile and graceful",
                f"{subj} bites {poss} {rc(['nails', 'lips'])}",
                f"{subj} constantly fidgets and is unable to sit or stand still",
                f"{subj} talks {rc(['far too loudly', 'too quietly to be heard'])}",
                f"{subj} has allergies",
                f"{subj} raises {poss} voice at the end of every sentence like it's a question",
                f"{subj} has bad breath and is unaware of it",
                f"{subj} always covers {poss} mouth with {poss} hand when speaking or eating",
                f"{subj} is uncomfortable eating or drinking in front of people",
                f"{subj} walks an unusually long distance from others to relieve {reflex}",
                f"{subj} always seems to be sweating for no apparent reason",
                f"{subj} seems to have an insatiable appetite but is not overweight",
                f"{subj} never seems to eat anything but is not emaciated",
                f"{subj} always seems to be apologizing for something, even things outside {poss} control",
                f"{subj} is always apologizing but always seems insincere about it",
                f"{subj} cracks {poss} knuckles or joints",
                f"{subj} is constantly asking questions",
                f"{subj} has an oddly {rc(['shaped', 'colored', 'located', 'sized', 'magical'])} birthmark",
                f"{subj} has a birthmark that seems periodically to change locations",
                f"{subj} has a birthmark that appears to be {rc(['increasing', 'decreasing'])} in size",
                f"{subj} has double-jointed elbows or other joints that bend in an uncanny way",
                f"{subj} is {rc(['left-handed', 'ambidextrous'])}",
                f"{subj} strongly resembles someone {rc(['famous', 'the party knows', 'dead', 'in the party'])}",
                f"{subj} {rc(['sneezes', 'coughs', 'talks', 'eats and drinks', 'snores', 'walks'])} extremely loudly",
                f"{subj} laughs {rc(['silently', 'loudly', 'rapidly', 'slowly', 'in a high pitch', 'in a low pitch'])}",
                f"{subj} stands uncomfortably close to others while {rc(['talking', 'speaking'])} to them",
                f"{subj} stands unusually far away while {rc(['talking', 'speaking'])} to others",
                f"{subj} casually puts {poss} hand on others' shoulder or arm when talking to them",
                f"{subj} always speaks to others in a confidential manner, as if confiding important secrets to them",
                f"{subj} constantly squints but doesn't appear to have any vision problems",
                f"{subj} closes {poss} eyes while speaking about serious matters",
                f"{subj} asks people to close their eyes when {subj_l} is telling them a story",
                f"{subj} always holds the hand of the person {subj_l} is speaking to",
                f"{subj} appears happy or sad at inappropriate times",
                f"{subj} appears far away during social gatherings, as if thinking about someone else",
                f"{subj} always seems to be too hot",
                f"{subj} always seems to be too cold",
                f"{subj} is overly sensitive to offensive odors",
                f"{subj} is sensitive to moonlight but not sunlight",
                f"{subj} is always excusing {reflex} to go to the bathroom, perhaps suspiciously",
                f"{subj} always looks over {poss} shoulder while walking as if {subj_l} is afraid of being followed",
                f"{subj} has a strong foreign accent",
                f"{subj} is shedding a still-detectable accent",
                f"{subj} does not understand the common language spoken in the region",
                f"{subj} is mute, or wants others to believe {subj_l} is mute",
                f"{subj} is {rc(['pretending to be', 'going', 'used to be'])} deaf",
                f"{subj} is {rc(['pretending to be', 'going', 'used to be'])} blind",
                f"{subj} cannot experience pain and is prone to unnoticed cuts, bruises, and injuries",
                f"{subj} acts as if no one ever believes {obj}",
                f"{subj} always feels like {subj_l}'s being treated {rc(['fairly', 'unfairly', 'like a child', 'like royalty'])}",
                f"{subj} always speaks about {reflex} in the third person",
                f"{subj} is always muttering under {poss} breath",
                f"{subj} tries to use big words {subj_l} doesn't understand",
                f"{subj} dresses well for a {gender} of {poss} profession",
                f"{subj} dresses poorly for a {gender} with {poss} vocation",
                f"{subj} refers to events or information {subj_l} knows that others don't have and then pretends to be surprised when they say they haven't heard of it",
                f"{subj} always interrupts others telling stories to provide details left out, even if {subj_l} wasn't there",
                f"{subj} is always {rc(['carrying', 'reading', 'writing in', 'eyeing', 'concealing', 'perusing'])} a book",
                f"{subj} is always writing{random.choices([' secret ', ' official-looking ', ' public proclamation ', ' '], weights=[20, 15, 15, 50])[0]}letters and looking for messengers to hire",
                f"{subj} carries a secret {rc(['book', 'ledger', 'item'])} on {poss} person",
                f"{subj} is a hoarder and so finds it difficult to throw anything away",
                f"{subj} has difficulty sleeping",
                f"{subj} is afraid of water",
                f"{subj} is afraid of heights",
                f"{subj} has a fear of insects, spiders, and snakes",
                f"{subj} is afraid of {rc(['dogs', 'cats', 'mice', 'horses', 'spiders', 'flying insects', 'wolves', 'pets', 'magical creatures', 'the undead', 'places where people have died'])}",
                f"{subj} is afraid of being {rc(['poisoned', 'enchanted', 'swindled', 'assassinated', 'sued', 'demoted or surpassed', 'charmed', 'attractive', 'forgotten', 'the object of a scandal'])}",
                f"{subj} always tries to avoid being overheard",
                f"{subj} is always {rc([f'sharpening {poss} weapons', f'practicing {poss} spells'])}",
                f"{subj} is hiding {poss} {rc(['weapon', 'spell focus'])}",
                f"{subj} is attempting (but failing) to conceal a {rc(['weapon', 'spell focus'])}",
                f"{subj} mispronounces a certain {rc(['word', 'phrase', 'name', 'spell', 'incantation'])} to an outrageous and comical degree",
                f"{subj} apologizes for swearing but can't seem to stop",
                f"{subj} whistles or makes bird calls",
                f"{subj} uses big words to try to impress people",
                f"{subj} doesn't speak much in private and not at all in group settings",
                f"{subj} never uses contractions like \"don't\" for \"do not\"",
                f"{subj} has a habit of giving people nicknames",
                f"{subj} often repeats one or more common sayings, e.g., \"Fortune favors the bold\"",
                f"{subj} hates being interrupted",
                f"{subj} will pause in the middle of saying something in order to recall a word that has slipped {poss} mind",
                f"{subj} often starts to tell a story but stops when {subj_l} realizes the story has no {rc(['point', 'conclusion', 'relevance'])} and then tries to hide {poss} embarrassment",
                f"{subj} argues with people who agree with {obj} as if {subj_l}'s not convinced they fully understand",
                f"{subj} is uncomfortable with silence and always tries to fill it up with something, even humming, tapping, or other irritating noises if necessary",
                f"{subj} always acts harried and busy even when {subj_l} has nothing to do",
                f"{subj} {rc(['taunts foes', 'is always trying to pick a fight'])}",
                f"{subj} hates confrontation and tries to keep the peace between hostile parties",
                f"{subj} gossips about people not present",
                f"{subj} refuses to be party to gossip",
                f"{subj} has a stutter",
                f"{subj} is overfond of using metaphors and similes",
                f"{subj} laughs at {poss} own jokes, even before {subj_l} has gotten the joke fully out",
                f"{subj} frequently references historical examples of {rc(['present situations', 'current events'])}",
                f"{subj} frequently talks to {reflex}",
                f"{subj} talks to inanimate objects",
                f"{subj} often interrupts others but gets upset when {subj_l} is interrupted",
                f"{subj} speaks with a poetic or literary flair",
                f"{subj} is reluctant to {rc(['speak', 'talk'])} about {reflex} or {poss} past",
                f"{subj} calls everyone \"sir\" or \"ma'am\", even children and animals",
                f"{subj} always talks of the good old days, even if there was nothing particularly good about them",
                f"{subj} always talks of the bad old days, even if there was nothing particularly bad about them",
                f"{subj} is afraid to speak ill of the dead",
                f"{subj} shows respect for tombstones and memorials",
                f"{subj} always seems tired but can always keep going",
                f"{subj} always seems full of energy but never gets much done or moves very quickly",
                f"{subj} is superstitious",
                f"{subj} likes the challenge of {rc(['completing a task', 'doing a job'])} with missing or makeshift supplies",
                f"{subj} has a cold heart that can be melted by youth, charm, passion, or idealism",
                f"{subj} is forgetful",
                f"{subj} has a habit of counting things",
                f"{subj} is prone to sit on tables, stand on chairs, or use furniture in otherwise unconventional ways",
                f"{subj} {rc(['enjoys', 'seeks out', 'delights in'])} the company of children",
                f"{subj} {rc(['dislikes', 'avoids', 'takes no pleasure in'])} the company of children",
                f"{subj} gets up before dawn",
                f"{subj} dislikes resting or going to bed",
                f"{subj} {rc(['enjoys', 'seeks out', 'delights in'])} the company of {rc(['mages', 'magic-users', 'people who can use magic'])}",
                f"{subj} {rc(['dislikes', 'avoids', 'takes no pleasure in'])} the company of {rc(['mages', 'magic-users', 'people who can use magic'])}",
                f"{subj} loses things easily, which turn up in unexpected places, possibly by magic",
                f"{subj} is always combing {poss} hair with {rc([f'{poss} fingers', 'a particular comb', 'a small brush'])}"
                f"{subj} avoids romantic entanglements because of a past heartbreak",
                f"{subj} thinks {subj_l} knows everyone's true motives, even after {subj_l} is corrected",
                f"{subj} plays a musical {rc(['instrument', 'instrument and can will that it magically play itself'])}",
                f"{subj} has a superb signing {rc(['voice', 'voice--one might even say that it is...enchanting'])}",
                f"{subj} is fond of riddles and logic puzzles.  Solving one will make {obj} agreeably disposed towards you",
                f"{subj} avoids social gatherings and is uncomfortable with people standing behind {obj}",
                f"{subj} is constantly arranging social gatherings in the fear of an uneventful evening, a prospect {subj_l} regards as unbearable",
                f"{subj} doesn't want to be left out of social gatherings and conversations",
                f"{subj} always tries to arrange social gatherings with {rc(['odd', 'interesting', 'unconventional', 'fantastical', 'historical', 'religious', 'grotesque', 'magical', 'absurd', 'surreal', 'ancient', 'educational'])} themes",
                f"{subj} is fond of maps, cartographers, and travel, and is looking for a party of travellers to tag along with",
                f"{subj} feels compelled to leave {poss} hometown and passionately wants to see the world",
                f"{subj} never wants to leave {poss} hometown for any reason",
                f"{subj} was banished from {poss} {q_places()} for {rc([f'a crime {subj_l} did not commit', f'a crime {subj_l} claims {subj_l} did not commit', f'a crime {subj_l} admits to having committed'])}",
                f"{subj} was banished from {poss} {q_places()} {rc(['for being a certain race or type of creature', 'for knowing magic', f'for the crimes of {poss} family', f'for being a member of an ousted royal or aristocratic family', 'after being framed for an assassination'])}",
                f"{subj} is concealing {rc(['magical', 'non-magical'])} scars with makeup",
                f"{subj} is presumed dead in {poss} {q_places()}",
                f"{subj} is thought to be dead and trying to remain {rc(['inconspicuous', 'hidden'])}",
                f"{subj} has a tendency to stare at people and stop breathing until {subj_l} is woken from {poss} reverie or passes out",
                f"{subj} doesn't realize that staring at people makes them uncomfortable and cannot seem to stop",
                f"{subj} never breaks eye contact during a conversation",
                f"{subj} says long goodbyes, even to people with whom {subj_l} is not particularly close",
                f"{subj} always says \"what?\", even though {subj_l} heard you; {subj_l} just hadn't processed what you said yet",
                f"{subj} is always looking around as if {subj_l} lost something, but nothing ever seems to be missing",
                f"{subj} has a magical sinus infection such that {poss} sinus cavity is inhabited by a sentient ooze",
                f"{subj} is always rolling a coin back and forth over {poss} knuckles",
                f"{subj} will not talk to or make eye contact with strangers until they are introduced",
                f"{subj} insists on being introduced to people {subj_l} doesn't know",
                f"{subj} breaks the ice with strangers by pretending to know them already or have seen them around",
                f"{subj} gets distracted while drinking and forgets to swallow; will squirt the drink out of {poss} nose if startled",
                f"{subj} sniffles a lot, even when healthy",
                f"{subj} always has to have something in {poss} hand",
                f"{subj} speaks in a monotone",
                f"{subj} speaks in {rc(['an exaggerated and dramatic way', 'multiple voices', 'different pitches'])}",
                f"{subj} is susceptible to gambling and taking bets and dares",
                f"{subj} engages complete strangers in conversation about a religion or cause {subj_l} feels strongly about",
                f"{subj} {rc(['thinks', 'believes', 'pretends', 'acts as if'])} {subj_l} has a profession or rank that {subj_l} doesn't have",
                f"{subj} {rc(['thinks', 'believes', 'pretends', 'acts as if'])} {subj_l} is another race or type of creature than {subj_l} is",
                f"{subj} believes {subj_l} has a profession that {subj_l} doesn't have",
                f"{subj} often feels like {subj_l} knows someone, although {subj_l} can't say where {subj_l} knows them from",
                f"{subj} is afraid of magic",
                f"{subj} distrusts people who use magic",
                f"{subj} is fascinated by {rc(['mages', 'magic-users', 'people who can use magic', 'wizards', 'sorcerers'])}",
                f"{subj} believes those who can use magic are {rc(['a cut above the rest', 'better than other people', 'superior to everyone else', 'more sophisticated'])}",
                f"{subj} believes those who use magic are compensating for something",
                f"{subj} has a drinking problem{rc([' and refuses to admit it', ' and wants to be freed from it', ''])}",
                f"{subj} becomes more social and talkative when drunk",
                f"{subj} becomes angrier when drunk",
                f"{subj} smokes a pipe {rc(['at dinner', 'with a long stem', 'in the evenings', 'with an oddly fragrant and sweet-smelling tobacco', 'without apparently having to put anything in it', f'that lights when {subj_l} inhales'])}",
                f"{subj} dislikes having to wear clothes",
                f"{subj} is always falling asleep at inopportune times",
                f"{subj} has trouble remembering {rc(['names but not faces', 'faces but not names', 'dates, events, and directions'])}",
                f"{subj} takes pride in the fact that {subj_l} has never seen a play, sporting event, public announcement, festival, or important event",
                f"{subj} takes pride in never missing a play, sporting event, public announcement, festival, or important event, if {subj_l} can help it",
                f"{subj} always assumes the best in people",
                f"{subj} always assumes the worst in people",
                f"{subj} has a slow and lumbering gait",
                f"{subj} always walks with purpose",
                f"{subj} is an excellent cook but always does it in private so that others can't see what {subj_l} is putting in the pot",
                f"{subj} can do magic tricks or sleight of hand but not real magic",
                f"{subj} gives children coins by pretending to make them appear from behind their ears",
                f"{subj} has a {rc(['high', 'low'])} tolerance for pain due to {rc([f'{poss} temperament', f'{poss} past', 'an enchantment', 'an injury'])}",
                f"{subj} knows how to ride a horse and is good at handling animals",
                f"{subj} is incapable of writing legibly {rc([f'because {poss} hand shakes', f'because {subj_l} uses the other hand, inexplicably'])}",
                f"{subj} {rc(['has', f'mistakenly thinks {subj_l} has'])} a serious debt problem",
                f"{subj} believes that {subj_l} is under a spell{rc([' ', ' but is not', f', and although it is not obvious at first, {subj_l} is', f' because {subj_l} is under a spell, the only effect of which is that {subj_l} thinks {subj_l} is under a spell'])}",
                f"{subj} claims to be under a {rc(['spell', 'curse'])}",
                f"{subj} never wears shoes or any kind of footwear",
                f"{subj} is never seen without {poss} {rc(['hat', 'spectacles', 'pet', 'purse of gold', 'weapon', 'spell focus', 'friend', f'an apple in {poss} hand', 'retinue'])}",
                f"{subj} dresses only in one color",
                f"{subj} always dresses in multiple colors",
                f"{subj} always pauses at the sight of {poss} own reflection, but not necessarily because {subj_l} is vain",
                f"{subj} tries to avoid seeing {poss} own reflection",
                f"{subj} has no reflection{rc(['', ' and does not know why', ' and will not say why'])}",
                f"{subj} wears clothes inappropriate for the {rc(['weather', 'temperature', 'occasion'])}",
                f"{subj} is always trying to take sips from a hidden flask without being noticed.  Someone who saw might assume it was alcohol, but it may be a magical potion or elixir",
                f"{subj} only reads {rc(['new', 'old'])} books",
                f"{subj} only reads books {rc(['by a certain author', 'in a particular language', ])}",
                f"{subj} is adept at {rc(['mathematics', 'geography and navigation', 'mechanics and invention', 'finances and record-keeping', 'acting and improvisation', 'Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation', 'alchemy', 'astrology', 'astronomy'])}"
                f"{subj} is vastly knowledgeable concerning the history of {rc(['magic', 'the world', 'religion', 'civilizations'])}",
                f"{subj} is a vegetarian but hates beans so much that {subj_l} would rather die than run through a field of them (as did the ancient mathematician, Pythagoras, according to legend)",
                f"{subj} dresses in surprisingly many layers, so that {subj_l} is actually much smaller than {subj_l} appears",
                f"{subj} hates not being in the know",
                f"{subj} actually prefers to be out of the loop and can't be bothered with the mundane affairs of others",
                f"{subj} is excessively {rc(['worried', 'concerned'])} about the end of {rc(['the world', 'a reign', 'a kingdom', 'an era'])} {rc(['and has good reason', 'and carries a certain letter as evidence', 'but just sounds paranoid', f'and is looking for someone to believe {obj}', f'and is used to people not believing {obj}'])}",
                f"{subj} likes to play cards and has a {rc(['special', 'magic'])} deck that {subj_l} keeps on {poss} person",
                f"{subj} refuses to believe in magic, even if {subj_l}'s witnessed it first-hand",
                f"{subj} makes sure everyone knows about {poss} dietary restrictions and dislikes",
                f"{subj} distrusts strangers",
                f"{subj} hates getting wet and will not go out in the rain or cross streams on foot",
                f"{subj} has a lisp and tries to avoid words that have the letter \"s\" in them",
                f"{subj} considers punching someone in the shoulder a sign of affection",
                f"{subj} pretends to be fluent in a language {subj_l} only knows a few words or phrases in",
                f"{subj} is fluent in many languages{rc(['', f'but does not know how {subj_l} learned them', f'but will not say where {subj_l} learned them'])}",
                f"{poss.capitalize()} eyes that don't point in the same direction, and it is difficult to {rc(['tell', 'know'])} where {subj_l}'s looking",
                f"{subj} has just been {rc(['poisoned', 'executed', 'put under a spell', 'married', 'imprisoned', 'killed', 'drowned', 'trampled to death', 'resurrected', 'healed'])}",
                f"{subj} was {rc(['poisoned', 'cursed'])} {rc(['a few moments', 'an hour', 'a few hours', 'two days', 'a few days', 'a week', 'a few weeks'])} ago and is fighting for {poss} life",
                f"{subj} was {rc(['poisoned', 'cursed'])} {rc(['a month', 'a few months', 'a year', 'a few years', 'ten years', 'nearly a lifetime'])} ago and is still fighting for {poss} life",
                f"{subj} has just now appeared in public, having been thought dead",
                f"{subj} has been arrested on the charge of {rc(['concocting a poison', 'brewing a potion', 'preparing a spell', 'beginning a ritual'])} with evil intent {rc(['but claims to have a perfectly reasonable explanation', f'and pled guilty, but claims that {poss} confession was coerced', 'and pled guilty, but the evidence points to someone else', 'but claims to have done no such thing', f'but claims {subj_l} is being framed', 'but expects to be released by powerful friends', 'but says this is all just a big misunderstanding', 'purposely in order to get close to someone already in prison', f'but refuses to say a word in defense of {reflex} or even to enter a plea'])}",
                f"{subj} does not know magic, and yet {subj_l} appears to be casting spells at random and doesn't know how to stop",
                f"{subj} is very slowly turning invisible{rc(['', ' from the extremities inward'])}--and starting to panic",
                f"{subj} {rc(['has', 'claims to have'])} no memory of the past {rc(['hour', 'few hours', 'day', 'two days', 'three days', 'week', 'month', 'year'])}",
                f"{subj} {rc(['seems', 'appears', 'claims'])} to have memories that don't belong to {obj}",
                f"{subj} has magical burns on {poss} skin but {cannot_} say how {subj_l} got them",
                f"{subj} has magical injuries but {cannot_} say how {subj_l} got them",
                f"{subj} denies that {subj_l} can use magic, despite suspicions to the contrary",
                f"{subj} claims to be able to use magic but {rc(['is', 'is apparently', 'is embarrassingly'])} unable to prove it",
                f"{subj} has been transformed into an animal and is desperately trying to communicate",
                f"{subj} often leans back against a wall or tree with one leg up, foot flat against it",
                f"{subj} enunciates {poss} words with increasing precision and intensity the angrier {subj_l} gets",
                f"{subj} has been {rc(['magically', 'alchemically'])} shrunken to the size of a {rc(['doll', 'thimble'])}",
                f"{subj} has been {rc(['magically', 'alchemically'])} enlarged to the size of a {rc(['horse', 'giant', 'house', 'tree'])}",
                f"{subj} is always covering {poss} mouth with {poss} hand when {subj_l} is not speaking",
                f"{subj} has been magically transported to another plane of existence.  {subj} is still visible in this one, but translucent, intangible, and mute",
                f"{subj} has just appeared covered in blood.  Upon inspection, it is not {poss} own",
                f"{subj} collapses to the ground in pain, cupping {poss} ears with {poss} hands.  {subj} does not speak without shouting and appears to be suffering from some extremely loud, continuous noise that no one else can hear",
                f"{subj} is standing nearby when {poss} exact duplicate shows up.  It is not obvious which one, if either, is real",
                f"{subj} has neither slept nor rested for {rc(['two', 'three', 'four', 'seven', 'fourteen', 'thirty', 'sixty', 'ninety'])} days, yet seems wide awake",
                f"believes in a {rc(['foreign', 'uncommon', 'little-known'])} deity",
                f"{subj} practices {rc(['an illegal religion', 'illegal magic'])} in secret",
                f"{subj} advocates for the legalization of a certain religion and so is under suspicion of practicing it {reflex}",
                f"{subj} advocates for the legalization of a certain spell or type of magic -- and so is suspected of knowing it",
                f"{subj} accidentally killed someone with magic as a child and has neither studied nor practiced it since",
                f"{subj} is thought by some to be the orchestrator of an elaborate and successful hoax that made {rc(['all magic', 'a certain type of magic', 'a certain religion'])} illegal in the region",
                f"{subj} was the victim of an attack that caused {rc(['all magic', 'a certain type of magic', 'a certain religion'])} to be outlawed in the region, though {subj_l} certainly did not wish for that result",
                f"{subj} was the victim of an attack that caused {rc(['all magic', 'a certain type of magic', 'a certain religion'])} to be outlawed in the region, which {subj_l} regards as an unlooked-for benefit",
                f"{subj} was a victim of an attack that caused magic to be outlawed in the region; so now {subj_l} has to practice it in secret",
                f"{subj} was the first of a number of people to suddenly and inexplicably gain the ability to use magic, and so {subj_l} is generally thought to be the catalyst or reason for it",
                f"{subj} brought magic to the region from afar",
                f"{subj} was granted a wish that {subj_l} would never again be able to experience physical pain--and is now prone to unnoticed scrapes, bruises, and injuries",
                f"{subj} once wished that {subj_l} would never be able to experience heartache again and is now incapable of feeling love, empathy, or guilt for any of {poss} actions",
                f"{subj} always seems embarrassed and tries not to look directly at anyone, since {subj_l} can see through everyone's clothes but can't do anything about it",
                f"{subj} has aims or ideals that are contrary to those of at least one member of the party but seems to be willing to work with the group in order to achieve a common goal",
                f"{subj} is a refugee from a recently destroyed {q_places_lite()}",
                f"{subj} is a spy sent ahead by an enemy.  Invasion is imminent",
                f"{subj} is presently in the form of a talking animal and cannot be convinced that {subj_l} wasn't always one",
                f"{subj} is, unbeknownst to the players, the identical twin of an NPC they already know",
                f"{subj} does not currently have the exercise of {poss} free will and is being controlled by {rc(['someone', 'something', 'a creature', 'a force', 'a group'])} hostile to the player characters",
                f"{subj} has just arrived from a {q_places_lite()} that {subj_l} claims has vanished by magic",
                f"{subj} claims that there is a nearby {rc([q_places_lite(), 'ghost town'])} that just appeared overnight",
                f"{subj} always sleeps facing {rc(['north', 'south', 'east', 'west'])} and keeps a compass with {obj} to make sure",
                f"{subj} is cursed with true prophecies of the future that no one believes.  The players' characters will have an opportunity to believe one of these prophecies, but only if they are very lucky with the dice",
                f"{subj} is cursed with prophetic {rc(['dreams', 'visions'])}.  Whenever {subj_l} tries to relate one of these prophecies, {subj_l} is forced to tell the exact opposite of the truth, an oddity which {subj_l} is unable to relate to others; they must discover it for themselves",
                f"{subj} is cursed with the inability to see the ground or the floor--and so is always tripping and falling down stairs",
                f"{subj} is in prison, but curiously, no one seems to know why, though they are certain {subj_l} belongs there.  They seem to be under a spell",
                f"{subj} finds daylight oppressive and immediately gets sunburned out of doors, a fact which others find suspicious",
                f"Because of a curse, {subj_l} is totally blind after sunset until dawn each day",
                f"{subj} is from a enchanted country where it is always {rc(['day', 'night', 'summer', 'winter'])}",
                f"{poss.capitalize()} mood is strongly dependent upon the weather",
                f"Because of a curse, {subj_l} always displays the emotion exactly the opposite of what {subj_l} is actually feeling",
                f"{subj} {rc(['hums', 'sings', 'twitches', f'drums {poss} nails', 'laughs', 'shivers', 'trembles', f'constantly clears {poss} throat', f'clicks {poss} tongue', f'smacks {poss} lips', f'wrings {poss} hands', f'shifts {poss} weight from one foot to the other', 'stands behind another party member', 'looks down', 'looks up', 'paces', f'clasps {poss} hands', f'cracks {poss} knuckles', 'dances about', 'frequently has to urinate', 'gives little involuntary shrieks'])} when nervous",
                f"{subj} is in possession of a painting that is alive.  It either grants a quest or poses a threat to the party, possibly both",
                f"{subj} is {rc(['spreading false rumors about', 'singing the praises of'])} the party",
                f"{subj} decides everything with a coin toss",
                f"{subj} hides things in unconventional and unexpected places",
                f"{subj} conceals {poss} money on {poss} person",
                f"{subj} was disappointed long ago by someone {subj_l} looked up to, and now doesn't look up to anyone",
                f"{subj} {rc(['receives', 'received', 'will receive'])} an unexpected gift: a cursed {q_obj()}",
                f"{subj} offers the party a gift that magically causes tensions in the group",
                f"{subj} offers the party a {q_obj()} that magically causes tensions in the group",
                f"{subj} is in possession of a treasure map leading to a magical treasure",
                f"{subj} is in possession of a treasure map leading to a magical {q_obj()}",
                f"{subj} is in possession of a magical {q_obj()}",
                f"{subj} is in possession of a treasure map that, unbenownst to {obj}, will actually lead {obj} into an ambush",
                f"{subj} is caught {rc(['eavesdropping on', 'following', 'staring at'])} the party",
                f"{subj} recently attended a {rc(['wedding', 'funeral', 'trial', 'festival'])} from which the party needs quest-related information",
                f"{subj} refuses to talk to {rc(['a certain member', 'any member', 'certain members'])} of your party, for reasons that may not be immediately obvious",
                f"{subj} {rc(['mistakes', 'pretends to mistake'])} a member of your party for someone {subj_l} knows",
                f"{subj} always seems to be present when {rc(['curious', 'dangerous', 'deadly'])} accidents happen (may be the perpetrator or the target, or else there are unknown forces at work)",
                f"{subj} falls immediately in love with a member of your party (whether naturally or magically is yet to be determined)",
                f"{subj} has an immediate hatred for one or more members of your party (is this impulse magical or natural, and do they have a history?)",
                f"{subj} seems to have all the {rc(['worst', 'best', 'the wrong kind of', 'the right kind of', 'weirdest'])} influences in {poss} life",
                f"{subj} always seems prone to failure, despite receiving a lot of support",
                f"{subj} succeeds in spite of massive {rc(['obstacles', 'handicaps', 'impediments', 'burdens', 'setbacks', 'resistance', 'opposition', 'unpopularity', 'hostility', 'competition', 'rivalry', 'conflict'])}",
                f"{subj} seems pressed for time",
                f"{subj} falls through the ceiling of the room your party is in",
                f"{subj} appears in the room with your party, even if the door was locked",
                f"{subj} is struggling mightily against a temptation that would destroy {rc([f'{obj}', f'someone {subj_l} cares about', f'something {subj_l} cares about'])}",
                f"{subj} is under a strange curse: {subj_l} has no thoughts of {poss} own but can only think the thoughts of the people around {obj} that would most approximate {poss} own",
                f"{subj} is under a terrible curse: {subj_l} has no thoughts of {poss} own but must think those of everyone around {obj}, both for good and for evil.  {subj} appears very confused and very disturbed",
                f"{subj} has a strange {rc(['curse', 'birth-trait'])}: darkness gives {obj} sunburn; sunlight makes {obj} pale",
                f"{subj} has finally learned to pick {poss} battles.  Unfortunately, {subj_l} fights all the least important ones",
                f"{subj} is in possession of a scroll on which is written very old magic in an ancient tongue",
                f"{subj} knows a secret way {rc(['through the city wall', 'out of the city', 'into the castle', 'into someplace the party wants to go', 'out of a clear and present danger for the party'])}",
                f"As it happens, the minds of all lay open to a powerful {rc(['creature', 'being', 'monster', 'wizard', 'group', 'clan', 'race of beings', 'organization'])} that can read and control thoughts.  Only {subj_l} knows how to create a mental barrier between the party and their danger",
                f"{subj} has the means to make amends with the authorities on behalf of the party for any wrongdoing (real or perceived) they have done",
                f"{subj} is swept away in a flash flood and will be presumed dead if the party doesn't save {obj}",
                f"{subj} has burn scars from a fire in which {subj_l} almost {rc(['died', 'perished'])} as a child.  As a result, {subj_l} is afraid of open flames",
                f"{subj} is lost in a thick fog that creeps over the land.  There are voices in the fog",
                f"{subj} is missing, like so many others, as a result of a mighty and mysterious storm that has swept through the region",
                f"{subj} lost {poss} home in {rc(['an earthquake', 'a mudslide', 'a tornado', 'a hurricane', 'a tropical storm', 'a flood', 'a military invasion', 'a volcanic eruption'])}",
                f"{subj} {rc(['refuses to', 'cannot', 'wishes to', 'can never', f'claims {subj_l} wants to', 'pretends to want to'])} return to {poss} own {q_places()}",
                f"{subj} is prone to pacing",
                f"{subj} has a large and impressive vocabulary",
                f"{subj} makes up acronyms for everything, but doesn't explain what they stand for{rc(['', ' unless asked', ', even when asked'])}",
                f"{subj} is a kleptomaniac{rc(['', ' but is unaware of it', ' and knows it', ' and tries to hide it', ' and cannot stop because of a curse'])}",
                f"{subj} has a phobia for anything {subj_l} perceives to be unclean",
                f"{subj} wears glasses but doesn't seem to need them.  Perhaps they are magical",
                f"{subj} memorizes whole books and large amounts of text without effort or even intending to",
                f"{subj} is always thirsty",
                f"{subj} is clumsy and constantly dropping and breaking things",
                f"{subj} refuses to travel by walking unless there is no other way",
                f"{subj} refuses to travel by any means other than walking unless it is absolutely necessary",
                f"{subj} loves symmetry",
                f"{subj} snores",
                f"{subj} changes {poss} clothes every day, if possible",
                f"{subj} has only one set of clothes that {subj_l} prefers to wear and so will try to wash them somewhere {subj_l} cannot be seen",
                f"{subj} constantly speaks in quotes and proverbs",
                f"{subj} is a mouth-breather",
                f"{subj} strongly prefers magic over technology or mechanical innovations",
                f"{subj} strongly prefers technology and mechanical innovations over the use of magic",
                f"{subj} thinks those who use magic are compensating for their weakness",
                f"{subj} thinks those who do not use magic are unintelligent and uncultured",
                f"{subj} is fascinated by the dead, lost civilizations, and forgotten magic",
                f"{subj} has a {rc(['small pet', 'familiar'])} that is always with {obj}",
                f"{subj} claims to have a {rc(['small pet', 'familiar'])}, though no one else can see or hear it",
                f"{subj} has a different {rc(['hair', 'eye'])} color every day",
                f"{subj} has a {rc(['different', 'much lighter', 'much darker'])} {rc(['hair', 'eye', 'skin'])} color {rc(['in low light', 'in darkness', 'indoors'])} than {subj_l} does in broad daylight",
                f"{subj} has a different {rc(['hair', 'eye'])} color depending upon {rc([f'{poss} mood', 'the weather', f'what direction {subj_l} is facing', f'{poss} proximity to magic'])}",
                f"{subj} is unable to have children{rc(['', ' and is searching for a cure', ' because of a hereditary curse', ' because of a family curse', ' because of a curse that plagues the land', f' because {subj_l} offended a powerful being', f' until {subj_l} completes a quest given to {obj} by a powerful being'])}",
                f"{subj} is often mistaken for someone else in public{rc(['', ', and so hates going out', ', and so loves to go out', f'; so {subj_l} tries to alter {poss} appearance'])}",
                f"{subj} is bad at navigating and predicting the {rc(['weather', 'temperature', 'terrain', 'length of journeys', 'time it takes to travel between places', 'dangers ahead'])}",
                f"{subj} has a knack for navigating and rarely gets lost, even in new surroundings",
                f"{subj} doesn't appear to be quite touching the ground, but the gap is barely perceptible",
                f"{subj} is affected by light differently.  The side of {obj} that should be lighted is in shadow and vice versa",
                f"{poss.capitalize()} appearance is less affected by light than others.  In bright light, {subj_l} doesn't appear as well-lit as everyone else; in low light, {subj_l} doesn't appear as dark",
                f"{subj} walks with a limp {rc([' and a cane', ' but without a cane'])}.  The limp goes away in specific situations, which causes some to think {subj_l} is faking it",
                f"{subj} prefers the company of people {rc(['older', 'younger', 'smarter', 'less intelligent', 'stronger', 'weaker', 'more attractive', 'less attractive', 'wealthier', 'poorer'])} than {subj_l} is"
                f"{subj} is able to comprehend metaphors, subtlety, and imprecision of speech, but prefers not to",
                f"{subj} has little patience for people who require others to speak with precision, correct grammar, and lofty words",
                f"{subj} often interjects with information of little value in order to seem useful",
                f"{subj} can hold {poss} breath indefinitely",
                f"{subj} thinks that surrounding oneself with {rc(['lead', 'gold', 'silver', 'tin', 'virgins', 'magic skeptics', 'bones', 'upright stones', 'oak trees', 'tuning forks', 'burning frankincense'])} can keep out unwanted magic and scrying eyes",
                f"{subj} thinks pouring water on someone can cure most minor ailments and stimulate the mind",
                f"{subj} has a superstitious fear of eating the meat of any animal {subj_l} didn't kill {reflex} or witness someone else kill",
                f"{subj} does not drink water but only {rc(['ale', 'beer', 'wine'])} or tea",
                f"{subj} does not get {poss} sleep all at once but takes short naps every few hours throughout the day and night",
                f"{subj} is an insomniac who has to walk in circles around a table or other object until {subj_l} is tired enough to fall asleep",
                f"{subj} believes {subj_l} can learn everything {subj_l} needs to know about a person by how they eat their food",
                f"{subj} believes that breathing through one's mouth will help one write better and do other mental tasks",
                f"{subj} can write backwards as easily as forwards and even prefers it",
                f"On the advice of a physician, {subj_l} cured a speech impediment {subj_l} had by talking for hours at a time in front of a mirror with {rc(['rocks', 'marbles'])} in {poss} mouth",
                f"{subj} believes that standing naked outdoors for an hour each morning is good for one's health.  {subj} tries to take these \"air baths\" from time to time and is even comfortable with taking meetings in the nude",
                f"{subj} brags that no one has seen {obj} naked since birth",
                f"{subj} believes there is an undiscovered race of {rc(['beings', 'creatures', 'elves', 'aberrations', 'mole people', 'humanoids', 'rodent-like people', 'dwarves', 'cold-blooded creatures', 'reptilians', 'gnomes', 'magical creatures', 'magical beasts', 'spirit beings', 'elementals'])} living in the ground and is planning an expedition into the earth to prove their existence and set up {rc(['diplomatic relations', 'trade negotiations'])}",
                f"{subj} likes to {rc([f'discuss {poss} plans with', 'confide in', 'pet', 'conceal'])} {poss} {q_familiar()} familiar",
                f"{subj} takes {poss} {q_familiar()} familiar's advice when {rc(['composing a letter', 'deciding a course of action'])}",
                f"{subj} wears {poss} boots for months at a time without taking them off.  When {subj_l} finally does, some of {poss} skin comes away with them",
                f"Of late {subj_l} has grown so secluded that {subj_l} will only speak to others through a locked door or window",
                f"{subj} is so afraid of ghosts, spirits, and other incorporeal beings that {subj_l} pays lots of money to have {poss} {rc(['home', 'room', 'property'])} fortified with warding magic, and so has become an easy mark for con men",
                f"{subj} can write with {rc([f'{poss} toes', f'a magic quill that obeys {poss} thoughts', 'an unseen servant', 'an invisible familiar'])}",
                f"{subj} keeps an aviary of carrier {rc(['pigeons', 'bats', 'pixies', 'sprites', 'owls', 'ravens', 'imps', 'pseudodragons'])}",
                f"{subj} {rc(['believes', 'claims'])} that {subj_l} is being {rc(['pursued', 'hunted', 'followed', 'visited'])} by a glass wolf named King Charles the Mad",
                f"{subj} once witnessed {poss} {rc(['father', 'brother', 'son'])} {rc(['die', 'kill a man'])} in {rc(['a public', 'a private', 'a magic', 'a fencing', 'an honor', 'a drunken'])} duel",
                f"{subj} is fond of jousting tournaments",
                f"{subj} always walks around a building before entering it", ]

    # OTHER NPCS

    quirks_2 = [f"{subj} wears {q_jewel()} to remember {poss} {rc([circ, 'dead'])} {p1}",
                f"{subj} accidentally {rc(['killed', 'injured'])} {poss} {p1} with magic as a child and has neither studied nor practiced it since",
                f"{subj} was accused of {rc(['injuring', 'killing'])} {poss}{circ_spc90}{p1} with magic and now claims not to {rc(['study', 'practice', 'know'])} it",
                f"{subj} is struggling mightily against a temptation that would destroy {poss} {p1}",
                f"{subj} has a tattoo to remember {poss}{circ_spc50}{p1}",
                f"{subj} is always talking about {poss} {circ} {p1}",
                f"{subj} is grieving {poss} lost {p1}",
                f"{subj} is still grieving the loss of {poss} {p1}, who died many years ago",
                f"{subj} is always showing people a letter from {poss}{circ_spc50}{p1}",
                f"{subj} tries to hide the fact that {subj_l} {rc(['is constantly rereading', 'frequently rereads'])} a letter from {poss}{circ_spc25}{p1}",
                f"{subj} {rc(['has', 'claims to have'])} received a death threat from {poss}{circ_spc50}{p1}",
                f"{subj} is trying to {rc(['hide', 'destroy', 'publish'])} a letter from {poss}{circ_spc25}{p1}",
                f"{subj} is trying to {rc(['intercept', 'deliver', 'destroy'])} a letter from {poss}{circ_spc75}{p1} to {poss} {p2}",
                f"{subj} claims that {poss}{circ_spc90}{p1} is trying to {rc(['destroy', 'kill'])} {obj}",
                f"{subj} distrusts anyone who reminds {obj} of {poss}{circ_spc90}{p1}",
                f"{subj} has a weak spot for anyone who reminds {obj} of {poss}{circ_spc90}{p1}",
                f"{subj} often talks to {poss}{circ_spc90}{p1} as if {p1_subj} were present",
                f"{subj} thinks that {poss} dead {p1} still talks to {obj} -- {p1_subj} {rc(['is', isnt])}",
                f"{subj} {rc(['is', f'claims {subj_l} is', f'thinks {subj_l} is'])} being pursued by {rc(['an', f'{poss}'])} obsessed {p1}",
                f"{subj} {rc(['is afraid', 'believes', 'is hopeful'])} that {poss}{circ_spc90}{p1} is searching for {obj}",
                f"{subj} is trying to find {poss}{circ_spc50}{p1}",
                f"{subj} is searching for {poss}{circ_spc75}{p1}, who {subj_l} believes is also looking for {obj}",
                f"{subj} is hiding from {poss}{circ_spc90}{p1}, who has tracked {obj} to this area",
                f"{subj} {rc(['was', 'feels'])} betrayed by {poss}{circ_spc90}{p1}{rc(['', ' but is too cowardly to do anything about it', ' and is planning to do something about it'])}",
                f"{subj} was accused of betraying {poss}{circ_spc90}{p1}",
                f"{subj} betrayed {poss} {p1}",
                f"{poss.capitalize()} {p1} {rc(['thinks', 'claims that'])} {subj_l} {rc(['betrayed', 'stole from', 'deceived'])} {p1_obj}",
                f"{subj} is on the run, accused of killing {poss} {p1}",
                f"{poss.capitalize()} {p1} is on the run, accused of {rc(['killing', 'betraying', 'poisoning', 'stealing from'])} {poss} {p2}",
                f"{subj} {rc(['killed', 'injured'])} {poss} {p1} {rc(['in self-defense', 'by accident'])} and was legally acquitted {rc(['but still does not want', 'and wants'])} this fact to be known",
                f"{subj} is trying to reconnect with {poss}{circ_spc50}{p1}",
                f"{subj} is trying to contact {poss}{circ_spc50}{p1}",
                f"{subj} is trying to expose {poss}{circ_spc25}{p1}",
                f"{subj} {rc(['has received', 'receives', 'is about to receive'])} a {rc(['cursed', 'magic'])} {q_obj()} from {poss}{circ_spc90}{p1}",
                f"{subj} is {rc(['trying', 'about', 'unknowingly about'])} to send a {rc(['cursed', 'magic'])} {q_obj()} to {poss}{circ_spc90}{p1}",
                f"{subj} is concerned because {subj_l} recently received a {rc(['cursed', 'magic'])} {q_obj()} from {poss}{circ_spc90}{p1} and doesn't understand {rc(['why', f'{p1_poss} reasons', f'{p1_poss} motives'])}",
                f"{subj} is weighing the possible consequences of sending a {rc(['cursed', 'magic'])} {q_obj()} to {poss}{circ_spc90}{p1}",
                f"{poss.capitalize()} {p1} left {obj} a {rc(['cursed', 'magic'])} {q_obj()} in {p1_poss} will, which {subj_l} has just received",
                f"{subj} is trying to {rc(['get', 'persuade', 'make'])} {poss}{circ_spc75}{p1} to send a {rc(['cursed', 'magic'])} {q_obj()} to {poss} {p2}",
                f"{subj} is trying to {rc(['stop', 'prevent', 'dissuade'])} {poss}{circ_spc75}{p1} from sending a {rc(['cursed', 'magic'])} {q_obj()} to {poss} {p2}",
                f"{subj} is try to intercept a {rc(['cursed', 'magic'])} {q_obj()} {rc(['en route', f'sent from {poss} {p2}'])} to {poss} {p1}",
                f"{subj} is trying to kill {poss}{circ_spc50}{p1} for reasons that {rc(['are', 'are not'])} obvious to those who know {rc([f'{obj}', f'{p1_obj}'])}",
                f"{subj} is trying to kill {poss}{circ_spc50}{p1}",
                f"{subj} is trying to prevent {poss}{circ_spc50}{p1} from {rc(['killing', 'destroying', 'ruining', 'meeting', 'ruining the reputation of', 'restoring the reputation of', 'improving the reputation of', 'lying to', 'liking', 'making amends with', 'running into', 'forgetting', 'remembering'])} {poss} {p2}",
                f"{subj} is trying to get {poss}{circ_spc50}{p1} to {rc(['meet', 'forgive', 'make amends with', 'impersonate', 'slander', 'disown', 'destroy', 'be on good terms with', 'get in the good graces of', 'reconcile with', 'run into', 'restore the reputation of', 'ruin the reputation of', 'avoid', 'forget', 'remember'])} {poss} {p2}",
                f"{subj} is trying to locate {poss}{circ_spc50}{p1}",
                f"{subj} is trying to {rc(['restore', 'ruin', 'establish'])} the reputation of {poss}{circ_spc25}{p1}",
                f"{subj} is trying to separate {poss} {p1} from {p1_poss} lover",
                f"{subj} is {rc(['knowingly', 'unwittingly'])} trying to ruin {poss} {p1}'s {rc(['life', 'business', 'plans', 'prospects'])}",
                f"{subj} {rc(['regrets', 'claims to regret'])} not listening to {poss}{circ_spc75}{p1} while {subj_l} still had the chance",
                f"{subj} is trying to improve {poss} {p1}'s life",
                f"{subj} is trying to keep {poss}{circ_spc50}{p1} and {poss} {p2} {rc(['apart', 'together'])}",
                f"{subj} is trying to pay back {poss}{circ_spc50}{p1}",
                f"{subj} is trying to {rc(['get back in the good graces of', 'make amends with', 'placate', 'forgive'])} {poss}{circ_spc50}{p1}",
                f"{subj} is trying to impress {poss}{circ_spc25}{p1}",
                f"{subj} is trying to escape from {poss}{circ_spc50}{p1}",
                f"{subj} is trying to avoid {poss}{circ_spc50}{p1}",
                f"{subj} is trying to {rc(['appease', 'get along with'])} {poss}{circ_spc50}{p1}",
                f"{subj} wants people to {rc(['think', 'believe'])} {subj_l}'s on good terms with {poss}{circ_spc50}{p1}",
                f"{subj} wants people to {rc(['think', 'believe'])} {poss}{circ_spc90}{p1} is on good terms with {poss} {p2}",
                f"{subj} {rc(['bought', 'is buying', 'wants to buy'])} a gift for {poss}{circ_spc50}{p1}",
                f"{subj} {rc(['thought', 'thinks'])} highly of {poss}{circ_spc25}{p1}",
                f"{subj} refuses to believe that {poss}{circ_spc75}{p1} is dead{rc(['', f', but {p1_subj} is', ' -- and happens to be right'])}",
                f"{poss.capitalize()}{circ_spc50}{p1} ruined {poss} {rc(['reputation', 'life', 'livelihood', f'relationship with {poss}{circ_spc90}{p2}'])}",
                f"{subj} {rc(['has a', f'never knew the name of {poss}', 'may have gotten rid of a'])} rival for the affections of {poss}{circ_spc90}{p1}",
                f"{poss.capitalize()}{circ_spc90}{p1} {rc(['has recently shown', 'has just shown', 'will soon show'])} up looking for {rc(['revenge', 'answers', 'restitution', 'a confrontation', f'{obj}', 'an apology', 'a remedy', 'a miracle', 'reconciliation', 'a chance to make up for lost time'])}",
                f"{subj} is receiving {rc(['unwanted', 'undeserved', 'unexpected', 'unusual'])} attention from {poss}{circ_spc50}{p1}",
                f"{subj} has an odd relationship with {poss}{circ_spc75}{p1}",
                f"{subj} has an embattled relationship with {poss}{circ_spc50}{p1}",
                f"{subj} is alienated from {poss}{circ_spc75}{p1}",
                f"{subj} is obsessed with {poss}{circ_spc50}{p1}",
                f"{subj} is trying to resurrect {poss} {p1} {rc(['', f'without {poss} {p2} finding out', f'with the help of {poss} {p2}'])}",
                f"{subj} is often visited by {poss} dead {p1} in {rc(['dreams', 'visions', 'nightmares'])}{rc(['', f'.  {p1_subj.capitalize()} was killed by {poss} {p2}', f'.  {p1_subj.capitalize()} may have been killed by {poss} {p2}', f'.  {poss.capitalize()} {p2} was the last person to see {p1_obj} alive', f'.  {poss.capitalize()} {p2} suspects {obj} of the crime', f'.  {subj} and {poss} {p2} were unable to save {p1_obj}', f'.  {subj} and {poss} {p2} were the last ones to see {p1_obj} alive', ])}",
                f"{subj} is hiding {poss}{circ_spc75}{p1} from {rc(['the authorities', 'an angry mob', 'a pursuer', f'{poss} {p2}', f'the people who killed {poss} {p2}', 'criminals'])}",
                f"{subj} {rc(['thinks', 'knows', 'has discovered', 'suspects'])} that {poss}{circ_spc90}{p1} is hiding {poss} {p2} from {obj}",
                f"{subj} {rc(['thinks', 'knows', 'has discovered', 'suspects'])} that {poss} {p2} is hiding {poss}{circ_spc90}{p1} from {obj}",
                f"{subj} is planning to intervene between {poss}{circ_spc50}{p1} and {poss} {p2}",
                f"{subj} is planning to introduce {poss}{circ_spc25}{p1} to {poss} {p2}",
                f"{subj} {rc(['thinks', 'fears', 'has discovered', 'suspects'])} that {poss}{circ_spc90}{p1} and {poss} {p2} are conspiring against {obj}",
                f"{subj} {rc(['thinks', 'knows', 'fears', 'hopes', 'suspects'])} that {poss}{circ_spc90}{p1} and {poss} {p2} know each other better than they let on",
                f"{poss.capitalize()}{circ_spc50}{p1} is trying to {rc([f'reconcile {obj} to', f'separate {obj} from'])} {poss} {p2}",
                f"{poss.capitalize()} {p2} is trying to {rc([f'reconcile {obj} to', f'separate {obj} from'])} {poss}{circ_spc50}{p1}",
                f"{poss.capitalize()}{circ_spc50}{p1} is {rc([f'distancing {p1_reflex} from', 'avoiding', 'trying to meet', 'trying to make amends with'])} {poss} {p2}",
                f"{subj} told {poss}{circ_spc50}{p1} that {poss} {p2} was {rc(['alive', 'dead', 'out of the picture', 'a good person', 'evil', 'a mage', 'wealthy', 'poor'])}",
                f"{subj} told {poss}{circ_spc50}{p1} that {poss} {p2} was {rc(['in', 'no longer in'])} possession of {rc(['a', f'{poss}', f'{p1_poss}'])} {rc(['magic', 'cursed'])} {q_obj()}",
                ]
    # ORGANIZATIONS
    quirks_org = [f"{subj} {rc(['has', 'claims to have'])} received a death threat from {org}",
                  f"{subj} is struggling mightily against a temptation that would destroy {org}",
                  f"{subj} {rc(['has', 'claims to have', 'is hiding', 'is about to destroy', 'is looking for', 'is hoping for', 'has lost'])} a recruitment letter from {org}",
                  f"{subj} {rc(['has', 'claims to have', 'is hiding', 'is about to destroy', 'is looking for', 'is trying to intercept', 'has lost'])} {poss}{circ_spc90}{p1}'s recruitment letter from {org}",
                  f"{subj} is trying to {rc(['hide', 'destroy', 'intercept', 'elicit', 'deliver', 'return', 'identify', 'locate', 'burn', 'forge', 'report', 'publish'])} a letter from {org}",
                  f"{subj} claims that {org} is trying to {rc(['recruit', 'kill', 'ruin', 'destroy'])} {obj}",
                  f"{subj} claims that {org} is trying to gain {poss} support",
                  f"{subj} claims that {org} is trying to {rc(['recruit', 'destroy'])} {poss}{circ_spc75}{p1}",
                  f"{subj} claims that {org} is trying to {rc(['recruit', 'destroy'])} {poss}{circ_spc75}{p1} and {p2}",
                  f"{poss.capitalize()}{circ_spc90}{p1} thinks that {org} is trying to {rc(['recruit', 'destroy'])} {rc([f'{obj}', f'{p1_obj}', f'{poss} {p2}'])}",
                  f"{subj} {rc(['is', 'is not', 'may be', 'is suspected of'])} aiding {poss}{circ_spc75}{p1} in trying to {rc(['destroy', 'dismantle', 'found', 'join', 'establish'])} {org}",
                  f"{subj} is{rc([' ', ' thought to be ', ' suspected of being ', ' known to be ', ' secretly '])}a member of {org}",
                  f"{subj} is trying to rescue {poss}{circ_spc50}{p1} from {org}",
                  f"{poss.capitalize()}{circ_spc90}{p1} is trying to {rc(['rescue', 'separate'])} {obj} from {org}",
                  f"{poss.capitalize()}{circ_spc90}{p1} is trying to stop {obj} from {rc(['joining', 'leaving', 'destroying', 'starting', 'supporting', 'establishing', 'founding', 'recruiting for'])} {org}",
                  f"{subj} is trying to stop {poss}{circ_spc90}{p1} from {rc(['joining', 'leaving', 'destroying', 'starting', 'supporting', 'establishing', 'founding', 'recruiting for'])} {org}",
                  f"{subj} is trying to infiltrate {org} to find {poss}{circ_spc50}{p1}",
                  f"{subj} is trying to keep a magic {q_obj()} out of the hands of {org}",
                  f"{subj} is trying to deliver a {rc(['magic', 'cursed'])} {q_obj()} to {org}",
                  f"{subj} has just received a {rc(['magic', 'cursed'])} {q_obj()} from {org}",
                  f"{subj} is trying to {rc(['obtain', 'hide', 'destroy'])} a {rc(['magic', 'cursed'])} {q_obj()} for {poss}{circ_spc90}{p1} in {org}",
                  f"{subj} received a {rc(['magic', 'cursed'])} {q_obj()} from {poss}{circ_spc90}{p1} just before {p1_subj} was {rc(['killed', 'abducted', 'recruited', 'indoctrinated'])} by {org}",
                  f"{poss.capitalize()}{circ_spc90}{p1} gave {obj} a {rc(['magic', 'cursed'])} {q_obj()} for safe keeping before {p1_subj} left to {rc(['investigate', 'join', 'infiltrate'])} {org}",
                  f"Before {p1_subj} died, {poss}{circ_spc90}{p1} gave {obj} a magic {q_obj()} and told {obj} to {rc(['deliver it to', 'keep it out of the hands of'])} {org}",
                  f"{org.capitalize()} is trying to deliver a {rc(['magic', 'cursed'])} {q_obj()} to {obj}",
                  f"{org.capitalize()} is trying to deliver a {rc(['magic', 'cursed'])} {q_obj()} to {obj} through {poss}{circ_spc90}{p1}",
                  f"{subj} is trying to negotiate with {org} for {poss}{circ_spc90}{p1} with a {rc(['magic', 'cursed'])} {q_obj()}",
                  f"{poss.capitalize()}{circ_spc50}{p1} wants {obj} to deliver a {rc(['magic', 'cursed'])} {q_obj()} to {poss} {p2} in {org}",
                  f"{poss.capitalize()}{circ_spc50}{p1} has charged {obj} with {rc(['getting', 'picking up', 'recovering', 'stealing'])} a {rc(['magic', 'cursed'])} {q_obj()} from {poss} {p2} in {org}",
                  f"{org.capitalize()} is trying to {rc(['recover', 'steal'])} a {rc(['magic', 'cursed'])} {q_obj()} from {obj}",
                  f"{org.capitalize()} is trying to {rc(['recover', 'steal'])} a {rc(['magic', 'cursed'])} {q_obj()} from {obj} through {poss}{circ_spc75}{p1}",
                  f"{subj} is trying to {rc(['get', 'bribe'])} {poss}{circ_spc90}{p1} not to {rc(['join', 'support', 'destroy', 'expose'])} {org} with a magic {q_obj()}",
                  f"{org.capitalize()} and {poss}{circ_spc90}{p1} are both trying to keep a {rc(['magic', 'cursed'])} {q_obj()} out of {poss} hands",
                  f"{org.capitalize()} and {poss}{circ_spc90}{p1} are both trying give {obj} a {rc(['magic', 'cursed'])} {q_obj()}",
                  f"Both {poss} {p1} and {poss} {p2} died trying to protect {obj} from {org}",
                  f"{subj} is trying to help {poss}{circ_spc75}{p1} join {org}",
                  f"{subj} is trying to talk {poss}{circ_spc75}{p1} out of joining {org}",
                  f"{subj} is trying to talk {org} out of accepting {poss}{circ_spc75}{p1}",
                  f"{subj} is trying to join {org} to impress {poss}{circ_spc50}{p1}",
                  f"{subj} is trying to join {org} to spite {poss}{circ_spc50}{p1}",
                  f"{subj} left {org} for {poss}{circ_spc50}{p1}",
                  f"{subj} {rc(['had', 'has', 'will have'])} to choose between {org} and {poss}{circ_spc50}{p1}",
                  f"{subj} is trying to get {poss}{circ_spc75}{p1} to leave {org}",
                  f"{subj} arrived at the same time that a resurgence of magic occurred in the land and is now being targeted by {org}",
                  f"{subj} has recently been inducted into {org}",
                  f"{subj} is the purported founder of {org}",
                  f"{subj} is somehow connected to the dissolution of {org}",
                  f"{subj} wants to found {org} for {poss}{circ_spc25}{p1}",
                  f"{subj} {rc(['thinks', 'suspects', 'hopes', 'fears'])} {rc(['magic', 'internal corruption', 'a rival'])} will {rc(['break up', 'destroy'])} {org}",
                  f"{subj} is receiving unwanted attention from {org}",
                  f"{poss.capitalize()}{circ_spc90}{p1} is receiving unwanted attention from {org}",
                  f"{subj} {rc(['stumbles', 'stumbled', 'will stumble'])} upon a private meeting of {org}",
                  f"{poss.capitalize()}{circ_spc90}{p1} stumbled upon the private meeting of {org}",
                  f"{subj} is hiding {poss}{circ_spc75}{p1} from {org}",
                  f"{org.capitalize()} is hiding {obj} from {poss}{circ_spc75}{p1}{rc(['', '. For a price'])}",
                  f"{poss.capitalize()}{circ_spc90}{p1} is hiding {rc([f'{obj}', '', f'{poss} {p2}'])} {rc(['from', 'in'])} {org}",
                  f"{subj} {rc(['thinks', 'suspects', 'fears', 'knows'])} that {org} is hiding {poss}{circ_spc75}{p1} from {obj}",
                  f"{subj} {rc(['thinks', 'suspects', 'fears', 'knows'])} that {poss}{circ_spc90}{p1} left {obj} to join {org}",
                  f"{subj} {rc(['thinks', 'suspects', 'fears', 'knows'])} that {poss}{circ_spc75}{p1} is hiding from {obj} in {org}"]

    # CALCULATING RESULTS
    quirks = []
    quirks.extend(quirks_1)
    quirks.extend(quirks_2)
    quirks.extend(quirks_org)
    return random.choice(quirks)


# FUNCTIONS - GENDER


def sex_gen():
    # randomly determines the sex of an NPC #
    sex = ["male", "female"]
    return random.choice(sex)


def gender_noun(sex):
    # determines gender based on the NPC's sex #
    if sex == "male":
        return "man"
    else:
        return "woman"


def gender_subj(sex):
    # determines gender pronoun (subject) based on NPC's sex #
    if sex == "male":
        return "he"
    else:
        return "she"


def gender_poss(sex):
    # determines gender adjective (possessive) based on NPC's sex #
    if sex == "male":
        return "his"
    else:
        return "her"


def gender_obj(sex):
    # determines gender pronoun (object) based on NPC's sex #
    if sex == "male":
        return "him"
    else:
        return "her"


def gender_reflex(sex):
    # determines gender pronoun (reflexive) based on NPC's sex #
    if sex == "male":
        return "himself"
    else:
        return "herself"


# FUNCTIONS - CHARACTER AND PERSONALITY


def char_gen():
    # randomly determines an NPC's moral character #
    character = ["good", "neutral", "evil"]
    return random.choices(character, weights=[1, 2, 1])[0]


def prin_gen(char):
    # determines how principled an NPC is based on their moral character #
    principles = ["principled", "neutral", "unprincipled"]
    if char == "good":
        return random.choices(principles, weights=[60, 20, 20])[0]
    elif char == "neutral":
        return random.choices(principles, weights=[25, 50, 25])[0]
    else:
        return random.choices(principles, weights=[20, 20, 60])[0]


def law_disp(char, prin, subj, poss, obj, reflex):
    # determines the NPC's attitude towards rules and laws based on their character and principles #
    if char == "good" and prin == "principled":
        return "This is a law-abiding citizen who has the utmost respect for law and order."
    elif char == "good" and prin == "neutral":
        return subj.capitalize() + " has a high respect for rules and laws, unless they are obviously unjust."
    elif char == "good" and prin == "unprincipled":
        return subj.capitalize() + " has no regard for rules or laws, but always does what " + subj + " thinks is right in " + poss + " own eyes."
    elif char == "neutral" and prin == "principled":
        return subj.capitalize() + " believes law to be good but can be tempted to break it if it suits " + obj + " and no one will get hurt."
    elif char == "neutral" and prin == "neutral":
        return subj.capitalize() + " generally does the right thing but is ambivalent towards rules and laws and can be tempted to break them as long as it would not get " + obj + " in too much trouble or offend " + poss + " conscience."
    elif char == "neutral" and prin == "unprincipled":
        return subj.capitalize() + " generally does what " + subj + " considers to be the right thing but has no regard for rules or laws and will break them without hesitation, unless doing so would be dangerous or seriously hurt someone."
    elif char == "evil" and prin == "principled":
        return subj.capitalize() + " is evil but considers " + reflex + " to be good because " + subj + " is extremely principled and has the highest respect for rules or laws.  It does not occur to " + obj + " that the rules or laws " + subj + " follows may be unjust, and as long as " + subj + " abides by them, " + subj + " considers all " + poss + " actions to be just and good, no matter who gets hurt or exploited."
    elif char == "evil" and prin == "neutral":
        return subj.capitalize() + " either knows that what " + subj + " does is evil and doesn't care, or " + subj + " rationalizes " + poss + " actions with some pretty questionable rules " + subj + " invented or adopted."
    else:
        return subj.capitalize() + " has no regard at all for rules or laws and will do whatever " + poss + " evil heart desires or " + subj + " thinks is in " + poss + " own best interests, without regard for the welfare of others.  If " + subj + " follows rules at all, it is only to blend into the group and deceive others."


def trait_type_gen(char):
    trait_types = ["positive", "negative"]
    if char == "good":
        return random.choices(trait_types, weights=[90, 10])[0]
    elif char == "neutral":
        return random.choices(trait_types, weights=[50, 50])[0]
    else:
        return random.choices(trait_types, weights=[30, 70])[0]


def trait_gen(trait_type):
    trait_pool = []
    if trait_type == "positive":
        trait_pool.extend(all_traits_pos)
    else:
        trait_pool.extend(all_traits_neg)
    return random.choice(trait_pool)


def conf_traittrait(trait1, trait2):
    # Determines whether two traits are contradictory
    # False = No Conflict
    # True = Contradictory Traits
    if trait1 in traits1_char_is_good and trait2 in traits1_char_not_good:
        return True
    elif trait1 in traits2_char_is_honor and trait2 in traits2_char_not_honor:
        return True
    elif trait1 in traits3_char_is_bene and trait2 in traits3_char_not_bene:
        return True
    elif trait1 in traits4_char_is_humble and trait2 in traits4_char_not_humble:
        return True
    elif trait1 in traits5_char_is_pure and trait2 in traits5_char_not_pure:
        return True
    elif trait1 in traits6_char_is_just and trait2 in traits6_char_not_just:
        return True
    elif trait1 in traits7_char_is_honest and trait2 in traits7_char_not_honest:
        return True
    elif trait1 in traits8_char_is_const and trait2 in traits8_char_not_const:
        return True
    elif trait1 in traits9_char_is_forgive and trait2 in traits9_char_not_forgive:
        return True
    elif trait1 in traits10_char_is_charit and trait2 in traits10_char_not_charit:
        return True
    elif trait1 in traits11_char_is_brave and trait2 in traits11_char_not_brave:
        return True
    elif trait1 in traits12_char_is_pious and trait2 in traits12_char_not_pious:
        return True
    elif trait1 in traits13_char_is_indust and trait2 in traits13_char_not_indust:
        return True
    elif trait1 in traits14_char_is_flex and trait2 in traits14_char_not_flex:
        return True
    elif trait1 in traits15_char_is_contr and trait2 in traits15_char_not_contr:
        return True
    ############################## FLIP #########################################
    elif trait2 in traits1_char_is_good and trait1 in traits1_char_not_good:
        return True
    elif trait2 in traits2_char_is_honor and trait1 in traits2_char_not_honor:
        return True
    elif trait2 in traits3_char_is_bene and trait1 in traits3_char_not_bene:
        return True
    elif trait2 in traits4_char_is_humble and trait1 in traits4_char_not_humble:
        return True
    elif trait2 in traits5_char_is_pure and trait1 in traits5_char_not_pure:
        return True
    elif trait2 in traits6_char_is_just and trait1 in traits6_char_not_just:
        return True
    elif trait2 in traits7_char_is_honest and trait1 in traits7_char_not_honest:
        return True
    elif trait2 in traits8_char_is_const and trait1 in traits8_char_not_const:
        return True
    elif trait2 in traits9_char_is_forgive and trait1 in traits9_char_not_forgive:
        return True
    elif trait2 in traits10_char_is_charit and trait1 in traits10_char_not_charit:
        return True
    elif trait2 in traits11_char_is_brave and trait1 in traits11_char_not_brave:
        return True
    elif trait2 in traits12_char_is_pious and trait1 in traits12_char_not_pious:
        return True
    elif trait2 in traits13_char_is_indust and trait1 in traits13_char_not_indust:
        return True
    elif trait2 in traits14_char_is_flex and trait1 in traits14_char_not_flex:
        return True
    elif trait2 in traits15_char_is_contr and trait1 in traits15_char_not_contr:
        return True
    else:
        return False


def conf_traitchar(char, trait):
    # Determines the level of conflict between character and a character trait
    # False = No conflict
    # True = Trait conflicts with character
    if char == "good" and trait in char_traits_neg:
        return True
    elif char == "evil" and trait in char_traits_pos:
        return True
    else:
        return False


# FUNCTIONS - PROFESSION

def prof_type_gen(char):
    # determines profession type based somewhat on the NPC's moral character #
    prof_types = ["common", "government", "criminal", "medical", "artistic", "high"]
    if char == "good":
        return random.choices(prof_types, weights=[49, 15, 1, 15, 10, 10])[0]
    elif char == "neutral":
        return random.choices(prof_types, weights=[50, 15, 5, 10, 10, 10])[0]
    else:
        return random.choices(prof_types, weights=[15, 20, 45, 5, 5, 10])[0]


def prof_gen(prof_type, sex):
    prof_pool = []
    if prof_type == "common":
        prof_pool.extend(prof_com)
        if sex == "male":
            prof_pool.extend(prof_com_m)
        else:
            prof_pool.extend(prof_com_f)
    elif prof_type == "government":
        prof_pool.extend(prof_gov)
        if sex == "male":
            prof_pool.extend(prof_gov_m)
        else:
            prof_pool.extend(prof_gov_f)
    elif prof_type == "criminal":
        prof_pool.extend(prof_crime)
        if sex == "male":
            prof_pool.extend(prof_crime_m)
        else:
            prof_pool.extend(prof_crime_f)
    elif prof_type == "medical":
        prof_pool.extend(prof_med)
        if sex == "female":
            prof_pool.extend(prof_med_f)
    elif prof_type == "artistic":
        prof_pool.extend(prof_art)
    else:
        prof_pool.extend(prof_high)
        if sex == "male":
            prof_pool.extend(prof_high_m)
        else:
            prof_pool.extend(prof_high_f)
    return random.choice(prof_pool)


# FUNCTIONS - CONSTITUTION AND APPEARANCE


def con_gen():
    # determines the constitution of the NPC #
    # -2 = serious health concern, 0 = perfect health #
    health_range = [-2, -1, 0]
    return random.choices(health_range, weights=[1, 5, 94])[0]


def ill_gen(con, sex, prof_type):
    # selects a condition for NPCs in poor health #
    affliction_pool = []
    if con == -2:
        affliction_pool.extend(con_2_ill)
        affliction_pool.extend(con_2_ill_mag)
        affliction_pool.extend(con_2_ill_disfig)
        affliction_pool.extend(con_2_inj)
        affliction_pool.extend(con_2_inj_mag)
        affliction_pool.extend(con_2_inj_disfig)
        if sex == "female":
            affliction_pool.extend(con_2_ill_f)
        if prof_type == "common" or prof_type == "crime":
            affliction_pool.extend(con_2_ill_poor)
    elif con == -1:
        affliction_pool.extend(con_1_ill)
        affliction_pool.extend(con_1_ill_disfig)
        affliction_pool.extend(con_1_inj)
        affliction_pool.extend(con_1_inj_mag)
        affliction_pool.extend(con_1_inj_disfig)
        if prof_type == "common" or prof_type == "crime":
            affliction_pool.extend(con_1_ill_poor)
    else:
        affliction_pool.append("no illnesses or injuries")
    return random.choice(affliction_pool)


def looks_gen(sex):
    # determines how good-looking the NPC is
    if sex == "female":
        looks_pool = ["hideous", "ugly", "homely", "plain-looking", "pretty", "beautiful", "divinely beautiful"]
    else:
        looks_pool = ["hideous", "ugly", "unattractive", "plain-looking", "good-looking", "handsome",
                      "extremely handsome"]
    return random.choices(looks_pool, weights=[1, 5, 15, 40, 20, 15, 4])[0]


# CLASSES

class NPC:
    num_of_NPCs = 0

    def __init__(self):
        # SEX AND GENDER
        self.sex = sex_gen()
        self.gender = gender_noun(self.sex)
        self.subj = gender_subj(self.sex)
        self.poss = gender_poss(self.sex)
        self.obj = gender_obj(self.sex)
        self.reflex = gender_reflex(self.sex)

        # CHARACTER AND PERSONALITY
        self.char = char_gen()
        self.principles = prin_gen(self.char)
        self.law_disposition = law_disp(self.char, self.principles, self.subj, self.poss, self.obj, self.reflex)
        self.trait1_type = trait_type_gen(self.char)
        self.trait2_type = trait_type_gen(self.char)
        self.trait1 = trait_gen(self.trait1_type)
        self.trait2 = trait_gen(self.trait2_type)
        self.conf_ct1 = conf_traitchar(self.char, self.trait1)
        self.conf_ct2 = conf_traitchar(self.char, self.trait2)
        self.conf_tt = conf_traittrait(self.trait1, self.trait2)
        self.quirk = quirk_gen(self)
        # PROFESSION
        self.prof_type = prof_type_gen(self.char)
        self.prof = prof_gen(self.prof_type, self.sex)
        # CONSTITUTION AND APPEARANCE
        self.con = con_gen()
        self.ill = ill_gen(self.con, self.sex, self.prof_type)
        self.looks = looks_gen(self.sex)

        NPC.num_of_NPCs += 1


# PRINTING

def profile_view(NPC):
    print("\n==================================================")
    print("Gender: " + str(NPC.gender.capitalize()))
    print("Profession: " + str(NPC.prof.capitalize()))
    print("Character: " + str(NPC.char.capitalize()))
    print("Principles: " + str(NPC.principles.capitalize()))
    print("Traits: " + str(NPC.trait1.capitalize()) + ", " + str(NPC.trait2.capitalize()))
    print("Appearance: " + str(NPC.looks.capitalize()))
    if NPC.con != 0:
        print("Health Condition: " + str(NPC.ill.capitalize()))
    # print("\nAttitude towards rules and laws: \n" + str(NPC.law_disposition))
    print("Detail: {}.".format(NPC.quirk))
    print("==================================================")


def narrative_view(NPC):
    # VARIABLES

    # 'Seeming' word
    seeming_word_list = ["seemingly", "apparently", "ostensibly", "evidently"]
    seemingly = random.choices(seeming_word_list, weights=[80, 10, 5, 5])[0]

    # Character: 'a' or 'an'
    if NPC.char == "evil":
        c_an = "an"
    else:
        c_an = "a"

    # Looks: 'a' or 'an'
    if NPC.looks == "ugly" or NPC.looks == "unattractive" or NPC.looks == "extremely handsome":
        l_an = "an"
    else:
        l_an = "a"

    # PRINT NPC NUMBER
    print(str(NPC.num_of_NPCs) + ".", end=" ")

    # PRINT INITIAL STATEMENT

    # Statement of Profession
    print(f"The {NPC.prof} is", end=" ")

    # Statement of Morality
    if NPC.char == "neutral" and random.randint(1, 10) == 1:  # 10% chance for moral neutrality to be stated
        print("neither a very good nor a very evil", end=" ")
        morality_stated = True
    elif NPC.char != "neutral":  # if not neutral and morality still unstated, print morality
        print(f"{c_an} {NPC.char}", end=" ")
        morality_stated = True
    else:  # character is neutral and their morality has not been stated
        morality_stated = False

    # Statement of Appearance
    if not morality_stated:  # morality has not been stated; try stating appearance
        if NPC.looks == "plain-looking" and random.randint(1,
                                                           10) == 1:  # 10% chance to state a plain-looking character's appearance
            print(f"{l_an} {NPC.looks}", end=" ")
            looks_stated = True
        elif NPC.looks != "plain-looking":  # if character is not plain-looking and their appearance has not been stated, state it
            print(f"{l_an} {NPC.looks}", end=" ")
            looks_stated = True
        else:  # character is plain-looking and their appearance has not been stated
            looks_stated = False
    else:
        looks_stated = False

    # Statement of Gender if Preceded by a Modifier
    if morality_stated or looks_stated:
        print(f"{NPC.gender},", end=" ")

    # PRINT SUBSEQUENT STATEMENT

    # Stating Traits in Initial Statement, Since No Modifier Has Been Given
    if not morality_stated and not looks_stated:  # not possible at this point for traits to conflict with character, since character is neutral
        if NPC.conf_tt:  # if the traits contradict each other, state them both
            print(f"somehow both {NPC.trait1} and {NPC.trait2}.", end=" ")
        else:
            print(f"{NPC.trait1} and {NPC.trait2}.", end=" ")
        # END STATEMENT

    # Stating Traits Subsequently, Since a Modifier Was Already Given
    if morality_stated or looks_stated:
        if morality_stated:  # if morality has been stated, looks have not: chance to print them
            if NPC.looks == "plain-looking" and random.randint(1,
                                                               4) == 1:  # 25% chance to state a plain-looking character's appearance
                print(f"{NPC.looks}", end=", ")
            elif NPC.looks != "plain-looking":  # if character is not plain-looking and their appearance has not been stated, state it
                print(f"{NPC.looks}", end=", ")
            else:  # character is plain-looking and their appearance will not be stated at all
                pass
        # Morality and Appearance Statements Resolved; Now Printing Traits
        if NPC.conf_tt:  # traits conflict; print them both
            print(f"somehow both {NPC.trait1} and {NPC.trait2}.", end=" ")
        elif not NPC.conf_ct1 and not NPC.conf_ct2:  # if neither trait conflicts with character, print them both
            print(f"{NPC.trait1} and {NPC.trait2}.", end=" ")
        elif not NPC.conf_ct1 and NPC.conf_ct2:  # trait2 conflicts with character, but trait1 does not
            print(f"{NPC.trait1} and {seemingly} {NPC.trait2}.", end=" ")
        elif NPC.conf_ct1 and not NPC.conf_ct2:  # trait1 conflicts with character, but trait2 does not
            print(f"{NPC.trait2} and {seemingly} {NPC.trait1}.", end=" ")
        else:  # both traits conflict with character; print them both
            print(f"{seemingly} {NPC.trait1} and {NPC.trait2}.", end=" ")
        # END STATEMENT
    if NPC.con != 0:
        print(str(NPC.subj).capitalize() + " has a health condition: " + str(NPC.ill) + ".", end=" ")
    # Quirk
    print(NPC.quirk + ".")
    print(" ")
    print(" ")
    # End


current_NPCs = []
# view_mode = input("View mode (1 for profile view, 2 for narrative view): ")
view_mode = 2

while input(" ").lower() != "stop":
    current_NPCs.append(NPC())
    if view_mode == "1":
        profile_view(current_NPCs[-1])
    else:
        narrative_view(current_NPCs[-1])

print("Number of NPCs created: " + str(len(current_NPCs)))

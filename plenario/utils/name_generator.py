import random


def generate_name():

    # Generate a (highly probably) unique name.
    # References so far:
    # - The Hitchhiker's Guide to the Galaxy
    # - Rick and Morty

    firstnames = [
        "7dimensional",
        "aldebaran",
        "algorithmic",
        "alphacentauri",
        "altair",
        "antares",
        "arcturus",
        "argabuthon",
        "arkintoofle",
        "artificial",
        "asgardian",
        "barnardian",
        "bartledan",
        "bartrax",
        "betelgeuse",
        "bethselamin",
        "birdy",
        "bistro",
        "blagulon",
        "blippy",
        "brantisvogan",
        "brequinda",
        "brontitall",
        "broopy",
        "burger",
        "chitzy",
        "cinematic",
        "citadel",
        "cromulon",
        "cronenberg",
        "damogran",
        "dangrabad",
        "dimension",
        "doopidoo",
        "dordellis",
        "earthly",
        "fallia",
        "fancy",
        "flanux",
        "flargathon",
        "folfanga",
        "foth",
        "frastra",
        "frazfraga",
        "frogstar",
        "gagrakacka",
        "galactic",
        "gazorpazorp",
        "geared",
        "giant",
        "golgafrincham",
        "greasy",
        "hamster",
        "hanwavel",
        "hastromil",
        "hawalius",
        "hollop",
        "holographic",
        "horsehead",
        "hunian",
        "huntringfurl",
        "interdimensional",
        "imperial",
        "jaglan",
        "jajazikstak",
        "jerryboree",
        "kakrafoon",
        "king",
        "krikkit",
        "lamuella",
        "lilbits",
        "magrathea",
        "maximegalon",
        "megabrantis",
        "megadodo",
        "millenium",
        "milliways",
        "nano",
        "nowwhat",
        "oglaroon",
        "orionbeta",
        "paranoid",
        "party",
        "planets",
        "pleiades",
        "poghril",
        "purging",
        "qualactin",
        "qvarne",
        "river",
        "santraginus",
        "saquopilia",
        "shoed",
        "siriustau",
        "solar",
        "sqornshellous",
        "stavromula",
        "stegbartle",
        "striterax",
        "stug",
        "terrace",
        "traal",
        "universal",
        "ursaminor",
        "viltvodle",
        "vod",
        "vogsphere",
        "voondon",
        "wubaluba",
        "xaxis",
        "ysllodins",
        "zarss",
        "zentalquabula",
        "zirzla"
    ]

    lastnames = [
        "agda",
        "android",
        "agrajag",
        "alexander",
        "allitnils",
        "anjie",
        "annie",
        "arkleseizure",
        "armagheadon",
        "arthricia",
        "aseed",
        "bangbang",
        "barmen",
        "bartlett",
        "beeblebrox",
        "beta-seven",
        "bird",
        "birdperson",
        "blimblam",
        "blueshirt",
        "bob",
        "bodyguard",
        "bozo",
        "captain",
        "carlinton",
        "cave",
        "caveman",
        "centaur",
        "clone",
        "colin",
        "consultant",
        "creature",
        "cromulons",
        "cronenberg",
        "cyborg",
        "cynthia",
        "dale",
        "deepthought",
        "dent",
        "desiato",
        "disasterarea",
        "dish",
        "doofus",
        "dubdub",
        "eccentrica",
        "eddie",
        "effrafax",
        "elvis",
        "emperor",
        "falcon",
        "fenchurch",
        "fitzmelton",
        "frankie",
        "frat",
        "frootmig",
        "gag",
        "gail",
        "garblovians",
        "gargravarr",
        "garkbit",
        "garmanarnar",
        "gazorpazorpfield",
        "genghis",
        "glipglop",
        "god",
        "gogrilla",
        "golgafrinchans",
        "googleplex",
        "graduate",
        "grunthos",
        "hactar",
        "haggunenon",
        "hairdresser",
        "heimdall",
        "hollop",
        "hooli",
        "hunter",
        "hurtenflurst",
        "ix",
        "jerry",
        "johnson",
        "kapelsen",
        "karl",
        "kavula",
        "krikkit",
        "krikkiters",
        "kwaltz",
        "lallafa",
        "lintilla",
        "loonquawl",
        "lord",
        "lunkwill",
        "lury",
        "lyricon",
        "magician",
        "majikthise",
        "mark",
        "marvin",
        "marketer",
        "mckenna",
        "meeseeks",
        "megadodo",
        "megafreighter",
        "minetti",
        "morty",
        "murray",
        "nullify",
        "numberone",
        "numbertwo",
        "officials",
        "omnicognate",
        "oolon",
        "pag",
        "phouchg",
        "plumbus",
        "poet",
        "poles",
        "poodoo",
        "prak",
        "pralite",
        "president",
        "princess",
        "prosser",
        "questular",
        "quordlepleen",
        "raffle",
        "receptionists",
        "rick",
        "roosta",
        "ruler",
        "russell",
        "sanchez",
        "sanitizer",
        "saunders",
        "scary",
        "sheila",
        "slartibartfast",
        "smith",
        "smithers",
        "snuffles",
        "strinder",
        "sulijoo",
        "thor",
        "thrashbarg",
        "traflorkians",
        "tribesmen",
        "trintragula",
        "vantrashell",
        "varntvar",
        "versenwald",
        "vogon",
        "voojagig",
        "vranx",
        "vroomfondel",
        "werdle",
        "whale",
        "wonko",
        "wowbagger",
        "wsogmm",
        "zaphod",
        "zarniwoop",
        "zarquon",
        "zem"
    ]

    return random.choice(firstnames)+"_"+random.choice(lastnames)
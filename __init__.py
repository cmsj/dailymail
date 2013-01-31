#!/usr/bin/python
"""#dailymail
##by Chris Jones <cmsj@tenshu.net>
##ported from the original Javascript by Chris Applegate (www.qwghlm.co.uk)
##Released under the GNU GPL v2 or later
----------------------------------------

This is a class with a simple purpose, it creates fictional headlines from the
British newspaper The Daily Mail.

They are well known for their ability to completely suspend all rational
thought and print the craziest nonsense. So crazy that parody is almost
unnecessary, but still a lot of fun.

To use this class, simply pop it somewhere in your python path and do something
like:

    import dailymail
    paper = dailymail.dailymail()
    print paper.headline()

Easy!

(P.S. If you work for the Daily Mail and find this library useful, please let
me know)
"""

import random

class verb(object):
    """Class implementing a verb"""

    def __init__(self, plural, singular, tense):
        """Class initialiserr"""
        self.singular = singular
        self.plural = plural
        self.tense = tense


class noun(object):
    """Class implementing a noun"""

    def __init__(self, word, person, number):
        """Class initialiser"""
        self.word = word
        self.person = person
        self.number = number


class phrase(object):
    """Class implementing a phrase"""

    def __init__(self, present, past, active, target):
        """Class initialiser"""
        self.present = present
        self.past = past
        self.active = active
        self.target = target


class dailymail(object):
    """Class implementing basically all of the work the Daily Mail does"""

    auxiliary_verbs = [
        verb("will", "will", "present"),
        verb("could", "could", "present"),
        verb("are", "is", "active"),
        verb("have", "has", "past"),
    ]

    subjects = [
        noun("the labour party",3,1),
        noun("brussels",3,1),
        noun("the bbc",3,1),
        noun("the e.u.",3,1),
        noun("the euro",3,1),
        noun("the loony left",3,1),
        noun("the unions",3,2),
        noun("channel 4",3,1),
        noun("your local council",3,1),
        noun("the french",3,2),
        noun("the germans",3,2),
        noun("the poles",3,2),
        noun("brussels bureaucrats",3,2),
        noun("muslims",3,2),
        noun("immigrants",3,2),
        noun("teachers",3,2),
        noun("the unemployed",3,2),
        noun("gypsies",3,2),
        noun("yobs",3,2),
        noun("hoodies",3,2),
        noun("feral children",3,2),
        noun("chavs",3,2),
        noun("the p.c. brigade",3,2),
        noun("cyclists",3,2),
        noun("foxes",3,2),
        noun("asylum seekers",3,2),
        noun("gays",3,2),
        noun("lesbians",3,2),
        noun("single mothers",3,2),
        noun("paedophiles",3,2),
        noun("working mothers",3,2),
        noun("teenage sex",3,1),
        noun("political correctness",3,1),
        noun("health & safety",3,1),
        noun("feminism",3,1),
        noun("the metric system",3,1),
        noun("dumbing-down",3,1),
        noun("rip-off britain",3,1),
        noun("the internet",3,1),
        noun("facebook",3,1),
        noun("twitter",3,1),
        noun("filth on television",3,1),
        noun("the human rights act",3,1),
        noun("the nanny state",3,1),
        noun("cancer",3,1),
        noun("binge drinking",3,1),
        noun("the MMR jab",3,1),
        noun("the house price crash",3,1) 
    ]

    transitive_phrases = [
        phrase("give", "given", "giving", "cancer"),
        phrase("give", "given", "giving", "cancer"),
        phrase("infect", "infected", "infecting", "with AIDS"),
        phrase("give", "given", "giving", "swine flu"),
        phrase("make", "made", "making", "obese"),
        phrase("give", "given", "giving", "diabetes"),
        phrase("make", "made", "making", "impotent"),
        phrase("turn","turned","turning","gay"),
        phrase("scrounge off","scrounged off","scrounging off",""),
        phrase("tax", "taxed", "taxing", ""),
        phrase("cheat", "cheated", "cheating", ""),
        phrase("defraud", "defrauded", "defrauding", ""),
        phrase("steal from","stolen from","stealing from",""),
        phrase("burgle","burgled","burgling",""),
        phrase("devalue","devalued","devaluing",""),
        phrase("rip off","ripped off","ripping off",""),
        phrase("molest","molested","molesting",""),
        phrase("have sex with","had sex with","having sex with",""),
        phrase("impregnate", "impregnated", "impregnating", ""),
        phrase("steal the identity of","stolen the identity of","stealing the identity of",""),
        phrase("destroy","destroyed","destroying",""),
        phrase("kill","killed", "killing",""),
        phrase("ruin","ruined","ruining",""),
        phrase("hurt","hurt", "hurting","")
    ]

    objects = [
        "the british people",
        "the middle class",
        "middle britain",
        "england",
        "hard-working families",
        "homeowners",
        "pensioners",
        "drivers",
        "taxpayers",
        "taxpayers' money",

        "house prices",
        "property prices",
    
        "britain's farmers",
        "the countryside",

        "british justice",
        "british sovereignty",
        "common sense and decency",

        "the queen",
        "the royal family",
        "the church",

        "you",
        "your mortgage",
        "your pension",
        "your daughters",
        "your children",
        "your house",
        "your pets",

        "the conservative party",
        "cliff richard",
        "the memory of diana",
        "Britain's swans"
    ]

    def match_verb_and_subject(self, subject, verb):
        """Match an auxiliary verb with the subject"""
        if subject.number == 1 and subject.person == 3:
            return(verb.singular)
        else:
            return(verb.plural)

    def match_verb_and_tense(self, verb, phrase):
        """Match the transitive verb's tense with that of the verb"""
        if verb.tense == "present":
            return(phrase.present)
        elif verb.tense == "past":
            return(phrase.past)
        elif verb.tense == "active":
            return(phrase.active)

    def headline(self):
        """Return a randomly generated headline"""
        sentence = []
        subject = random.choice(self.subjects)
        phrase = random.choice(self.transitive_phrases)
        verb = random.choice(self.auxiliary_verbs)
        target = random.choice(self.objects)

        sentence.append(self.match_verb_and_subject(subject, verb))
        sentence.append(subject.word)
        sentence.append(self.match_verb_and_tense(verb, phrase))
        sentence.append(target)

        if phrase.target != "":
            sentence.append(phrase.target)

        final = ' '.join(sentence) + '?'
        return(final.upper())

if __name__ == "__main__":
    paper = dailymail()
    print paper.headline()


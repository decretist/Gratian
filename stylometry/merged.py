#!/usr/bin/python
from __future__ import print_function
import sys
words = ['in', 'non', 'et', 'est', 'quod', 'de', 'unde', 'ad',
    'qui', 'sed', 'uel', 'ut', 'cum', 'autem', 'si', 'a', 'ex',
    'sunt', 'uero', 'enim', 'etiam', 'ab', 'que', 'ait', 'item',
    'quia', 'ergo', 'esse', 'nec', 'his', 'per', 'se', 'hoc',
    'scribit', 'papa', 'sicut', 'ita', 'concilio', 'nisi', 'legitur',
    'tamen', 'ecclesiae', 'illud', 'pro', 'auctoritate', 'sit',
    'sibi', 'quam', 'quibus', 'sic', 'eius', 'augustinus', 'dicens',
    'episcopo', 'eorum', 'libro', 'quo', 'gregorius', 'eis', 'hinc',
    'omnibus', 'licet', 'causa', 'possunt', 'potest', 'aut', 'contra',
    'aliud', 'post', 'sine', 'ecclesia', 'sua', 'an', 'suae',
    'auctoritatibus', 'probatur', 'queritur', 'siue', 'eo', 'debet',
    'eum', 'quis', 'episcopus', 'ne', 'b', 'inter', 'fuerit',
    'intelligendum', 'quoque', 'sint', 'super', 'ea', 'hec',
    'dicitur', 'fieri', 'ei', 'statutum', 'eos', 'episcopi',
    'episcopis', 'suis', 'atque', 'uxorem', 'idem', 'intelligi',
    'qua', 'ante', 'papae', 'quem', 'etc', 'prohibetur', 'dei',
    'illa', 'ille', 'suo', 'ideo', 'prohibentur', 'ecce', 'intelligitur',
    'uerum', 'dominus', 'alia', 'propter', 'dum', 'sui', 'tantum',
    'alii', 'deo', 'domino', 'supra', 'aliis', 'cui', 'episcopum',
    'ieronimus', 'apud', 'datur', 'id', 'patet', 'quid', 'aliquando',
    'eodem', 'ius', 'oportet', 'suam', 'testatur', 'debent',
    'fuerint', 'secundum', 'quos', 'tunc', 'uidelicet', 'apostolus',
    'exemplo', 'quando', 'tempore', 'peccatum', 'sacerdotes',
    'solum', 'uidetur', 'coniugium', 'erat', 'quorum', 'dictum',
    'habere', 'illi', 'lege', 'peccata', 'quamuis', 'domini', 'iure',
    'postea', 'titulo', 'accusatione', 'capitulo', 'ecclesiam',
    'etsi', 'fide', 'ii', 'illis', 'namque', 'obicitur', 'gregorii',
    'sententia', 'apparet', 'deus', 'epistola', 'ambrosius', 'esset',
    'itaque', 'nunc', 'possit', 'sacris', 'uiro', 'hic', 'nulli',
    'poterit', 'respondetur', 'scribens', 'ualet', 'canonibus',
    'cuius', 'ipsa', 'leo', 'nulla', 'penitenciam', 'hac', 'liceat',
    'nichil', 'premissis', 'sinodo', 'facit', 'similiter', 'gelasius',
    'inuenitur', 'offitio', 'sacerdotibus', 'uos', 'aliquid',
    'episcoporum', 'ordinibus', 'propria', 'hanc', 'hereticis',
    'infra', 'modo', 'potestatem', 'rebus', 'sententiam', 'alterius',
    'christi', 'colligitur', 'concilii', 'forte', 'res', 'aliquis',
    'bonum', 'christus', 'filios', 'posse', 'probantur', 'suorum',
    'auctoritas', 'crimen', 'eam', 'econtra', 'generaliter', 'illo',
    'iudicium', 'omnia', 'permittitur', 'tolletano', 'augustini',
    'consensu', 'filii', 'habet', 'iuxta', 'peccato', 'prius',
    'quomodo', 'sacramenta']

kestemont = [
    'in',       # preposition
    'non',      # adverb
    'et',       # conjunction
    'quod',     # conjunction
    'de',       # preposition
    'unde',     # adverb
    'ad',       # preposition
    'qui',      # adverb [?]
    'sed',      # conjunction
    'uel',      # conjunction
    'ut',       # adverb, conjunction
    'cum',      # preposition, conjunction
    'autem',    # conjunction
    'si',       # conjunction
    'a',        # preposition
    'enim',     # conjunction
    'etiam',    # adverb
    'quia',     # conjunction
    'ergo',     # adverb
    'nec',      # conjunction
    'per',      # preposition
    'sicut',    # adverb
    'xque',     # conjunction
    'ita',      # adverb
    'nisi',     # conjunction
    'tamen',    # adverb
    'pro',      # preposition
    'quam',     # conjunction
    'sic',      # adverb
    'licet',    # conjunction
    'aut',      # conjunction
    'contra',   # preposition, adverb
    'post',     # preposition, adverb
    'sine',     # preposition
    'siue',     # conjunction
    'ne',       # conjunction, adverb
    'inter',    # preposition
    'quoque',   # conjunction
    'super',    # adverb, preposition
    'atque',    # conjunction
    'idem',     # adverb [?]
    'ante',     # preposition
    'propter',  # preposition
    'dum',      # conjunction
    'apud',     # preposition
    'uidelicet',# adverb
    'tunc',     # adverb
    'nunc',     # adverb
    'hic'       # adverb
]

adverbs_0 = ['non', 'unde', 'ut', 'etiam', 'ergo', 'sicut', 'ita',
    'tamen', 'sic', 'contra', 'post', 'ne', 'super', 'uidelicet',
    'tunc', 'nunc', 'hic', 'quomodo']

conjunctions_0 = ['et', 'quod', 'sed', 'uel', 'ut', 'cum', 'autem',
    'si', 'enim', 'quia', 'nec', 'xque', 'nisi', 'quam', 'licet',
    'aut', 'siue', 'ne', 'quoque', 'atque', 'dum']

prepositions_0 = ['in', 'de', 'ad', 'cum', 'a', 'per', 'pro', 'contra',
    'post', 'sine', 'inter', 'super', 'ante', 'propter', 'apud']

adverbs_1 = [
    'uero',     # adverb
    'item',     # adverb
    'quo',      # adverb
    'ideo',     # adverb
    'ecce',     # adverb
    'supra',    # adverb, preposition
    'aliquando',# adverb
    'quando',   # conjunction, adverb
    'postea',   # adverb
    'similiter',# adverb
    'infra',    # adverb, preposition
    'forte',    # adverb
    'generaliter',      # adverb
    'prius'     # adverb
]

conjunctions_1 = [
    'an',       # conjunction
    'nam',      # conjunction
    'quando',   # conjunction, adverb
    'quamuis',  # conjunction
    'etsi',     # conjunction
    'itaque',   # conjunction
    'namque',   # conjunction
]

prepositions_1 = [
    'ex',       # preposition
    'ab',       # preposition
    'supra',    # adverb, preposition
    'infra',    # adverb, preposition
    'iuxta',    # preposition
    'secundum', # preposition, adjective
]

# DENY

misc = ['b', 'etc', 'ii']

adjectives = ['omnibus', 'omnia', 'aliud', 'alia', 'alii', 'aliis', 
    'tolletano', 'sacris', 'nulli', 'nulla', 'propria', 'prius',
    'alterius', 'bonum', 'tantum', 'solum', 'uerum', 'secundum']

nouns = ['papa', 'concilio', 'ecclesiae', 'auctoritate', 'augustinus',
    'episcopo', 'libro', 'gregorius', 'causa', 'ecclesia',
    'auctoritatibus', 'episcopus', 'statutum', 'episcopi', 'episcopis',
    'uxorem', 'papae', 'dei', 'dominus', 'deo', 'episcopum',
    'ieronimus', 'domino', 'ius', 'apostolus', 'exemplo', 'tempore',
    'peccatum', 'sacerdotes', 'coniugium', 'dictum', 'lege',
    'peccata', 'domini', 'titulo', 'iure', 'accusatione', 'capitulo',
    'ecclesiam', 'fide', 'gregorii', 'sententia', 'deus', 'epistola',
    'ambrosius', 'uiro', 'canonibus', 'leo', 'penitenciam', 'sinodo',
    'gelasius', 'offitio', 'sacerdotibus', 'episcoporum', 'ordinibus',
    'hereticis', 'potestatem', 'rebus', 'sententiam', 'christi',
    'concilii', 'christus', 'filios', 'iudicium', 'res',
    'auctoritas', 'crimen', 'augustini', 'filii', 'peccato',
    'consensu', 'modo', 'bomum', 'nichil', 'sacramenta', 'uerum']

pronouns_starred = ['illud', 'eius', 'eorum', 'eis', 'sua', 'suae', 'eo',
    'eum', 'ea', 'ei', 'eos', 'suis', 'ille', 'suo', 'illa', 'sui',
    'id', 'suam', 'illi', 'illis', 'suorum', 'eam', 'illo']

pronouns = ['que', 'his', 'se', 'hoc', 'sibi', 'quibus', 'hinc',
    'hec', 'quem', 'cui', 'quos', 'quorum', 'cuius', 'hac', 'ipsa',
    'uos', 'aliquid', 'hanc', 'quis', 'quid', 'qui', 'idem', 'eodem',
    'aliquis', 'qua']

verbs = ['est', 'sunt', 'ait', 'esse', 'scribit', 'legitur', 'sit',
    'dicens', 'possunt', 'potest', 'probatur', 'queritur', 'debet',
    'fuerit', 'intelligendum', 'sint', 'dicitur', 'fieri', 'intelligi',
    'prohibentur', 'prohibetur', 'intelligitur', 'patet', 'datur',
    'oportet', 'testatur', 'debent', 'fuerint', 'erat', 'uidetur',
    'habere', 'obicitur', 'apparet', 'esset', 'possit', 'poterit',
    'respondetur', 'scribens', 'ualet', 'liceat', 'facit', 'inuenitur',
    'colligitur', 'posse', 'probantur', 'permittitur', 'habet',
    'premissis']

def main():
    allow = adverbs_0 + adverbs_1 + conjunctions_0 + conjunctions_1 + prepositions_0 + prepositions_1
    deny = adjectives + misc + nouns + pronouns_starred + pronouns + verbs
    for word in words:
        # diagnostic: most be in either allow or deny
        if word not in allow and word not in deny:
            # print(word, file=sys.stderr)
            print('#' + word + ' Decide!')

        if word in allow:
        # if word not in deny:
            print(word)
        if word in deny:
            if word in pronouns_starred:
                print('#' + word + '*')
            else:
                print('#' + word)

if __name__ == '__main__':
    main()

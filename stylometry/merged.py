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

# allow

kestemont_allow = [
    'a',        # preposition
    'ad',       # preposition
    'ante',     # preposition
    'apud',     # preposition
    'atque',    # conjunction
    'aut',      # conjunction
    'autem',    # conjunction
    'contra',   # preposition, adverb
    'cum',      # preposition, conjunction
    'de',       # preposition
    'dum',      # conjunction
    'enim',     # conjunction
    'ergo',     # adverb
    'et',       # conjunction
    'etiam',    # adverb
    'hic'       # adverb
    'idem',     # pronoun
    'in',       # preposition
    'inter',    # preposition
    'ita',      # adverb
    'licet',    # conjunction
    'ne',       # conjunction, adverb
    'nec',      # conjunction
    'nisi',     # conjunction
    'non',      # adverb
    'nunc',     # adverb
    'per',      # preposition
    'post',     # preposition, adverb
    'pro',      # preposition
    'propter',  # preposition
    'quam',     # conjunction
    'qui',      # relative pronoun
    'quia',     # conjunction
    'quod',     # conjunction
    'quoque',   # conjunction
    'sed',      # conjunction
    'si',       # conjunction
    'sic',      # adverb
    'sicut',    # adverb
    'sine',     # preposition
    'siue',     # conjunction
    'super',    # adverb, preposition
    'tamen',    # adverb
    'tunc',     # adverb
    'uel',      # conjunction
    'uidelicet',# adverb
    'unde',     # adverb
    'ut',       # adverb, conjunction
    'xque',     # conjunction
]

adverbs = [
    'aliquando',# adverb
    'contra',   # preposition, adverb
    'ecce',     # adverb
    'ergo',     # adverb
    'etiam',    # adverb
    'forte',    # adverb
    'generaliter',      # adverb
    'hic',      # adverb
    'ideo',     # adverb
    'infra',    # adverb, preposition
    'ita',      # adverb
    'item',     # adverb
    'ne',       # conjunction, adverb
    'non',      # adverb
    'nunc',     # adverb
    'post',     # preposition, adverb
    'postea',   # adverb
    'prius',    # adverb
    'quando',   # conjunction, adverb
    'quo',      # adverb
    'quomodo',  # adverb
    'sic',      # adverb
    'sicut',    # adverb
    'similiter',# adverb
    'super',    # adverb, preposition
    'supra',    # adverb, preposition
    'tamen',    # adverb
    'tunc',     # adverb
    'uero',     # adverb
    'uidelicet',# adverb
    'unde',     # adverb
    'ut',       # adverb, conjunction
]

conjunctions = [
    'an',       # conjunction
    'atque',    # conjunction
    'aut',      # conjunction
    'autem',    # conjunction
    'cum',      # preposition, conjunction
    'dum',      # conjunction
    'enim',     # conjunction
    'et',       # conjunction
    'etsi',     # conjunction
    'itaque',   # conjunction
    'licet',    # conjunction
    'nam',      # conjunction
    'namque',   # conjunction
    'ne',       # conjunction, adverb
    'nec',      # conjunction
    'nisi',     # conjunction
    'quam',     # conjunction
    'quamuis',  # conjunction
    'quando',   # conjunction, adverb
    'quia',     # conjunction
    'quod',     # conjunction
    'quoque',   # conjunction
    'sed',      # conjunction
    'si',       # conjunction
    'siue',     # conjunction
    'uel',      # conjunction
    'ut',       # adverb, conjunction
    'xque',     # conjunction
]

prepositions = [
    'a',        # preposition
    'ab',       # preposition
    'ad',       # preposition
    'ante',     # preposition
    'apud',     # preposition
    'contra',   # preposition, adverb
    'cum',      # preposition, conjunction
    'de',       # preposition
    'ex',       # preposition
    'in',       # preposition
    'infra',    # adverb, preposition
    'infra',    # adverb, preposition
    'inter',    # preposition
    'iuxta',    # preposition
    'per',      # preposition
    'post',     # preposition, adverb
    'pro',      # preposition
    'propter',  # preposition
    'secundum', # preposition, adjective
    'sine',     # preposition
    'super',    # adverb, preposition
    'supra',    # adverb, preposition
    'supra',    # adverb, preposition
]

# deny

adjectives = ['alia', 'alii', 'aliis', 'aliud', 'alterius', 'bonum',
    'nulla', 'nulli', 'omnia', 'omnibus', 'prius', 'propria',
    'sacris', 'secundum', 'solum', 'tantum', 'tolletano', 'uerum']

nouns = ['accusatione', 'ambrosius', 'apostolus', 'auctoritas',
    'auctoritate', 'auctoritatibus', 'augustini', 'augustinus',
    'bomum', 'canonibus', 'capitulo', 'causa', 'christi', 'christus',
    'concilii', 'concilio', 'coniugium', 'consensu', 'crimen',
    'dei', 'deo', 'deus', 'dictum', 'domini', 'domino', 'dominus',
    'ecclesia', 'ecclesiae', 'ecclesiam', 'episcopi', 'episcopis',
    'episcopo', 'episcoporum', 'episcopum', 'episcopus', 'epistola',
    'exemplo', 'fide', 'filii', 'filios', 'gelasius', 'gregorii',
    'gregorius', 'hereticis', 'ieronimus', 'iudicium', 'iure',
    'ius', 'lege', 'leo', 'libro', 'modo', 'nichil', 'offitio',
    'ordinibus', 'papa', 'papae', 'peccata', 'peccato', 'peccatum',
    'penitenciam', 'potestatem', 'rebus', 'res', 'sacerdotes',
    'sacerdotibus', 'sacramenta', 'sententia', 'sententiam', 'sinodo',
    'statutum', 'tempore', 'titulo', 'uerum', 'uiro', 'uxorem']

pronouns = ['aliquid', 'aliquis', 'cui', 'cuius', 'eodem', 'hac',
    'hanc', 'hec', 'hinc', 'his', 'hoc', 'idem', 'ipsa', 'qua',
    'que', 'quem', 'qui', 'quibus', 'quid', 'quis', 'quorum', 'quos',
    'se', 'sibi', 'uos']

pronouns_deleted = ['ea', 'eam', 'ei', 'eis', 'eius', 'eo', 'eorum',
    'eos', 'eum', 'id', 'illa', 'ille', 'illi', 'illis', 'illo',
    'illud', 'sua', 'suae', 'suam', 'sui', 'suis', 'suo', 'suorum']

verbs = ['ait', 'apparet', 'colligitur', 'datur', 'debent', 'debet',
    'dicens', 'dicitur', 'erat', 'esse', 'esset', 'est', 'facit',
    'fieri', 'fuerint', 'fuerit', 'habere', 'habet', 'intelligendum',
    'intelligi', 'intelligitur', 'inuenitur', 'legitur', 'liceat',
    'obicitur', 'oportet', 'patet', 'permittitur', 'posse', 'possit',
    'possunt', 'poterit', 'potest', 'premissis', 'probantur',
    'probatur', 'prohibentur', 'prohibetur', 'queritur', 'respondetur',
    'scribens', 'scribit', 'sint', 'sit', 'sunt', 'testatur',
    'ualet', 'uidetur']

other = ['b', 'etc', 'ii']

def main():
    allow = adverbs + conjunctions + prepositions
    deny = adjectives + nouns + pronouns + pronouns_deleted + verbs + other
    for word in words:
        # diagnostic: most be in either allow or deny
        if word not in allow and word not in deny:
            # print(word, file=sys.stderr)
            print('#' + word + ' Decide!')

        if word in allow:
        # if word not in deny:
            print(word)
        if word in deny:
            if word in pronouns_deleted:
                print('#' + word + '*')
            else:
                print('#' + word)

if __name__ == '__main__':
    main()

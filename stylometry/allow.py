#!/usr/bin/python
words = ['in', 'non', 'et', 'est', 'quod', 'de', 'unde', 'ad',
    'qui', 'sed', 'uel', 'ut', 'cum', 'autem', 'si', 'a', 'ex',
    'sunt', 'uero', 'enim', 'etiam', 'ab', 'que', 'ait', 'item',
    'quia', 'ergo', 'esse', 'nec', 'his', 'per', 'se', 'hoc',
    'scribit', 'papa', 'sicut', 'xque', 'ita', 'concilio', 'nisi',
    'legitur', 'tamen', 'ecclesiae', 'illud', 'pro', 'auctoritate',
    'sit', 'sibi', 'quam', 'quibus', 'sic', 'eius', 'augustinus',
    'dicens', 'episcopo', 'eorum', 'libro', 'quo', 'eis', 'gregorius',
    'hinc', 'omnibus', 'licet', 'causa', 'possunt', 'potest', 'aut',
    'contra', 'post', 'sine', 'aliud', 'ecclesia', 'sua', 'an',
    'suae', 'probatur', 'queritur', 'siue', 'auctoritatibus', 'eo',
    'debet', 'eum', 'quis', 'episcopus', 'ne', 'b', 'inter', 'fuerit',
    'intelligendum', 'quoque', 'sint', 'super', 'ea', 'hec',
    'dicitur', 'ei', 'fieri', 'statutum', 'eos', 'episcopi',
    'episcopis', 'suis', 'atque', 'idem', 'intelligi', 'qua',
    'uxorem', 'ante', 'papae', 'quem', 'etc', 'dei', 'ille', 'suo',
    'ideo', 'illa', 'prohibentur', 'prohibetur', 'ecce', 'intelligitur',
    'uerum', 'dominus', 'nam', 'alia', 'propter', 'dum', 'sui',
    'tantum', 'alii', 'deo', 'supra', 'aliis', 'cui', 'episcopum',
    'ieronimus', 'apud', 'domino', 'id', 'patet', 'quid', 'datur',
    'eodem', 'ius', 'oportet', 'suam', 'testatur', 'debent',
    'secundum', 'fuerint', 'quos', 'uidelicet', 'aliquando',
    'apostolus', 'exemplo', 'quando', 'tempore', 'tunc', 'peccatum',
    'sacerdotes', 'solum', 'coniugium', 'erat', 'uidetur', 'dictum',
    'habere', 'illi', 'lege', 'peccata', 'quamuis', 'quorum',
    'domini', 'postea', 'titulo', 'iure', 'accusatione', 'capitulo',
    'ecclesiam', 'etsi', 'ii', 'obicitur', 'fide', 'gregorii',
    'illis', 'sententia', 'apparet', 'deus', 'epistola', 'ambrosius',
    'esset', 'itaque', 'sacris', 'nulli', 'nunc', 'possit', 'poterit',
    'respondetur', 'scribens', 'uiro', 'canonibus', 'cuius', 'leo',
    'nulla', 'ualet', 'hac', 'hic', 'liceat', 'nichil', 'penitenciam',
    'sinodo', 'facit', 'premissis', 'similiter', 'gelasius',
    'inuenitur', 'ipsa', 'offitio', 'sacerdotibus', 'uos', 'aliquid',
    'episcoporum', 'ordinibus', 'propria', 'hanc', 'hereticis',
    'infra', 'modo', 'potestatem', 'rebus', 'sententiam', 'alterius',
    'christi', 'colligitur', 'concilii', 'forte', 'aliquis', 'bonum',
    'christus', 'filios', 'posse', 'probantur', 'suorum', 'auctoritas',
    'crimen', 'eam', 'econtra', 'generaliter', 'illo', 'iudicium',
    'omnia', 'permittitur', 'tolletano', 'augustini', 'consensu',
    'filii', 'habet', 'iuxta', 'peccato', 'prius', 'quomodo', 'res']

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
    'tunc', 'nunc', 'hic']

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
]

prepositions_1 = [
    'ex',       # preposition
    'ab',       # preposition
    'supra',    # adverb, preposition
    'infra',    # adverb, preposition
    'iuxta',    # preposition
]

def main():
    allow = adverbs_0 + adverbs_1 + conjunctions_0 + conjunctions_1 + prepositions_0 + prepositions_1
    for word in words:
        if word in allow:
            print(word)

if __name__ == '__main__':
    main()

#!/usr/bin/python
#
# Paul Evans
#
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

misc = ['b', 'etc', 'ii']

k_other = ['quis', 'tantum', 'secundum', 'nichil', 'quomodo']

adjectives = ['omnibus', 'omnia', 'aliud', 'alia', 'alii', 'aliis', 
    'tolletano', 'sacris', 'nulli', 'nulla', 'propria', 'prius'
    'idem', 'eodem', 'alterius', 'bonum']

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
    'consensu', 'modo', 'bomum']

pronouns_starred = ['illud', 'eius', 'eorum', 'eis', 'sua', 'suae', 'eo',
    'eum', 'ea', 'ei', 'eos', 'suis', 'ille', 'suo', 'illa', 'sui',
    'id', 'suam', 'illi', 'illis', 'suorum', 'eam', 'illo']

pronouns = ['que', 'his', 'se', 'hoc', 'sibi', 'quibus', 'hinc',
    'hec', 'quem', 'cui', 'quos', 'quorum', 'cuius', 'hac', 'ipsa',
    'uos', 'aliquid', 'hanc']

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
    deny = adjectives + misc + nouns + pronouns_starred + pronouns + verbs
    for word in words:
        if word not in deny:
            print(word)

if __name__ == '__main__':
    main()

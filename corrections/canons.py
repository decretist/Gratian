#!/usr/local/bin/python3
#
# Paul Evans (10evans@cardinalmail.cua.edu)
#
import re
import sys
def main():
    f = open('./edF.txt', 'r')
    file = f.read()
    toc = open('./toc.txt', 'r')
    dictionary = {}
    # (?<=...) positive lookbehind assertion.
    canons = re.findall('(?:\<T T\>|(?<=\<T T\>))(.*?)'    # canon starts with text (<T T>) tag.
        '(?:'                   # non-capturing group.
            '\<1 [CD][CP]?\>|'  # canon ends with major division,
            '\<2 \d{1,3}\>|'    # or number of major division,
            '\<3 \d{1,2}\>|'    # or number of question,
            '\<4 \d{1,3}\>|'    # or number of canon,
            '\<P 1\>|'          # or Palea,
            # '\<T [AIPT]\>'    # or inscription or text tag.
            '\<T [APT]\>'      # or dicta or text tag.
        ')', file, re.S)        # re.S (re.DOTALL) makes '.' special character match any character including newline.
    # print('expected 4392 canons, found ' + str(len(canons)) + ' canons', file=sys.stderr)
    for canon in canons:
        canon = re.sub('\<S \d{1,4}\>\<L 1\> \-\d{1,4}\+', '', canon) # remove page and line number tags.
        canon = re.sub('\<P 1\> \-\[PALEA\.\+', '', canon) # remove Palea tag.
        canon = re.sub('\<P 0\>', '', canon) # remove Palea tag.
        canon = re.sub('\<T I\>', '', canon) # remove inscription tag.
        canon = re.sub(re.compile('\-\[.*?\]\+', re.S), '', canon)
        canon = re.sub('\-.*?\+', '', canon)
        canon = re.sub('\s+', ' ', canon)
        canon = re.sub('^\s+', '', canon) # remove leading whitespace characters
        canon = re.sub('\s+$', '', canon) # remove trailing whitespace characters
        key = toc.readline().rstrip()
        if key in dictionary:
        # if there's already a dictionary entry with this key, merge the entries
            # print('duplicate key: ' + key, file=sys.stderr)
            canon = dictionary[key] + ' ' + canon
        dictionary[key] = canon

    keysandpatterns = [
        {'key': 'D.5 c.4', 'pattern': '(Ad eius uero.*?qui gignitur ablactetur\.).*?(Si autem filios.*?est, ut esuriamus\.)'},
        {'key': 'D.9 c.1', 'pattern': '(Quicumque legibus imperatorum.*?acquirit grande premium\.)'},
        {'key': 'D.10 c.1', 'pattern': '(Lege imperatorum non.*?iura ecclesiastica dissolui\.).*?(Non quod imperatorum.*?inferre preiudicium asseramus\.)'},
        {'key': 'D.17 c.1', 'pattern': '(Sinodum episcoporum absque.*?potestis regulariter facere\.)'},
        {'key': 'D.19 c.1', 'pattern': '(Si Romanorum Pontificum.*?sibi ueniam denegari\.).*?(Dicendo uero: "omnia.*?Gelasium, mandasse probauimus\.)'},
        {'key': 'D.32 c.6', 'pattern': '(Preter hoc autem.*?ecclesiae communione separentur\.)'},
        {'key': 'D.38 c.4', 'pattern': '(Nulli sacerdotum liceat.*?Patrum regulis obuiare\.)'},
        {'key': 'D.48 c.2', 'pattern': '(Sicut neophitus dicebatur,.*?abrupta querit ascensum\.)'},
        {'key': 'D.50 c.52', 'pattern': '(Hii, qui altario.*?offitia ulterius promoueri\.)'},
        {'key': 'D.55 c.13', 'pattern': '(illi, cui erutus.*?sui perderet facultatem\.)'},
        {'key': 'D.56 c.1', 'pattern': '(Presbiterorum filios a sacris ministeriis remouemus,)'},
        {'key': 'D.61 c.3', 'pattern': '(Non negamus in.*?prestare quam sumere\.)'},
        {'key': 'D.61 c.5', 'pattern': '(Patrum beatorum uenerabiles.*?loci premium debetur\.)'},
        {'key': 'D.61 c.16', 'pattern': '(Obitum Victoris Panormitanae.*?credimus\) poterit inueniri,)'},
        {'key': 'D.62 c.1', 'pattern': '(Nulla ratio sinit,.*?a plebibus expetiti,)'},
        {'key': 'D.62 c.2', 'pattern': '(Docendus est populus, non sequendus,)'},
        {'key': 'D.67 c.2', 'pattern': '(Episcopus sacerdotibus ac ministris solus honorem dare potest,)'},
        {'key': 'D.68 c.4', 'pattern': '(Quamuis corepiscopis et.*?cuilibet epistolas mittere\.).*?(Quoniam, quamquam consecrationem.*?apicem non habent\.)'},
        {'key': 'D.74 c.2', 'pattern': '(sicut iustum est,.*?ministerio deiciatur iniuste\.)'},
        {'key': 'D.89 c.5', 'pattern': '(cauendum est a.*?amministrent, quam accusent\.)'},
        {'key': 'D.93 c.13', 'pattern': '(Diaconos propriam constituimus.*?facere plerumque conceditur\.)'},
        {'key': 'D.93 c.14', 'pattern': '(in sua diaconi.*?ministerio cessare debebit\.)'},
        {'key': 'D.93 c.19', 'pattern': '(Diaconus sedeat iubente.*?presbiterorum interrogatus loquatur\.)'},
        {'key': 'C.1 q.1 c.16', 'pattern': '(Cito turpem sequitur.*?transit in posteros\.)'},
        {'key': 'C.1 q.1 c.27', 'pattern': '(Non est putanda.*?offeruntur ex scelere\.).*?(Nimis ergo declinandum.*?symoniacae hereseos perpetrare\.)'},
        {'key': 'C.1 q.1 c.28', 'pattern': '(Vulnerato namque pastore.*?semetipsos placare debuerant\.)'},
        {'key': 'C.1 q.1 c.47', 'pattern': '(Sicut urgeri uideor,.*?operibus mortua est\.)'},
        {'key': 'C.1 q.1 c.97', 'pattern': '(Quod quidam dicunt.*?non posse iudicatur\?)'},
        {'key': 'C.2 q.1 c.7', 'pattern': '(de falsis se capitulis.*?modis omnibus reuocetur\.)'},
        {'key': 'C.2 q.3 c.6', 'pattern': '(Paulum itaque diaconum.*?ei culpam ignoscimus\.)'},
        {'key': 'C.2 q.6 c.12', 'pattern': '(omnium appellantium apostolicam.*?reseruata esse liquet;)'},
        {'key': 'C.3 q.4 c.3', 'pattern': '(Si quis uero.*?fide suspecti sunt\.)'},
        {'key': 'C.3 q.4 c.4', 'pattern': '(Consanguineorum coniunctiones nec.*?omnes eis consentientes\.)'},
        {'key': 'C.3 q.5 c.15', 'pattern': '(Athanasius a patriarcha suo.*?suae ecclesiae reddi precipitur)'},
        {'key': 'C.3 q.7 c.3', 'pattern': '("Qui sine peccato.*?illam lapidem mittat\.").*?(prius ipsi purgandi.*?uicia corrigere festinant\?)'},
        {'key': 'C.3 q.7 c.4', 'pattern': '(Iudicet ille de alterius.*?nulla leuitate ducatur\.)'},
        {'key': 'C.3 q.9 c.10', 'pattern': '(Decreuimus uestram debere.*?occasione non utitur\.)'},
        {'key': 'C.4 q.4 c.1', 'pattern': '(Nullus umquam presumat.*?idoneos accusatores, defensores)'},
        {'key': 'C.5 q.3 c.1', 'pattern': '(Si egrotans fuerit.*?prout causa dictauerit\.)'},
        {'key': 'C.5 q.6 c.3', 'pattern': '(Quia iuxta canonicas.*?famae plenitudine caruisse\.)'},
        {'key': 'C.6 q.4 c.7', 'pattern': '(Osius episcopus dixit:.*?Sinodus respondit: Placet\.)'},
        {'key': 'C.7 q.1 c.4', 'pattern': '(Pontifices, qui aliqua.*?presumptionis pullulet ambicio\.)'},
        {'key': 'C.8 q.3 c.1', 'pattern': '(Cum hic filius.*?promereri non poterit\.)'},
        {'key': 'C.9 q.2 c.3', 'pattern': '(Nullus primas, nullus metropolitanus,.*?rerum dispositio prohibetur\.)'},
        {'key': 'C.9 q.3 c.8', 'pattern': '(Conquestus est apostolatui.*?priuilegia seruentur ecclesiis,)'},
        {'key': 'C.11 q.1 c.5', 'pattern': '(Continua lege sancimus,.*?commune cum legibus\.)'},
        {'key': 'C.11 q.1 c.29', 'pattern': '(Neque enim iudicem.*?salus hominibus datur\.)'},
        {'key': 'C.11 q.1 c.36', 'pattern': '(Omnes itaque causae.*?episcoporum sententia deciderit\.)'},
        {'key': 'C.11 q.1 c.38', 'pattern': '(De persona presbiteri.*?executioni perfecte contradi\.")'},
        {'key': 'C.11 q.1 c.41', 'pattern': '(Sacerdotibus autem non.*?nos iudicemus Deos\.")'},
        {'key': 'C.11 q.1 c.45', 'pattern': '(Si quis cum.*?litis contestatione numerandum\.).*?(Non autem aliter.*?huiusmodi causis habentibus\.)'},
        {'key': 'C.11 q.3 c.66', 'pattern': '(Qui recte iudicat,.*?acceptione pecuniae uendit\.)'},
        {'key': 'C.11 q.3 c.89', 'pattern': '(Iniustum iudicium et.*?acta, non ualeat\.)'},
        {'key': 'C.11 q.3 c.93', 'pattern': '(Si dominus iubet.*?quam hominibus obedire\.)'},
        {'key': 'C.12 q.1 c.1', 'pattern': '(Omnis etas ab.*?testem uitae habeant\.)'},
        {'key': 'C.12 q.1 c.9', 'pattern': '(Scimus uos non.*?illis omnia communia\.)'},
        {'key': 'C.13 q.2 c.2', 'pattern': '(Ebron dicitur esse.*?in uno sepulcro\.")'}, # related to Beinecke MS 413 De iure sepulturae
        {'key': 'C.15 q.6 c.1', 'pattern': '(Si sacerdotibus uel.*?successoribus, sustinere permittimus\.).*?(Confessio ergo in.*?aut necessitatem fiunt\.)'},
        {'key': 'C.16 q.1 c.12', 'pattern': '(Qui uere et.*?ipsius ciuitatis episcopo.).*?(Conuenit uero ciuitatis.*?necessariam monasteriis exhibere.)'},
        {'key': 'C.16 q.1 c.60', 'pattern': '(Constitutum est a.*?iure presumant auferre,)'},
        {'key': 'C.16 q.2 c.8', 'pattern': '(Si quis episcoporum.*?cuius territorium est,)'},
        {'key': 'C.16 q.3 c.2', 'pattern': '(Illud etiam annecti.*?ita emanauit auctoritas\.)'},
        {'key': 'C.16 q.5 c.1', 'pattern': '(Consuetudo noua in.*?presumpserit, anathema sit\.).*?(Is autem, qui.*?neglexerit, anathema sit\.)'},
        {'key': 'C.16 q.7 c.31', 'pattern': '(Filiis, uel nepotibus.*?iudici corrigenda denuncient\.).*?(Ipsis tamen heredibus.*?iuris potestatem preferre,)'},
        {'key': 'C.17 q.4 c.5', 'pattern': '(Omnes ecclesiae raptores.*?sacrilegos esse iudicamus;)'},
        {'key': 'C.18 q.2 c.5', 'pattern': '(Quam sit necessarium.*?aliquem honorem promoueat\.)'},
        {'key': 'C.19 q.2 c.2', 'pattern': '(Duae sunt, inquit,.*?lex est canonum,).*?(Lex uero priuata.*?in corde scribitur,)'},
        {'key': 'C.19 q.3 c.6', 'pattern': '(Monasteriis omnibus fraternitas.*?modo audeant tonsorare\.)'},
        {'key': 'C.21 q.4 c.1', 'pattern': '(episcopos uel clericos.*?qui unguentis unguntur\.).*?(Priscis enim temporibus.*?domibus regum sunt\.")'},
        {'key': 'C.22 q.2 c.4', 'pattern': '(qui dicit falsum.*?autem uoluntate mentitur\.)'},
        {'key': 'C.22 q.4 c.8', 'pattern': '(Unusquisque simplicem sermonem.*?quod amicitiae fuit\.)'},
        {'key': 'C.22 q.5 c.1', 'pattern': '(Qui conpulsus a.*?quam animam dilexit\.)'},
        {'key': 'C.23 q.3 c.7', 'pattern': '(Non in inferenda,.*?ille, qui facit\.)'},
        {'key': 'C.23 q.3 c.9', 'pattern': '(Iustum est, ut.*?seuerioribus corrigantur uindictis,)'},
        {'key': 'C.23 q.4 c.7', 'pattern': '(Quisquis autem in.*?habet socium criminis\.)'},
        {'key': 'C.23 q.5 c.9', 'pattern': '(nequaquam contra hoc.*?homicidii crimine innectitur\.)'},
        {'key': 'C.23 q.7 c.4', 'pattern': '(Si autem consideremus.*?societate catholica utantur,)'},
        {'key': 'C.24 q.1 c.26', 'pattern': '(Fides ergo.*?correptionem deuita\.")'},
        {'key': 'C.24 q.1 c.40', 'pattern': '(Si quem forte.*?unitatem seruabat,)'}, # see ch. 2
        {'key': 'C.24 q.2 c.2', 'pattern': '(Mortuos suscitasse.*?esse absoluendum\.)'},
        {'key': 'C.26 q.5 c.4', 'pattern': '(Non oportet sacris.*?suarum uincula conprobantur\.)'},
        {'key': 'C.26 q.6 c.13', 'pattern': '(Agnouimus penitenciam morientibus.*?Dei pietate desperet,).*?(Quid hoc, rogo,.*?eo promittente promeruit\.)'},
        {'key': 'C.27 q.1 c.9', 'pattern': '(He uero, que.*?etc\. et infra\.).*?(Nam si Apostolus.*?fidem conatae sunt\.)'},
        {'key': 'C.27 q.1 c.18', 'pattern': '(ualeat custodiri, detrudere,.*?ualeas sollicitudine minuere\.)'},
        {'key': 'C.27 q.2 c.19', 'pattern': '(Sunt qui dicunt,.*?quis audeat accusare\?).*?(Si uero continentiam,.*?habet, sed mulier\.")'},
        {'key': 'C.27 q.2 c.46', 'pattern': '(Desponsatas puellas et.*?ante fuerant desponsatae,)'},
        {'key': 'C.30 q.1 c.2', 'pattern': '(Si quis filiastrum.*?ab uxore sua,)'},
        {'key': 'C.30 q.4 c.5', 'pattern': '(Post uxoris obitum.*?unionem spiritus pertransitur\.)'},
        {'key': 'C.30 q.5 c.3', 'pattern': '(Nostrates, tam mares.*?uelamen celeste suscipiunt\.)'},
        {'key': 'C.32 q.5 c.4', 'pattern': '(Lucretiam, matronam nobilem.*?unus adulterium admisit.")'},
        {'key': 'C.32 q.5 c.6', 'pattern': '(De pudicitia quis.*?possit in corpore\.).*?(Item Augustinus in.*?prius insita castitate\.)'},
        {'key': 'de Pen. D.1 c.30', 'pattern': '(Item, sicut auctoritas.*?in oris confessione\.)'},
        {'key': 'de Pen. D.1 c.51', 'pattern': '(Et paulo post.*?Dei non habet\.)'},
        {'key': 'de Pen. D.1 c.81', 'pattern': '(Tres sunt autem.*?Domino utique iudicaremur\.)'},
        {'key': 'de Pen. D.3 c.6', 'pattern': '(Penitenciam agere digne.*?auaritiae estibus anhelat\?)'},
        {'key': 'de Pen. D.7 c.2', 'pattern': '("Si quis positus.*?bene hinc exit;).*?(Si autem uis.*?non tu illa\.")'},
        {'key': 'C.33 q.5 c.4', 'pattern': '(Quod Deo pari.*?nullus defendisset annorum\.)'},
        {'key': 'C.35 q.2 c.10', 'pattern': '(Nec eam, quam.*?et cunctis hominibus\.)'},
        {'key': 'C.35 q.9 c.3', 'pattern': '(Quod quis conmisit.*?uult uitare, dampnabit\.)'},
        # {'key': '', 'pattern': '(.*?\.)'},
        # {'key': '', 'pattern': '(.*?\.).*?(.*?\.)'},
    ]

    for i in range (len(keysandpatterns)):
        key = keysandpatterns[i]['key']
        pattern = keysandpatterns[i]['pattern']
        result = re.search(pattern, dictionary[key])
        if result:
            if len(result.groups()) == 1:
                dictionary[key] = fixString(result.group(1))
            elif len(result.groups()) == 2:
                dictionary[key] = fixString(result.group(1)) + ' ' + fixString(result.group(2))
            # print(dictionary[key], file=sys.stderr)
        else:
            print('no match: ' + key + '\n' + dictionary[key], file=sys.stderr)

    # mid-sentence joins
    keysandpatterns = [
        {'key': 'C.2 q.6 c.11', 'pattern': '(Decreto nostro uestram rogantes karitatem mandamus,).*?(ut nichil prius de eo.*?aliis inferre presumant\.)'},
        {'key': 'C.2 q.6 c.22', 'pattern': '(Propter superfluam appellatorum.*?his quinque diebus).*?(spatium dierum, quo iter agi possit, conputetur\.)'},
        {'key': 'C.3 q.5 c.4', 'pattern': '(Suspectos, aut inimicos, aut facile litigantes,).*?(accusatores esse et.*?temporibus futuris excludimus\.)'},
        {'key': 'C.6 q.1 c.17', 'pattern': '(Infames esse ea.*?gradus debent prouehi).*?(nec ad accusationem.*?iuste recipi possunt\.)'},
        {'key': 'C.12 q.1 c.10', 'pattern': '(Nolo, ut aliquis.*?quisquis cum ypocrisi).*?(faciat testamentum.*?possit felicitatis hereditatem\.)'},
        {'key': 'C.12 q.2 c.21', 'pattern': '(Indigne ad altare.*?substantiam pauperum derelicta).*?(dispergit\.)'},
        {'key': 'C.21 q.1 c.1', 'pattern': '(Clericus ab instanti).*?(michi opus erant,.*?ministrauerunt manus istae\.)'},
        # {'key': '', 'pattern': '(.*?\.).*?(.*?\.)'},
    ]

    for i in range (len(keysandpatterns)):
        key = keysandpatterns[i]['key']
        pattern = keysandpatterns[i]['pattern']
        result = re.search(pattern, dictionary[key])
        if result:
            dictionary[key] = result.group(1) + ' ' + result.group(2)
            # print(dictionary[key], file=sys.stderr)
        else:
            print('no match: ' + key + '\n' + dictionary[key], file=sys.stderr)

    # insert
    key = 'C.1 q.1 c.51'
    dictionary[key] = '''Hii qui ab hereticis baptismum acceperunt formam tantum baptismi sine sanctificationis uirtute sumpserunt.''' # OK
    # insert
    key = 'C.1 q.1 c.113'
    dictionary[key] = '''Ordinationes, que interueniente pretio uel precibus, uel obsequio alicui personae ea intentione inpenso fuerit falsas esse diiudicamus.''' # OK
    # special fix
    key = 'C.2 q.1 c.7'
    dictionary[key] = '''Quod quidam frater ''' + dictionary[key][0].lower() + dictionary[key][1:]
    # C.2 q.3 c.4a has to be added to the table of contents by hand
    key = 'C.2 q.3 c.4a'
    dictionary[key] = '''Qui non probauerit quod obiecerit penam quam intulerit ipse patiatur.''' # OK
    # special fix
    key = 'C.4 q.4 c.1'
    dictionary[key] = dictionary[key][0:-1] + ' atque testes.'

    # C.11 q.1 c.33-d.p.c.34

    # interpolate
    key = 'C.12 q.4 c.1'
    pattern = '(Sacerdotes, uel quilibet.*?cura conmissa est,).*?(suarum rerum noscuntur.*?iure conquisitio pertinebit\.)'
    result = re.search(pattern, dictionary[key])
    if result:
        dictionary[key] = result.group(1) + ' si ' + result.group(2)
    else:
        print('no match: ' + key + '\n' + dictionary[key], file=sys.stderr)
    # interpolate
    key = 'C.13 q.2 c.15'
    pattern = '(Precipiendum est secundum.*?de rebus illius).*?(exigatur, siue ab illis.*?conficitur, nullatenus sepeliantur\.)'
    result = re.search(pattern, dictionary[key])
    if result:
        dictionary[key] = result.group(1) + ' a quibus ' + result.group(2)
    else:
        print('no match: ' + key + '\n' + dictionary[key], file=sys.stderr)
    # C.14 q.4 c.9a has to be added to the table of contents by hand
    key = 'C.14 q.4 c.9a'
    dictionary[key] = '''Nullus clericorum amplius recipiat quam cuiquam accomodauit; si pecuniam, pecuniam; si speciem, speciem.''' # OK
    # add
    key = 'C.19 q.2 c.2'
    dictionary[key] = dictionary[key] + ''' Si quis horum qui priuata lege ducitur spiritu sancto afflatus proprium, quod sub episcopo retinet, dimittere et in monasterio se saluare uoluerit, quoniam priuata ducitur publica lege non tenetur. Dignior enim est priuata lex quam publica Quisquis ergo hac lege ducitur etiam episcopo suo contradicente erit liber nostra auctoritate.''' # OK
    # special fix
    key = 'C.22 q.2 c.4'
    dictionary[key] = '''Non est iudicandus mendax ''' + dictionary[key][0].lower() + dictionary[key][1:]
    # insert
    key = 'C.22 q.5 c.15'
    dictionary[key] = '''Pueri ante xiiii annos iurare cogantur.'''
    # add
    key = 'C.23 q.7 c.4'
    dictionary[key] = '''Quicquid ergo nomine ecclesiarum a parte Donati possidebant, Christiani imperatores legibus religiosis cum ipsis ecclesiis ad catholicam transferre iusserunt. Et post pauca: ''' + dictionary[key] # OK
    # C.26 q.7 c.16a has to be added to the table of contents by hand
    key = 'C.26 q.7 c.16a'
    dictionary[key] = '''Qui diuinationes expetunt et morem gentilium subsecuntur aut in domos suas huiusmodi homines introducunt, exquirendi aliquid arte malefica aut expiandi causa, sub regula quinquennii iaceant secundum gradum penitentie definitos.'''
    # add
    key = 'C.30 q.4 c.5'
    dictionary[key] = dictionary[key] + ''' Post susceptum uero de fonte filium uel filiam spiritualem, qui ex conpatre uel conmatre nati fuerint, matrimonio coniungi non possunt, quia leges seculi non emancipatos adoptiuis prohibent copulari.''' # OK
    # add
    key = 'C.32 q.5 c.4'
    dictionary[key] = '''Idem: ''' + dictionary[key]
    # interpolate
    key = 'C.34 q.1 c.1'
    pattern = '(Cum per bellicam.*?tam culpabilis iudicetur).*?(in ius alienum.*?merito sunt laudandae\.)'
    result = re.search(pattern, dictionary[key])
    if result:
        dictionary[key] = result.group(1) + ' si ' + result.group(2)
    else:
        print('no match: ' + key + '\n' + dictionary[key], file=sys.stderr)

    count = 1
    keys = tuple(open('./toc_r1.txt', 'r')) # uniq toc.txt > dedup.txt
    for key in keys:
        key = key.rstrip()
        #
        # print(key + '\n\n' + dictionary[key] + '\n')
        #
        # print('{:0=4}'.format(count) + ' _ ' + dictionary[key])
        # count = count + 1
        #
        # outfilename = './tmp/' + key + '.txt'
        # f = open(outfilename, 'w')
        # f.write(dictionary[key] + '\n')
        # f.close

def fixString(string):
    if string[0].islower():
        string = string[0].upper() + string[1:]
    if string[-1] == ',' or string[-1] == ';':
        string = string[0:-1] + '.'
    if string[-1].isalpha():
        string = string + '.'
    # print(string[0:36] + ' ... ' + string[-36:], file=sys.stderr)
    return string

if __name__ == '__main__':
    main()

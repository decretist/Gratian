---
title: Distant Reading of Gratian’s _Decretum_
author: Paul Evans
bibliography: project.bib
csl: chicago-fullnote-bibliography.csl
---
##Statement of the Problem and Background

Gratian, an otherwise unknown teacher, finished compiling and writing
the _Concordia Discordantium Canonum_ ("Agreement of Disagreeing
Canons") or _Decretum_ around 1140 in Bologna as a textbook for
university students studying canon law. In 1996, Anders Winroth
discovered that there were two versions or recensions of the
_Decretum_, and that four surviving 12th-century manuscripts preserve
the text of the first recension. Winroth argued that different
authors (Gratian 1 and Gratian 2) compiled and wrote the two
recensions, and that it was the first recension that the author
finished and began to circulate around 1140, not the second.

Gratian compiled the _Decretum_ out of canons taken from decrees
of church councils, from papal letters, from Roman law, and from
patristic authors like Augustine, Ambrose, Jerome, and Gregory.
Gratian collected the texts for the canons that he used from formal
sources (previous canonical collections) as opposed to material
(original) sources. There are 1,860 canons in the first recension
and 3,945 in the second. On his own authority as a jurist, he
commented on the canons in the form of sayings or _dicta_. Gratian
organized the canons and _dicta_ in the first part of the _Decretum_
into 101 distinctions and those in the second part into 36 cases.
He introduced each of the cases in the second part with a hypothetical
case statement that sets out the facts of the case and divides it
into questions. In addition to the cases, the second part of the
_Decretum_ includes a treatise on penance (_de Penitentia_). The
third part, a treatise on the sacraments (_de Consecratione_), was
added to the _Decretum_ at a late stage in the composition of the
second recension. Other teachers of canon law added approximately
150 canons (_paleae_) to the second recension after it began to
circulate.

Winroth’s identification of the Florence (Fd), Barcelona (Bc), Paris
(P), and Admont (Aa) manuscripts as a first recension of Gratian’s
_Decretum_ has been generally accepted, but some of the conclusions
he drew from the discovery remain controversial. Winroth argues
that Gratian 1 and Gratian 2 were probably not the same person,
because Gratian 2 makes much fuller use of the _Codex_ and _Digest_
of Justinian than does Gratian 1, whose Roman law sources were
largely limited to excerpts from barbarian legal codes that he found
in previous canonical collections. Pennington argues that Gratian
made earlier and more sophisticated use of Roman law concepts and
terminology than Winroth gives Gratian credit for, but his argument
depends in part on evidence from the St. Gall (Sg) manuscript of
the _Decretum_, which Winroth rejects as an abbreviation.

Moreover, Winroth rejects the hypothesis that a _dictum_ that
apparently refers to the Second Lateran Council of 1139 is an
interpolation. He is consequently committed to a late date for the
first recension (around 1140). Winroth originally argued for a late
date (mid-1150s) for the second recension as well, but as evidence
emerged that the second recension was in general circulation by
1150, he shifted to arguing for a period of just a few years between
the first and second recensions, while continuing to insist that
1140 is the earliest possible date for the first recension, and
that the first and second recensions are the work of two different
individuals. Recently, Winroth reexamined the 12th-century tradition
that Gratian had been a bishop, and argues that a "Gratian of Chiusi,
bishop" mentioned in a Siena necrology, who may have died in 1144
or 1145, is the Master Gratian responsible for the first recension
of the _Decretum_. Winroth considers this further evidence that
Gratian 1 and Gratian 2 were not the same person.

The controversy over the identity of Gratian is an aspect of a
broader debate over what the discovery of the recension preserved
in Fd, Bc, P, and Aa adds to our understanding of the evolution of
the _Decretum_. For the last fifteen years, that debate has revolved
primarily around the question of whether Sg represents a recension
of the _Decretum_ earlier than the first recension. Winroth maintains
that the first recension was a finished product that Gratian 1
released into circulation, and that Sg is an abbreviation of the
first recension. Pennington, on the other hand, argues that both
Sg and the first recension are snapshots taken at particular moments
in a much longer process of continuous textual evolution (going
back as far as the 1120s), and that Sg represents an earlier stage
in the development of the _Decretum_ than the first recension. The
debate over Sg has been fought to a stalemate, and new evidence is
needed to move the discussion forward.

##Purpose

The purpose of the project is to reconsider the debates over the
identity of Gratian and the evolution of the _Decretum_ between the
first and second recensions using statistical analysis of word
frequencies in the text as evidence. The first question concerns
the identity of Gratian: whether or not the _Decretum_ is the work
of a single master who compiled the canons and composed the case
statements and _dicta_ organizing the presentation of and commenting
on those canons. The result will be an assessment of the likelihood
that the case statement and _dicta_ were written by one, two, or
more authors.  Many topics that Gratian covered in the first recension
were expanded upon in the second recension by the incorporation of
additional canons and _dicta_. At least one entirely new topic –
the status of Jews in canon law – was added in the second recension.
The second question concerns the evolution of the text of the
_Decretum_ between the first and second recensions: what other
entirely new topics were added to the _Decretum_ in the second
recension? The result will be the identification of additional
entirely new topics, if any.

##Methodology

Ideally, electronic texts of good critical editions of the first
and second recensions of the _Decretum_, following consistent
orthographic conventions, would be available for analysis. In
practice, what is available is the electronic text of Friedberg's
problematic 1879 edition of the _Decretum_ that the MGH used to
produce its Gratian concordance. Friedberg's text can be transformed
into a proxy for the second recension by removing _de Consecratione_
and the _paleae_. The resulting second recension text can then be
transformed into a proxy for the first recension by applying the
differences found in the appendix of Winroth's  _The Making of
Gratian's Decretum_.

For authorship attribution, we are interested in analyzing common
function words like conjunctions and prepositions in the case
statements and the _dicta_ – those parts of the text of the _Decretum_
attributed since the 12th century to Gratian himself. Three samples
are used: the case statements, which do not differ substantially
between the first and second recensions; the first recension _dicta_;
and a sample including _dicta_ found only in the second recension,
plus words that appear only in the second-recension forms of those
_dicta_ that differ between the first and second recension. The
statistical frequency of the function words in each of the samples
will then be analyzed using principal component analysis to determine
whether it is possible to distinguish the author(s) of the case
statements and the first and second-recension _dicta_ from one
another. Principal component analysis is concerned only with words
that are indeclinable forms in Latin, so there is no need to lemmatize
the samples.

To identify entirely new topics added to the second recension of
the _Decretum_, we are interested in analyzing content words in
both the _dicta_ and the canons. Two samples are used: the
first-recension _dicta_ and canons; and a sample including _dicta_
and canons found only in the second recension, plus words that
appear only in the second-recension forms of those _dicta_ and
canons that differ between the first and second recensions. A list
of common stop words found in _Wortkonkordanz zum Decretum Gratiani_
will first be removed from the samples, which will then be lemmatized
using the Schinke Latin word stemming algorithm. (The lemmatization
algorithm uses an exclusion list of words ending in –que for which
the ending is interpreted as part of the word rather than as an
enclitic. Preliminary results indicate that the list needs further
refinement.) Finally, the statistical frequency of unique or most
distinctive words will be used to determine whether it is possible
to identify topics which appear only in the second recension. If
new topics are identified, they will be verifiable by close reading.
Traditional scholarly methods can then be used to more fully explore
their implications for our understanding of the evolution of the
text of the _Decretum_ between the first and second recensions.

Python and the Natural Language Toolkit (NLTK) will be used for
corpus preparation. R and the Stylometry with R package (stylo)
will be used for Principal Component Analysis and for analysis of
Most Distinctive Words.

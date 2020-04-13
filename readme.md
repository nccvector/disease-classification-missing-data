# Disease Classification using Bayesian Networks and Missing Data (decision making under uncertainity)

## The problem
Olertawo is a university town in New Zealand in which there is a strange medical condition called Dunetts Syn-
drome. Dunetts Syndrome comes in two forms: mild and severe (as well as not being there at all). It is known
that about half the population of Olertawo have Dunetts, and that about half of those with Dunetts have it in severe
form. Dunetts Syndrome has three observable symptoms, Sloepnea, Foriennditis, and Degar spots, all of which
may be present if the patient has Dunetts, but with varying frequencies. In particular, it is well known that Fori-
ennditis is present much more often when the condition is in its mild form (it is not as common in severe cases),
whereas Degar spots are present much more often when the condition is in its severe form (and not as common in
the mild cases). Sloepnea is present in either form of Dunetts Syndrome. However, about 10% of the population
have a gene (called TRIMONO-HT/S) that makes it so they hardly ever show symptom Sloepnea (whether they
have Dunetts Syndrome or not), but does not affect the other two symptoms. Symptoms Sloepnea, Foriennditis, and
Degar spots are sometimes present (but much less often) even if the person does not have Dunetts Syndrome.
<br/>
You are given a dataset from 2000 patients, giving the existence of the three symptoms Sloepnea, Forienndi-
tis and Degar spots, and whether they have gene TRIMONO-HT/S or not. About 5% of the data also has a
record of whether the patient actually had Dunetts Syndrome or not.

## Initial Bayesian Network for the problem
<img src="figs/network graph.jpg" align="middle" />

<br />

# Dependencies
- pomegranate

## Use
```sh
$ pip install pomegranate

$ python main.py
```
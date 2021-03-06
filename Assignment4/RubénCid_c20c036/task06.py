# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSv61ejXESrp34CUz1PqZCsoA43tzc8y

**Task 06: Modifying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))

print("\n\n[TASK 0]")
for s, p, o in g:
  print(s,p,o)

""""**TASK 6.1: Create a new class named "University"**"""

g.add((ns.University, RDF.type, RDFS.Class))

print("\n\n[TASK 1]")
for s, p, o in g:
  print(s, p, o)

"""
**TASK 6.2: Add "Researcher" as a subclass of "Person"**
"""
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

print("\n\n[TASK 2]")
for s, p, o in g:
  print(s, p, o)


"""
**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**
"""
jane = ns.JaneSmith

g.add((jane, RDF.type, ns.Researcher))

print("\n\n[TASK 3]")
for s, p, o in g:
  print(s, p, o)


"""
**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

"""

from rdflib import FOAF


g.add((jane, FOAF.name, Literal("Jane Smith")))
g.add((jane, FOAF.family_name, Literal("Smith")))
g.add((jane, FOAF.familyName, Literal("Smith")))
g.add((jane, VCARD.FN, Literal("Jane Smith")))

print("\n\n[TASK 4]")
for s, p, o in g:
  print(s, p, o)

"""
**TASK 6.5: Add UPM as the university where John Smith works**
"""

upm = ns.UPM
g.add((upm, RDF.type, ns.University))
g.add((jane, VCARD.Work, upm))


print("\n\n[TASK 5]")
for s, p, o in g:
  print(s, p, o)


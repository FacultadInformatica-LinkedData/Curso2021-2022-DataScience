# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F8QTD2IXyjoi9kO89TiRa2tXd0tPTMyH

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
# Visualize the results

#for r in g.query(q1):
#  print(r)

from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
    SELECT ?sc
    WHERE {
      ?sc rdfs:subClassOf ns:Person.
    }''', initNs = {"rdfs": RDFS, "ns": ns})

for r in g.query(q1):
  print(r)

# ns = Namespace("http://somewhere#") comprobación
# for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  # print(s,p,o)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results

for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s, p, o)

for triple in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, p1, o1 in g.triples((None, RDF.type, triple[0])):
    print(s1, p1, o1)

q2 = prepareQuery('''
    SELECT ?p
    WHERE {
      { ?p rdf:type ns:Person.
    } UNION {?sc rdfs:subClassOf ns:Person.
    ?p rdf:type ?sc }
    }
    ''', initNs = {"rdf": RDF, "rdfs": RDFS, "ns": ns})

for r2 in g.query(q2):
  print(r2)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)):
    print(s1, p1, o1)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, p1, o1 in g.triples((None, RDF.type, s)):
    for s2, p2, o2 in g.triples((s1, None, None)):
      print(s2, p2, o2)

q3 = prepareQuery('''
    SELECT ?p ?prop1 ?prop2
    WHERE {
      { ?p rdf:type ns:Person. 
        ?p ?prop1 ?prop2
      } UNION{
        ?sc rdfs:subClassOf ns:Person. 
        ?p rdf:type ?sc.
        ?p ?prop1 ?prop2
      }
    }''', initNs = {"rdf": RDF, "rdfs": RDFS, "ns": ns})

for r3 in g.query(q3):
  print(r3)
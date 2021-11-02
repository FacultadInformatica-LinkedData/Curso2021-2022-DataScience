from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

with open('example6.rdf', 'r') as f:
    g = Graph()
    g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
    g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
    g.parse(f, format="xml")

""" Leemos el fichero RDF de la forma que lo hemos venido haciendo """
# github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"
# g2 = Graph()
# g2.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
# g2.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
# g2.parse("https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4/resources/example6.rdf", format="xml")

# Definimos los namespaces:
ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

""" List all subclasses of "Person" with RDFLib and SPARQL """
subclass_of_person = []
# with RDFlib:
print("Resultados query RDFlib:")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)
    subclass_of_person += [s]

# With SPARQL:
print("Resultados query SPARQL:")
q1 = prepareQuery('''
  SELECT ?Subclass WHERE { 
    ?Subclass RDFS:subClassOf ns:Person. 
  }
  ''',
                  initNs={"RDFS": RDFS, "ns": ns}
                  )

for r in g.query(q1):
    print(r.Subclass)

print("----------------------------------------------------------")

""" List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses) """
# With RDFlib:
personas = []
print("Resultados query RDFlib:")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    personas += [s]
    print(s)
for subclass in subclass_of_person:
    for s1, p1, o1 in g.triples((None, RDF.type, subclass)):
        print(s1)
        personas += [s1]

# With SPARQL:
# Individuals directos de Person
q2 = prepareQuery('''
  SELECT DISTINCT ?Persons WHERE { 
    ?Persons RDF:type ns:Person.

  }
  ''',
                  initNs={"ns": ns, "RDF": RDF}
                  )
# Individuals de las subclases de Person
q3 = prepareQuery('''
  SELECT DISTINCT ?Persons WHERE { 
    ?Subclass RDFS:subClassOf ns:Person.
    ?Persons RDF:type ?Subclass

  }
  ''',
                  initNs={"RDFS": RDFS, "ns": ns, "RDF": RDF}
                  )

print("Resultados query SPARQL:")
for r in g.query(q2):
    print(r.Persons)
for r in g.query(q3):
    print(r.Persons)

print("----------------------------------------------------------")

""" List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL """
# With RDFlib:
print("Resultados query RDFlib:")
for person in personas:
    print("Persona: ", person, "---->")
    for s, p, o in g.triples((person, None, None)):
        print(p, o)

# With SPARQL:
# Individuals directos de Person y sus propiedades
q4 = prepareQuery('''
  SELECT DISTINCT ?Persons ?Property ?Object WHERE { 
    ?Persons RDF:type ns:Person.
    ?Persons ?Property ?Object

  }
  ''',
                  initNs={"ns": ns, "RDF": RDF}
                  )

# Individuals de las subclases de Person y sus propiedades
q5 = prepareQuery('''
  SELECT DISTINCT ?Persons ?Property ?Object WHERE { 
    ?Subclass RDFS:subClassOf ns:Person.
    ?Persons RDF:type ?Subclass.
    ?Persons ?Property ?Object.

  }
  ''',
                  initNs={"RDFS": RDFS, "ns": ns, "RDF": RDF}
                  )

print("Resultados query SPARQL:")
for person in personas:
    print("Persona: ", person, "---->")
    for r in g.query(q4):
        if r.Persons == person:
            print(r.Property, r.Object)
    for r in g.query(q5):
        if r.Persons == person:
            print(r.Property, r.Object)

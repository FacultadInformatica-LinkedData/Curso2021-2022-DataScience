from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

with open('example5.rdf', 'r') as f:
    g = Graph()
    g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
    g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
    g.parse(f, format="xml")


# Namespaces:
ns = Namespace("http://somewhere#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
# github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4" \
#                  "/course_materials "
# g = Graph()
# g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
# g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
# g.parse(github_storage + "/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
    print(s, p, o)

print("--------------------------------------------------------------------------------------------------------------")

"""Create a new class named 'University' """
# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

print("--------------------------------------------------------------------------------------------------------------")

""" Add "Researcher" as a subclass of "Person" """
# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

print("--------------------------------------------------------------------------------------------------------------")

""" Create a new individual of Researcher named "Jane Smith" """
# TO DO
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

print("--------------------------------------------------------------------------------------------------------------")

""" Add to the individual JaneSmith the fullName, given and family names """
# TO DO
g.add((ns.JaneSmith, vcard.FN, Literal('Jane Smith')))
g.add((ns.JaneSmith, vcard.Given, Literal('Jane')))
g.add((ns.JaneSmith, vcard.Family, Literal('Smith')))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

print("--------------------------------------------------------------------------------------------------------------")

""" Add UPM as the university where John Smith works """
# TO DO
g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, vcard.worksAt, ns.UPM))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

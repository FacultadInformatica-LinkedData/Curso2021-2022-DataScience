
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery


G = Graph()
G.parse("./rdf/museos.ttl", format="ttl")

# Carga de los Namespaces

prop = Namespace("https://www.mapmadrid.org/ontology/0.1.0/Propiedades/")
clases = Namespace("https://www.mapmadrid.org/ontology/0.1.0/Clases/")

#

q = prepareQuery("""
    SELECT ?l
    WHERE{
        ?x prop:isLocated ?loc.
        ?loc prop:hasCoordinates ?lat.
        ?lat schema:latitude ?l.
    }   
    """,
    initNs={
        "prop": "https://www.mapmadrid.org/ontology/0.1.0/Propiedades/",
        "schema": "http://www.schema.org/"
        }
)

for name in G.query(q):
    print(name[0])

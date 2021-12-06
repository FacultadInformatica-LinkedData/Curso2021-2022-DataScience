
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery


G = Graph()
G.parse(r"./Group01/rdf/linked_museos.ttl", format="ttl")
print("TEXT PARSED")
# Carga de los Namespaces

prop = Namespace("https://www.mapmadrid.org/ontologia/Propiedades/")
clases = Namespace("https://www.mapmadrid.org/ontologia/Clases/")

#

q = prepareQuery("""SELECT DISTINCT ?value
    WHERE{
        ?name rdf:type <https://www.mapmadrid.org/ontology/0.1.0/Clases/Museos>.
        ?name <https://www.mapmadrid.org/ontology/0.1.0/Propiedades/isLocated> ?loc.
        ?loc <https://www.mapmadrid.org/ontology/0.1.0/Propiedades/inNeighborhood> ?value.
    }
    """
)

print("[DOING QUERY]")
for dist in G.query(q):
    print(dist)

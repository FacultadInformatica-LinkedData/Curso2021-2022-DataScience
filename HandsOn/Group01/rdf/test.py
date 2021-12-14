
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery


G = Graph()
G.parse(r"museos_linked.ttl", format="ttl")
print("TEXT PARSED")
# Carga de los Namespaces

prop = Namespace("https://www.mapmadrid.org/ontologia/Propiedades/")
clases = Namespace("https://www.mapmadrid.org/ontologia/Clases/")

#
q = prepareQuery("""
    SELECT DISTINCT ?prop, COUNT(DISTINCT ?values) as ?posiblesValores
    WHERE{
        ?name rdf:type <https://www.mapmadrid.org/ontologia/Museo>.
        ?name ?prop ?value.
    }
    """
)

print("[DOING QUERY]")
for dist in G.query(q):
    print(dist)

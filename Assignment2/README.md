@prefix :<http://www.ontologies.org/ontologies/clas#>.
@prefix rdf:<http://www.ontologies.org/ontologies/properties#>.

:Class01
:includes :Sensor029;
:includes :Computer101 .
:Sensor029
rdf:hasMeasurement :Measurement8401 .
:Measurement8401
rdf:hasTemperatue 29;
rdf:atTime "2010-06-12T12:00:12"^^xsd:dateTime .
:Computer101
rdf:hasOwner :User10A .
:User10A
rdf:hasName "Pedro".

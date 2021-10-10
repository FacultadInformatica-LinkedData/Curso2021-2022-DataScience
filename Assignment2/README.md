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
@prefix : <http://example.org/#> .
@prefix prop: <http://www.oeg-upm.net/Properties#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

:class01 prop:includes :Sensor029;
         prop:includes :Computer101 .

:Sensor029 prop:hasMeasurement :Measurement8401 .

:Measurement8401 prop:hasTemperature "29"^^xsd:integrer;
                 prop:atTime "2010-06-12T12:00:12"^^xsd:dateTime .

:Computer101 prop:hasOwner :User10A .

:User10A prop:hasName "Pedro".
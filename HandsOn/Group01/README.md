
# Grupo 01
## Datos Selecionados
Para la realización de está practica, se ha selecionado un dataset relacionado con las 
smart cities y las centros culturales. Para ver más [ver](https://htmlpreview.github.io/?https://github.com/RubenCid35/Curso2021-2022-DataScience/master/HandsOn/Group02/requirementes/datasetRequirements.html).


## Información sobre la App
### Para siguientes partes.
<br><br><br>


## Problemas Con la aplicación Helio
Durante el proceso de mapear los datos y pasarlos a rdf utilizando RML. No pudimos completar dado que la
aplicación de helio presentaba problemas si intentabamos ejecutar los mappings con conjuntos de datos
medianos ( +100 lineas del CSV) y grandes. Daba errores con algun elemento interno que ejecuta Queries SQL y por alguna razón,
estas se rompian y daban error al introducir ciertos datos en ellas.
Por si acaso y para demostrar que funciona, se han parseado correctamente para todos los museos y alrededor de 100 monumentos.
        
### Ejemplo de dichos problemas
```
22:00:12.497 [pool-1455-thread-2] WARN  helio.materialiser.evaluator.H2Evaluator - org.h2.jdbc.JdbcSQLException: Syntax error in SQL statement INSERT INTO LINKRULES(LINKING_ID, SOURCE, TARGET, EXPRESSION, SOURCE_VALUES, TARGET_VALUES, PREDICATE, INVERSE_PREDICATE) VALUES ( 52491184, 'https://www.mapmadrid.org/resources/Localizaciones/CO'donnellNum78233', 'null', 'S({ParsedPostal}) = T({ParsedPostal})', '[{"ParsedPostal":"10000N64724[*]"}]', 'null', 'https://www.mapmadrid.org/ontology/0.1.0/Propiedades/hasAddress', 'null') [42000-60]
```

## Colaboradores

- [David Lázaro](https://github.com/davidlm28)
- [Lara Herrera](https://github.com/laraherrerafernandez)
- [Pablo Martín](https://github.com/pablomartinescobar1)
- [Rubén Cid](https://github.com/RubenCid35)

<br><br><br>


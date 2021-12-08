1
    General
    Analysis
        - No es recomendable que las URIs tengan información de versionado ("0.1.0"), ya que al cambiar la versión se romperán los enlaces.
        - No es necesario tener rutas distintas para clases y propiedades.
        - No son necesarias las URIs para los tipos (ej. "MuseumType"), la URI del tipo es la de la clase correspondiente.
        - Es buena práctica nombrar las clases (y por consiguiente las rutas) en singular ("Museos"->"Museo").
    Ontology
        - Corregir errata ("equpiment")
        - No mezcléis etiquetas en castellano y en inglés.
        - Las clases "MuseumTipo" y "MonumentType" no son necesarias; eso está definido en la jerarquía de clases.
        - La label de MuseumTipo no es correcta.
        - Algunas de las datatype properties que usais podrían ser object properties y conectar a otros recursos que podríais usar en el enlazado (ej. Neighbourhood, District).
    RDF generated
        - Hay un fallo en el prefijo de schema.org ("http://www.schema.orgGeoCoordinatess").
        - Los tipos de datos de las coordenadas no son correctos.
        - Las tildes aparecen como "#". Revisar el encoding.

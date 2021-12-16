import pygame


def buscar_site_por_nombre(name: str) -> str:
    querie = "?sujeto" + " " + "<https://dbpedia.org/ontology/name>" + " " + "'" + name + "'" + "."
    querie1 = "?sujeto rdf:type <http://www.w3.org/ns/org/Site>."
    return querie + "\n" + querie1


def buscar_site_por_direcc(direcc: str) -> str:
    querie = "?sujeto" + " " + "<http://www.schema.org/streetAddress>" + " " + "'" + direcc + "'" + "."
    querie1 = "?sujeto rdf:type <http://www.schema.org/Place>."
    return querie + "\n" + querie1


def buscar_descripcion_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/description> ?descripcion"
    return "SELECT ?descripcion WHERE{" + querie_nombre + "\n" + querie + "}"


def buscar_descripcion_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <http://www.schema.org/description> ?descripcion."
    return "SELECT ?descripcion WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_accesibilidad_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://museosymonumentos.es/ontology/ConoceMadrid#accessibility> ?accesibilidad"
    return "SELECT ?accesibilidad WHERE{" + querie_nombre + "\n" + querie + "}"


def buscar_accesibilidad_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <http://museosymonumentos.es/ontology/ConoceMadrid#accessibility> ?accesibilidad."
    return "SELECT ?accesibilidad WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_horario_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/openingHours> ?horario"
    return "SELECT ?horario WHERE{" + querie_nombre + "\n" + querie + "}"


def buscar_horario_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <http://www.schema.org/openingHours> ?horario."
    return "SELECT ?horario WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_email_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/email> ?email"
    return "SELECT ?email WHERE{" + querie_nombre + "\n" + querie + "}"


def buscar_email_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <http://www.schema.org/email> ?email."
    return "SELECT ?email WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_telef_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/telephone> ?telef"
    return "SELECT ?telef WHERE{" + querie_nombre + "\n" + querie + "}"


def buscar_telef_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <http://www.schema.org/telephone> ?telef."
    return "SELECT ?telef WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_nombre_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sitio <http://www.schema.org/place> ?sujeto."
    querie = "?sitio <https://dbpedia.org/ontology/name> ?nombre."
    return "SELECT ?nombre WHERE{" + querie_direcc + "\n" + querie + "\n" + querie1 + "}"


def buscar_direcc_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/place> ?localizacion."
    querie1 = "?localizacion <http://www.schema.org/streetAddress> ?direcc."
    return "SELECT ?direcc WHERE{" + querie_nombre + "\n" + querie + "\n" + querie1 + "}"


def buscar_coord_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/place> ?localizacion."
    querie1 = "?localizacion <http://www.schema.org/geo> ?coord."
    querie2 = "?coord <http://www.schema.org/latitude> ?lat."
    querie3 = "?coord <http://www.schema.org/longitude> ?lon."
    return "SELECT ?lat ?lon WHERE{" + querie_nombre + "\n" + querie + "\n" + querie1 + "\n" + querie2 + "\n" + querie3 + "}"


def buscar_coord_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sujeto <http://www.schema.org/geo> ?coord."
    querie2 = "?coord <http://www.schema.org/latitude> ?lat."
    querie3 = "?coord <http://www.schema.org/longitude> ?lon."
    return "SELECT ?lat ?lon WHERE{" + querie_direcc + "\n" + querie1 + "\n" + querie2 + "\n" + querie3 + "}"


def buscar_district_nombre(nombre: str) -> str:
    querie_nombre = buscar_site_por_nombre(nombre)
    querie = "?sujeto <http://www.schema.org/place> ?localizacion."
    querie1 = "?localizacion <https://dbpedia.org/ontology/district> ?distr."
    querie2 = "?distr <https://dbpedia.org/ontology/name> ?distrito"
    return "SELECT ?distrito WHERE{" + querie_nombre + "\n" + querie + "\n" + querie1 + "\n" + querie2 + "\n" + "}"


def buscar_district_direcc(direcc: str) -> str:
    querie_direcc = buscar_site_por_direcc(direcc)
    querie1 = "?sujeto <https://dbpedia.org/ontology/district> ?distr."
    querie2 = "?distr <https://dbpedia.org/ontology/name> ?distrito"
    return "SELECT ?distrito WHERE{" + querie_direcc + "\n" + querie1 + "\n" + querie2 + "\n" + "}"


def querie_distrito(distrito: str) -> str:
    querie = "?distrito <https://dbpedia.org/ontology/name> " + "'" + distrito + "'" + "."
    querie1 = "?lugar <https://dbpedia.org/ontology/district> ?distrito."
    querie2 = "?sujeto <https://dbpedia.org/ontology/name> ?nombre."
    querie3 = "?sujeto <http://www.schema.org/place> ?lugar."
    return "SELECT ?nombre WHERE {" + querie + "\n" + querie1 + "\n" + querie2 + "\n" + querie3 + "}"


def querie_barrio(barrio: str) -> str:
    querie = "?barrio <https://dbpedia.org/ontology/name> " + "'" + barrio + "'" + "."
    querie1 = "?lugar <https://dbpedia.org/ontology/neighbourhood> ?barrio."
    querie2 = "?sujeto <https://dbpedia.org/ontology/name> ?nombre."
    querie3 = "?sujeto <http://www.schema.org/place> ?lugar."
    return "SELECT ?nombre WHERE {" + querie + "\n" + querie1 + "\n" + querie2 + "\n" + querie3 + "}"


pygame.init()

# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NARANJA = (237, 208, 19)


# Establecemos el largo y alto de la pantalla
dimensiones = (780, 300)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Culturízate")

fuente = pygame.font.Font(None, 25)
fuenti = pygame.font.Font(None, 15)
fuenton = pygame.font.Font(None, 35)

nombre = fuente.render("Nombre", True, BLANCO)
distrito = fuente.render("Distrito", True, BLANCO)
direcc = fuente.render("Dirección", True, BLANCO)
barrio = fuente.render("Barrio", True, BLANCO)
descripcion = fuenti.render("Descripción", True, BLANCO)
acceso = fuenti.render("Acceso", True, BLANCO)
horario = fuenti.render("Horario", True, BLANCO)
email = fuenti.render("Email", True, BLANCO)
telefono = fuenti.render("Teléfono", True, BLANCO)
coord = fuenti.render("Coordenadas", True, BLANCO)
nombri = fuenti.render("Nombre", True, BLANCO)
distriti = fuenti.render("Distrito", True, BLANCO)
diricc = fuenti.render("Dirección", True, BLANCO)
busqueda = fuente.render("Elija el elemento en el que basar su búsqueda", True, BLANCO)

cambio = False
name = False
dirr = False


hecho = False
while not hecho:

    for evento in pygame.event.get():  # El usuario realizó alguna acción
        if evento.type == pygame.QUIT:  # Si el usuario hizo click sobre salir
            hecho = True  # Marcamos que hemos acabado y abandonamos este bucle

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if 20 <= pos[0] <= 170 and 100 <= pos[1] <= 200 and not cambio:
                name = True
                cambio = True
            elif 190 <= pos[0] <= 340 and 100 <= pos[1] <= 200 and not cambio:
                valor = str(input("Introduce el nombre del distrito"))
                print(querie_distrito(valor))
            elif 360 <= pos[0] <= 510 and 100 <= pos[1] <= 200 and not cambio:
                dirr = True
                cambio = True
            elif 530 <= pos[0] <= 680 and 100 <= pos[1] <= 200 and not cambio:
                valor = str(input("Introduce el nombre del barrio"))
                print(querie_barrio(valor))

            elif cambio:
                if 20 <= pos[0] <= 95 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_descripcion_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_descripcion_direcc(valor))
                if 115 <= pos[0] <= 190 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_accesibilidad_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_accesibilidad_direcc(valor))
                if 210 <= pos[0] <= 285 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_horario_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_horario_direcc(valor))
                if 305 <= pos[0] <= 380 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_email_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_email_direcc(valor))
                if 400 <= pos[0] <= 475 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_telef_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_telef_direcc(valor))
                if 495 <= pos[0] <= 570 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_direcc_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_nombre_direcc(valor))
                if 590 <= pos[0] <= 665 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_coord_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_coord_direcc(valor))
                if 685 <= pos[0] <= 760 and 100 <= pos[1] <= 200:
                    if name:
                        valor = str(input("Introduce el nombre del museo"))
                        print(buscar_district_nombre(valor))
                    elif dirr:
                        valor = str(input("Introduce la dirección"))
                        print(buscar_district_direcc(valor))



    # Limpiamos la pantalla y establecemos su fondo.
    pantalla.fill(NARANJA)
    if not cambio:
        pygame.draw.rect(pantalla, ROJO, (20, 100, 150, 100))
        pygame.draw.rect(pantalla, ROJO, (190, 100, 150, 100))
        pygame.draw.rect(pantalla, ROJO, (360, 100, 150, 100))
        pygame.draw.rect(pantalla, ROJO, (530, 100, 150, 100))
        pygame.draw.rect(pantalla, NEGRO, (20, 100, 150, 100), 5)
        pygame.draw.rect(pantalla, NEGRO, (190, 100, 150, 100), 5)
        pygame.draw.rect(pantalla, NEGRO, (360, 100, 150, 100), 5)
        pygame.draw.rect(pantalla, NEGRO, (530, 100, 150, 100), 5)

        pantalla.blit(nombre, [40, 130])
        pantalla.blit(distrito, [210, 130])
        pantalla.blit(direcc, [380, 130])
        pantalla.blit(barrio, [550, 130])
        pantalla.blit(busqueda, [40, 50])
    else:
        pygame.draw.rect(pantalla, ROJO, (20, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (115, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (210, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (305, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (400, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (495, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (590, 100, 75, 100))
        pygame.draw.rect(pantalla, ROJO, (685, 100, 75, 100))

        pantalla.blit(descripcion, [30, 130])
        pantalla.blit(acceso, [125, 130])
        pantalla.blit(horario, [220, 130])
        pantalla.blit(email, [315, 130])
        pantalla.blit(telefono, [410, 130])
        pantalla.blit(coord, [600, 130])
        pantalla.blit(distriti, [695, 130])

        if name:
            pantalla.blit(diricc, [505, 130])
        elif dirr:
            pantalla.blit(nombri, [505, 130])





    pygame.display.flip()

import rdflib

g = rdflib.Graph()
print("Espere un momento, por favor")
print("Cargando...")
result = g.parse("data.rdf")

print("El dataset tiene %s personas." % len(g))

person = 1
while person:
  person = int(input("Elige el numero de persona para ver los detalles. (0 salir)"))
  
  query = """
  PREFIX db: <http://dbpedia.org/ontology/>
  PREFIX gvp: <http://vocab.getty.edu/ontology#>
  
  SELECT * where{
    ?person a db:Person .
    ?person db:birthYear ?birth .
    ?person db:gender ?gender .
    ?person db:neighbourhood ?neigh .
    ?person db:district ?disc .
    ?person gvp:nationalityNonPreferred ?natio .
    
    FILTER (str(?person)="http://dbpedia.org/Person-%d"^^xsd:string)
  }
  """%(person)

  for row in g.query(query):
    for data in row:
      print(data)

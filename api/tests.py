# Graphene tools 
import graphene 
from api.schema import Query, Mutation
from graphene.test import Client
# Django Tests
from django.test import TestCase
# Models
from api.models import Movie, Character, Planet, Filmmaking
from collections import OrderedDict

class PlanetTest(TestCase): 
    
    def setUp(self):
        super().setUp()
        self.query = """
            query {
                allPlanets {
                edges {
                node { 
                id, 
                    name, 
                population
                } 
                }
            }
            }
        """

    def test_get_planets_query(self): 
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data, {'allPlanets': {'edges': []}})

    def test_planet_mutation(self):
        schema = graphene.Schema(query=Query, mutation=Mutation)
        client = Client(schema)
        mutation = """
            mutation {
            planetMutation(input: {
                name: "Anoat testing"
            }) {
                planet {
                    id, 
                    name, 
                    population
                }
            }
            }
        """
        expected = {'data': OrderedDict([('planetMutation', {'planet': {'id': 'UGxhbmV0Tm9kZTox', 'name': 'Anoat testing', 'population': None}})])}
        executed = client.execute(mutation)

        self.assertIsNotNone(executed)
        self.assertEqual(executed, expected)

class MovieTest(TestCase):
    def setUp(self):
        super().setUp()
        self.query = """
            query {
                allMovies {
                    edges {
                    node {
                        id, 
                        title, 
                        publishedAt
                    }
                    }
                }
            }
        """

    def test_get_movies_query(self):
        Movie.objects.create(
            title='movietest', 
            published_at='1999-05-19'
        )
        
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        expected = {
            "allMovies" : {
                "edges" : [{
                    "node" : {
                        "id": "TW92aWVOb2RlOjE=",
                        "title": "movietest", 
                        "publishedAt": "1999-05-19"
                    }
                }]
            }
        }
        

        self.assertEqual(result.data, expected)
    
    def test_movie_mutation(self):
        Planet.objects.create(
            id=1,
            name='Test', 
            population=None
        )
        Filmmaking.objects.create(
            id=1,
            first_name = "John", 
            last_name = "Doe", 
            date_of_birth = "2017-12-09"
        )

        schema = graphene.Schema(query=Query, mutation=Mutation)
        client = Client(schema)
        mutation = """
            mutation {
            movieMutation(input: {
                title: "Testing new movie",
                description: "This is a description for testing! ", 
                publishedAt: "09-12-2017", 
                planets: "1",
                filmmakers: "1"
            }) {
                movie {
                    id, 
                    title, 
                    publishedAt
                }
            }
            }
        """
        expected = {'data': OrderedDict([('movieMutation', {'movie': {'id': 'TW92aWVOb2RlOjE=', 'title': 'Testing new movie', 'publishedAt': '2017-12-09'}})])}
        executed = client.execute(mutation)
        
        self.assertIsNotNone(executed)
        self.assertEqual(executed, expected)

class CharacterTest(TestCase):
    def setUp(self):
        super().setUp()
        self.query = """
            query {
            allCharacters {
                edges {
                node {
                    id, 
                    firstName,
                    lastName
                }
                }
            }
            }
        """

    def test_get_character_query(self):
        Character.objects.create(
            first_name='John', 
            last_name='Doe'
        )
        
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        expected = {
            "allCharacters" : {
                "edges" : [{
                    "node" : {
                        "id": "Q2hhcmFjdGVyTm9kZTox",
                        "firstName": "John",
                        "lastName": "Doe"
                    }
                }]
            }
        }
        

        self.assertEqual(result.data, expected)


    def test_character_mutation(self):
        Planet.objects.create(
            id=1,
            name='Test', 
            population=None
        )
        Filmmaking.objects.create(
            id=1,
            first_name = "John", 
            last_name = "Doe", 
            date_of_birth = "2017-12-09"
        )
        Movie.objects.create(
            id=1, 
            title="Movietest", 
            published_at = "2017-01-01"
        )
       

        schema = graphene.Schema(query=Query, mutation=Mutation)
        client = Client(schema)
        mutation = """
            mutation {
                characterMutation (input: {
                firstName: "Leia", 
                lastName: "Organa", 
                dateOfBirth: "19 BBY", 
                species: "Humano", 
                gender: "F", 
                movies: "1"
            }) {
                character {
                id,
                firstName, 
                lastName
                }
            }
            }
        """
        expected = {'data': OrderedDict([('characterMutation', {'character': {'id': 'Q2hhcmFjdGVyTm9kZTox', 'firstName': 'Leia', 'lastName': 'Organa'}})])}
        executed = client.execute(mutation)
        
        self.assertIsNotNone(executed)
        self.assertEqual(executed, expected)


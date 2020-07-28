# Graphene's tools
from graphene import relay, ObjectType, Mutation, String, Field, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

# Models 
from .models import Character, Movie, Filmmaking, Planet

# Utils
from datetime import datetime

# Nodes 
class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = {
            'first_name': ['exact', 'icontains', 'istartswith'],
            'last_name': ['exact', 'icontains'],
        }
        interfaces = (relay.Node,)

class MovieNode(DjangoObjectType):
    class Meta:
        model = Movie
        filter_fields = ['title']
        interfaces = (relay.Node,)

class FilmmakerNode(DjangoObjectType):
    class Meta:
        model = Filmmaking
        convert_choices_to_enum = False

class PlanetNode(DjangoObjectType):
    class Meta: 
        model = Planet
        filter_fields = ['name']
        interfaces = (relay.Node,)
        
# Mutations 

class PlanetMutation(relay.ClientIDMutation):
    planet = Field(PlanetNode)

    class Input: 
        name = String(required=True)
        population = String()
    

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        planet = Planet(
            name = input.get('name'), 
            population = input.get('population')
        )

        planet.save()

        return PlanetMutation(planet=planet)

class MovieMutation(relay.ClientIDMutation):
    movie = Field(MovieNode)

    class Input: 
        title = String(required=True)
        description = String(required=True)
        published_at = String(required=True)
        planets = String(required=True)
        filmmakers = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        movie = Movie(
            title = input.get('title'), 
            description = input.get('description'), 
            published_at = datetime.strptime(input.get('published_at'), '%d-%m-%Y')
        )

        movie.save()
        movie.planets.add(input.get('planets'))
        movie.filmmakers.add(input.get('filmmakers'))

        return MovieMutation(movie=movie)

class CharacterMutation(relay.ClientIDMutation):
    character = Field(CharacterNode)

    class Input: 
        first_name = String(required=True)
        last_name = String(required=True)
        date_of_birth = String(required=True)
        species = String(required=True)
        gender = String(required=True)
        movies = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        character = Character(
            first_name = input.get('first_name'), 
            last_name = input.get('last_name'), 
            date_of_birth = input.get('date_of_birth'), 
            species = input.get('species'), 
            gender = input.get('gender')
        )

        character.save()
        character.movies.add(input.get('movies'))

        return CharacterMutation(character=character)


class Mutation(ObjectType): 
    planet_mutation = PlanetMutation.Field()
    movie_mutation = MovieMutation.Field()
    character_mutation = CharacterMutation.Field()

class Query(ObjectType):
    characters = relay.Node.Field(CharacterNode)
    all_characters = DjangoFilterConnectionField(CharacterNode)

    movies = relay.Node.Field(MovieNode)
    all_movies = DjangoFilterConnectionField(MovieNode)

    planets = relay.Node.Field(PlanetNode)
    all_planets = DjangoFilterConnectionField(PlanetNode)
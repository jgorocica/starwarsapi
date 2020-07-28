# Star Wars API 

Este es un repositorio creado para aplicar a la vacante de desarrollador backend en Python de *Lo Que Necesito*.


## Usar el proyecto con Docker 🐳
1. Instalar Docker & Docker Compose
2. Git

 
## Baby Steps  🤱🍼

- Renombrar el archivo [pruebalqn]/.django_env.example a .django_env, cambiar las variables.   
- Renombrar el archivo [pruebalqn]/docker-compose.yml.example a docker-compose.yml, cambiar las variables.   
- Si el proyecto se esta corriendo localmente, se debe instalar las dependencias del archivo requirements.txt. 
- Ejecutar los siguientes comandos: 
    - `docker-compose up -d `
    - Luego, verificar que los contenedores esten funcionando con el siguiente comando: 
    - `docker-compose ps `
  

### Listo, ingresar a la url: 
> http://localhost:8000/graphql 
> http://localhost:8000/admin (Se necesita crear el super user)

#### Baby Steps ll 🤱🤱🍼
Correr las migraciones y seeds
  - Correr el archivo loaddata.sh 
    - Dentro del contenedor `./loaddata.sh`
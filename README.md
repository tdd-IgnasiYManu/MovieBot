# MovieBot
## Descripción
Problema a resolver: queremos desarrollar una herramienta que permita a los usuarios buscar información sobre películas y que le recomiende otras películas relacionadas con dicha búsqueda.

Solución propuesta: crear un bot para Telegram usando su API. La información de las películas se recogerá de la API de https://www.themoviedb.org/

## Herramientas para el desarrollo

Después de discutir en la Issues [Herramientas a usar](https://github.com/tdd-IgnasiYManu/MovieBot/issues/6), se ha llegado a la conclusión siguiente:

- Como sistema de logging usaremos `logstash` por ser software libre y gratuito.
- Usaremos `Python` con sus bibliotecas `Pyrogram` debido a la calidad de su documentación y el ya conocido `requests` para hacer llamadas a las APIs http.
- Instalaremos una herramienta de configuración remota (`etcd`) por comodidad.
- Nuestro SGBD será `PostgreSQL`.
- El despliegue será en `Heroku` por ser gratuito.

## Participantes

| Nombre  | Nick          | Correo                    |
| ------- | ------------- | ------------------------- |
| Manuel Jesús Núñez   | @ManuJNR  | mjnunez@correo.ugr.es |
| Ignasi Camacho | @IgnasiCR | ignasicr@correo.ugr.es  |

## Instrucciones

Para instalar las dependencias que tenemos en nuestro proyecto hemos utilizado `poetry`. Habrá que lanzar el comando de que hay a continuación en la consola para así instarlas.

	poetry install

 Para poder ejecutar los test que nosotros hemos realizado para nuestro proyecto necesitaremos lanzar el comando.

	poetry run python -m pytest

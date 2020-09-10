# Plantilla del curso programación para QA
## Descripción
Problema a resolver: queremos desarrollar una herramienta que permita a los usuarios buscar información sobre películas y que le recomiende otras películas relacionadas con dicha búsqueda.

Solución propuesta: crear un bot para Telegram usando su API. La información de las películas se recogerá de la API de https://www.themoviedb.org/


## Herramientas para el desarrollo
- Como sistema de logging usaremos `logstash` por ser software libre y gratuito.
- Usaremos `Python` con sus bibliotecas `Pyrogram` debido a la calidad de su documentación y el ya conocido `Flask` para hacer llamadas a las APIs http.
- Instalaremos una herramienta de configuración remota (`etcd`) por comodidad.
- El despliegue será en `GCP` ya que nos dan 300$ de prueba.

## Participantes

| Nombre  | Nick          | Correo                    |
| ------- | ------------- | ------------------------- |
| Manuel Jesús Núñez   | @ManuJNR  | mjnunez@correo.ugr.es |
| Ignasi Camacho | @IgnasiCR | ignasicr@correo.ugr.es  |


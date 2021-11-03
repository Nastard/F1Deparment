# F1Department
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
>Proyecto a desarrollar de la asignatura Cloud Computing del Máster en Ingeniería Informática, curso 2021-2022.

## Descripción del Proyecto y Lógica de Negocio
Descripción del proyecto y de la lógica de negocio disponible [aquí](./documentacion/descripcion_y_logica.md).

## Descripción de Hitos e Historias de usuario.

Se describen a continuación los Hitos donde cada uno de ellos implementará un producto mínimamente viable. Cada Hito tiene además una serie de historias de usuario.

* [Hito1: Creación de la interfaz principal.](https://github.com/Nastard/F1Deparment/milestone/2) Se crea la interfaz principal para poder cargar los datos usados en el cálculo de las predicciones. Se definen también las principales funciones del proyecto.

	* [[HU1] Como usuario de la aplicación, quiero indicar de forma sencilla el piloto y el circuito de la predicción de carrera.](https://github.com/Nastard/F1Deparment/issues/18)

	* [[HU2] Como usuario de la aplicación, quiero indicar de forma sencilla el piloto y el circuito de la predicción de la pole de una carrera.](https://github.com/Nastard/F1Deparment/issues/19)

* [Hito2: Cálculo de predicciones de carrera.](https://github.com/Nastard/F1Deparment/milestone/3) Se implementará algoritmos de predicción para calcular diversas predicciones que se pueden dar en un evento de F1.

	* [[HU3] Como usuario de la aplicación, quiero saber la probabilidad de que un piloto gane una carrera, para saber cuánto dinero apostar por el piloto en dicha carrera.](https://github.com/Nastard/F1Deparment/issues/4)

	* [[HU4] Como usuario de la aplicación, quiero saber la probabilidad de que un piloto haga la pole de una carrera, para saber cuánto dinero apostar por el piloto en la pole de la carrera indicada.](https://github.com/Nastard/F1Deparment/issues/17)

* [Hito3: Crear visualizaciones de gráficas.](https://github.com/Nastard/F1Deparment/milestone/4) Se crearán funciones que devuelven diferentes gráficas.

	* Historias de usuarios no definidas aún.


* [Hito4: API.](https://github.com/Nastard/F1Deparment/milestone/5) Diseño de una API que sirva para ofrecer la funcionalidad de la lógica de negocio.

	* Historias de usuarios no definidas aún.

## Entidades generadas.

Dada las historias de usuario, se ha creado una clase principal denominada *Predictor*, sujetas a evolución según sean necesarios nuevos requisitos futuros. El archivo [cc.yaml](./cc.yaml) contiene esta clase, necesaria para que el [Hito1](https://github.com/Nastard/F1Deparment/milestone/2) sea un producto mínimamente viable.


## Documentación adicional
Enlaces con documentación adicional al proyecto:
* [Descripción del Proyecto y Lógica de Negocio](./descripcion_y_logica.md).
* [Configuración inicial de GIT](./documentacion/doc_hito0.md)

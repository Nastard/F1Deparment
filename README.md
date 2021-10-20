# F1Department
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
>Proyecto a desarrollar de la asignatura Cloud Computing del Máster en Ingeniería Informática, curso 2021-2022.

## Descripción del Proyecto y Lógica de Negocio
Descripción del proyecto y de la lógica de negocio disponible [aquí](./documentacion/descripcion_y_logica.md).

## Descripción de Hitos e Historias de usuario.

Se describen a continuación los Hitos donde cada uno de ellos implementará un producto mínimamente viable. Cada Hito tiene además una serie de historias de usuario.

* [Hito1: Implementación de las entidades necesarias.](https://github.com/Nastard/F1Deparment/milestone/2) Se implementará una serie de clases las cuales van a ser necesarias para poder almacenar los datos que usará la lógica de negocio.

	* [[HU1] Como usuario de la aplicación, quiero saber la información de un piloto específico. Si el piloto no existe, se devolverá un objeto vacío.](https://github.com/Nastard/F1Deparment/issues/4)

	* [[HU2] Como usuario de la aplicación, quiero saber la información de un constructor específico. Si el constructor no existe, se devolverá un objeto vacío.](https://github.com/Nastard/F1Deparment/issues/5)

	* [[HU3] Como usuario de la aplicación, quiero saber la información de un circuito de carreras. Si el circuito no existe, se devolverá un objeto vacío.](https://github.com/Nastard/F1Deparment/issues/6)

* [Hito2: Cálculo de predicciones de carrera.](https://github.com/Nastard/F1Deparment/milestone/3) Se implementará algoritmos de predicción para calcular diversas predicciones que se pueden dar en un evento de F1.

	* [[HU4] Como usuario de la aplicación, quiero saber una predicción del ganador de una carrera.](https://github.com/Nastard/F1Deparment/issues/7)

	* [[HU5] Como usuario de la aplicación, quiero saber una predicción de quien tendrá la pole en una clasificación de carrera.](https://github.com/Nastard/F1Deparment/issues/8)

* [Hito3: Crear visualizaciones de gráficas.](https://github.com/Nastard/F1Deparment/milestone/4) Se crearán funciones que devuelven diferentes gráficas.

	* [[HU6] Como usuario de la aplicación, quiero visualizar la clasificación general de pilotos en una gráfica de polígono de frecuencias.](https://github.com/Nastard/F1Deparment/issues/9)

	* [[HU7] Como usuario de la aplicación, quiero visualizar la clasificación general de constructores en una gráfica de polígono de frecuencias.](https://github.com/Nastard/F1Deparment/issues/10)

* [Hito4: API.](https://github.com/Nastard/F1Deparment/milestone/5) Diseño de una API que sirva para ofrecer la funcionalidad de la lógica de negocio.

	* Historias de usuarios no definidas aún.

## Entidades generadas.

Dada las historias de usuario, se han creado las primeras entidades, sujetas a evolución según sean necesarios nuevos requisitos. El archivo [cc.yaml](./cc.yaml) contiene estas entidades, necesarias para que el [Hito1](https://github.com/Nastard/F1Deparment/milestone/2) sea un producto mínimamente viable. En concreto:

* [Circuito.py](./src/Circuito.py). Necesario para el [HU1](https://github.com/Nastard/F1Deparment/issues/4).

* [Constructor](./src/Constructor.py). Necesario para el [HU2](https://github.com/Nastard/F1Deparment/issues/5).

* [Piloto.py](./src/Piloto.py). Necesario para el [HU3](https://github.com/Nastard/F1Deparment/issues/6).

## Documentación adicional
Enlaces con documentación adicional al proyecto:
* [Descripción del Proyecto y Lógica de Negocio](./descripcion_y_logica.md).
* [Configuración inicial de GIT](./documentacion/doc_hito0.md)

# Proyecto de Microservicios - Documentación para el profe 

Este proyecto es una introducción a la arquitectura de microservicios utilizando Python y Flask. A través de dos servicios independientes, esto con la finalidad de saber como se interactua y como podemos sacarle el mayor provecho a la relación con microservicios.

## Descripción General

En este proyecto, desarrollamos dos microservicios:

1. **Servicio de Clientes**: Gestiona una lista de clientes.
2. **Servicio de Compras**: Gestiona una lista de pedidos y permite consultar los pedidos de un cliente específico.

Cada servicio funciona de manera independiente, pero pueden interactuar entre ellos.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- **Python 3**: Necesario para ejecutar los servicios.
- **Flask**: Un framework de Python que permite crear aplicaciones web simples. Puedes instalar Flask ejecutando este comando en la terminal:


Servicio de Clientes (servicio_clientes.py)
Este microservicio responde a solicitudes HTTP GET y devuelve una lista de clientes en formato JSON.

 Servicio de Compras (servicio_compras.py)
Este servicio gestiona las compras y permite buscar pedidos por cliente:

Rutas: Este servicio tiene dos rutas:
/compras: Devuelve una lista general de compras.
/compras/cliente/<int:id_cliente>: Devuelve las compras asociadas a un cliente específico.
Flask: Funciona igual que en el servicio de clientes, pero aquí interactuamos con un "diccionario" que guarda las compras de cada cliente.

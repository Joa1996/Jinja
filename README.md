Jinja es una manera simple de  armar templates  de manera dinamica en python, ademas se destaca por su facil forma de entenderlo por 
los humanos
Ejemplos de su uso es para crear archivos de configuracion de conexiones como archivos ".yaml", o variables dinamicas.

Sintaxis:
Feature                     | Syntax
Variables                   |{{ variable }}
Control Structures (if,for) | {% if condition %} ... {% endif %}
Comments                    |{# This is a comment #}
Template Inheritance        |{% extends "base.html" %}
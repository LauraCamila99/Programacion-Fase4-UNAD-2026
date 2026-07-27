"""
Módulo de Registro de Logs - Sistema Software FJ
"""

import logging
import os

# Configuración del archivo log donde se guardarán los registros
LOG_FILENAME = "sistema_software_fj.log"

logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def registrar_evento(mensaje: str):
    """Registra eventos e informaciones generales del sistema."""
    logging.info(mensaje)

def registrar_error(mensaje: str):
    """Registra errores y excepciones capturadas."""
    logging.error(mensaje)

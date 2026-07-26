import logging
import os

# Configuración del archivo de registro de logs del sistema Software FJ
LOG_FILE = "sistema_software_fj.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")

def registrar_evento(mensaje: str):
    """
    Registra eventos informativos del sistema en el archivo de log.
    """
    logger.info(mensaje)

def registrar_error(mensaje: str, exc: Exception = None):
    """
    Registra errores y excepciones con su detalle técnico en el archivo de log.
    """
    if exc:
        logger.error(f"{mensaje} | Detalle técnico: {exc}", exc_info=True)
    else:
        logger.error(mensaje)

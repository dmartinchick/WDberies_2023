from dependency_injector import containers, providers

from src.config import logger


class Container(containers.DeclarativeContainer):
    logger.info("Container was created!")

    wiring_config = containers.WiringConfiguration(modules=["src.posts.item.roters"])

    config = providers.Configuration(yaml_files=['config.yml'])



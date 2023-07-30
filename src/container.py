from dependency_injector import containers, providers

from src.config import logger
from .database import Database

from src.posts.item.repositories import ItemRepository
from src.posts.item.services import ItemService


class Container(containers.DeclarativeContainer):
    logger.info("Container was created!")

    wiring_config = containers.WiringConfiguration(modules=["src.posts.item.routers"])

    config = providers.Configuration(yaml_files=['config.yml'])

    db = providers.Singleton(Database, db_url=config.db.url)

    item_repository = providers.Factory(
        ItemRepository,
        session_factory=db.provided.session,
    )

    item_service = providers.Factory(
        ItemService,
        item_repository=item_repository,
    )

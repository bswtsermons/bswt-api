import logging
from datetime import datetime
from argparse import ArgumentParser

from sqlalchemy.orm import Session

# from bswt.models import Service, Minister
from bswt.sqlalchemy import Base, engine


logger = logging.getLogger()


def instantiate_test_data():
    logger.info('instantiating test data')
    from bswt.models.service import Service, Minister
    
    with Session(engine) as session:
        minister1 = Minister(
            first_name='Smith',
            last_name='Wigglesworth'
        )
        
        service1 = Service(
            ministered_on=datetime.now(),
            subseries_title='The Best Sermon Ever',
            minister=minister1
        )

        session.add_all([minister1, service1])


def create_tables():
    logger.info('creating tables')
    from bswt.models.service import Service, Minister
    Base.metadata.create_all(bind=engine)


def main(command: str) -> None:
    if command == 'create_tables':
        create_tables()
    if command == 'instantiate_test_data':
        instantiate_test_data()
    else:
        raise NotImplementedError(f'command {command} not implemented')


if __name__ == '__main__':
    parser = ArgumentParser('BSWT Database Controller')
    parser.add_argument('-c', '--command', required=True, choices=[
        'create_tables',
        'instantiate_test_data'
    ])
    args = parser.parse_args()

    main(args.command)

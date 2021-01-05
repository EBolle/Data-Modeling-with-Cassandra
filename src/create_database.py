"""This module takes care of initializing the Cassandra database."""


from cassandra.cluster import Cluster
from logger import logger


class CreateDatabase:
    """
    This class initializes a local Cassandra instance including a 'udacity' keyspace, filled with tables
    from the statements in the create_queries list.
    """
    def __init__(self, create_queries: list, drop_queries: list):
        self.cluster = None
        self.create_queries = create_queries
        self.drop_queries = drop_queries
        self.session = None

    def create_database_pipeline(self) -> tuple:
        """
        - initialize the cluster and session
        - setup the udacity keyspace
        - drop tables if exists to guarantee freshly created tables
        - create the tables

        The cluster and session instances are returned so they can be used and closed after the database is created.
        """
        logger.info("Create database pipeline started...")

        self.init_cluster_and_session()
        self.set_udacity_keyspace()
        self.drop_tables()
        self.create_tables()

        return self.cluster, self.session

    def init_cluster_and_session(self) -> None:
        logger.info("Initializing the local Cassandra cluster and session")

        try:
            self.cluster = Cluster(['127.0.0.1'])
        except Exception:
            logger.exception("ERROR while creating a cluster of a local Cassandra instance")
        else:
            try:
                self.session = self.cluster.connect()
            except Exception:
                logger.exception("ERROR while setting up a session of the local cluster")

    def set_udacity_keyspace(self) -> None:
        logger.info("Setting up the udacity keyspace")

        keyspace_query = """
        CREATE KEYSPACE IF NOT EXISTS udacity 
        WITH REPLICATION = 
        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
        """

        try:
            self.session.execute(keyspace_query)
        except Exception:
            logger.debug("ERROR while setting up the udacity keyspace")
        else:
            self.session.set_keyspace('udacity')

    def drop_tables(self) -> None:
        logger.info("Dropping tables if exists")

        for idx, query in enumerate(self.drop_queries):
            try:
                self.session.execute(query)
            except Exception:
                logger.exception(f"ERROR while dropping table at index {idx}")

    def create_tables(self) -> None:
        logger.info("Creating tables")

        for idx, query in enumerate(self.create_queries):
            try:
                self.session.execute(query)
            except Exception:
                logger.exception(f"ERROR while creating table at index {idx}")

from geoalchemy2 import Geometry
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import relationship

from plenario import db
from plenario.database import session, Base, app_engine

sensor_to_node = Table('sensor__sensor_to_node', db.Model.metadata,
                      Column('sensor', String, ForeignKey('sensor__sensors.name')),
                      Column('node', String, ForeignKey('sensor__node_metadata.id'))
                      )


class NetworkMeta(db.Model):
    __tablename__ = 'sensor__network_metadata'

    name = Column(String, primary_key=True)
    nodes = relationship('NodeMeta')
    info = Column(JSONB)

    @staticmethod
    def index():
        networks = session.query(NetworkMeta)
        return [network.name for network in networks]


class NodeMeta(db.Model):
    __tablename__ = 'sensor__node_metadata'

    id = Column(String, primary_key=True)
    sensor_network = Column(String, ForeignKey('sensor__network_metadata.name'))
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    sensors = relationship('Sensor', secondary='sensor__sensor_to_node')
    info = Column(JSONB)

    @staticmethod
    def index(network_name=None):
        nodes = session.query(NodeMeta).all()
        return [node.id for node in nodes if node.sensor_network == network_name or network_name is None]


class FeatureOfInterest(db.Model):
    __tablename__ = 'sensor__features_of_interest'

    name = Column(String, primary_key=True)
    observed_properties = Column(JSONB)

    @staticmethod
    def index(network_name=None):
        features = []
        for node in session.query(NodeMeta).all():
            for sensor in node.sensors:
                for prop in sensor.observed_properties:
                    if node.sensor_network == network_name or network_name is None:
                        features.append(prop.split('.')[0])
        return list(set(features))


class Sensor(db.Model):
    __tablename__ = 'sensor__sensors'

    name = Column(String, primary_key=True)
    observed_properties = Column(ARRAY(String))
    info = Column(JSONB)

    @staticmethod
    def index(network_name=None):
        sensors = session.query(Sensor).all()
        return [sensor.name for sensor in sensors if
                network_name in [node.sensor_network for node in session.query(NodeMeta).filter(sensor.in_(NodeMeta.sensors)).all()] or network_name is None]

if __name__ == "__main__":
    Base.metadata.create_all(app_engine, extend_existing=True)
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from models.databases import Base


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_link = Column(String)
    health_total = Column(Integer)
    health_current = Column(Integer)
    energy_total = Column(Integer)
    energy_current = Column(Integer)
    power = Column(Integer)
    damage = Column(Integer)
    armor = Column(Integer)
    lucky = Column(Integer)
    level = Column(Integer, ForeignKey('level_info.id'))
    level_point_exp = Column(Integer)
    side = Column(Integer, ForeignKey('side_info.id'))
    quantity_point = Column(Integer)
    is_user = Column(Integer)
    exp_for_kill = Column(Integer)

    # def __init__(self, full_name: list[str], age: int, address: str, id_group: int):
    #     self.surname = full_name[0]
    #     self.name = full_name[1]
    #     self.patronymic = full_name[2]
    #     self.age = age
    #     self.address = address
    #     self.group = id_group
    #
    # def __repr__(self):
    #     info: str = f'Студент [ФИО: {self.surname} {self.name} {self.patronymic}, ' \
    #         f'Возраст: {self.age}, Адрес: {self.address}, ID группы: {self.group}]'
    #     return info


class Level_info(Base):
    __tablename__ = 'level_info'

    id = Column(Integer, primary_key=True)
    total_level_point = Column(Integer)
    person = relationship('Person')

    # def __repr__(self):
    #     return f'Группа [ID: {self.id}, Название: {self.group_name}]'


class Side_info(Base):
    __tablename__ = 'side_info'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    person = relationship('Person')
    quest = relationship('Quest')


class Quests(Base):
    __tablename__ = 'quests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    complexity = Column(Integer)
    image_link = Column(String)
    side = Column(Integer, ForeignKey('side_info.id'))
    energy_need = Column(Integer)
    point_exp = Column(Integer)


class Quests_steps(Base):
    __tablename__ = 'quests_steps'

    id = Column(Integer, primary_key=True)
    quest_steps_id = Column(Integer, ForeignKey('quests.id'))
    level = Column(Integer)
    image_link = Column(String)
    lucky_win_yes_percent = Column(Integer)
    lucky_win_no_percent = Column(Integer)
    text = Column(String)


association_table = Table('qty_quest_for_person', Base.metadata,
                          Column('person_id', Integer, ForeignKey('person.id')),
                          Column('quest_id', Integer, ForeignKey('quests.id'))
                          )
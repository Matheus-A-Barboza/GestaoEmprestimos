from infra.config.connection import DBConnectionHandler
from infra.entities.funcionario import Funcionario

class FuncionarioRepository:
    @staticmethod
    def select_funcionario_by_id(id_funcionario):
        with DBConnectionHandler() as db:
            funcionario = db.session.query(Funcionario).\
                filter(Funcionario.id == id_funcionario).first()
            return funcionario

    @staticmethod
    def select_funcionario_by_cpf(cpf_funcionario):
        with DBConnectionHandler() as db:
            funcionario = db.session.query(Funcionario). \
                filter(Funcionario.id == cpf_funcionario).first()
            return funcionario

    @staticmethod
    def select_all_funcionario():
        with DBConnectionHandler() as db:
            funcionario = db.session.query(Funcionario).all()
            return funcionario

    @staticmethod
    def select_first_funcionario():
        with DBConnectionHandler() as db:
            funcionario = db.session.query(Funcionario).first()
            return funcionario

    @staticmethod
    def insert_one_funcionario(funcionario):
        with DBConnectionHandler() as db:
            db.session.add(funcionario)
            db.session.commit()

    @staticmethod
    def insert_many_funcionario(funcionarios):
        with DBConnectionHandler() as db:
            db.session.add(funcionarios)
            db.session.commit()

    @staticmethod
    def update_funcionario(funcionario):
        with DBConnectionHandler() as db:
            db.session.query(Funcionario).filter(Funcionario.id == funcionario.id).\
                update({'nome':funcionario.nome, 'cpf': funcionario.cpf})
            db.session.commit()

    @staticmethod
    def delete_funcionario(funcionario):
        with DBConnectionHandler() as db:
            db.session.query(Funcionario).filter(Funcionario.id == funcionario.id). \
                update({'ativo': False})
            db.session.commit()
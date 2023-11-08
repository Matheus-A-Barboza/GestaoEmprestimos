from PySide6.QtWidgets import QMessageBox

from infra.entities.funcionario import Funcionario
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.main_window_service import MainWindowService


class FuncionarioService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()

    def insert_funcionario(self, main_window):
        funcionario = Funcionario()
        funcionario.nome = main_window.txt_nome.text()
        funcionario.cpf = main_window.txt_cpf.text()
        funcionario.ativo = True
        try:
            self.funcionario_repository.insert_one_funcionario(funcionario)
            main_window.txt_nome.setText('')
            main_window.txt_cpf.setText('')
            self.service_main_window.populate_table_funcionario(main_window)
            QMessageBox.information(main_window, 'Funcionários', 'Funcionário Cadastrado com sucesso')
        except Exception as e:
            QMessageBox.information(main_window, 'Funcionários', f'Erro ao Cadastrar Funcionário\n'
                                                                 f'Erro : {e}')

    def select_funcionario(self, emprestimo_ui):
        if emprestimo_ui.btn_consulta_funcionario.text() == 'Limpar':
            emprestimo_ui.txt_nome_emprestimo.setText('')
            emprestimo_ui.txt_cpf_emprestimo.setText('')
            emprestimo_ui.txt_cpf_emprestimo.setReadOnly(False)
            emprestimo_ui.selected_funcionario = None
            emprestimo_ui.btn_consulta_funcionario.setText('Consultar')
        else:
            try:
                if emprestimo_ui.txt_cpf_emprestimo.text() != '':
                    funcionario_emprestimo = self.funcionario_repository.select_funcionario_by_cpf(
                        emprestimo_ui.txt_cpf_emprestimo.text())
                    emprestimo_ui.selected_funcionario = funcionario_emprestimo
                    emprestimo_ui.txt_nome_emprestimo.setText(funcionario_emprestimo.nome)
                    emprestimo_ui.txt_cpf_emprestimo.setReadOnly(True)
                    emprestimo_ui.btn_consulta_funcionario.setText('Limpar')
                else:
                    QMessageBox.warning(emprestimo_ui, 'Funcionários', 'Insira um CPF para Consultar Funcionário')
            except Exception as e:
                QMessageBox.information(emprestimo_ui, 'Funcionários', f'Erro ao Consultar Funcionário\n'
                                                                         f'Erro : {e}')
                emprestimo_ui.txt_nome_emprestimo.clear()

    def update_funcionario(self, main_window):
        if main_window.btn_editar_funcionario.text() == 'Editar':
            selected_rows = main_window.tb_funcionario.selectionModel().selectedRows()
            if not selected_rows:
                QMessageBox.warning(main_window, 'Funcionários', f'Selecione um Funcionário')
                return
            selected_rows = selected_rows[0]
            main_window.txt_nome.setText(main_window.tb_funcionario.item(selected_rows, 0).text())
            main_window.txt_cpf.setText(main_window.tb_funcionario.item(selected_rows, 1).text())

    def delete_funcionario(self, main_window):
        selected_rows = main_window.tb_funcionario.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(main_window, 'Funcionários', f'Selecione um Funcionário')
            return
        selected_row = selected_rows[0].row()
        funcionario_delete = self.funcionario_repository.select_funcionario_by_cpf(
            main_window.tb_funcionario.item(selected_row, 1).text()
        )
        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle('Remover Funcionario')
        msg_box.setText(f'Tem certeza que deseja remover o funcionario {funcionario_delete.nome}?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('Sim', QMessageBox.YesRole)
        no_button = msg_box.addButton('Não', QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            try:
                self.funcionario_repository.delete_funcionario(funcionario_delete)
                self.service_main_window.populate_table_funcionario(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, 'Atenção', f'Problema ao remover Funcionário. \n'
                                                            f'Erro: {e}')


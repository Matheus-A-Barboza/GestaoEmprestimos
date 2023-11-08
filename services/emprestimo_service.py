from PySide6.QtWidgets import QMessageBox

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.funcionario_repository import FuncionarioRepository
from infra.repository.uniforme_repository import UniformeRepository
from services.main_window_service import MainWindowService


class EmprestimoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.uniforme_repository = UniformeRepository()
        self.funcionario_repository = FuncionarioRepository()

    def insert_emprestimo(self, emprestimo_ui):
        if emprestimo_ui.cb_tipo_uniforme.currentText() != 'Selecione um item' \
                and emprestimo_ui.selected_funcionario is not None:
            uniforme = self.uniforme_repository.select_uniforme_by_name(emprestimo_ui.cb_tipo_uniforme.currentText())
            try:
                self.emprestimo_repository.insert_emprestimo(emprestimo_ui.selected_funcionario, uniforme)
                QMessageBox.information(emprestimo_ui, 'Empréstimos', 'Empréstimo Cadastrado com sucesso')
            except Exception as e:
                QMessageBox.information(emprestimo_ui, 'Empréstimos', f'Erro ao Cadastrar Empréstimos.\n'
                                                                      f'Erro : {e}')

        elif emprestimo_ui.cb_tipo_uniforme.currentText() == 'Selecione um item' and emprestimo_ui.selected_funcionario is not None:
            QMessageBox.warning(emprestimo_ui, 'Empréstimos', f'Selecione um Uniforme.')

        elif emprestimo_ui.cb_tipo_uniforme.currentText() != 'Selecione um item' and emprestimo_ui.selected_funcionario is not None:
            QMessageBox.warning(emprestimo_ui, 'Empréstimos', f'Selecione um Funcionário.')

        else:
            QMessageBox.warning(emprestimo_ui, 'Empréstimos', f'Selecione um Uniforme e um Funcionário.')


    def finalize_emprestimo(self, main_window):
        selected_row = main_window.tb_emprestimos_ativos.selectionModel().selectedRows()
        if not selected_row:
            QMessageBox.warning(main_window, 'Empréstimos', f'Selecione um Empréstimo a Receber.')
        selected_row = selected_row[0].row()
        cpf_funcionario = main_window.tb_emprestimos_ativos.item(selected_row, 1).text()
        uniforme_selecionado = main_window.tb_emprestimos_ativos.item(selected_row, 3).text()

        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle('Finalizar Empréstimo')
        msg_box.setText('Tem Certeza que Deseja Finalizar?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('Sim', QMessageBox.YesRole)
        no_button = msg_box.addButton('No', QMessageBox.NoRole)
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:
            funcionario = self.funcionario_repository.select_funcionario_by_cpf(cpf_funcionario)

            uniforme = self.uniforme_repository.select_uniforme_by_name(uniforme_selecionado)
            try:
                self.emprestimo_repository.finalize_emprestimo(funcionario, uniforme)
                QMessageBox.information(main_window, 'Empréstimos', f'Emprestimo Finaliza com Sucesso')
                self.service_main_window.populate_emprestimo_ativos(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, 'Empréstimos', f'Erro ao Finalizar Empréstimo.\n'
                                                                 f'Erro {e}')
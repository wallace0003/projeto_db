
class Reserva:
    def __init__(self, codigo_reserva: int, codigo_usuario: int, codigo_livro: int,
                 data_reserva: str, data_expiracao: str, status: str, codigo_pessoa: int):
        
        self.codigo_reserva = codigo_reserva
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro
        self.data_reserva = data_reserva
        self.data_expiracao = data_expiracao
        self.status = status
        self.codigo_pessoa = codigo_pessoa

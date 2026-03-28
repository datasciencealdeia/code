class InvalidCpf(Exception):
    """Exceção personalizada para CPF inválido"""
    def __init__(self, cpf, message="CPF Inválido"):
        self.cpf = cpf
        self.message = message
        super().__init__(self.message)
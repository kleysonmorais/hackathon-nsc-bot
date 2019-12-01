import requests
from Mapping import ApiModel
from datetime import datetime

class MachineLearning:

    nome = ""
    bairro = ""
    descricao = ""
    status = 1
    def getResposta(self, text):
        print(text)
        text = text.lower()
        if self.status == 1:
            self.status = 2
            return self.getBoasVindas()
        elif self.status == 2:
            self.status = 3
            return self.getAjuda(text)
        elif text == "1" and self.status == 3:
            self.status = 8
            return self.getDenuncia()
        elif text == "2" and self.status == 3:
            self.status = 6
            return self.getSugestao()
        elif text == "3" and self.status == 3:
            self.status = 7
            return self.getReclamacao()
        elif self.status == 8:
            self.status = 4
            return self.qualSeuBairro(text)
        elif self.status == 4:
            self.status = 1
            return self.getObrigado(text)
        elif self.status == 6:
            self.status = 8
            return self.getSugestaoAux()
        elif self.status == 7:
            self.status = 8
            return self.getReclamacaoAux()

    def getBoasVindas(self):
        return "Olá, eu sou a Catarina, estagiária automatizada da NSC. Qual o seu nome?"

    def getAjuda(self, text):
        self.nome = text
        return "Ótimo, " + text + ". Como eu posso te ajudar?\n\nDigite:\n1 - Denúncias\n2 - Sugestões\n3 - Reclamações"

    def qualSeuBairro(self, text):
        self.descricao = text
        return "Por favor, me informe o seu bairro? Vou precisar dele."

    def getDenuncia(self):
        return "Escreva a sua denúncia."

    def getSugestao(self):
        return "Sua sugestão é referente a:\n\n1 - Programa de Tv\n2 - Jornal\n3 – Rádio\n4- Site\n5 - programação\n6 - outros"

    def getReclamacao(self):
        return "Me conta qual sua reclamação:\n\n1 - Clube NSC\n2 - Programa de Tv\n3 - Jornal\n4 – Rádio\n5 - Site\n6 - programação\n7 - outros"

    def getObrigado(self, text):
        self.bairro = text
        return "Obrigado."

    def getSugestaoAux(self):
        return "Escreva a sua sugestão."
    
    def getReclamacaoAux(self):
        return "Escreva sua reclamação."
    
    def getData(self, id):
        if self.nome != "" and self.bairro != "" and self.descricao != "":
            return {"nome": self.nome, "bairro": self.bairro, "descricao": self.descricao, "id": id}
        return None

    def clearData(self):
        self.nome = ""
        self.descricao = ""
        self.bairro = ""

if __name__ == '__main__':
    bot = MachineLearning()

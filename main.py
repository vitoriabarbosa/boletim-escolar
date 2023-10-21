class DesempenhoAcademico():
    def __init__(self, nome, turma):
        self.nome = nome
        self.situacao = False
        self.turma = turma
        self.media = 0

    def mediaAluno(self, notas):
        print(f'{"--"*50}\n\nMédia Português: {notas[0]:.1f}\tMédia Matemática: {notas[1]:.1f}\t  Média Ciências: {notas[2]:.1f}')
        print(f'\t\tMédia História: {notas[3]:.1f}\t\tMédia Geografia: {notas[4]:.1f}\n\n{"--"*50}')
        self.media = (sum(notas)) / len(notas)
        print(f'média total: {self.media:.1f}'.upper().center(100," "))
        if self.media >= 7.00:
            self.situacao = True
        return self.media

    def calcularMediaAposFinal(self, final):
        self.media =  (self.media + final) / 2
        if ((self.media >= 5.00) and (self.media <= 6.99)):
            self.situacao = True
            print(f'{"--"*50}\nnota da final: \t{final:.1f}\t\t\t\tmédia final: \t{self.media:.1f}\n'.upper())
        return self.media

    def situacaoAluno(self):
        if (self.situacao == True and self.media >= 7.00):
            print(f'{"situação:":<65}{"aprovado por média"}'.upper())
        elif (self.situacao == True and self.media >= 5.00 and self.media <= 6.99):
            print(f'{"situação:":<70}{"aprovado na final"}'.upper())
        else:
            print(f'{"situação:":<80}{"reprovado"}'.upper())
        print("--"*50)

print(f'{"-="*37}\n{"consultar boletim".center(95," ")}\n{"-="*37}'.upper())
nome = input("\nnome do aluno: ".upper()).upper()
turma = input("turma:".upper()).upper()
print("\n\t\t\t\tentre com as notas do aluno\n".upper())

# entrada das notas do 1° e 2° semestre
print("primeiro semestre\n".upper())
s1 = [float(input("Portugês: ")), float(input("Matemática: ")), float(input("Ciências: ")),
         float(input("Hisótria: ")), float(input("Geografia: "))]

print("\nsegundo semestre\n".upper())
s2 = [float(input("Portugês: ")), float(input("Matemática: ")), float(input("Ciências: ")),
         float(input("Hisótria: ")), float(input("Geografia: "))]

# imprimindo o boletim
print(f'\n{"--"*50}\n{"boletim escolar".center(100," ")}\n{"--"*50}\n'.upper())
print("harvard university".upper().center(95, " "))
print("\nnome:".upper(), nome, "\nturma:".upper(), turma)
print("--"*50, "\n\n1° semestre - 2023\t\t\t|\t2° semestre - 2023".upper())
print("--"*50, "%s \t\t %s \t\t|\t %s \t\t %s" %("\nMATÉRIA", "NOTAS", "MATÉRIA", "NOTAS"))
print("--"*50, "\n%s \t\t\t %.1f \t\t\t|\t %s \t\t %.1f" %("Portugês", s1[0], "Portugês", s2[0]))
print("%s \t\t %.1f \t\t\t|\t %s \t\t %.1f" %("Matemática", s1[1], "Matemática", s2[1]))
print("%s \t\t\t %.1f \t\t\t|\t %s \t\t %.1f" %("Ciências", s1[2], "Ciências", s2[2]))
print("%s \t\t\t %.1f \t\t\t|\t %s \t\t\t %.1f" %("Hisótria", s1[3], "Hisótria", s2[3]))
print("%s \t\t %.1f \t\t\t|\t %s \t\t %.1f" %("Geografia", s1[4], "Geografia", s2[4]))

notas = [(s1[0] + s2[0]) / 2, (s1[1] + s2[1]) / 2, (s1[2] + s2[2]) / 2, (s1[3] + s2[3]) / 2, (s1[4] + s2[4]) / 2]
aluno = DesempenhoAcademico(nome, turma)
aluno.mediaAluno(notas)
aluno.calcularMediaAposFinal(7)
aluno.situacaoAluno()

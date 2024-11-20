import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from src.assets.data.BD_questions import BD_Questions

def load_questions():
    # Instancia a classe
    bd_questions = BD_Questions()

    # Carrega as perguntas de Soft Skills e Hard Skills
    soft_skills = bd_questions.soft_skills
    hard_skills = bd_questions.hard_skills

    # Retorna as perguntas organizadas em um dicionário
    return {
        "Soft Skills": soft_skills,
        "Hard Skills": hard_skills
    }

def obter_resposta_validada():
    # Respostas válidas
    respostas_validas = ['1- NAO', '2- PROVAVELMENTE NAO', '3- NAO SEI', '4- PROVAVELMENTE SIM', '5- SIM']
    
    # Loop até que o usuário forneça uma resposta válida
    while True:
        print("\nEscolha uma opção:")
        print("\n".join(respostas_validas))
        
        escolha = input().strip()
        
        # Mapeando as opções para as respostas válidas
        if escolha == '1':
            return 'NAO'
        elif escolha == '2':
            return 'PROVAVELMENTE NAO'
        elif escolha == '3':
            return 'NAO SEI'
        elif escolha == '4':
            return 'PROVAVELMENTE SIM'
        elif escolha == '5':
            return 'SIM'
        else:
            print("Resposta inválida. Tente novamente.")

def main():
    # Carrega as perguntas usando a função
    all_questions = load_questions()
    
    # Exibe as perguntas carregadas e interage com o usuário para obter respostas
    print("\n=== Seja bem vindo(a) ao Talent Rank!! ===")
    print("=== Sistema de Avaliação de Desenvolvedores ===")
    for category, questions in all_questions.items():
        print(f"\nPerguntas sobre {category}:")
        for skill, question_list in questions.items():
            print(f"\n{skill.upper()}:")
            for question in question_list:
                print(f"{question}")
                resposta = obter_resposta_validada()

if __name__ == "__main__":
    main()

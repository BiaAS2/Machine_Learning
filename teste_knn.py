from src.assets.data.BD_perguntas import BD_Perguntas
from src.assets.data.sugestoes_nivel import Sugestoes_Nivel
from knn_classificador import treinar_knn, prever_nivel

def carregar_perguntas():
    """
    Método para carregar e retornar um dicionário de questões.
    
    Retorna:
    - Um dicionário de perguntas (Soft e Hard skills)
    """

    # Instancia a classe
    perguntas = BD_Perguntas()

    # Carrega as perguntas de Soft Skills e Hard Skills
    soft_skills = perguntas.soft_skills
    hard_skills = perguntas.hard_skills

    # Retorna as perguntas organizadas em um dicionário
    return {
        "Soft Skills": soft_skills,
        "Hard Skills": hard_skills
    }

def obter_resposta_validada(pergunta):
    """
    Solicita ao usuário uma resposta para a pergunta e valida se ela está entre as opções permitidas.

    Parâmetros:
    - pergunta (str): A pergunta a ser exibida ao usuário.
    
    Retorna:
    - str: A resposta válida selecionada pelo usuário.
    """
    
    # Respostas válidas
    respostas_validas = BD_Perguntas().possiveis_respostas 
    
    # Loop até que o usuário forneça uma resposta válida
    while True:
        print(f"\n{pergunta}")
        print("Opções de resposta:")
        for i, resp in enumerate(respostas_validas, 1):
            print(f"{i}. {resp}")
        
        try:
            resposta_usuario = int(input("Escolha uma opção de resposta (1-5): "))
            if 1 <= resposta_usuario <= 5:
                return resposta_usuario
            print("Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Por favor, digite um número válido.")
    
def exibir_sugestoes(sugestoes):
    """
    Método para formatar a saída das sugestões no console

    Parâmetros:
    - nivel: classificação do usuário (Júnior, Pleno, Sênior)
    - sugestoes: Links do site RoadMap de aprimoramento profissional para cada tipo de nível

    Retorna: 
    - Uma string formatada das sugestões no console    
    
    """
    print("\n=== SUGESTÕES PARA VOCÊ ===")
    for linha in sugestoes:
        print(linha)

def TalentRank_KNN():
    # Carrega as perguntas usando a função
    todas_perguntas = carregar_perguntas()
    respostas = []
    sugestoes_por_nivel = Sugestoes_Nivel()
    
    # Exibe as perguntas carregadas e interage com o usuário para obter respostas
    print("\n=== Seja bem-vindo(a) ao Talent Rank!! ===")
    print("=== Sistema de Avaliação de Desenvolvedores ===")

    for categoria, perguntas in todas_perguntas.items():
        print(f"\nPerguntas sobre {categoria}:")
        for skill, lista_perguntas in perguntas.items():
            print(f"\n{skill.upper()}:")
            for i, pergunta in enumerate(lista_perguntas, 1):
                resp = obter_resposta_validada(pergunta)
                respostas.append(resp)

    classificar_knn, scaler = treinar_knn()
    nivel_usuario = prever_nivel(classificar_knn, scaler, respostas)

    # Se você ainda quiser usar a pontuação para comparar
    print("\n=== Resultado Final ===")
    print(f"Nível classificado: {nivel_usuario}")

    if nivel_usuario == 'Júnior':
        exibir_sugestoes(sugestoes_por_nivel.junior)
    elif nivel_usuario == 'Pleno':
        exibir_sugestoes(sugestoes_por_nivel.pleno)
    else:
        exibir_sugestoes(sugestoes_por_nivel.senior)

if __name__ == "__main__":
    TalentRank_KNN()

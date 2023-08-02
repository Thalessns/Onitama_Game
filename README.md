* Sobre o projeto:
        Foi criado apenas para fins de aprendizado, feito com base em um trabalho proposto na faculdade, originalmente para a linguagem Java,
    resolvi voltar a programar em Python para praticar os conceitos de orientação a objetos vistos em sala. Dessa forma, este projeto foi ótimo
    para aplicar esses conhecimentos, claro que ainda há muito a melhorar e com certeza deve existir alguns erros de estruturas no código, mas
    com o tempo irei aperfeiçoar mais esses quesitos.

* Regras do jogo:
    1 - Cada jogador terá duas cartas e uma outra carta ficará na mesa.
    2 - Depois que um jogador utilizar uma carta, a carta utilizada será trocada com a carta da mesa.
    3 - O jogador não pode mover uma peça para um espaço que já contém uma peça aliada.
    4 - O jogo acaba quando o jogador derrota o mestre do adversário ou quando o jogador posiciona o seu mestre no templo adversário. 
    (Templo denomina o espaço de origem de cada mestre. Templo BLUE = 0,2 e Templo RED = 4,2).
    R = Mestre Vermelho
    r = Peça vermelha comum
    B = Mestre Azul
    b = Peça azul comum

* Como o projeto funciona:
        1 - Use o seguinte comando para rodar o projeto, tendo em vista que o terminal está aberto na pasta contendo os arquivos: python app.py
        2 - Você pode inserir os nomes dos jogadores, não há nenhum tipo de restrição.
        3 - Agora, você poderá observar o jogador atual, a cor das peças dele, carta da mesa e as cartas que o jogador atual possui.
        4 - Primeiramente, será requisitado a posição da peça que será movida, sendo assim, é necessário passar o número da linha x e número da coluna y, da seguinte forma: x,y
        5 - Agora, escolha o número da carta que será utilizada
        6 - Escolha o número do movimento da carta que você escolheu
        7 - Os passos 3, 4, 5 e 6 continuarão até que o jogo acabe
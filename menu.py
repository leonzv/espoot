import pyglet

# Cria uma janela
window = pyglet.window.Window(width=1024, height=768)

# Define as opções do menu
opcoes = [ "Sair", "Opções", "Iniciar jogo"]

# Cria os botões do menu
botoes = []
distancia = 50  # Distância entre os botões
for i, opcao in enumerate(opcoes):
    botao = pyglet.text.Label(opcao, x=window.width//2, y=window.height//2 + i*distancia, anchor_x="center", anchor_y="center")
    botoes.append(botao)

# Seleciona a opção inicial
opcao_selecionada = 0

# Desenha os botões
@window.event
def on_draw():
    window.clear()
    for i, botao in enumerate(botoes):
        if i == opcao_selecionada:
            botao.color = (255, 0, 0, 255)
        else:
            botao.color = (255, 255, 255, 255)
        botao.draw()

# Move a seleção para cima ou para baixo com as setas do teclado
@window.event
def on_key_press(tecla, mod):
    global opcao_selecionada
    if tecla == pyglet.window.key.UP:
        opcao_selecionada = (opcao_selecionada - 1) % len(opcoes)
    elif tecla == pyglet.window.key.DOWN:
        opcao_selecionada = (opcao_selecionada + 1) % len(opcoes)

# Inicia o jogo ou sai quando a opção é selecionada com Enter
@window.event
def on_key_release(tecla, mod):
    global opcao_selecionada
    if tecla == pyglet.window.key.ENTER:
        if opcao_selecionada == 0:
            # Iniciar jogo
            pass
        elif opcao_selecionada == 1:
            # Abrir opções
            pass
        elif opcao_selecionada == 2:
            # Sair do jogo
            pyglet.app.exit()
            
pyglet.app.run()
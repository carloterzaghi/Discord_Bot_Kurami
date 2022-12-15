from discord.ext import commands
import discord
import random
from discord.ext.commands.core import command

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]



class Tictactoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "tictactoe", help = "Inicia uma partida de jogo da velha contra outro membro.")
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            # print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("Vez do <@" + str(player1.id) + ">.")
            elif num == 2:
                turn = player2
                await ctx.send("Vez do <@" + str(player2.id) + ">.")
        else:
            await ctx.send("Um jogo já está em andamento! Termine antes de começar um novo.")
        
    @commands.command(name = "place", help = "Posiciona uma marca a onde quer marcar ponto no jogo da velha.")
    async def place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    
                    checkWinner(winningConditions, mark)
                    print(count)
                    if gameOver == True:
                        await ctx.send(mark + " venceu!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("É um empate!")

                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Certifique-se de escolher um número inteiro entre 1 e 9 (inclusive) e um bloco não marcado.")
            else:
                await ctx.send("Não é a sua vez.")
        else:
            await ctx.send("Por favor, inicie um novo jogo usando o comando k!tictactoe.")

    def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Por favor, mencione 2 jogadores para este comando.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Certifique-se de mencionar os jogadores / pingar o jogador (ie. <@688534433879556134>).")

    @place.error
    async def place_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Por favor, insira uma posição que você gostaria de marcar.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Certifique-se de inserir um número inteiro.")

def checkWinner( winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True
def setup(bot):
    bot.add_cog(Tictactoe(bot))
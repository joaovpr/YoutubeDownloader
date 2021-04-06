#Script Python para baixar videos do youtube

#Biblioteca pytube (Para instalar: pip install pytube)
from pytube import YouTube

#Coletando link do video e path para o local onde o video deve ser salvo
videoLink = input("Insira aqui o link do video: ")
path = input("Insira aqui o diretório onde salvar o video: ")
yt = YouTube(videoLink)

#Exibindo Informações do video
print(" \n <<<<<<<<<<<<<<<VIDEO>>>>>>>>>>>>>>> \n")
print(yt.title, "\n")
print("Duração:",yt.length, "s")
print("-----------------------------------")

#Selecionando melhor resolução possivel
ys = yt.streams.get_highest_resolution()

#Baixando o video
print("...")
ys.download(path)
print("BAIXADO")


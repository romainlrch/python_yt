#pip install pytube

from pytube import YouTube

nb_tours = int(input("Combien de tours de boucle voulez-vous ? "))
liste_url = []
num_url = 1

for i in range(nb_tours):
    url = input("Entrez l'URL n°{} : ".format(num_url))
    liste_url.append(url)
    num_url = num_url + 1

for url in liste_url:
    print(url)
    my_video = YouTube(url)

    print("----- Video Title -----")
    print(my_video.title)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
import os

def read_folder(folder: str, extensions: tuple = ("")) -> list:
    """
    Lê e retorna uma lista com o caminho de todos os arquivos
    listados em uma pasta (incluindo dentro das subpastas), o tamanho 
    e o nome do arquivo com a opção de listar arquivos 
    de formatos específicos. 
    """
    audio_folder = folder

    audio_extensions = extensions

    audio_files = []

    for root, dirs, files in os.walk(audio_folder):
        for file in files:
            if file.lower().endswith(audio_extensions):
                full_path = os.path.join(root, file)
                size = os.path.getsize(full_path)
                file_name = file[:-4]
                audio_files.append((full_path, file_name, size))

    # ordenar do menor para o maior
    audio_files.sort(key=lambda x: x[2])

    return audio_files
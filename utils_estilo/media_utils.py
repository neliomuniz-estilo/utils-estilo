from pathlib import Path
import imageio_ffmpeg
import subprocess


class MediaManager:
    """
    Gerencia operações sobre um conjunto de arquivos multimidia,
    operando em uma lista de arquivos definida na inicialização.
    """
    def __init__(self, arquivos: list):
        global ffmpeg_path
        ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
        self.arquivos = arquivos

    def convert(self, formato: str, pasta_saida: str | Path = None):
        """
        Converte uma lista de arquivos multimidia para um formato
        definido. O arquivo de saída será salvo no mesmo caminho
        do arquivo de entrada caso esse caminho não for especificado.
        """

        Path.mkdir(pasta_saida) if not pasta_saida.exists() else ''

        for arquivo in self.arquivos.iterdir():
            arquivo = Path(arquivo)
            if pasta_saida is None:
                pasta_saida = arquivo.parent
            saida = Path.joinpath(pasta_saida, arquivo.stem)
            saida = saida.with_suffix(formato)

            try:
                command = [
                            ffmpeg_path,
                            "-i", arquivo,
                            saida
                          ]

                subprocess.run(command)

            except Exception as e:
                print(f"Erro ao converter arquivo {arquivo}: {e}")

    def merge(self, saida: str | Path):
        """
        Une arquivos multimídia em um diretório ou lista em um novo arquivo.
        """
        input_files = Path(r'src\inputs.txt')
        input_dir = input_files.parent

        Path.mkdir(input_dir) if not input_dir.exists() else ''

        for arquivo in self.arquivos.iterdir():
            with open(input_files, 'a') as f:
                f.write(f"file '{arquivo}'\n")

        command = [
                    ffmpeg_path,
                    "-y", "-f", "concat", "-safe", "0",
                    "-i", input_files, "-c", "copy", saida
                  ]

        subprocess.run(command)

        Path.unlink(input_files)
        Path.rmdir(input_files.parent)

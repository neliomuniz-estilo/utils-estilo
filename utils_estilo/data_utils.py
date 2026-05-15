import json
from pathlib import Path


def jsonl_to_list(file_path: str | Path) -> list:
    """
    Lê um arquivo JSONL e retorna uma lista,
    processando cada linha como um objeto.
    """
    records = []

    with open(file_path, "r", encoding="utf-8") as f:
        conteudo = f.read()

    conteudo = conteudo.replace("None", "null")
    conteudo = conteudo.replace(" None", " null")

    linhas = conteudo.split("\n")

    for i, line in enumerate(linhas):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            records.append(obj)
        except json.JSONDecodeError as e:
            print(f"Linha {i+1} ignorada — erro: {e}")
            print(f"  Conteúdo: {repr(line[:100])}")

    return records

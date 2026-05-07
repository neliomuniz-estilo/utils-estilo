def segundos_para_hhmmss(segundos: int) -> str:
    """
    Converte um valor em segundos para o formato hh:mm:ss.
    """
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = segundos % 60

    return f"{horas:02d}:{minutos:02d}:{segundos_restantes:05.2f}"
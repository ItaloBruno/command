from controle_tv import ControleRemoto
from comando_ligar_tv import ComandoLigarTV
from comando_desligar_tv import ComandoDesligarTV
from comando_aumentar_volume_tv import ComandoAumentarVolumeTV
from comando_diminuir_volume_tv import ComandoDiminuirVolumeTV
from botao_dispositivo import BotaoDispositivo


if __name__ == '__main__':
    tv = ControleRemoto.pegar_dispositivo_eletronico()

    ligar_tv = ComandoLigarTV(dispositivo=tv)
    botao_pressionado = BotaoDispositivo(comando=ligar_tv)
    botao_pressionado.apertar()

    aumentar_volume = ComandoAumentarVolumeTV(dispositivo=tv)
    botao_pressionado = BotaoDispositivo(comando=aumentar_volume)
    botao_pressionado.apertar()
    botao_pressionado.apertar()
    botao_pressionado.apertar()
    botao_pressionado.apertar()
    botao_pressionado.apertar()

    diminuir_volume = ComandoDiminuirVolumeTV(dispositivo=tv)
    botao_pressionado = BotaoDispositivo(comando=diminuir_volume)
    botao_pressionado.apertar()
    botao_pressionado.apertar()

    desligar_tv = ComandoDesligarTV(dispositivo=tv)
    botao_pressionado = BotaoDispositivo(comando=ligar_tv)
    botao_pressionado.apertar()



import platform
import psutil

def dados_os():
    dados = dict()
    dados['Sistema_Operacional'] = {
        'Sistema_Operacional' : platform.system(),
        'Nome_OS' : platform.platform(),
        'Versão' : platform.version(),
        'Kernel' : platform.release(),
        'Arquitetura' : platform.machine()
    }
    return dados['Sistema_Operacional']

def dados_cpu():
    dados = dict()
    dados['CPU'] = {
        'Processador' : platform.processor(),
        'qtd_cpu_fisico' : psutil.cpu_count(logical=False),
        'qtd_cpu_logico' : psutil.cpu_count(logical=True),
        'frequencia_atual_mhz' : psutil.cpu_freq().current,
        'uso_cpu_nucleo_percentual' : psutil.cpu_percent(percpu=True, interval=1),
        'uso_cpu_total_percentual' : psutil.cpu_percent(interval=1)
    }
    return dados['CPU']

def dados_memoria():
    dados = dict()
    dados['memoria'] = {
        'tamanho_total_memoria_ram' : psutil.virtual_memory().total / 1000000000,
        'tamanho_memoria_em_uso_ram' : psutil.virtual_memory().used / 1000000000,
        'tamanho_restante_ram' : (psutil.virtual_memory().total / 1000000000) - (psutil.virtual_memory().used / 1000000000)
    }
    return dados['memoria']

def _dados_disco():
    dados = dict()

    particoes = psutil.disk_partitions()
    for p in particoes:
        print('Dispositivo:', p.device)
        print('Ponto de Montagem: ', p.device)
        print('Tamanho total: ', psutil.disk_usage(p.mountpoint).total)
        print('Livre: ', psutil.disk_usage(p.mountpoint).free)

    dados['disco'] = {
        'particao' : p.device,
        'montado' : p.mountpoint,
        'detalhes' : {
            'tamanho' : psutil.disk_usage(p.mountpoint).total,
            'utilizado' : psutil.disk_usage(p.mountpoint).used,
            'livre' : psutil.disk_usage(p.mountpoint).free,

        }
    }

    return dados

def estrutura(pedido):
     #Criar uma função que se responsabiliza por tudo

    str(pedido)

    pedido = pedido.lower()

    if pedido == 'cpu':
        return _dados_cpu()

    if  pedido == 'disco':
        return _dados_disco()

    if pedido == 'memoria':
        return _dados_memoria()

    if pedido == 'os':
        return _dados_os()
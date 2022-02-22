import PIL
from PIL import Image as Image_pil
import os


def redutorImagem(path: str, size: tuple) -> bool:
    try:
        im = Image_pil.open(path)
    except Exception as e:
        return False
    print(path)
    width = im.width
    height = im.height
    original_size = os.path.getsize(path)
    if width > size[0] or height > size[0]:
        exif_exists = im.info
        if "exif" in exif_exists:
            exif = im.info['exif']
            im.thumbnail(size, Image_pil.ANTIALIAS)
            im.save(path, exif=exif)

        else:
            print('imagem sem metadados')
            im.thumbnail(size, Image_pil.ANTIALIAS)
            im.save(path)
        compressed_size = os.path.getsize(path)
        redux = (1 - (compressed_size/original_size)) * 100
        print('Imagem reduzida em --> {:.2f}%'.format(redux))
        return True
    else:
        print(f'imagem não foi reduzida')
        return False


def percorrer(origin_path: str) -> tuple:
    total_images = 0
    total_compacted_images = 0
    for path, folders, files in os.walk(origin_path):
        for file in files:
            if str(file).lower().endswith('jpg'):
                total_images += 1
                abs_path = os.path.join(path, file)
                compacted = redutorImagem(abs_path, (800, 800))
                if compacted:
                    total_compacted_images += 1
    return total_images, total_compacted_images

def pergunta():
    text = input('Insira a pasta para reduzir as imagens:\n')
    print('')
    print(f'\t*********')
    print(f'\t Atenção')
    print(f'\t*********')
    print('')
    print(f' Todas as imagens da pasta "{text}" serão reduzidas')
    print('')
    print('Digite "s" para confirmar, "e" para sair ou "c" para mudar a pasta das imagens\n')
    confirma = input('Confirma ? (S/E/C):  ')
    while confirma.lower() != 's' and confirma.lower() != 'e' and confirma.lower() != 'c':
        print('')
        print('Opção inválida !')
        print('Digite "s" para confirmar, "e" para sair ou "c" para mudar a pasta das imagens\n')
        confirma = input('Confirma ? (S/E/C):  ')
    inicio(confirma, text)


def inicio(resposta:str, text:str):
    if resposta.lower() == 's':
            total_images, total_compacted_images = percorrer(text)
            print(f'*** total de {total_images} imagens')
            print(f'*** {total_compacted_images} imagens foram reduzidas')
    elif resposta.lower() == 'c':
            pergunta()

    os.system('pause')
    quit(0)


# text = 'D:\\OneDrive - ANTT- Agencia Nacional de Transportes Terrestres\\SharePointCRO\\RTA\\2 - '
#           'Diários\\2022\\2022-02\\2022_02_09 RDO\\PAV'

pergunta()



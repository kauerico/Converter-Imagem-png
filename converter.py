from PIL import Image
import os

def convert_png_to_jpg_and_replace(input_folder):
    # Itera por todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            # Carrega a imagem PNG
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path).convert("RGB")  # Converte para RGB, necessário para JPG
            
            # Define o novo nome do arquivo com extensão .jpg
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            new_path = os.path.join(input_folder, new_filename)
            
            # Salva a imagem no formato JPG e remove o arquivo .png antigo
            img.save(new_path, "JPEG")
            os.remove(img_path)
            print(f"Imagem convertida e substituída: {filename} -> {new_filename}")

# Exemplo de uso
input_folder = "C:/Users/ribei/Documents/ProjetoSoja/datasetSoja/mancha_parda"

convert_png_to_jpg_and_replace(input_folder)

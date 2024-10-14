import argparse
from pathlib import Path
import logging
from shutil import move, Error

logging.basicConfig(
    filename="file_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_files(folder: Path) -> list[Path]:
    """Retorna uma lista de arquivos no diretório fornecido."""
    try:
        return [
            file for file in folder.iterdir() if file.is_file() or file.is_symlink()
        ]
    except Exception as e:
        logging.error(f"Erro ao obter arquivos do diretório {folder}: {e}")
        return []


def organize_files_by_extension(folder: Path) -> None:
    """Organiza os arquivos em pastas com base nas suas extensões."""
    try:
        files: list[Path] = get_files(folder)

        if not files:
            logging.warning(f"Nenhum arquivo encontrado no diretório {folder}")
            return

        for file in files:
            try:
                extension: str = file.suffix[1:]  # Pega a extensão sem o ponto
                if extension:  # Verifica se o arquivo tem extensão
                    target_folder: Path = folder / extension
                    target_folder.mkdir(exist_ok=True)  # Cria a pasta se não existir
                    new_location: Path = target_folder / file.name

                    logging.info(f"Movendo {file} para {new_location}")
                    move(str(file), str(new_location))
            except Error as e:
                logging.error(
                    f"Erro ao mover o arquivo {file} para {new_location}: {e}"
                )
            except Exception as e:
                logging.error(f"Erro ao processar o arquivo {file}: {e}")
    except Exception as e:
        logging.error(f"Erro ao organizar os arquivos no diretório {folder}: {e}")


def main() -> None:
    try:
        parser = argparse.ArgumentParser(
            description="Organiza arquivos em pastas por extensão"
        )
        parser.add_argument("--path", required=True, help="Caminho para a pasta")
        args: argparse.Namespace = parser.parse_args()

        folder = Path(args.path)
        if folder.exists() and folder.is_dir():
            organize_files_by_extension(folder)
        else:
            logging.error(f"O caminho fornecido não é válido: {folder}")
    except Exception as e:
        logging.error(f"Erro no programa principal: {e}")


if __name__ == "__main__":
    main()

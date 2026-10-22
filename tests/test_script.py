"""Testes com arquivos temporários: nunca modificam a pasta do usuário."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from Script import organizar


class OrganizadorTests(unittest.TestCase):
    def test_simulacao_nao_move_arquivos(self):
        with tempfile.TemporaryDirectory() as temp:
            pasta = Path(temp)
            (pasta / "foto.png").write_text("imagem", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                contagem, conflitos = organizar(pasta, simular=True)
            self.assertEqual(contagem["png"], 1)
            self.assertEqual(conflitos, 0)
            self.assertTrue((pasta / "foto.png").exists())
            self.assertFalse((pasta / "png").exists())

    def test_conflito_preserva_arquivos(self):
        with tempfile.TemporaryDirectory() as temp:
            pasta = Path(temp)
            (pasta / "pdf").mkdir()
            (pasta / "pdf" / "relatorio.pdf").write_text("antigo", encoding="utf-8")
            (pasta / "relatorio.pdf").write_text("novo", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                _, conflitos = organizar(pasta)
            self.assertEqual(conflitos, 1)
            self.assertEqual((pasta / "pdf" / "relatorio.pdf").read_text(encoding="utf-8"), "antigo")
            self.assertEqual((pasta / "relatorio.pdf").read_text(encoding="utf-8"), "novo")

    def test_move_por_extensao_e_sem_extensao(self):
        with tempfile.TemporaryDirectory() as temp:
            pasta = Path(temp)
            (pasta / "foto.JPG").write_text("foto", encoding="utf-8")
            (pasta / "README").write_text("texto", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                contagem, _ = organizar(pasta)
            self.assertEqual(contagem["jpg"], 1)
            self.assertTrue((pasta / "jpg" / "foto.JPG").exists())
            self.assertTrue((pasta / "sem_extensao" / "README").exists())


if __name__ == "__main__":
    unittest.main()

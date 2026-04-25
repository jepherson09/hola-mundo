import unittest
from app import app

class TestHolaMundo(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config["TESTING"] = True

    def test_ruta_principal_retorna_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_ruta_principal_contiene_hola_mundo(self):
        response = self.client.get("/")
        self.assertIn(b"Hola Mundo", response.data)

    def test_ruta_inexistente_retorna_404(self):
        response = self.client.get("/pagina-que-no-existe")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()

def es_par(numero):
    return numero % 2 == 0

class TestEsPar:

    def test_es_par_para_par(self):
        self.assertTrue(es_par(4))

    def test_es_par_para_impar(self):
        self.assertFalse(es_par(7))

    def test_es_par_para_cero(self):
        self.assertTrue(es_par(0))


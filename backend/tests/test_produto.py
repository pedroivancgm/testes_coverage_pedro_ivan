from backend.entity.produto import Produto
import pytest
from backend.exceptions.excecoes import CampoObrigatorioVazioError


def test_criar_produto_com_sucesso():
    """Garante que o Produto seja criado com dados válidos."""
    cafe = Produto("cafe", 18, 50, 3, 1234567890, "alimenticio", 250)
    assert cafe._nome == "cafe"
    assert cafe._preco == 18 and cafe._quant_estoque == 50 and \
        cafe._validade == 3 and cafe._codigo_barras == 1234567890 and \
        cafe._categoria == "alimenticio" and cafe._peso == 250

def test_criar_produto_sem_nome():
    """Garante que o Produto rejeite um nome vazio."""
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("", 18, 50, 3, 1234567890, "alimenticio", 250)

def test_criar_produto_sem_preco():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Nome-Produto",None,50,3,1234567890,"alimenticio",250)

def test_produto_estoque_none():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Teste, o produto", 30, None, 3, 1234567890, "alimentício",250)

def test_produto_validade_none():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Gorila Cyberpunk",30,30,None,1234567890,"Animalesco",3000)

def  test_produto_code_none():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Action figure do Caue Salespunk",30,30,3,None,"Brinquedo",1000)

def test_produto_categoria_none():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Ronaldo Action Figure",30,30,3,12314123123,"",7)

def test_produto_peso_none():
    with pytest.raises(CampoObrigatorioVazioError):
        Produto("Fóton",300,300,80,123123123,"Luz",None)

# Produto que será usado nos proximos testes:
# Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)

def test_produto_getter_nome():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.nome == "Fini Dentaduras"

def test_produto_setter_nome():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.nome = "Fini Beijos"
    assert p.nome == "Fini Beijos"

def test_produto_getter_preco():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.preco == 11

def test_produto_setter_preco():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.preco = 13
    assert p._preco == 13

def test_produto_getter_estoque():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.quant_estoque == 300

def test_produto_setter_estoque():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.quant_estoque = 200
    assert p._quant_estoque == 200

def test_produto_getter_validade():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.validade == 1000

def test_produto_setter_validade():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.validade = 3
    assert p._validade == 3

def test_produto_getter_codigo():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.codigo_barras == 123456

def test_produto_setter_codigo():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.codigo_barras = 12345
    assert p._codigo_barras == 12345

def test_produto_getter_categoria():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.categoria == "Alimentício"

def test_produto_setter_categoria():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.categoria = "Veneno"
    assert p.categoria == "Veneno"

def test_produto_getter_peso():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    assert p.peso == 250

def test_produto_setter_peso():
    p = Produto("Fini Dentaduras",11,300,1000,123456,"Alimentício",250)
    p.peso = 200
    assert p.peso == 200

def test_retornar_msg_exception():
    exception = CampoObrigatorioVazioError("mensagem")
    print(exception.__str__())
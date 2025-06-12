import pytest
from django.urls import reverse

from parques.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:parque_2'))
    return resp


# testes do cabeçalho da página
def test_status_code(resp):
    assert resp.status_code == 200


def test_favicon(resp):
    assert_contains(resp, '<link rel="icon" href="/static/img/contagem.png">')


def test_link_para_secao_sobre_esta_na_pagina(resp):
    assert_contains(resp, '<a href="#sobre"')


def test_link_para_secao_parques_esta_na_pagina(resp):
    assert_contains(resp, '<a href="#parques"')


def test_link_para_secao_contato_esta_na_pagina(resp):
    assert_contains(resp, '<a href="#contato"')


# testes do corpo da página
def test_imagem_inicial_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/mata.jpg"')


def test_tres_imagens_da_galeria_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/parques.jpg"')
    assert_contains(resp, '<img src="/static/img/parque.JPG"')
    assert_contains(resp, '<img src="/static/img/oi.jpg"')


def test_localizacao_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!'
                          '1d3772.2185153464085!2d-44.01071928460752!3d-19.894713839'
                          '44988!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0'
                          'xa68f6d60ab735b%3A0x98b58c2b3fe1ec4e!2sParque%20Fern%C3%A'
                          '3o%20Dias!5e0!3m2!1spt-BR!2sbr!4v1718044812345!5m2!1spt-BR!2sbr" ')


# testes do rodapé da página

def test_link_para_instagram_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.instagram.com/"')


def test_link_para_tiktok_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.tiktok.com/"')


def test_link_para_youtube_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.youtube.com/"')


def test_links_para_as_paginas_dos_parques_esta_no_rodape(resp):
    assert_contains(resp, f'<a href="{reverse("base:parque_1")}')
    assert_contains(resp, f'<a href="{reverse("base:parque_2")}')
    assert_contains(resp, f'<a href="{reverse("base:parque_3")}')


def test_link_da_prefeitura_esta_na_pagina(resp):
    assert_contains(resp, '<a href="https://www.contagem.mg.gov.br/"')

import pytest
from django.urls import reverse

from parques.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:base'))
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
def test_video_dos_parques_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://player.vimeo.com/video/1092238847?'
                          'background=1&autoplay=1&loop=1&muted=1&quality=1080p"')


def test_titulo_do_video_esta_na_pagina(resp):
    assert_contains(resp, '<h1>Conheça os Parques Fernão Dias, Gentil Diniz e Sapucaias</h1>')


def test_imagem_da_secao_sobre_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/rafa.JPG"')


def test_tres_imagens_da_secao_parques_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/parques.jpg"')
    assert_contains(resp, '<img src="/static/img/oi.jpg"')
    assert_contains(resp, '<img src="/static/img/parque.JPG"')


def test_horario_de_funcionamento_esta_na_pagina(resp):
    assert_contains(resp, '<strong>Horário de Funcionamento:</strong> das 8h às 18h – todos os dias')


def test_central_de_informacoes_esta_na_pagina(resp):
    assert_contains(resp, '<strong>Central de Informações:</strong> (31) 3456-7890')


def test_email_esta_na_pagina(resp):
    assert_contains(resp, 'href="mailto:semad.gabinete@contagem.mg.gov.br"')


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

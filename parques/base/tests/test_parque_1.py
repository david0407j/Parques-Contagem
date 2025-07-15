import pytest
from django.urls import reverse

from parques.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:parque_1'))
    return resp


# testes do cabeçalho da página
def test_status_code(resp):
    assert resp.status_code == 200


def test_favicon(resp):
    assert_contains(resp, '<link rel="icon" href="/static/img/contagem.png">')


def test_link_para_secao_sobre_esta_na_pagina(resp):
    assert_contains(resp, f'<a href="{reverse("base:base")}#sobre"')


def test_link_para_secao_parques_esta_na_pagina(resp):
    assert_contains(resp, f'<a href="{reverse("base:base")}#parques"')


def test_link_para_secao_contato_esta_na_pagina(resp):
    assert_contains(resp, f'<a href="{reverse("base:base")}#contato"')


# testes do corpo da página
def test_imagem_inicial_esta_na_pagina(resp):
    assert_contains(resp, "url('/static/img/parques.jpg')")


def test_video_inicial_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.youtube.com/embed/SmGIFFwgb1Q?si=Ru0WTg0L_'
                          'vKq7WhO&autoplay=1&mute=0&loop=1&playlist=SmGIFFwgb1Q"')


def test_imagens_da_galeria_carrossel_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/amigos.JPG"')
    assert_contains(resp, '<img src="/static/img/blz.JPG"')
    assert_contains(resp, '<img src="/static/img/claro.JPG"')
    assert_contains(resp, '<img src="/static/img/davidson.JPG"')
    assert_contains(resp, '<img src="/static/img/leo.JPG"')
    assert_contains(resp, '<img src="/static/img/deus.JPG"')
    assert_contains(resp, '<img src="/static/img/joia2.JPG"')
    assert_contains(resp, '<img src="/static/img/joia.JPG"')
    assert_contains(resp, '<img src="/static/img/joia3.JPG"')
    assert_contains(resp, '<img src="/static/img/tim.JPG"')
    assert_contains(resp, '<img src="/static/img/vivo.JPG"')
    assert_contains(resp, '<img src="/static/img/parques.jpg"')


def test_localizacao_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3773.'
                          '1012914784697!2d-44.0774933!3d-19.9398386!2m3!1f0!2f0!3f0!3m2!1i'
                          '1024!2i768!4f13.1!3m3!1m2!1s0xa6955e2562291d%3A0x2419451e445d007'
                          'f!2sParque%20Fern%C3%A3o%20Dias!5e0!3m2!1spt-BR!2sbr!4v171882679'
                          '2004!5m2!1spt-BR!2sbr"')


# testes do rodapé da página

def test_link_para_instagram_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.instagram.com/vivo.contagem?igsh=NWhhYTRlaW9uYjN3"')


def test_link_para_tiktok_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.tiktok.com/@vivo.contagem?_t=ZM-8xrjCIPXiy6&_r=1"')


def test_link_para_youtube_esta_no_rodape(resp):
    assert_contains(resp, '<a href="https://www.youtube.com/playlist?list=PLVlAusYJJ6U5OWsbUJDNv0HEYOcs3Z77J"')


def test_links_para_as_paginas_dos_parques_esta_no_rodape(resp):
    assert_contains(resp, f'<a href="{reverse("base:parque_1")}')
    assert_contains(resp, f'<a href="{reverse("base:parque_2")}')
    assert_contains(resp, f'<a href="{reverse("base:parque_3")}')


def test_link_da_prefeitura_esta_na_pagina(resp):
    assert_contains(resp, '<a href="https://www.contagem.mg.gov.br/"')

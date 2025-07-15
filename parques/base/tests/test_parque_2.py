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
    assert_contains(resp, f'<a href="{reverse("base:base")}#sobre"')


def test_link_para_secao_parques_esta_na_pagina(resp):
    assert_contains(resp, f'<a href="{reverse("base:base")}#parques"')


def test_link_para_secao_contato_esta_na_pagina(resp):
    assert_contains(resp, f'<a href="{reverse("base:base")}#contato"')


# testes do corpo da página
def test_video_inicial_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.youtube.com/embed/FFltTLGUNfg?si=1LKNaYfBuMq5AJ_'
                          'W&autoplay=1&mute=0&loop=1&playlist=FFltTLGUNfg"')


def test_imagens_da_galeria_carrossel_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/foto1.JPG"')
    assert_contains(resp, '<img src="/static/img/foto2.JPG"')
    assert_contains(resp, '<img src="/static/img/foto3.JPG"')
    assert_contains(resp, '<img src="/static/img/foto4.JPG"')
    assert_contains(resp, '<img src="/static/img/foto5.JPG"')
    assert_contains(resp, '<img src="/static/img/foto6.JPG"')
    assert_contains(resp, '<img src="/static/img/foto7.JPG"')
    assert_contains(resp, '<img src="/static/img/foto8.JPG"')
    assert_contains(resp, '<img src="/static/img/foto9.JPG"')
    assert_contains(resp, '<img src="/static/img/foto10.JPG"')
    assert_contains(resp, '<img src="/static/img/foto11.JPG"')
    assert_contains(resp, '<img src="/static/img/foto12.JPG"')
    assert_contains(resp, '<img src="/static/img/foto13.JPG"')
    assert_contains(resp, '<img src="/static/img/foto14.JPG"')
    assert_contains(resp, '<img src="/static/img/foto15.JPG"')
    assert_contains(resp, '<img src="/static/img/foto16.JPG"')
    assert_contains(resp, '<img src="/static/img/foto17.JPG"')
    assert_contains(resp, '<img src="/static/img/foto18.JPG"')
    assert_contains(resp, '<img src="/static/img/foto20.JPG"')
    assert_contains(resp, '<img src="/static/img/foto21.JPG"')
    assert_contains(resp, '<img src="/static/img/foto22.JPG"')
    assert_contains(resp, '<img src="/static/img/foto23.JPG"')
    assert_contains(resp, '<img src="/static/img/foto24.JPG"')
    assert_contains(resp, '<img src="/static/img/foto25.JPG"')
    assert_contains(resp, '<img src="/static/img/foto26.JPG"')
    assert_contains(resp, '<img src="/static/img/foto27.JPG"')
    assert_contains(resp, '<img src="/static/img/foto28.JPG"')
    assert_contains(resp, '<img src="/static/img/foto29.JPG"')
    assert_contains(resp, '<img src="/static/img/foto30.JPG"')
    assert_contains(resp, '<img src="/static/img/foto31.JPG"')


def test_localizacao_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3772.'
                          '331918256478!2d-44.04357862571785!3d-19.88962333719462!2m3!1f0!2'
                          'f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xa692d1ff03aa6b%3A0xf6'
                          '1dd9431e4c66cc!2sParque%20Gentil%20Diniz!5e0!3m2!1spt-BR!2sbr!4v'
                          '1718044812345!5m2!1spt-BR!2sbr"')


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

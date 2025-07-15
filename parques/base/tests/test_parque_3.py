import pytest
from django.urls import reverse

from parques.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:parque_3'))
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
    assert_contains(resp, "url('/static/img/parque.JPG')")


def test_tres_imagens_da_galeria_esta_na_pagina(resp):
    assert_contains(resp, '<img src="/static/img/parque3_foto_1.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_2.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_3.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_4.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_5.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_6.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_7.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_8.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_9.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_10.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_11.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_12.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_14.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_15.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_17.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_18.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_19.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_20.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_21.JPG"')
    assert_contains(resp, '<img src="/static/img/parque3_foto_22.JPG"')


def test_localizacao_esta_na_pagina(resp):
    assert_contains(resp, 'src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3773.'
                          '6688579293244!2d-44.1283599!3d-19.9231581!2m3!1f0!2f0!3f0!3m2!1i'
                          '1024!2i768!4f13.1!3m3!1m2!1s0xa6ea8611d270b1%3A0x19ab840303b1956'
                          '3!2sParque%20Sapucaias!5e0!3m2!1spt-BR!2sbr!4v1718826825478!5m2!'
                          '1spt-BR!2sbr"')


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

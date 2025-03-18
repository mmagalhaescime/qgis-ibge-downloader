# IBGE Downloader

Plugin QGIS para download e extração de dados geoespaciais do IBGE (Instituto Brasileiro de Geografia e Estatística).

## Descrição

O IBGE Downloader é um plugin para QGIS que facilita o download e a extração de arquivos geoespaciais diretamente do servidor do IBGE. Com uma interface simples, você pode baixar shapefiles de malhas territoriais, cartas topográficas e outros dados geoespaciais sem precisar navegar pelo site do IBGE.

## Funcionalidades

- Download direto de arquivos do servidor do IBGE
- Suporte para URLs personalizadas
- Extração automática de arquivos ZIP
- Interface gráfica simples e intuitiva

## Instalação

### Instalação via Gerenciador de Complementos do QGIS

*Ainda não disponível no repositório oficial de plugins QGIS*

### Instalação Manual

1. Baixe o arquivo ZIP mais recente na seção [Releases](https://github.com/seuusuario/ibge-downloader/releases)
2. No QGIS, vá para `Complementos > Gerenciar e Instalar Complementos > Instalar a partir do ZIP`
3. Selecione o arquivo ZIP baixado e clique em "Instalar Plugin"
4. Ative o plugin na lista de plugins instalados

## Como Usar

1. Clique no ícone do IBGE Downloader na barra de ferramentas do QGIS
2. Digite a URL completa do arquivo que deseja baixar 
   - Exemplo para carta topográfica: `https://geoftp.ibge.gov.br/cartas_e_mapas/folhas_topograficas/vetoriais/escala_250mil/shapefile/g04_na20.zip`
3. Selecione a pasta de destino onde o arquivo será salvo
4. Clique em "Baixar"
5. Após o download, você terá a opção de extrair automaticamente o arquivo se for um ZIP

## URLs Úteis do IBGE

### Malhas Municipais
- Base: `https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/`
- Exemplo: `https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/UF/BA/BA_Municipios_2022.zip`

### Cartas Topográficas
- Base: `https://geoftp.ibge.gov.br/cartas_e_mapas/folhas_topograficas/vetoriais/escala_250mil/shapefile/`
- Exemplo: `https://geoftp.ibge.gov.br/cartas_e_mapas/folhas_topograficas/vetoriais/escala_250mil/shapefile/g04_na20.zip`

## Resolução de Problemas

### Erro "getaddrinfo failed"
Este erro ocorre quando há problemas de conexão. Verifique:
- Se a URL está correta
- Se você está conectado à internet
- Se o servidor do IBGE está disponível
- Se há um firewall ou proxy bloqueando a conexão

## Contribuições

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## Licença

Este projeto é licenciado sob a GNU General Public License v2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

Matheus Magalhães Cardoso - [magalhaes.matheus@ime.eb.br](mailto:seu.email@example.com)

---

*Este plugin não é afiliado, associado, autorizado, endossado por, ou de qualquer forma oficialmente conectado ao IBGE. Os nomes IBGE e Instituto Brasileiro de Geografia e Estatística, bem como marcas relacionadas, são marcas registradas de seus respectivos proprietários.*

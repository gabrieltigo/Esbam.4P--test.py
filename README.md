# Testes de Integração em API Pública

Este repositório contém testes para diversas APIs públicas. 
O objetivo é verificar se as APIs funcionam corretamente ao 
realizar chamadas de sucesso e erro, garantindo que os dados 
retornados atendem às expectativas.

# Estrutura dos Testes
- Testes de Sucesso: Validam se a API responde corretamente para raças válidas.
- Testes de Erro: Simulam cenários de falha, como raças inexistentes.
- Verificação de Dados: Validam a estrutura e o conteúdo das respostas.

# Pacotes Utilizados
## requests
- **Descrição**: Este pacote é usado para enviar requisições HTTP (GET, POST, etc.)
 para APIs e manipular suas respostas.
- **Utilização no projeto**:
1. Envio de requisições para APIs públicas como Dog CEO, Rest Countries, PokeAPI, CoinGecko e OMDb.
2. Captura das respostas retornadas pelas APIs em formato JSON.
Validação do status das respostas e extração de informações específicas para os testes.

## pytest

- **Descrição**: Framework de testes em Python que permite criar e executar testes automatizados de forma simples e eficiente.
- **Utilização no projeto**:
1. Estruturação de testes para validar os endpoints das APIs.
2. Automação de cenários de teste, como verificações de sucesso (status 200) e 
erros (status 404 ou respostas inválidas).
3. Uso do recurso @pytest.mark.parametrize para executar testes em diferentes
 cenários com conjuntos de dados variados.
4. Geração de relatórios claros sobre os resultados dos testes.

## APIs Testadas

1. **Dog CEO API**: Retorna imagens de cães de diversas raças, 
focando em raças grandes como "mastiff" e "newfoundland".
2. **Rest Countries API**: Fornece informações sobre países, 
incluindo leis rigorosas, verificando países como Arábia Saudita, Singapura e Irã.
3. **PokeAPI**: Informações sobre Pokémon, incluindo dados detalhados do Arcanine.
4. **CoinGecko API**: Retorna dados sobre criptomoedas, incluindo preços de mercado
 para moedas como Bitcoin e Ethereum.
5. **OMDb API**: Fornece informações sobre séries de TV, incluindo títulos e 
classificações, com foco em séries brasileiras.

# Arquivos Ad
- requirements.txt: Contém as dependências necessárias para rodar os testes.
- As bibliotecas principais são pytest e requests.
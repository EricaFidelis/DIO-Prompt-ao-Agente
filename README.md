# Bootcamp CI&T - Do Prompt ao Agente 🚀

<p align="center">
  <img src="selo.png" alt="Selo Do Prompt ao Agente CI&T" width="200">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue?style=for-the-badge" alt="Status">
    <img src="https://img.shields.io/badge/DIO-Bootcamp-orange?style=for-the-badge" alt="DIO">
    <img src="https://img.shields.io/badge/AI-Generative-brightgreen?style=for-the-badge" alt="IA">
</p>

## 📌 Sobre o Projeto
Este repositório contém a compilação dos desafios e projetos práticos desenvolvidos durante o bootcamp **Do Prompt ao Agente**, realizado pela **CI&T** em parceria com a **DIO**. O foco principal é explorar o potencial da Inteligência Artificial, desde a engenharia de prompts até a criação de agentes inteligentes.

## 🛠️ Tecnologias e Ferramentas
* **IA Generativa:** (Ex: ChatGPT, Claude, Gemini)
* **Engenharia de Prompt**
* **Copilot**
* **Automação com IA**

## 📂 Desafios Realizados

Abaixo, os links e descrições dos prompts e roteiros desenvolvidos:

1. **Roteiro de Carreira com IA**
   * Descrição: Utilização de IA para planejar passos de evolução profissional.
   * [Acessar Chat 1] https://copilot.microsoft.com/chats/TKhXcpBUSv4puSxiF71bs
   * [Acessar Chat 2] https://copilot.microsoft.com/chats/LqVeWKeN4TLAcCcAWqJPf

2. **[Explore o Poder do NotebookLM]**
   * Descrição:🚀 Miniguia de Estudos: IA na Automação de Processos com NotebookLM
📝 Contexto e Objetivos
Este projeto faz parte do desafio da DIO "Acelere sua Aprendizagem com IA". O foco principal deste caderno temático é a Automação de Tarefas e Processos, um pilar central para minha carreira.
O objetivo é utilizar o NotebookLM para consolidar conhecimentos sobre como integrar IAs e scripts de automação (como Python) para otimizar fluxos de trabalho, reduzir erros humanos e aumentar a produtividade, tomando como caso de estudo prático o desenvolvimento de automações de e-mail.
📚 Curadoria de Fontes
Para alimentar a inteligência do meu caderno no NotebookLM, selecionei as seguintes fontes (substitua pelos links ou PDFs que você usou):
1.	Repositório Base: https://github.com/EricaFidelis/Automa-ao-de-e-mails
	
2.	Documentação: Disponivel no mesmo repositório citado acima. .
  
3.	Guia Prático: "Melhores práticas para segurança em scripts de automação" (Focado em variáveis de ambiente e proteção de credenciais).
	
🧠 Engenharia de Prompts
Aqui registro o processo de refinamento das consultas para extrair o melhor da IA:
•	Prompt 1 (Visão Geral): "Com base no código do repositório da Erica Fidelis,  https://github.com/EricaFidelis/Automa-ao-de-e-mails explique de forma simples como a automação lida com o envio em massa de e-mails."

o	Resultado: A IA explicou bem a lógica e intuitiva todo processo de envio de e-mail com a plataforma criada. 
•	Prompt 2 (Refinamento/Troubleshooting): "O código usa bibliotecas nativas do Python. Como posso tornar esse script mais seguro para não expor minha senha no código-fonte?"
o	Cicatriz: A IA sugeriu Uso de Variáveis de Ambiente


•	 Prompt 3 (Estratégico): "Crie um roteiro de estudos para quem quer escalar esse projeto de automação simples para um sistema que lê dados de uma planilha Excel e personaliza o corpo do e-mail."

📧 Guia de Estudo: Automação de E-mails com Python
Este documento resume a lógica de automação de envios em massa utilizando o protocolo SMTP e boas práticas de segurança digital.
🔄 O Fluxo da Automação
A automação substitui o clique manual pelo processamento em lote, seguindo quatro pilares:
1.	Conexão: O script "disca" para o servidor (ex: smtp.gmail.com) usando a porta 587 (padrão para conexões seguras TLS).
2.	Construção: O Python utiliza a biblioteca email.message para montar o "envelope" (Assunto, De, Para) e o "conteúdo" (Corpo em texto ou HTML).
3.	Disparo: Um laço de repetição (for) percorre a lista de contatos, enviando um por um e finalizando a sessão ao terminar.
	
________________________________________
🔍 Glossário Técnico
•	SMTP: O "carteiro" digital. É o protocolo que leva sua mensagem do script até o servidor do destinatário.
•	smtplib: Biblioteca nativa do Python que traduz comandos de programação para a linguagem do servidor de e-mail.
•	.env / Variáveis de Ambiente: O "cofre" do código. Local onde escondemos senhas para que não fiquem visíveis no GitHub.
•	HTML/MIME: Formatos que permitem que o e-mail tenha negrito, cores, links e imagens, em vez de apenas texto simples.

________________________________________
🛠️ Checklist de Segurança e Melhores Práticas
•	 [ ] Senha de Aplicativo: Verifique se a Verificação em Duas Etapas está ativa para gerar a senha específica.
•	[ ] Delays de Envio: Ao enviar para muitos contatos, use time.sleep(2) entre os envios para evitar que o servidor te bloqueie por SPAM.
•	[ ] Tratamento de Erros: Use blocos try/except para que, se um e-mail falhar, o script não pare de enviar os outros.



## ✍️ Autora
**Erica Franco Fidelis**
* [LinkedIn](https://www.linkedin.com/in/ericafrancofidelis/)
* [GitHub](https://github.com/EricaFidelis)

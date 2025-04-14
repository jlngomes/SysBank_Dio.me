# GoBank - Simple Banking System → English 🌐

Welcome to GoBank, a simple banking system developed in Python. This project simulates basic banking operations, such as withdrawals, deposits, and statement inquiries, with specific rules, like daily withdrawal limits and maximum daily amount.

**Features:**

- Withdrawal: Allows withdrawals with the following restrictions:
  - Limit of 3 withdrawals per day.
  - Maximum limit of R$500.00 per day.
  - Insufficient balance verification.
- Deposit: Allows depositing positive amounts, recorded in the statement.
- Statement: Displays the history of withdrawals and deposits made.
- Interactive Menu: Text interface to facilitate user interaction.

**Code Structure:**

- menu: Text interface that displays available options (withdrawal, deposit, statement, exit).
- saque(): Function that manages withdrawals, checking daily limits and balance.
- deposito(): Function that processes deposits, accepting only positive amounts.
- extrato(): Function that displays the transaction history, separating withdrawals and deposits.

**Main Variables:**

- LIMITE_VALOR_DIARIO: Sets the daily limit of R$500.00.
- LIMITE_DE_SAQUES: Sets the limit of 3 withdrawals per day.
- saldo: Stores the current balance.
- extrato_total: List that records all transactions.

# GoBank - Sistema Bancário Simples → Português (Brasil)

Bem-vindo ao GoBank, um sistema bancário simples desenvolvido em Python. Este projeto simula operações bancárias básicas, como saques, depósitos e consulta de extrato, com algumas regras específicas, como limite diário de saques e valor máximo por dia.

**Funcionalidades:**
- Saque: Permite realizar saques com as seguintes restrições:
  - Limite de 3 saques por dia.
  - Limite máximo de R$500,00 por saque.
  - Verificação de saldo insuficiente.

- Depósito: Permite depositar valores positivos, com registro no extrato.
- Extrato: Exibe o histórico de saques e depósitos realizados.
- Menu Interativo: Interface de texto para facilitar a interação do usuário.

**Estrutura do Código:**
- menu: Interface de texto que exibe as opções disponíveis (saque, depósito, extrato, sair).
- saque(): Função que gerencia saques, verificando limites diários e saldo.
- deposito(): Função que processa depósitos, aceitando apenas valores positivos.
- extrato(): Função que exibe o histórico de transações, separando saques e depósitos.

**Variáveis principais:**
- LIMITE_VALOR_DIARIO: Define o limite diário de R$500,00.
- LIMITE_DE_SAQUES: Define o limite de 3 saques por dia.
- saldo: Armazena o saldo atual.
- extrato_total: Lista que registra todas as transações.

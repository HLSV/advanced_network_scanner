
# 🛡️ Ferramentas de Segurança e Análise de Rede para Termux

Este repositório contém **duas ferramentas essenciais** para administradores de redes, profissionais de segurança e entusiastas de tecnologia.  
Ambas foram desenvolvidas para rodar **no Termux sem necessidade de root**, sendo ideais para **iniciante, intermediário ou profissional** que deseja investigar, monitorar e proteger redes e servidores.

---

## 📌 Ferramentas Inclusas

### 1️⃣ **Scanner de Rede Automático (Sem Root)**
Ferramenta que identifica todos os dispositivos conectados à sua rede local e exibe:
- **IP** e **MAC Address** de cada dispositivo.
- **Fabricante** do dispositivo (com base no MAC).
- **Tipo de dispositivo** detectado (PC, celular, câmera, tablet, etc.).
- **Portas abertas** e serviços ativos usando **Nmap**.
- **Tecnologia** utilizada pelo serviço (HTTP, FTP, SSH, etc.).
- **Execução 100% sem root** com varredura baseada em `ping` e `arp-scan`.

---📂 Estrutura do Repositório

.
├── scanner/
│   ├── scanner.py
│   ├── requirements.txt
|     |-------README.md


🚀 Como Usar

📡 Scanner de Rede

cd scanner
python scanner.py

O script detecta seu IP automaticamente.

Faz varredura na faixa de IPs da sua rede.

Exibe informações detalhadas de cada dispositivo conectado.




📊 Exemplo de Saída (Scanner de Rede)

[+] Seu IP Local: 192.168.0.10
[+] Dispositivo Encontrado:
    - IP: 192.168.0.1
    - MAC: 00:11:22:33:44:55
    - Fabricante: TP-LINK Technologies
    - Tipo: Roteador
    - Portas Abertas:
        80/tcp - HTTP
        443/tcp - HTTPS


---
📄 Licença

Este projeto está licenciado sob a MIT License.
Você pode usar, modificar e distribuir livremente, desde que mantenha os créditos.


---

📢 Aviso Legal

⚠️ Este projeto é destinado a fins educacionais e de testes autorizados.
O uso indevido para invadir, espionar ou comprometer redes sem permissão é ilegal e pode resultar em sanções criminais.
O autor não se responsabiliza por uso indevido.


---

🤝 Contribuindo

Se quiser melhorar este projeto:

1. Faça um fork do repositório.


2. Crie uma branch para suas modificações.


3. Envie um pull request.




---

📬 Contato
Nome do criador do projeto: igor
📧 Email: legendmaster955t@gmail.com
🐙 GitHub: HLSV

---

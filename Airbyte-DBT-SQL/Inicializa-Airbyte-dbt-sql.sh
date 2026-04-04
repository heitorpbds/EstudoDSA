# 1. Remove a instalação atual
abctl local uninstall

# 2. Limpa o diretório de dados (Cuidado: isso apaga configurações locais do Airbyte)
sudo rm -rf /home/heitorpbds/.airbyte/abctl/data

# 3. Garante as permissões da pasta base
sudo chown -R $USER:$USER /home/heitorpbds/.airbyte/

# 4. Tenta reinstalar com um timeout maior de contexto (se disponível) ou apenas execute:
abctl local install
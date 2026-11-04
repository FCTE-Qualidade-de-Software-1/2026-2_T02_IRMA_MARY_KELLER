# Ambiente de Testes

Os testes serão realizados em seis sistemas operacionais diferentes, cobrindo os principais sistemas propietários e abertos usados no desktop. Abaixo está a lista dos sistemas operacionais com a versão utilizada durante os testes, com exceção do Arch Linux que não adota versões fixas.

- Windows 11 Pro
- macOS XX
- Ubuntu 26.04
- Fedora 44
- Arch Linux
- OpenSUSE Leap 16.1

Todos os ambientes, com exceção do macOS, serão virtualizados com objetivo de garantir a padronização dos recursos de hardware que cada ambiente tem acesso. Todos os ambientes virtualizados terão acesso a 4 GB de memória e poderão utilizar 4 vCPUs, a tecnologia de virtualização usada para gerir os ambientes Linux será o QEMU/KVM, com frontend [Gnome Boxes](https://apps.gnome.org/pt-BR/Boxes/), e para o ambiente Windows será utilizado o Docker, com frontend [Winboat](https://www.winboat.app/).

## Quadro de Ferramentas e Versões

<!-- TODO: adicionar dia da última atualização -->
As maquinas virtuais foram todas atualizadas dia X de novembro de 2026 usando seus respectivos gestores de pacotes. 

|                     | Windows | macOS | Ubuntu | Fedora |  Arch  | OpenSUSE Leap |
| :-----------------: | :-----: | :---: | :----: | :----: | :----: | :-----------: |
|       Chrome        |  157.0  |   X   | 156.0  | 156.0  | 156.0  |     156.0     |
|       Firefox       |  159.1  |   X   | 159.0  | 159.0  | 159.0  |     153.5     |
|     Lighthouse      | 13.6.0  |   X   | 13.6.0 | 13.6.0 | 13.6.0 |    13.6.0     |
| NVDA/VoiceOver/Orca | 2026.3  |   X   |  50.3  |  50.3  |  51.1  |     50.0      |

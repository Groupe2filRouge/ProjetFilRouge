#!/bin/sh
sudo apt update

set -e #arrête le script si code retour non 0

# Variable de mise en forme
RED='\033[0;31m'	# Red Color
YELLOW='\033[0;33m'	# Yellow Color
GREEN='\033[0;32m'	# Grean Color
NC='\033[0m' 		# No Color

#Fonction 
#Installation des packages sous forme de fonction avec vérification si le package est installé
install_package() {
    PACKAGE="$1"
    if ! dpkg -l |grep --quiet "^ii.$PACKAGE"; then
        apt install -y "$PACKAGE"
    fi
}

# On installe l'utilitaire dos2unix
echo "${GREEN}$(date +'%Y-%m-%d %H:%M:%S') [ INFO  ] : Démarrage installation dos2unix ... ${NC}"
install_package "dos2unix"

# Installation des paquets necessaires
echo "${GREEN}$(date +'%Y-%m-%d %H:%M:%S') [ INFO  ] : Démarrage installation des paquets necessaire ... ${NC}"
install_package "ufw"

install_package "python3" 
install_package "python3-pip" 
install_package "python3-dev"
install_package "git"

#installation des composants necessaires
echo "${GREEN}$(date +'%Y-%m-%d %H:%M:%S') [ INFO  ] : Démarrage installation composants ... ${NC}"
pip3 install pymongo flask boto3 Markdown python-dotenv

echo "####### SUCCESS #######"

# On lance le serveur Flask et on presente notre API.
# python3 /home/shared/app.py


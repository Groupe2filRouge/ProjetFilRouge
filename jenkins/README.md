> A la fin de l'installation se rendre sur la vm pour récupérer le mot de passe initial de Jenkins.
'''
	sudo cat /var/lib/jenkins/secrets/initialAdminPassword
'''
 Copiez le.
> Se rendre à l'adresse http://{ip_instance_ec2}:8080/ et renseignez le mot de passe précédemment copié.

Une page s'affiche avec 2 options possibles.
- Choisir l'option 'Sélectionner les plugins à installer'.
- Sélectionner alors l'onglet recommandés et recherchez  et cochez les plugins suivants:
>  - Cobertura
>  - Warnings Next Generation
>  - GitHub
>  - Git Parameter


**Désactiver le plugin gradle**

Cliquez sur "Installer"

Arrive la page "Créer le 1er utilisateur"
Renseignez a minima les champs.
> - Nom d'utilisateur
> - Mot de passe
> - Confirmation du mot de passe

Cliquez sur "Sauver et continuer"
Cliquez sur "Sauver et terminer"
Cliquez sur "Commencer à utiliser Jenkins"

Vous arrivez sur la page principale
Sélectionner le menu "Administrer Jenkins" puis "Gestion des plugins". Placez vous sur l'onglet "Disponibles

Dans la barre de recherche, recherchez les plugins suivants
>  - Docker
>  - Docker pipeline
>  - Slack Notification

Pour chacun cochez la case et cliquez sur "Install without restart"

Penser à renseigner les credentials pour le dockerhub, l'idée est OBLIGATOIREMENT dockerhub car il est utilisé dans le pipeline.

https://medium.com/@gustavo.guss/jenkins-building-docker-image-and-sending-to-registry-64b84ea45ee9

Sélectionnez "Tableau de bord" puis "Nouveau item"
Renseignez un nom de projet puis sélectionnez "Pipeline"
Cliquez sur "Ok"

Une nouvelle page apparait
ou Cliquez sur le projet puis "Configurer"
Sélectionnez la case à cocher "GitHub hook trigger for GITScm polling"
Copiez alors le contenu du fichier "pipeline.txt" du projet
Cliquez sur "Sauver"

Sur la page principale vous pouvez alors cliquer sur "Lancer un build"

### Slack

https://medium.com/appgambit/integrating-jenkins-with-slack-notifications-4f14d1ce9c7a

https://www.baeldung.com/ops/jenkins-slack-integration

### Others

https://www.rderewianko.com/getting-started-with-the-ec2-plugin-for-jenkins/

https://api.github.com/meta

https://intellipaat.com/community/8886/jenkins-private-subnet-webhook-with-github-does-not-trigger-automatic-build

https://support.cloudbees.com/hc/en-us/articles/224621648-GitHub-webhook-troubleshooting

https://www.bogotobogo.com/DevOps/Jenkins/Jenkins_on_EC2_4_GitHubHook_Notification_to_Jenkins_Server.php

https://caylent.com/jenkins-plugins-updated-2020

https://spectralops.io/blog/top-25-jenkins-plugins-for-2021/

https://www.baeldung.com/ops/jenkins-slack-integration

https://www.cprime.com/resources/blog/how-to-integrate-jenkins-github/

https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks

https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/#Download%20and%20Install%20Jenkins

Si la configuration est la bonne à la fin du build vous devez obtenir ceci:

![Capture slack](capture.png)

![Capture rapports](rapports.png)

======================================================

Pense bete...
> https://opensource.triology.de/jenkins/pipeline-syntax/globals
> https://webhookrelay.com/v1/installation/cli.html
> https://git-scm.com/docs/pretty-formats
> https://www.jenkins.io/doc/book/pipeline/docker/
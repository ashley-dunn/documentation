---
title: Timeboard
kind: documentation
---

## Changer le nom de votre Timeboard

1. Cliquez sur l'icône d'information en haut à droite de votre Timeboard:
    {{< img src="graphing/dashboards/timeboard/timeboard_name.png" alt="Timeboard name" responsive="true" popup="true" style="width:75%;">}}
2. Cliquez sur l'icône pinceau et éditez le titre et la description
3. Cliquez sur la checkmark pour enregistrer les modifications

## Lecture seule

[Un Administrateur](/account_management/team/#datadog-user-roles) ou le créateur d'un Timeboard peut passer un Timeboard en lecture seule en cliquant sur l'icône engrenage (coin droit du Timeboard) puis sur le lien **Permissions**:

{{< img src="graphing/dashboards/timeboard/read_only.png" alt="Read Only" responsive="true" popup="true" style="width:30%;">}}

**Cliquer sur "Yes" dans la fenêtre de confirmation passe le Timeboard en lecture seule**

Seul les comptes [administrateurs](/account_management/team/#datadog-user-roles) et le créateur du Timeboard peuvent passer le Timeboard en lecture seule. Tous les utilisateurs de l'organisation pourront cependant souscrire au Timeboard afin de recevoir des notifications de modifications.

Si un utilisateur décide de suivre les modifications pour un Timeboard, les modifications du Timeboard sont signalées à l'utilisateur via un événement dans [l'event stream](/graphing/event_stream):

1. Changements de texte (titre, description)
2. Changement d'élément
3. Clonage de Timeboard
4. Suppression de Timeboard

Afin d'éviter les changements énumérés ci-dessus, un administrateur (admins de compte + créateur de Timeboard) peut activer la vue en lecture seule désactivant toutes les modifications possibles aux non-administrateurs et aussi la suppression du  Timeboard.

Même en mode lecture seule, les utilisateurs non administrateurs peuvent toujours cloner le Timeboard, réorganiser la mosaïque de widget, prendre un snapshot sur un graph et afficher la mosaïque en plein écran. Tout réarrangement de la mosaïque par un utilisateur non-administrateur ne persiste pas si le Timeboard est défini en lecture seule.

## Suivi des modifications

Un utilisateur peut trouver tous les événements liés aux changements d'un Timeboard sur le Timeboard qu'ils suivent en recherchant: `tags:audit, <Screenboard_name>` dans le [flux d'événements](/graphing/event_stream/), chaque événement de notification est taggé avec ces deux tags.

## Audit de dashboards

Dans les dashboard, les notifications permettent de suivre les modifications à des fins d'audit. Toute modification effectuée crée un événement dans le [flux d'événements](/graphing/event_stream/) qui explique la modification et affiche l'utilisateur qui a effectué la modification.

Si des modifications sont apportées à vos dashboards, consultez-les avec la recherche d'événement suivante:

https://app.datadoghq.com/event/stream?per_page=30&query=tags:audit%20status:all

Cette fonctionnalité peut être activée en suivant ces étapes simples:

1. Dans l'angle supérieur droit d'un dashboard, cliquez sur l'icône représentant une roue dentée:
    {{< img src="graphing/dashboards/faq/enable_notifications.png" alt="enable notifications" responsive="true" popup="true" style="width:30%;">}}

2. Sélectionnez l'option **Notifications** et activez les notifications:

    {{< img src="graphing/dashboards/faq/notifications_pop_up.png" alt=" notifications pop up" responsive="true" popup="true" style="width:30%;">}}

## Sauvegarder mon Timeboard

En utilisant notre [API](/api), il est possible d'écrire un script pour sauvegarder vos définitions de Timeboard. Consultez ci-dessous des projets exemples de la façon dont ces sauvegardes peuvent être réalisées:

* https://github.com/brightcove/dog-watcher
* https://github.com/Shopify/doggy
* https://github.com/grosser/kennel

Un grand merci à [Brightcove](https://www.brightcove.com/), [Shopify](https://www.shopify.com/), et [Zendesk](https://www.zendesk.com/) pour partager ces projets!
# -*- coding: utf-8 -*-
"""Tous les textes du site GAZTAK, en français, anglais et espagnol.
Pour changer la carte (avril / octobre), il suffit de modifier CARTE ci-dessous."""

DOMAINE = "https://gaztak.fr"
LANGUES = ["fr", "en", "es"]

INFOS = {
    "nom": "GAZTAK",
    "rue": "40 rue Voltaire",
    "cp": "47000",
    "ville": "Agen",
    "lat": 44.2036061,
    "lon": 0.6148838,
    "tel": "+33638127892",
    "email": "lukian@gaztak.fr",
    "resmio": "https://app.resmio.com/gaztak/widget",
    "maps": "https://maps.google.com/?cid=4607134585899555750",
    "instagram": "https://www.instagram.com/gaztak_agen/",
    "facebook": "https://www.facebook.com/fromageriegaztak",
    "osm": "https://www.openstreetmap.org/export/embed.html?bbox=0.6094%2C44.2012%2C0.6204%2C44.2060&layer=mapnik&marker=44.20361%2C0.61488",
}

ROUTES = {
    "accueil": {"fr": "/", "en": "/en/", "es": "/es/"},
    "carte": {"fr": "/la-carte/", "en": "/en/menu/", "es": "/es/carta/"},
    "raclette": {"fr": "/raclette-agen/", "en": "/en/raclette-agen/", "es": "/es/raclette-agen/"},
}

# Textes d'interface communs à toutes les pages
T = {
    "fr": dict(
        nom_langue="Français", locale="fr_FR",
        nav_carte="La carte", nav_raclette="Raclette", nav_infos="Infos pratiques",
        reserver="Réserver", reserver_table="Réserver une table", voir_carte="Voir la carte",
        adresse="Adresse", horaires="Horaires", telephone="Téléphone",
        horaires_court="Du mardi au samedi, de 18 h à minuit",
        ferme_txt="Fermé le dimanche et le lundi",
        jours=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
        ferme="Fermé", heures="18 h – minuit", cuisine="Service jusqu’à tard.",
        acces="Parkings Reine-Garonne et de la Mairie à proximité. Accès PMR. Chiens bienvenus. Tous moyens de paiement acceptés.",
        map_btn="Ouvrir dans Google Maps", map_titre="Plan d’accès : GAZTAK, 40 rue Voltaire à Agen",
        resa_titre="Réserver une table", fermer="Fermer",
        resa_secours="Le module ne s’affiche pas ? Ouvrez-le dans un nouvel onglet.",
        resa_tel="Ou appelez le 06 38 12 78 92",
        resa_iframe="Module de réservation GAZTAK (resmio)",
        pied_tag="Le bar à fromages d’Agen", pied_trouver="Nous trouver", pied_suivre="Suivez-nous",
        mentions="Mentions légales", confid="Confidentialité",
        evitement="Aller au contenu", tel_aff="06 38 12 78 92",
        nav_label="Navigation principale", langue_label="Choix de la langue", legal_label="Informations légales",
        accueil_label="GAZTAK, retour à l’accueil",
    ),
    "en": dict(
        nom_langue="English", locale="en_GB",
        nav_carte="Menu", nav_raclette="Raclette", nav_infos="Visit us",
        reserver="Book", reserver_table="Book a table", voir_carte="See the menu",
        adresse="Address", horaires="Opening hours", telephone="Phone",
        horaires_court="Tuesday to Saturday, 6 pm to midnight",
        ferme_txt="Closed on Sunday and Monday",
        jours=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        ferme="Closed", heures="6 pm – midnight", cuisine="Food served until late.",
        acces="Reine-Garonne and Mairie car parks nearby. Wheelchair accessible. Dogs welcome. All payment methods accepted.",
        map_btn="Open in Google Maps", map_titre="Map: GAZTAK, 40 rue Voltaire, Agen",
        resa_titre="Book a table", fermer="Close",
        resa_secours="Booking form not showing? Open it in a new tab.",
        resa_tel="Or call +33 6 38 12 78 92",
        resa_iframe="GAZTAK booking form (resmio)",
        pied_tag="The cheese bar in Agen", pied_trouver="Find us", pied_suivre="Follow us",
        mentions="Legal notice (in French)", confid="Privacy (in French)",
        evitement="Skip to content", tel_aff="+33 6 38 12 78 92",
        nav_label="Main navigation", langue_label="Language", legal_label="Legal information",
        accueil_label="GAZTAK, back to the home page",
    ),
    "es": dict(
        nom_langue="Español", locale="es_ES",
        nav_carte="La carta", nav_raclette="Raclette", nav_infos="Cómo llegar",
        reserver="Reservar", reserver_table="Reservar mesa", voir_carte="Ver la carta",
        adresse="Dirección", horaires="Horario", telephone="Teléfono",
        horaires_court="De martes a sábado, de 18:00 a 00:00",
        ferme_txt="Cerrado domingo y lunes",
        jours=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
        ferme="Cerrado", heures="18:00 – 00:00", cuisine="Cocina abierta hasta tarde.",
        acces="Parkings Reine-Garonne y de la Mairie cerca. Accesible para personas con movilidad reducida. Se admiten perros. Se aceptan todos los medios de pago.",
        map_btn="Abrir en Google Maps", map_titre="Mapa: GAZTAK, 40 rue Voltaire, Agen",
        resa_titre="Reservar mesa", fermer="Cerrar",
        resa_secours="¿No aparece el módulo? Ábrelo en una pestaña nueva.",
        resa_tel="O llama al +33 6 38 12 78 92",
        resa_iframe="Módulo de reservas de GAZTAK (resmio)",
        pied_tag="El bar de quesos de Agen", pied_trouver="Dónde estamos", pied_suivre="Síguenos",
        mentions="Aviso legal (en francés)", confid="Privacidad (en francés)",
        evitement="Ir al contenido", tel_aff="+33 6 38 12 78 92",
        nav_label="Navegación principal", langue_label="Idioma", legal_label="Información legal",
        accueil_label="GAZTAK, volver al inicio",
    ),
}

ACCUEIL = {
    "fr": dict(
        title="GAZTAK – Le bar à fromages d’Agen | Planches et raclette à volonté",
        desc="Bar à fromages à Agen : planches de fromages fermiers et charcuteries artisanales, raclette à volonté l’hiver, terrasse toute l’année. 40 rue Voltaire.",
        h1="le bar à fromages d’Agen",
        accroche="Un vrai bar de quartier où l’on mange bien : fromages fermiers, charcuteries artisanales et, tout l’hiver, raclette à volonté.",
        alt_planche="Planche de fromages fermiers et de charcuteries artisanales chez GAZTAK à Agen",
        maison_h2="Un vrai bar de quartier, où l’on mange bien",
        maison_p="Ouvert en 2022 rue Voltaire, GAZTAK est aujourd’hui une institution à Agen. On y vient pour des fromages fermiers, au lait cru autant que faire se peut, français mais pas que, et des charcuteries artisanales servies en planches. Au comptoir : bières à la pression, vins faciles et cocktails, avec ou sans alcool.",
        guide="Référencé dans le Petit Futé depuis 2022",
        alt_plateau="Plateau de fromages fermiers avec noix, figues et confitures",
        terrasse="Une terrasse de 60 places, ouverte toute l’année",
        salle="Et 40 places en salle.",
        rac_h2="Raclette à volonté",
        rac_p="Tout l’hiver, comme à la montagne : fromage, patates et condiments à volonté, avec une portion de charcut’ comprise.",
        rac_btn="Tout sur la raclette",
        alt_raclette="Raclette à volonté : demi-meules de fromage qui fondent sur les appareils traditionnels",
        carte_h2="La carte",
        carte_p="Un aperçu de notre carte d’hiver. Les fromages et charcuteries changent au gré des arrivages.",
        carte_btn="Toute la carte",
        privat_h2="Privatiser GAZTAK",
        privat_p="Anniversaire, pot de départ, soirée d’entreprise : GAZTAK se privatise. 40 places en salle, 60 en terrasse. Appelez-nous ou écrivez-nous pour en parler.",
        appeler="Appeler le 06 38 12 78 92", ecrire="Écrire un e-mail", privat_sujet="Privatisation GAZTAK",
        resa_h2="Réserver",
        resa_p="Réservation conseillée, mais pas obligatoire : vous pouvez aussi passer à l’improviste.",
        infos_h2="Horaires", venir_h3="Venir",
    ),
    "en": dict(
        title="GAZTAK – Cheese bar in Agen | Cheese boards and all-you-can-eat raclette",
        desc="Cheese bar in Agen, France: farmhouse cheese and artisan charcuterie boards, all-you-can-eat raclette in winter, terrace open all year. 40 rue Voltaire.",
        h1="the cheese bar in Agen",
        accroche="A true neighbourhood bar where you eat well: farmhouse cheeses, artisan charcuterie and, all winter long, all-you-can-eat raclette.",
        alt_planche="Board of farmhouse cheeses and artisan charcuterie at GAZTAK in Agen",
        maison_h2="A true neighbourhood bar where you eat well",
        maison_p="Opened in 2022 on rue Voltaire, GAZTAK has become an Agen institution. People come for farmhouse cheeses, raw-milk whenever possible, from France and beyond, and artisan charcuterie served on sharing boards. At the bar: draught beers, easy-drinking wines and cocktails, with or without alcohol.",
        guide="Listed in the Petit Futé guide since 2022",
        alt_plateau="Platter of farmhouse cheeses with walnuts, figs and jams",
        terrasse="A 60-seat terrace, open all year round",
        salle="Plus 40 seats inside.",
        rac_h2="All-you-can-eat raclette",
        rac_p="All winter, just like in the mountains: unlimited cheese, potatoes and condiments, with a serving of charcuterie included.",
        rac_btn="All about our raclette",
        alt_raclette="All-you-can-eat raclette: half wheels of cheese melting on traditional raclette machines",
        carte_h2="The menu",
        carte_p="A taste of our winter menu. Cheeses and charcuterie change with what comes in.",
        carte_btn="Full menu",
        privat_h2="Private hire",
        privat_p="Birthday, leaving drinks, company evening: GAZTAK is available for private events. 40 seats inside, 60 on the terrace. Call or email us to talk it through.",
        appeler="Call +33 6 38 12 78 92", ecrire="Send an email", privat_sujet="Private hire at GAZTAK",
        resa_h2="Book",
        resa_p="Booking is recommended but not required: you’re welcome to just drop in.",
        infos_h2="Opening hours", venir_h3="Getting here",
    ),
    "es": dict(
        title="GAZTAK – Bar de quesos en Agen | Tablas y raclette a voluntad",
        desc="Bar de quesos en Agen (Francia): tablas de quesos de granja y embutidos artesanos, raclette a voluntad en invierno y terraza todo el año. 40 rue Voltaire.",
        h1="el bar de quesos de Agen",
        accroche="Un auténtico bar de barrio donde se come bien: quesos de granja, embutidos artesanos y, todo el invierno, raclette a voluntad.",
        alt_planche="Tabla de quesos de granja y embutidos artesanos en GAZTAK, Agen",
        maison_h2="Un auténtico bar de barrio donde se come bien",
        maison_p="Abierto en 2022 en la rue Voltaire, GAZTAK es hoy toda una institución en Agen. Aquí se viene por los quesos de granja, de leche cruda siempre que es posible, franceses y de otros lugares, y por los embutidos artesanos servidos en tablas para compartir. En la barra: cervezas de barril, vinos fáciles de beber y cócteles, con o sin alcohol.",
        guide="En la guía Petit Futé desde 2022",
        alt_plateau="Bandeja de quesos de granja con nueces, higos y mermeladas",
        terrasse="Una terraza de 60 plazas, abierta todo el año",
        salle="Y 40 plazas en el interior.",
        rac_h2="Raclette a voluntad",
        rac_p="Todo el invierno, como en la montaña: queso, patatas y acompañamientos a voluntad, con una ración de embutido incluida.",
        rac_btn="Todo sobre la raclette",
        alt_raclette="Raclette a voluntad: medias ruedas de queso fundiéndose en las máquinas tradicionales",
        carte_h2="La carta",
        carte_p="Un adelanto de nuestra carta de invierno. Los quesos y embutidos cambian según lo que llega.",
        carte_btn="Carta completa",
        privat_h2="Eventos privados",
        privat_p="Cumpleaños, despedidas, cenas de empresa: GAZTAK se puede reservar en exclusiva. 40 plazas en el interior y 60 en la terraza. Llámanos o escríbenos para hablarlo.",
        appeler="Llamar al +33 6 38 12 78 92", ecrire="Enviar un correo", privat_sujet="Evento privado en GAZTAK",
        resa_h2="Reservar",
        resa_p="Se recomienda reservar, aunque no es obligatorio: también puedes pasar sin reserva.",
        infos_h2="Horario", venir_h3="Cómo llegar",
    ),
}

# ---------------------------------------------------------------------------
# LA CARTE — carte d'hiver (octobre → avril). Sans les prix, à la demande du client.
# ---------------------------------------------------------------------------
CARTE = [
    {
        "id": "planches",
        "titre": {"fr": "Les planches", "en": "Boards", "es": "Tablas"},
        "intro": {
            "fr": "Nos planches sont composées de fromages fermiers au lait cru et/ou de charcuteries artisanales, autant que faire se peut. L’arrivage évolue très souvent !",
            "en": "Our boards feature farmhouse raw-milk cheeses and/or artisan charcuterie, whenever we can get them. What comes in changes very often!",
            "es": "Nuestras tablas llevan quesos de granja de leche cruda y/o embutidos artesanos, siempre que es posible. ¡Lo que llega cambia muy a menudo!",
        },
        "plats": [
            {"nom": "Ils font la paire", "detail": {"fr": "2 fromages", "en": "2 cheeses", "es": "2 quesos"}},
            {"nom": "Le carré magique", "detail": {"fr": "4 fromages", "en": "4 cheeses", "es": "4 quesos"}},
            {"nom": "Le beurre, l’argent du…", "detail": {"fr": "6 fromages", "en": "6 cheeses", "es": "6 quesos"}},
            {"nom": "La gaztak", "detail": {"fr": "mixte", "en": "mixed board", "es": "mixta"},
             "desc": {"fr": "Composée de fromages fermiers et de charcuteries sélectionnées.",
                      "en": "Farmhouse cheeses and selected charcuterie.",
                      "es": "Quesos de granja y embutidos seleccionados."}},
            {"nom": "Planche de charcut’",
             "desc": {"fr": "La charcutaille, y’a que ça de vrai ! Sélectionnées parmi les meilleures.",
                      "en": "Nothing beats good charcuterie, hand-picked from the best.",
                      "es": "Como un buen embutido, nada: seleccionados entre los mejores."}},
        ],
    },
    {
        "id": "hiver",
        "titre": {"fr": "En hiver", "en": "Winter specials", "es": "En invierno"},
        "plats": [
            {"nom": "Nos brochettes bœuf-fromage maison",
             "desc": {"fr": "Cantal AOP et pastrami français. Servies par 4.",
                      "en": "House-made beef and cheese skewers with Cantal AOP and French pastrami. Served in fours.",
                      "es": "Brochetas caseras de ternera y queso, con Cantal AOP y pastrami francés. Se sirven de 4 en 4."}},
            {"nom": "Mont d’Or AOP rôti à partager", "detail": {"fr": "500 g", "en": "500 g, to share", "es": "500 g, para compartir"},
             "desc": {"fr": "Rôti au vin jaune du Jura. Servi avec des grenailles rôties à l’ail et au thym, et de la charcut’ artisanale.",
                      "en": "Baked with Jura vin jaune. Served with garlic and thyme roasted baby potatoes and artisan charcuterie.",
                      "es": "Asado con vino amarillo del Jura. Con patatas baby asadas al ajo y tomillo, y embutido artesano."}},
            {"nom": "Notre reblochonnade",
             "desc": {"fr": "Reblochon AOP lardé de pancetta des Pyrénées, rôti au four. Servie avec des grenailles rôties à l’ail et au thym, et de la charcut’ artisanale.",
                      "en": "Reblochon AOP studded with Pyrenean pancetta and oven-baked. Served with garlic and thyme roasted baby potatoes and artisan charcuterie.",
                      "es": "Reblochon AOP mechado con panceta de los Pirineos y asado al horno. Con patatas baby asadas al ajo y tomillo, y embutido artesano."}},
        ],
    },
    {
        "id": "plaisirs",
        "titre": {"fr": "Les petits plaisirs", "en": "Little treats", "es": "Pequeños placeres"},
        "plats": [
            {"nom": "Rocamadour, mon amour"},
            {"nom": "Camembert AOP rôti et charcut’", "detail": {"fr": "entier ou demi", "en": "whole or half", "es": "entero o medio"},
             "desc": {"fr": "Grenailles rôties en supplément.",
                      "en": "Roasted baby potatoes available as a side.",
                      "es": "Patatas baby asadas como extra."}},
            {"nom": "Planchette de saucisson"},
        ],
    },
    {
        "id": "planchette",
        "titre": {"fr": "La planchette", "en": "La planchette", "es": "La planchette"},
        "texte": {
            "fr": "De quoi grignoter avec ta pinte ou ton pinard : un fromage, une charcut’ et un peu de pain.",
            "en": "A little something to nibble with your drink: one cheese, one charcuterie and a bit of bread.",
            "es": "Algo para picar con tu bebida: un queso, un embutido y un poco de pan.",
        },
    },
]

FORMULES = [
    {"nom": {"fr": "L’appareil authentique", "en": "The traditional machine", "es": "La máquina tradicional"},
     "cond": {"fr": "À partir de 3 personnes", "en": "From 3 people", "es": "A partir de 3 personas"},
     "desc": {"fr": "La demi-meule de fromage fond sur l’appareil traditionnel, à votre table.",
              "en": "A half wheel of cheese melts on the traditional machine, right at your table.",
              "es": "La media rueda de queso se funde en la máquina tradicional, en tu mesa."}},
    {"nom": {"fr": "À la bougie", "en": "Candle-heated", "es": "Con vela"},
     "cond": {"fr": "Dès 1 personne", "en": "From 1 person", "es": "Desde 1 persona"},
     "desc": {"fr": "Le petit appareil chauffé à la bougie, parfait en solo ou à deux.",
              "en": "The little candle-heated set, perfect on your own or for two.",
              "es": "El pequeño aparato que se calienta con una vela, perfecto solo o en pareja."}},
]

RESTE = {
    "fr": ["Fromage nature à volonté", "Patates et condiments à volonté", "Une portion de charcut’ comprise, puis supplément"],
    "en": ["Unlimited plain raclette cheese", "Unlimited potatoes and condiments", "One serving of charcuterie included, extra servings available"],
    "es": ["Queso natural a voluntad", "Patatas y acompañamientos a voluntad", "Una ración de embutido incluida; las siguientes, con suplemento"],
}

PAGE_CARTE = {
    "fr": dict(
        title="La carte | GAZTAK, bar à fromages à Agen",
        desc="La carte d’hiver de GAZTAK à Agen : planches de fromages fermiers, charcuteries artisanales, Mont d’Or rôti, reblochonnade et raclette à volonté.",
        h1="La carte",
        intro="Notre carte d’hiver et ses incontournables. Fromages et charcuteries changent au gré des arrivages : demandez ce qu’il y a de bon ce soir.",
        raclette_h2="Notre fameuse raclette à volonté",
        raclette_p="Deux possibilités, suivant le nombre de convives et les réservations de la soirée.",
        raclette_btn="Tout sur la raclette",
        boissons_h2="À boire",
        boissons_p="Bières à la pression, vins faciles à boire, cocktails avec et sans alcool.",
        note="Carte d’hiver, d’octobre à avril. Liste des allergènes disponible sur demande auprès de l’équipe.",
        menu_nom="Carte d’hiver",
    ),
    "en": dict(
        title="Menu | GAZTAK cheese bar in Agen",
        desc="GAZTAK’s winter menu in Agen: farmhouse cheese boards, artisan charcuterie, baked Mont d’Or, reblochonnade and all-you-can-eat raclette.",
        h1="The menu",
        intro="Our winter menu and its classics. Cheeses and charcuterie change with what comes in: ask us what’s good tonight. Dish names are kept in French, as on our menu.",
        raclette_h2="Our famous all-you-can-eat raclette",
        raclette_p="Two options, depending on the size of your group and that evening’s bookings.",
        raclette_btn="All about our raclette",
        boissons_h2="Drinks",
        boissons_p="Draught beers, easy-drinking wines, cocktails with or without alcohol.",
        note="Winter menu, October to April. Allergen information available from our team on request.",
        menu_nom="Winter menu",
    ),
    "es": dict(
        title="La carta | GAZTAK, bar de quesos en Agen",
        desc="La carta de invierno de GAZTAK en Agen: tablas de quesos de granja, embutidos artesanos, Mont d’Or asado, reblochonnade y raclette a voluntad.",
        h1="La carta",
        intro="Nuestra carta de invierno y sus imprescindibles. Los quesos y embutidos cambian según lo que llega: pregúntanos qué hay de bueno esta noche. Los nombres de los platos están en francés, como en nuestra carta.",
        raclette_h2="Nuestra famosa raclette a voluntad",
        raclette_p="Dos opciones, según el número de comensales y las reservas de la noche.",
        raclette_btn="Todo sobre la raclette",
        boissons_h2="Para beber",
        boissons_p="Cervezas de barril, vinos fáciles de beber, cócteles con y sin alcohol.",
        note="Carta de invierno, de octubre a abril. Información sobre alérgenos disponible a petición.",
        menu_nom="Carta de invierno",
    ),
}

PAGE_RACLETTE = {
    "fr": dict(
        title="Raclette à volonté à Agen | GAZTAK, bar à fromages",
        desc="Raclette à volonté à Agen chez GAZTAK : fromage, patates et condiments à volonté, dès 1 personne. Du mardi au samedi soir, tout l’hiver, 40 rue Voltaire.",
        h1="Raclette à volonté à Agen",
        intro="Tout l’hiver, GAZTAK sert sa fameuse raclette à volonté, comme à la montagne, en plein centre d’Agen.",
        deux_h2="Deux façons de la déguster",
        reste_h2="Et le reste, c’est pareil",
        note="La formule proposée dépend du nombre de convives et des réservations de la soirée.",
        faq_h2="Bon à savoir",
        faq=[
            ("Faut-il réserver pour la raclette ?",
             "Ce n’est pas obligatoire, mais c’est conseillé : la formule proposée dépend du nombre de convives et des réservations de la soirée."),
            ("Peut-on venir seul ou à deux ?",
             "Oui. La raclette à la bougie se sert dès 1 personne ; l’appareil authentique, avec sa demi-meule, à partir de 3 personnes."),
            ("Quand peut-on manger une raclette chez GAZTAK ?",
             "Pendant toute la saison d’hiver, d’octobre à avril, du mardi au samedi à partir de 18 h."),
            ("Y a-t-il d’autres plats au fromage fondu ?",
             "Oui : Mont d’Or AOP rôti au vin jaune, reblochonnade, camembert rôti… {lien_carte}"),
        ],
        lien_carte="Voir toute la carte",
        cta_h2="Une soirée raclette en vue ?",
        cta_p="Réservez en ligne en quelques clics, ou appelez-nous au 06 38 12 78 92.",
        appeler="Appeler le 06 38 12 78 92",
    ),
    "en": dict(
        title="All-you-can-eat raclette in Agen | GAZTAK cheese bar",
        desc="All-you-can-eat raclette in Agen at GAZTAK: unlimited cheese, potatoes and condiments, from 1 person. Tuesday to Saturday evenings all winter, 40 rue Voltaire.",
        h1="All-you-can-eat raclette in Agen",
        intro="All winter long, GAZTAK serves its famous all-you-can-eat raclette, just like in the mountains, right in the centre of Agen.",
        deux_h2="Two ways to enjoy it",
        reste_h2="Everything else is the same",
        note="The option offered depends on the size of your group and that evening’s bookings.",
        faq_h2="Good to know",
        faq=[
            ("Do I need to book for raclette?",
             "It isn’t required, but it’s recommended: the option offered depends on the size of your group and that evening’s bookings."),
            ("Can I come on my own or as a couple?",
             "Yes. Candle-heated raclette is served from 1 person; the traditional machine with its half wheel from 3 people."),
            ("When is raclette on the menu?",
             "Throughout the winter season, from October to April, Tuesday to Saturday from 6 pm."),
            ("Are there other melted-cheese dishes?",
             "Yes: Mont d’Or AOP baked with vin jaune, reblochonnade, roasted camembert… {lien_carte}"),
        ],
        lien_carte="See the full menu",
        cta_h2="Planning a raclette night?",
        cta_p="Book online in a few clicks, or call us on +33 6 38 12 78 92.",
        appeler="Call +33 6 38 12 78 92",
    ),
    "es": dict(
        title="Raclette a voluntad en Agen | GAZTAK, bar de quesos",
        desc="Raclette a voluntad en Agen en GAZTAK: queso, patatas y acompañamientos a voluntad, desde 1 persona. De martes a sábado por la noche, todo el invierno.",
        h1="Raclette a voluntad en Agen",
        intro="Todo el invierno, GAZTAK sirve su famosa raclette a voluntad, como en la montaña, en pleno centro de Agen.",
        deux_h2="Dos maneras de disfrutarla",
        reste_h2="Y lo demás, igual",
        note="La fórmula depende del número de comensales y de las reservas de la noche.",
        faq_h2="Bueno saberlo",
        faq=[
            ("¿Hay que reservar para la raclette?",
             "No es obligatorio, pero sí recomendable: la fórmula depende del número de comensales y de las reservas de la noche."),
            ("¿Se puede ir solo o en pareja?",
             "Sí. La raclette con vela se sirve desde 1 persona; la máquina tradicional, con su media rueda, a partir de 3 personas."),
            ("¿Cuándo hay raclette en GAZTAK?",
             "Durante toda la temporada de invierno, de octubre a abril, de martes a sábado a partir de las 18:00."),
            ("¿Hay otros platos de queso fundido?",
             "Sí: Mont d’Or AOP asado con vino amarillo, reblochonnade, camembert asado… {lien_carte}"),
        ],
        lien_carte="Ver la carta completa",
        cta_h2="¿Te apetece una noche de raclette?",
        cta_p="Reserva en línea en unos clics o llámanos al +33 6 38 12 78 92.",
        appeler="Llamar al +33 6 38 12 78 92",
    ),
}

MENTIONS = """
<h1 class="titre-l">Mentions légales</h1>
<h2>Éditeur du site</h2>
<p>SARL GAZTAK, au capital de 2 500 €<br>Siège social : 40 rue Voltaire, 47000 Agen<br>SIRET : 915 153 696 00017 – RCS Agen 915 153 696<br>Téléphone : <a href="tel:+33638127892">06 38 12 78 92</a> – E-mail : <a href="mailto:lukian@gaztak.fr">lukian@gaztak.fr</a></p>
<h2>Directeur de la publication</h2>
<p>Lukian Pillard, gérant.</p>
<h2>Hébergement</h2>
<p>GitHub, Inc. (service GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis – <a href="https://github.com" rel="noopener">github.com</a></p>
<h2>Propriété intellectuelle</h2>
<p>L’ensemble des contenus de ce site (textes, photographies, logo) est la propriété de la SARL GAZTAK, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2>Crédits</h2>
<p>Plan : © les contributeurs d’OpenStreetMap. Polices de caractères : Bricolage Grotesque et Instrument Sans, sous licence SIL Open Font License.</p>
<h2>Alcool</h2>
<p>L’abus d’alcool est dangereux pour la santé, à consommer avec modération. La vente d’alcool aux mineurs est interdite.</p>
"""

CONFIDENTIALITE = """
<h1 class="titre-l">Confidentialité et cookies</h1>
<h2>Aucun cookie de suivi</h2>
<p>Ce site ne dépose aucun cookie publicitaire ni de mesure d’audience. C’est pourquoi aucun bandeau de consentement ne s’affiche.</p>
<h2>Statistiques de fréquentation</h2>
<p>La fréquentation est mesurée avec Cloudflare Web Analytics, un outil sans cookie qui ne collecte aucune donnée permettant de vous identifier.</p>
<h2>Réservation en ligne</h2>
<p>Le module de réservation est fourni par resmio GmbH. Les informations saisies lors d’une réservation (nom, coordonnées, date, nombre de personnes) sont transmises à resmio et à GAZTAK uniquement pour gérer votre réservation. Le module n’utilise que les cookies techniques nécessaires à son fonctionnement. Pour en savoir plus, consultez la politique de confidentialité de resmio sur <a href="https://www.resmio.com" rel="noopener">resmio.com</a>.</p>
<h2>Plan d’accès</h2>
<p>Le plan est chargé depuis les serveurs d’OpenStreetMap, qui reçoivent à cette occasion votre adresse IP, comme pour l’affichage de toute page web.</p>
<h2>Contact</h2>
<p>Si vous nous écrivez ou nous appelez, vos coordonnées servent uniquement à vous répondre et ne sont jamais transmises à des tiers.</p>
<h2>Vos droits</h2>
<p>Conformément au RGPD, vous pouvez accéder à vos données, les rectifier ou demander leur effacement en écrivant à <a href="mailto:lukian@gaztak.fr">lukian@gaztak.fr</a>. Vous pouvez aussi adresser une réclamation à la CNIL (<a href="https://www.cnil.fr" rel="noopener">cnil.fr</a>).</p>
<h2>Hébergement</h2>
<p>Le site est hébergé par GitHub Pages (GitHub, Inc.), qui peut conserver des journaux techniques de connexion pour des raisons de sécurité.</p>
"""

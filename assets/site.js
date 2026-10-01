/* GAZTAK – ouvre le module de réservation resmio dans une fenêtre, sans quitter le site.
   Sans JavaScript, les boutons « Réserver » ouvrent resmio dans un nouvel onglet. */
(function () {
  var fenetre = document.getElementById('resa');
  if (!fenetre || typeof fenetre.showModal !== 'function') return;
  var cadre = fenetre.querySelector('iframe');

  document.addEventListener('click', function (e) {
    var bouton = e.target.closest('[data-resa]');
    if (!bouton) return;
    e.preventDefault();
    if (!cadre.getAttribute('src')) cadre.setAttribute('src', cadre.getAttribute('data-src'));
    fenetre.showModal();
  });

  fenetre.addEventListener('click', function (e) {
    if (e.target === fenetre) fenetre.close();
  });
  fenetre.querySelector('[data-fermer]').addEventListener('click', function () {
    fenetre.close();
  });
})();

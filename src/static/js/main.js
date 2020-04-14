window.addEventListener('DOMContentLoaded', () => {
  const _navbarBurgers = Array.from(document.querySelectorAll('.navbar-burger'));
  if (_navbarBurgers.length) {
    _navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        const target = el.dataset.target;
        const _target = document.querySelector(target);
        el.classList.toggle('is-active');
        _target.classList.toggle('is-active');
      })
    })
  }
  const _notifications = Array.from(document.querySelectorAll('.notification .delete')) || [];
  _notifications.forEach(_delete => {
    _delete.addEventListener('click', () => {
      _delete.parentNode.remove();
    })
  })
});
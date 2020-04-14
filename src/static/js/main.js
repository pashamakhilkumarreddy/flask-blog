window.addEventListener('DOMContentLoaded', () => {
  const _navbarBurgers = Array.from(document.querySelectorAll('.navbar-burger'));
  console.log(_navbarBurgers);
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
});
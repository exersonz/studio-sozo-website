(() => {
  const box = document.querySelector('.slideshow');
  if (!box) return;
  const slides = [...box.querySelectorAll('.slide')];
  const dotsBox = box.querySelector('.dots');
  let i = 0, timer;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const dots = slides.map((_, n) => {
    const d = document.createElement('button');
    d.setAttribute('aria-label', 'Go to slide ' + (n + 1));
    d.onclick = () => { show(n); restart(); };
    dotsBox.appendChild(d);
    return d;
  });

  function show(n) {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle('active', k === i));
    dots.forEach((d, k) => d.classList.toggle('on', k === i));
  }
  function restart() {
    clearInterval(timer);
    if (!reduce && slides.length > 1) timer = setInterval(() => show(i + 1), 4000);
  }

  box.querySelector('.prev').onclick = () => { show(i - 1); restart(); };
  box.querySelector('.next').onclick = () => { show(i + 1); restart(); };
  box.addEventListener('mouseenter', () => clearInterval(timer));
  box.addEventListener('mouseleave', restart);
  show(0); restart();
})();

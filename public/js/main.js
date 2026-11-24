// 1. Cards tilt in 3D only while you hover over them with the mouse.
document.querySelectorAll("[data-tilt]").forEach(function (card) {
  card.addEventListener("pointermove", function (e) {
    if (e.pointerType !== "mouse") return;
    var r = card.getBoundingClientRect();
    var x = (e.clientX - r.left) / r.width - 0.5;
    var y = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = "perspective(900px) rotateY(" + x * 6 + "deg) rotateX(" + -y * 6 + "deg) translateY(-4px)";
  });
  card.addEventListener("pointerleave", function () { card.style.transform = ""; });
});

// 2. Highlight the menu link of the section you are reading.
var links = document.querySelectorAll(".nav-links a");
var observer = new IntersectionObserver(function (entries) {
  entries.forEach(function (entry) {
    if (!entry.isIntersecting) return;
    links.forEach(function (a) { a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id); });
  });
}, { rootMargin: "-45% 0px -50% 0px" });
document.querySelectorAll("main section").forEach(function (s) { observer.observe(s); });

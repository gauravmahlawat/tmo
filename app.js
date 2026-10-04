const menuToggle = document.querySelector(".menu-toggle");
const siteNav = document.querySelector("#site-nav");

if (menuToggle && siteNav) {
  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    siteNav.classList.toggle("is-open", !isOpen);
  });

  siteNav.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      menuToggle.setAttribute("aria-expanded", "false");
      siteNav.classList.remove("is-open");
    }
  });
}

const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
if (!motionPreference.matches && "IntersectionObserver" in window) {
  document.documentElement.classList.add("js-motion");
  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        currentObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
}

const contactForm = document.querySelector("#contact-form");
if (contactForm) {
  contactForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const values = new FormData(contactForm);
    const subject = `Website enquiry from ${values.get("name")}`;
    const body = [
      `Name: ${values.get("name")}`,
      `Email: ${values.get("email")}`,
      `Company: ${values.get("company") || "Not provided"}`,
      "",
      values.get("message"),
    ].join("\n");

    window.location.href = `mailto:gauravmahlawat@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });
}

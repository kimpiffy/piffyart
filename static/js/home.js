document.addEventListener("DOMContentLoaded", () => {
  const siteNav = document.querySelector("[data-site-nav]");
  const navToggle = siteNav?.querySelector("[data-nav-toggle]");
  const navPanel = siteNav?.querySelector("[data-nav-panel]");
  const copyButton = document.querySelector("[data-copy-email]");
  const modal = document.getElementById("about-modal");
  const openers = document.querySelectorAll("[data-modal-open='about-modal']");
  const popTargets = document.querySelectorAll("[data-pop-blob]");
  const clipTargets = document.querySelectorAll("[data-blob-clip]");

  const setNavOpen = (isOpen) => {
    if (!siteNav || !navToggle || !navPanel) {
      return;
    }

    siteNav.classList.toggle("is-open", isOpen);
    navToggle.setAttribute("aria-expanded", String(isOpen));
  };

  const pulseNav = () => {
    if (!navToggle) {
      return;
    }

    navToggle.classList.remove("is-bouncing");
    void navToggle.offsetWidth;
    navToggle.classList.add("is-bouncing");
    window.setTimeout(() => navToggle.classList.remove("is-bouncing"), 520);
  };

  if (siteNav && navToggle) {
    navToggle.addEventListener("click", () => {
      const isOpen = !siteNav.classList.contains("is-open");
      setNavOpen(isOpen);
      if (isOpen) {
        pulseNav();
      }
    });

    document.addEventListener("click", (event) => {
      if (!siteNav.classList.contains("is-open")) {
        return;
      }

      if (!siteNav.contains(event.target)) {
        setNavOpen(false);
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        setNavOpen(false);
      }
    });
  }

  if (copyButton) {
    copyButton.addEventListener("click", async () => {
      const value = copyButton.getAttribute("data-copy-value") || "";

      try {
        await navigator.clipboard.writeText(value);
        copyButton.textContent = "Copied";
      } catch {
        const helper = document.createElement("textarea");
        helper.value = value;
        helper.setAttribute("readonly", "true");
        helper.style.position = "absolute";
        helper.style.left = "-9999px";
        document.body.appendChild(helper);
        helper.select();
        document.execCommand("copy");
        helper.remove();
        copyButton.textContent = "Copied";
      }

      window.setTimeout(() => {
        copyButton.textContent = "Copy";
      }, 1400);
    });
  }

  clipTargets.forEach((target) => {
    const clipId = target.getAttribute("data-blob-clip");
    if (!clipId) {
      return;
    }

    target.style.clipPath = `url(#${clipId})`;
    target.style.webkitClipPath = `url(#${clipId})`;
  });

  if (modal) {
    openers.forEach((trigger) => {
      trigger.addEventListener("click", () => {
        setNavOpen(false);
        if (typeof modal.showModal === "function") {
          modal.showModal();
        } else {
          modal.setAttribute("open", "open");
        }
      });
    });

    modal.addEventListener("click", (event) => {
      const box = modal.querySelector(".modal-shell");
      if (box && !box.contains(event.target) && typeof modal.close === "function") {
        modal.close();
      }
    });
  }

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.18 });

    popTargets.forEach((target) => observer.observe(target));
  } else {
    popTargets.forEach((target) => target.classList.add("is-visible"));
  }
});
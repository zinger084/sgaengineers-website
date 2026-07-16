/* SGA ENGINEERS - shared interactions (polished) */

(function () {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  const yearEls = document.querySelectorAll("[data-year]");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  yearEls.forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  // Sticky header - rAF-throttled for smoothness
  let ticking = false;
  const onScroll = () => {
    if (!header || ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      header.classList.toggle("is-scrolled", window.scrollY > 18);
      ticking = false;
    });
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Cinematic hero image settle
  const hero = document.querySelector(".hero");
  if (hero) {
    requestAnimationFrame(() => hero.classList.add("is-ready"));
  }

  // Mobile nav
  const setNavOpen = (open) => {
    if (!navLinks || !toggle) return;
    navLinks.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("nav-open", open);
  };

  if (toggle && navLinks) {
    toggle.addEventListener("click", () => {
      setNavOpen(!navLinks.classList.contains("is-open"));
    });

    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setNavOpen(false));
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setNavOpen(false);
    });

    // Close drawer if resizing to desktop
    window.addEventListener(
      "resize",
      () => {
        if (window.innerWidth > 960) setNavOpen(false);
      },
      { passive: true }
    );
  }

  // Scroll reveal with optional stagger via parent .reveal-stagger
  const reveals = document.querySelectorAll(".reveal");
  if (!reduceMotion && "IntersectionObserver" in window && reveals.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -8% 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-visible"));
  }

  // Auto-stagger common grids if not already marked
  document
    .querySelectorAll(
      ".services-grid, .audience-grid, .outcome-grid, .pillars, .process-steps, .next-steps, .perks, .markets-grid, .team-grid, .case-grid, .market-spotlight, .practice-matrix"
    )
    .forEach((grid) => {
      if (!grid.classList.contains("reveal-stagger")) {
        grid.classList.add("reveal-stagger");
      }
    });

  // Smooth internal anchor offset is handled via CSS scroll-padding-top

  // Contact form - mailto via visitor's email app (reliable with Microsoft 365).
  // FormSubmit and similar free relays often never reach M365 (silent drop).
  const form = document.querySelector("[data-contact-form]");
  const formSuccess = document.querySelector("[data-form-success]");
  let lastMailto = "";
  let lastBody = "";

  const buildContactPayload = (formEl) => {
    const data = new FormData(formEl);
    const name = String(data.get("name") || "").trim();
    const email = String(data.get("email") || "").trim();
    const company = String(data.get("company") || "").trim();
    const phone = String(data.get("phone") || "").trim();
    const location = String(data.get("location") || "").trim();
    const subject = String(data.get("subject") || "Project inquiry").trim();
    const message = String(data.get("message") || "").trim();

    const body = [
      `Name: ${name}`,
      `Email: ${email}`,
      company ? `Company: ${company}` : null,
      phone ? `Phone: ${phone}` : null,
      location ? `Project location: ${location}` : null,
      "",
      message,
    ]
      .filter((line) => line !== null)
      .join("\n");

    const mailto = `mailto:engineer@sgaengineers.com?subject=${encodeURIComponent(
      `SGA website: ${subject}`
    )}&body=${encodeURIComponent(body)}`;

    return { body, mailto, subject };
  };

  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!form.reportValidity()) return;

      const payload = buildContactPayload(form);
      lastMailto = payload.mailto;
      lastBody = payload.body;

      // Open the visitor's email app with a pre-filled message
      window.location.href = payload.mailto;

      if (formSuccess) {
        formSuccess.hidden = false;
        form.hidden = true;
        formSuccess.scrollIntoView({
          behavior: reduceMotion ? "auto" : "smooth",
          block: "center",
        });
      }
    });
  }

  const openMailBtn = document.querySelector("[data-form-open-mail]");
  if (openMailBtn) {
    openMailBtn.addEventListener("click", () => {
      if (lastMailto) window.location.href = lastMailto;
    });
  }

  const copyBtn = document.querySelector("[data-form-copy]");
  const copyStatus = document.querySelector("[data-form-copy-status]");
  if (copyBtn) {
    copyBtn.addEventListener("click", async () => {
      const text =
        lastBody ||
        (form && !form.hidden ? buildContactPayload(form).body : "");
      if (!text) return;
      try {
        await navigator.clipboard.writeText(
          `To: engineer@sgaengineers.com\n\n${text}`
        );
        if (copyStatus) {
          copyStatus.hidden = false;
          copyStatus.textContent = "Copied. Paste into a new email to engineer@sgaengineers.com.";
        }
      } catch {
        if (copyStatus) {
          copyStatus.hidden = false;
          copyStatus.textContent =
            "Could not copy automatically. Select and copy the message manually, or email engineer@sgaengineers.com.";
        }
      }
    });
  }

  // External images: fade-in when loaded (avoids pop-in)
  if (!reduceMotion) {
    document.querySelectorAll("img").forEach((img) => {
      if (img.closest(".logo")) return;
      const show = () => {
        img.style.transition = "opacity 0.5s ease";
        img.style.opacity = "1";
      };
      if (img.complete) {
        img.style.opacity = "1";
      } else {
        img.style.opacity = "0";
        img.addEventListener("load", show, { once: true });
        img.addEventListener("error", show, { once: true });
      }
    });
  }

  // Practice bubbles: anonymized example projects from portfolio
  const practiceRoot = document.querySelector("[data-practice-bubbles]");
  const examplesPanel = document.querySelector("[data-practice-examples]");
  if (practiceRoot && examplesPanel) {
    const eyebrowEl = examplesPanel.querySelector("[data-examples-eyebrow]");
    const titleEl = examplesPanel.querySelector("[data-examples-title]");
    const leadEl = examplesPanel.querySelector("[data-examples-lead]");
    const gridEl = examplesPanel.querySelector("[data-examples-grid]");
    const closeBtn = examplesPanel.querySelector("[data-examples-close]");
    const bubbles = practiceRoot.querySelectorAll(".practice-bubble");

    /** Anonymized examples drawn from real SGA work (names withheld). */
    const BUBBLE_EXAMPLES = {
      dbb: {
        category: "Delivery methods",
        title: "Design-bid-build",
        lead: "Sealed packages, clear bid sets, and CA support through award and construction.",
        projects: [
          {
            market: "Public safety",
            title: "New multi-bay fire station",
            blurb:
              "Full MEP and technology bid documents for apparatus bays, decon, bunk rooms, and generator backup.",
          },
          {
            market: "K-12 athletics",
            title: "Stadium concessions and lockers",
            blurb:
              "Ground-up support buildings with coordinated HVAC, kitchen exhaust, and plumbing for bid and permit.",
          },
          {
            market: "Municipal training",
            title: "City welding fabrication lab",
            blurb:
              "AWS-grade exhaust, power for process equipment, and fire protection sized for elevated hazard.",
          },
        ],
      },
      "design-assist": {
        category: "Delivery methods",
        title: "Design-assist",
        lead: "Early contractor collaboration so clearances, sequencing, and equipment realities shape the documents.",
        projects: [
          {
            market: "Industrial",
            title: "Process plant controls coordination",
            blurb:
              "Commissioning and peer review alongside install teams for BAS, PLC, and cable-tray routing.",
          },
          {
            market: "Flex / TI",
            title: "Warehouse-to-tenant fit-outs",
            blurb:
              "Fast MEP packages aligned with GC schedules for power, HVAC, and life safety in shell space.",
          },
          {
            market: "Higher ed CTE",
            title: "Welding and joining center",
            blurb:
              "Source-capture exhaust and process gases coordinated with equipment vendors before rough-in.",
          },
        ],
      },
      cmr: {
        category: "Delivery methods",
        title: "CMR",
        lead: "Construction Manager at Risk (CMR) delivery with progressive documents and cost-aware system choices.",
        projects: [
          {
            market: "Municipal recreation",
            title: "Community center expansion",
            blurb:
              "MEP and technology for gymnasium, multipurpose rooms, and food service under CMR-led procurement.",
          },
          {
            market: "Municipal public health",
            title: "Occupied health department renovation",
            blurb:
              "Central plant upgrades and office fit-out phased so staff floors stayed open during construction.",
          },
          {
            market: "Higher education",
            title: "Campus rec gym environment upgrade",
            blurb:
              "Humidity control and hybrid cooling for a renovated gym floor with CMR coordination on cutover.",
          },
        ],
      },
      "design-build": {
        category: "Delivery methods",
        title: "Design-build",
        lead: "Integrated design with the builder when speed, single-source accountability, and field feedback matter.",
        projects: [
          {
            market: "Utility training",
            title: "Welding training lab renovation",
            blurb:
              "MEPFT for steel and MDPE welding instruction spaces designed against existing building conditions.",
          },
          {
            market: "Industrial plant",
            title: "Plant office and lab expansion",
            blurb:
              "Multi-phase MEPFT for offices, labs, and cafeteria tied into live plant infrastructure.",
          },
          {
            market: "Hospitality adaptive reuse",
            title: "Historic barn event venue",
            blurb:
              "New MEP services into a structure with no existing systems, coordinated for builder-led delivery.",
          },
        ],
      },
      "lean-ipd": {
        category: "Delivery methods",
        title: "Lean IPD",
        lead: "Integrated lean project delivery with shared targets, early system decisions, and fewer handoffs.",
        projects: [
          {
            market: "Healthcare",
            title: "ED plant modernization",
            blurb:
              "Phased chiller, AHU, and controls work planned with owner and partners around live clinical operations.",
          },
          {
            market: "Mission critical mindset",
            title: "High-reliability plant cutover",
            blurb:
              "Concurrent maintainability thinking, open controls, and startup verification before reliance.",
          },
          {
            market: "K-12",
            title: "Geothermal classroom retrofit",
            blurb:
              "Dozens of WSHP replacements on a ground-loop plant with open BACnet sequences and balancing.",
          },
        ],
      },
      bim: {
        category: "Tools",
        title: "BIM / CAD",
        lead: "Revit and CAD coordination so trades see conflicts in the model, not after fabrication.",
        projects: [
          {
            market: "Higher ed CTE",
            title: "Welding center at LOD 350",
            blurb:
              "Full MEPFT modeled with process gases, compressed air, and exhaust integrated for clash detection.",
          },
          {
            market: "Healthcare clinic",
            title: "Outpatient clinic fit-out",
            blurb:
              "Core-and-shell plus interior packages coordinated in BIM for medical power, HVAC, and cabling.",
          },
          {
            market: "Municipal",
            title: "Traffic facility welding lab",
            blurb:
              "LOD 300 BIM for snorkel exhaust, equipment power, and elevated-hazard suppression design.",
          },
        ],
      },
      lidar: {
        category: "Tools",
        title: "Lidar",
        lead: "Scan-based existing conditions so renovations start from measured reality.",
        projects: [
          {
            market: "Healthcare",
            title: "Main-campus life safety survey",
            blurb:
              "Non-destructive above-ceiling investigation and documentation of fire, smoke, and egress systems.",
          },
          {
            market: "Federal",
            title: "Multi-site facility assessments",
            blurb:
              "As-built reviews across many locations to rank system condition and capital priorities.",
          },
          {
            market: "Corporate",
            title: "Headquarters MEPFT assessment",
            blurb:
              "Field capture of boilers, chillers, distribution, and fire systems for modernization planning.",
          },
        ],
      },
      "point-cloud": {
        category: "Tools",
        title: "Point cloud",
        lead: "Dense existing geometry for accurate routing through tight plenums and historic fabric.",
        projects: [
          {
            market: "Municipal historic",
            title: "Public health building renovation",
            blurb:
              "Plant and hydronic work coordinated through constrained floors while occupied levels stayed live.",
          },
          {
            market: "Higher education",
            title: "Rec center HVAC revisions",
            blurb:
              "Precise routing for humidity control and hybrid cooling through limited ceiling space.",
          },
          {
            market: "Assisted living",
            title: "Pool-to-office adaptive reuse",
            blurb:
              "High-volume space converted to offices with new MEP mapped to measured structure.",
          },
        ],
      },
      "capture-360": {
        category: "Tools",
        title: "360° capture",
        lead: "Visual as-builts for teams who need remote review, CA support, and clear field context.",
        projects: [
          {
            market: "Industrial",
            title: "Process plant commissioning walks",
            blurb:
              "Recurring site observation with documented conditions for controls and QA through startup.",
          },
          {
            market: "Healthcare",
            title: "Life safety documentation",
            blurb:
              "Clinical-area documentation practices that protect air quality while capturing system locations.",
          },
          {
            market: "Municipal",
            title: "Public works garage expansion",
            blurb:
              "Field records supporting oil interceptors, power, and technology pathways for emergency ops.",
          },
        ],
      },
      drones: {
        category: "Tools",
        title: "Drones",
        lead: "Aerial documentation for roofs, plants, and campuses when ladders and lifts are not enough.",
        projects: [
          {
            market: "Healthcare",
            title: "Central plant roof equipment work",
            blurb:
              "Rooftop AHU and plant equipment context for replacement and phasing studies.",
          },
          {
            market: "Municipal",
            title: "Campus-scale facility reviews",
            blurb:
              "Exterior and roof documentation feeding condition assessments and capital planning.",
          },
          {
            market: "Industrial",
            title: "Plant expansion coordination",
            blurb:
              "Site context for utility entrances, equipment yards, and construction logistics.",
          },
        ],
      },
      pe: {
        category: "Credentials",
        title: "PE",
        lead: "Licensed professional engineering leadership on sealed design and construction documents.",
        projects: [
          {
            market: "Healthcare",
            title: "ED and central plant modernization",
            blurb:
              "PE-led mechanical design for chiller plant, custom AHU, steam humidification, and open controls.",
          },
          {
            market: "Public safety",
            title: "New fire station package",
            blurb:
              "Sealed MEP and technology documents through bid, RFI support, and construction administration.",
          },
          {
            market: "Federal clinic",
            title: "Outpatient clinic renovation",
            blurb:
              "Full MEPFT packages meeting agency manuals and state code for clinical fit-out.",
          },
        ],
      },
      leed: {
        category: "Credentials",
        title: "LEED AP",
        lead: "LEED AP BD+C involvement where green strategies and documentation need real systems thinking.",
        projects: [
          {
            market: "Corporate commercial",
            title: "Workplace systems design",
            blurb:
              "HVAC, power, and lighting pathways aligned with high-performance workplace expectations.",
          },
          {
            market: "K-12",
            title: "Geothermal school retrofit",
            blurb:
              "Ground-source heat pumps and open controls aimed at efficiency and long-term operations.",
          },
          {
            market: "Higher education",
            title: "Campus gym humidity upgrade",
            blurb:
              "Energy-conscious cooling and humidification strategies integrated with campus BAS.",
          },
        ],
      },
      bcxp: {
        category: "Credentials",
        title: "BCxP",
        lead: "ASHRAE Building Commissioning Professional leadership for verification and retro-Cx.",
        projects: [
          {
            market: "Industrial",
            title: "Process plant Cx authority",
            blurb:
              "Functional testing, BAS/PLC validation, and recurring field QA through startup.",
          },
          {
            market: "Federal",
            title: "Multi-site facility assessments",
            blurb:
              "BCxP-led reviews of MEP, controls, and fire systems to prioritize deferred maintenance.",
          },
          {
            market: "Specialty",
            title: "Geothermal wellfield retro-Cx",
            blurb:
              "Flow verification and performance comparison against original design for an education building.",
          },
        ],
      },
      rcdd: {
        category: "Credentials",
        title: "RCDD",
        lead: "Registered Communications Distribution Designer depth for cabling and technology pathways.",
        projects: [
          {
            market: "Public safety",
            title: "Fire station structured cabling",
            blurb:
              "Data racks, jacks, pathways, and grounding for a 24/7 response facility.",
          },
          {
            market: "Healthcare clinic",
            title: "Clinic technology room design",
            blurb:
              "Dedicated electrical/data room and structured cabling for medical office fit-out.",
          },
          {
            market: "Municipal",
            title: "Emergency preparedness garage",
            blurb:
              "Fiber, WAP, access control, and camera pathways coordinated with owner IT standards.",
          },
        ],
      },
      ncees: {
        category: "Credentials",
        title: "NCEES",
        lead: "NCEES-supported multi-state PE mobility for projects that cross borders and boards.",
        projects: [
          {
            market: "Food manufacturing",
            title: "Plant office expansion (multi-state)",
            blurb:
              "MEPFT for offices, labs, and cafeteria integrated with live plant utilities.",
          },
          {
            market: "Campgrounds",
            title: "Overnight camp electrical modernization",
            blurb:
              "Utility upgrades, underground distribution, and pathway lighting across a large site.",
          },
          {
            market: "Federal",
            title: "Nationwide facility assessment program",
            blurb:
              "Consistent engineering judgment across many locations and jurisdictions.",
          },
        ],
      },
      green: {
        category: "Sustainability",
        title: "Green building principles",
        lead: "Practical green strategies: efficient systems, healthy air, and operable long-term assets.",
        projects: [
          {
            market: "K-12",
            title: "Geothermal heat-pump modernization",
            blurb:
              "Ground-loop optimization, open BAS, and classroom units designed for efficiency and comfort.",
          },
          {
            market: "K-12 athletics",
            title: "Locker room ERV design",
            blurb:
              "Energy recovery ventilation for moisture-prone spaces with demand-aware control thinking.",
          },
          {
            market: "Municipal",
            title: "Historic plant efficiency upgrade",
            blurb:
              "Condensing boilers, redundant chillers, and MERV filtration for public-health offices.",
          },
        ],
      },
      carbon: {
        category: "Sustainability",
        title: "Lower carbon footprint in design",
        lead: "Lower operating energy and smarter equipment selection without sacrificing reliability.",
        projects: [
          {
            market: "Higher education",
            title: "Hybrid cooling for winter loads",
            blurb:
              "Cooling strategy when campus chilled water is offline, reducing temporary energy waste.",
          },
          {
            market: "K-12",
            title: "Open-protocol geothermal plant",
            blurb:
              "BACnet staging and VFD pumping to match real loads instead of locked proprietary waste.",
          },
          {
            market: "Corporate",
            title: "HQ systems modernization roadmap",
            blurb:
              "Assessment recommendations for boiler/AHU upgrades, LED conversion, and BMS monitoring.",
          },
        ],
      },
    };

    const setActiveBubble = (key) => {
      bubbles.forEach((btn) => {
        const on = btn.getAttribute("data-bubble") === key;
        btn.classList.toggle("is-active", on);
        btn.setAttribute("aria-pressed", on ? "true" : "false");
      });
    };

    const closeExamples = () => {
      examplesPanel.hidden = true;
      setActiveBubble(null);
    };

    const openExamples = (key) => {
      const data = BUBBLE_EXAMPLES[key];
      if (!data || !gridEl || !eyebrowEl || !titleEl || !leadEl) return;

      setActiveBubble(key);
      eyebrowEl.textContent = data.category;
      titleEl.textContent = data.title;
      leadEl.textContent = data.lead;
      gridEl.innerHTML = data.projects
        .map(
          (p) => `
        <article class="example-project">
          <span class="example-project__market">${p.market}</span>
          <h4>${p.title}</h4>
          <p>${p.blurb}</p>
        </article>`
        )
        .join("");

      examplesPanel.hidden = false;
      if (!reduceMotion) {
        examplesPanel.style.animation = "none";
        // reflow to restart animation
        void examplesPanel.offsetWidth;
        examplesPanel.style.animation = "";
      }
      examplesPanel.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "nearest" });
    };

    bubbles.forEach((btn) => {
      btn.addEventListener("click", () => {
        const key = btn.getAttribute("data-bubble");
        if (!key) return;
        if (btn.classList.contains("is-active") && !examplesPanel.hidden) {
          closeExamples();
          return;
        }
        openExamples(key);
      });
    });

    if (closeBtn) {
      closeBtn.addEventListener("click", closeExamples);
    }

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !examplesPanel.hidden) closeExamples();
    });
  }
})();

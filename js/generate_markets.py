# -*- coding: utf-8 -*-
"""Generate SGA ENGINEERS market detail pages."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "markets"
OUT.mkdir(exist_ok=True)

MARKETS = [
    {
        "slug": "healthcare",
        "title": "Healthcare",
        "nav": "Healthcare",
        "meta": "Healthcare MEP engineering, medical gases, infection control systems, and commissioning for hospitals, clinics, and behavioral health.",
        "hero": "Engineering systems that support care, compliance, and continuous operation.",
        "lead": "Healthcare facilities demand precise environmental control, redundant infrastructure, and designs that respect infection prevention, life safety, and renovation in live buildings. SGA brings MEPFT design, medical gas systems, and commissioning experience shaped by clinical performance requirements - not just general commercial practice.",
        "image": "../assets/media/healthcare.jpg",
        "image_alt": "Healthcare facility exterior",
        "intro_title": "Clinical environments. Constructible systems.",
        "intro": [
            "We treat healthcare as a systems problem: patient safety, code density, and operational continuity all depend on mechanical, electrical, plumbing, fire, and technology working as one. That is how we approach hospitals, ambulatory care, specialty clinics, and behavioral health.",
            "Our team designs for clearances, service access, and phasing so facilities can keep running while systems are upgraded. We apply layered infection-control strategies informed by airborne and waterborne disease mitigation experience - primary and secondary measures that protect occupants and staff.",
        ],
        "services_title": "What we do in healthcare",
        "services": [
            "HVAC design for acute care, ORs, procedure rooms, isolation, and critical care environments",
            "Medical gas systems - manifold and central plant - and related plumbing specialty systems",
            "Redundant power, emergency generators, and essential electrical system planning",
            "Nurse call, security, access control, and structured cabling coordination",
            "Fire alarm, suppression, and life-safety interface with clinical operations",
            "Building automation strategies for temperature, humidity, and pressure relationships",
            "Infectious disease mitigation countermeasures in new design and renovations",
            "Commissioning, functional testing, and construction administration in live facilities",
            "Facility condition assessments and infrastructure master planning support",
            "Ligature-resistant fixture and system design for behavioral health settings",
        ],
        "outcomes_title": "How owners and architects benefit",
        "outcomes": [
            ("Code-aware documentation", "Designs that anticipate AHJ review, FGI-informed expectations, and the documentation density healthcare projects require."),
            ("Renovation that respects operations", "Phasing, temporary measures, and constructability so care delivery is not an afterthought to engineering."),
            ("Systems that operate as designed", "BCxP-informed commissioning pathways that verify critical environments perform at turnover - not only on paper."),
        ],
        "related": ["mission-critical", "assisted-living", "commissioning"],
    },
    {
        "slug": "industrial",
        "title": "Industrial",
        "nav": "Industrial",
        "meta": "Industrial MEP engineering for process facilities, specialty exhaust, industrial gases, utilities, and plant infrastructure.",
        "hero": "Plant-ready engineering for process, utility, and production environments.",
        "lead": "Industrial projects reward engineers who understand how systems are installed, maintained, and sequenced around production. SGA designs mechanical, electrical, plumbing, fire, and technology infrastructure for industrial facilities with an eye toward reliability, safety, and real-world constructability.",
        "image": "../assets/media/industrial.jpg",
        "image_alt": "Industrial facility infrastructure",
        "intro_title": "Process-aware building systems",
        "intro": [
            "Industrial work is integrated facility and process support - not a standard office fit-out. We design utilities that serve production, environments that protect product and people, and documentation contractors can build.",
            "Many of our teammates have installation experience. That shows up in clearances, maintenance access, hazardous exhaust strategies, and coordination with structural and process equipment.",
        ],
        "services_title": "What we do in industrial",
        "services": [
            "HVAC and ventilation for production, warehouse, and support spaces",
            "Hazardous exhaust system design and vehicle / noxious gas detection",
            "Industrial gases and specialty process-adjacent utility piping",
            "Central heating and cooling plant design for campus-scale industrial loads",
            "Power distribution, medium-voltage considerations, and equipment grounding",
            "Arc-flash risk assessments and protective device coordination",
            "Fire suppression including ESFR and specialty agent systems where required",
            "BAS integration for plant environments and energy optimization",
            "Temp- and humidity-controlled storage environments",
            "Commissioning, troubleshooting, and facility condition assessments",
        ],
        "outcomes_title": "How owners and partners benefit",
        "outcomes": [
            ("Designs operators can live with", "Serviceability, sequencing, and maintainability baked into the documents - not left for the field to invent."),
            ("Cross-pollination from food and mission-critical", "Lessons from high-reliability and process markets improve redundancy thinking and utility resilience."),
            ("Partner-ready delivery", "Design-bid-build, design-assist, and design-build support aligned to how industrial projects actually procure work."),
        ],
        "related": ["food-manufacturing", "automation", "water-wastewater"],
    },
    {
        "slug": "zoos-aquariums",
        "title": "Zoos & Aquariums",
        "nav": "Zoos & Aquariums",
        "meta": "MEP engineering for zoos and aquariums - specialty environments, public buildings, and resilient utility systems.",
        "hero": "Specialty environments where animal care, public experience, and building systems meet.",
        "lead": "Zoos and aquariums combine public assembly, education, and highly specialized environmental control. SGA supports MEPFT design and commissioning for these unique facilities - balancing guest comfort, staff operations, and the specialized systems animal care depends on.",
        "image": "../assets/media/zoos-aquariums.jpg",
        "image_alt": "Aquarium and aquatic environment",
        "intro_title": "Unique buildings, integrated engineering",
        "intro": [
            "Zoo and aquarium projects demand careful coordination of water, air, power reliability, and life safety with exhibit and operations groups.",
            "We bring full-discipline MEPFT capability, constructible documentation, and close coordination with life-support specialists, architects, and facility staff who know these buildings best.",
        ],
        "services_title": "What we do for zoos & aquariums",
        "services": [
            "Building HVAC for public, education, and back-of-house spaces",
            "Coordination of mechanical and electrical infrastructure supporting exhibit environments",
            "Plumbing, sanitary, and specialty drainage for complex facility programs",
            "Reliable power, emergency systems, and lighting for public and operational areas",
            "Fire protection and life-safety design appropriate to assembly and specialty spaces",
            "Technology systems - security, access control, structured cabling, A/V for education",
            "Commissioning and functional verification of building systems",
            "Renovation and infrastructure upgrades with phased construction awareness",
            "Energy strategies that respect 24/7 operational needs",
            "Construction administration and field coordination support",
        ],
        "outcomes_title": "How teams benefit",
        "outcomes": [
            ("Coordinated, not siloed", "MEPFT under one roof reduces interface gaps between building systems and specialty exhibit requirements."),
            ("Operations-first thinking", "Designs that consider how staff maintain systems around animal care and public hours."),
            ("Trusted partner stance", "Clear communication with owners, architects, and specialty consultants throughout design and CA."),
        ],
        "related": ["hospitality", "education-k12", "higher-education"],
    },
    {
        "slug": "education-k12",
        "title": "K-12 Education",
        "nav": "K-12 Education",
        "meta": "K-12 school MEP engineering - HVAC, power, plumbing, fire, technology, and commissioning for classrooms and campus renovations.",
        "hero": "Healthy, efficient learning environments that districts can afford to operate.",
        "lead": "K-12 projects need durable systems, clear budgets, and designs that work for facility staff long after ribbon-cutting. SGA provides MEPFT design and commissioning for new schools, additions, and renovations - balancing indoor air quality, energy, safety, and constructability.",
        "image": "../assets/media/k-12.jpg",
        "image_alt": "Modern school building",
        "intro_title": "Schools that perform for students and staff",
        "intro": [
            "Learning environments should support wellbeing and long-term performance. We translate that into practical MEPFT: ventilation and thermal comfort, reliable power, safe plumbing, fire protection, and technology infrastructure for modern classrooms.",
            "We understand bond-driven schedules, summer renovation windows, and the need for systems facility teams can service without specialty drama.",
        ],
        "services_title": "What we do for K-12",
        "services": [
            "HVAC design for classrooms, media centers, gyms, cafeterias, and administration",
            "Ventilation and IAQ strategies aligned with modern school expectations",
            "Power distribution, lighting, and lighting controls for learning spaces",
            "Emergency systems and life-safety coordination",
            "Plumbing for restrooms, kitchens, science labs, and athletic facilities",
            "Fire alarm, suppression, and notification systems",
            "Technology pathways - structured cabling, security, access control, paging",
            "Kitchen ventilation and grease-related plumbing where food service is included",
            "Commissioning and energy-conscious design support",
            "Construction administration timed to academic calendars",
        ],
        "outcomes_title": "How districts and architects benefit",
        "outcomes": [
            ("Budget-aware engineering", "Right-sized systems and clear scopes that support competitive bidding and long-term O&M."),
            ("Renovation literacy", "Phasing strategies that protect occupied campuses during upgrades."),
            ("Technology-ready buildings", "Infrastructure that supports security, connectivity, and evolving classroom tools."),
        ],
        "related": ["higher-education", "municipal", "religious"],
    },
    {
        "slug": "department-of-defense",
        "title": "Department of Defense",
        "nav": "Department of Defense",
        "meta": "DoD and federal MEP engineering - compliant design, documentation, coordination, and construction administration for mission facilities.",
        "hero": "Disciplined engineering for mission facilities that demand accountability.",
        "lead": "Department of Defense and federal work requires rigorous documentation, coordination, and respect for security, standards, and schedule. SGA supports MEPFT design and construction administration for facilities where compliance and reliability are non-negotiable.",
        "image": "../assets/media/department-of-defense.jpg",
        "image_alt": "Professional project planning and documentation",
        "intro_title": "Standards-driven delivery",
        "intro": [
            "We treat DoD projects as process-heavy as they are technical: criteria, reviews, and coordination matter as much as the equipment schedule.",
            "Our approach is honest scoping, thorough QA/QC, and engineers who stay engaged through construction - because field issues on mission facilities cannot wait on a handoff.",
        ],
        "services_title": "What we do for DoD and federal facilities",
        "services": [
            "Full MEPFT design for training, administrative, technical, and support facilities",
            "Power reliability, emergency systems, and grounding/bonding design",
            "HVAC for specialized training and technical environments",
            "Plumbing and fire protection coordinated with life-safety criteria",
            "Technology systems - security, access control, structured cabling, communications pathways",
            "BIM coordination and clash-aware documentation",
            "Construction administration: RFIs, submittals, site visits, and schedule coordination",
            "Commissioning support and functional performance verification",
            "Facility condition assessments and renovation planning",
            "Quality checkpoints from design through closeout",
        ],
        "outcomes_title": "How clients benefit",
        "outcomes": [
            ("Documentation discipline", "Clear packages that stand up to review cycles and contractor scrutiny."),
            ("Continuity of staff", "The team you meet remains accountable through design and CA."),
            ("Cross-market readiness", "Experience across technical training, healthcare-adjacent, and industrial-type facilities strengthens DoD delivery."),
        ],
        "related": ["mission-critical", "higher-education", "transportation"],
    },
    {
        "slug": "commissioning",
        "title": "Commissioning",
        "nav": "Commissioning",
        "meta": "Building commissioning services - BCxP-informed Cx, functional testing, energy optimization, FCAs, and digital documentation.",
        "hero": "Verify performance. Reduce risk. Close the gap between design intent and operation.",
        "lead": "Commissioning is how owners gain confidence that systems work as intended. SGA provides commissioning and related services led with BCxP credentials - across design-phase planning, construction, functional testing, and ongoing optimization.",
        "image": "../assets/media/commissioning.jpg",
        "image_alt": "Engineer reviewing building systems",
        "intro_title": "Commissioning with design fluency",
        "intro": [
            "We treat commissioning as a thread through the project - not a punch-list afterthought. Because we also design MEPFT systems, our Cx perspective is grounded in how buildings are actually engineered and built.",
            "We support owners, architects, and contractors who need independent rigor, clear issues logs, and functional tests that mean something on day one of occupancy.",
        ],
        "services_title": "What we do in commissioning",
        "services": [
            "Pre-design and design-phase commissioning planning",
            "BIM-era design reviews focused on operability and maintainability",
            "Construction-phase commissioning and issues tracking",
            "Functional testing and performance verification",
            "Training support, documentation, and digital twin-oriented deliverables",
            "Energy management and optimization strategies",
            "Troubleshooting and diagnostics for underperforming systems",
            "Energy modeling and audit support",
            "Facility condition assessments",
            "Expert witness and forensic engineering services",
            "Infectious disease mitigation assessments related to building systems",
            "Master planning and programming support for systems performance",
        ],
        "outcomes_title": "How owners benefit",
        "outcomes": [
            ("Risk reduction at turnover", "Catch integration issues before they become warranty noise and occupant complaints."),
            ("Credentialed leadership", "BCxP (ASHRAE) informs process quality and industry-aligned methods."),
            ("Design and Cx synergy", "Whether we designed the systems or commission another team's work, we speak fluent MEPFT."),
        ],
        "related": ["healthcare", "mission-critical", "corporate-commercial"],
    },
    {
        "slug": "hospitality",
        "title": "Hospitality",
        "nav": "Hospitality",
        "meta": "Hospitality MEP engineering for hotels, resorts, and guest-experience facilities - comfort, reliability, and efficient operations.",
        "hero": "Guest comfort and operational efficiency, engineered to work together.",
        "lead": "Hospitality projects live or die on guest experience and operating cost. SGA designs mechanical, electrical, plumbing, fire, and technology systems that support comfort, brand standards, and maintainable back-of-house operations.",
        "image": "../assets/media/hospitality.jpg",
        "image_alt": "Hospitality and hotel environment",
        "intro_title": "Front-of-house feel, back-of-house rigor",
        "intro": [
            "Hospitality engineering balances design coordination with utility performance: quiet HVAC, reliable domestic hot water, robust kitchens, and life safety that disappears into the guest journey.",
            "We design systems owners can operate across shifts - service access, controls strategies, and documentation that facility teams can use.",
        ],
        "services_title": "What we do in hospitality",
        "services": [
            "Guest-room and public-space HVAC with comfort and acoustics in mind",
            "Central plants and domestic hot water systems for high occupancy",
            "Kitchen ventilation, grease management, and food-service plumbing",
            "Power distribution, emergency systems, and efficient lighting/controls",
            "Fire alarm, suppression, and life-safety for assembly and residential-style occupancies",
            "Technology - access control, security, structured cabling, A/V, and guest-experience pathways",
            "Pool, spa, and amenity-adjacent mechanical/plumbing coordination",
            "Renovation of occupied properties with phasing awareness",
            "Energy strategies that protect OPEX without sacrificing comfort",
            "Commissioning and CA through opening",
        ],
        "outcomes_title": "How owners benefit",
        "outcomes": [
            ("Comfort that holds under load", "Systems designed for real occupancy peaks - not brochure conditions only."),
            ("Serviceable BOH", "Equipment locations and clearances that keep maintenance off the guest path."),
            ("Integrated low-voltage", "Security and communications planned with power and life-safety - not added late."),
        ],
        "related": ["retail", "corporate-commercial", "food-manufacturing"],
    },
    {
        "slug": "food-manufacturing",
        "title": "Food Manufacturing",
        "nav": "Food Manufacturing",
        "meta": "Food manufacturing MEP engineering - process utilities, hygiene-aware environments, ammonia plants, and production infrastructure.",
        "hero": "Production environments where hygiene, utilities, and uptime are non-negotiable.",
        "lead": "Food and beverage manufacturing requires disciplined environmental control, process-adjacent utilities, and robust infrastructure. SGA provides MEPFT design for food manufacturing facilities - including specialty systems such as ammonia chilled water plants, industrial gases, and temperature-controlled storage.",
        "image": "../assets/media/food-manufacturing.jpg",
        "image_alt": "Manufacturing and production facility",
        "intro_title": "Process-informed building engineering",
        "intro": [
            "Food plants are living systems: washdown, temperature zones, refrigeration, and electrical reliability all affect product safety and throughput. We engineer building systems that respect those realities.",
            "From packaging areas to cold storage and central utilities, we coordinate for constructability and long-term service - because downtime is measured in more than inconvenience.",
        ],
        "services_title": "What we do in food manufacturing",
        "services": [
            "HVAC and ventilation strategies for production and support spaces",
            "Ammonia chilled water plant design and industrial refrigeration interfaces",
            "Temp- and humidity-controlled storage environments",
            "Industrial gases and specialty utility piping",
            "Power systems sized and coordinated for process equipment loads",
            "Arc-flash studies and electrical safety documentation",
            "Plumbing, process drains, interceptors, and chemical containment as applicable",
            "Fire protection including ESFR and specialty approaches for storage/production",
            "BAS and controls integration for plant performance",
            "Commissioning, troubleshooting, and facility assessments",
        ],
        "outcomes_title": "How processors benefit",
        "outcomes": [
            ("Utility reliability", "Infrastructure planned around production criticality and maintainability."),
            ("Safety-aware electrical", "Studies and designs that support safer operations around industrial power."),
            ("Field-informed details", "Installation experience shows up in clearances, sequencing, and realistic details."),
        ],
        "related": ["industrial", "automation", "water-wastewater"],
    },
    {
        "slug": "municipal",
        "title": "Municipal",
        "nav": "Municipal",
        "meta": "Municipal MEP engineering for civic buildings, public facilities, and community infrastructure projects.",
        "hero": "Public facilities engineered for durability, accessibility, and long service life.",
        "lead": "Municipal projects serve communities for decades. SGA designs MEPFT systems for civic and public facilities with durable, maintainable solutions - and clear documentation for public procurement and construction.",
        "image": "../assets/media/municipal.jpg",
        "image_alt": "Civic and public architecture",
        "intro_title": "Stewardship-minded engineering",
        "intro": [
            "Public-sector work demands lifecycle value, transparent process, and systems that public works teams can operate. We bring that mindset to municipal buildings and related facilities.",
            "Whether renovation or new construction, we focus on serviceability, energy stewardship, and coordination that reduces change-order risk on publicly bid work.",
        ],
        "services_title": "What we do for municipal clients",
        "services": [
            "MEPFT design for civic buildings, public safety support spaces, and community facilities",
            "HVAC and controls strategies suited to intermittent and continuous occupancy patterns",
            "Power, emergency systems, and efficient lighting/controls",
            "Plumbing, storm, and specialty drainage as program requires",
            "Fire protection and life-safety design for public occupancy",
            "Technology infrastructure - security, access, cabling, public A/V pathways",
            "Facility condition assessments to prioritize capital planning",
            "Energy audits and improvement strategies",
            "Commissioning for public project accountability",
            "Construction administration through closeout",
        ],
        "outcomes_title": "How municipalities benefit",
        "outcomes": [
            ("Bid-ready documents", "Clear scopes that support fair public bidding and fewer RFIs born of ambiguity."),
            ("Maintainable systems", "Equipment choices and layouts public facility staff can support."),
            ("Capital clarity", "Assessments and designs that help leaders sequence investments wisely."),
        ],
        "related": ["water-wastewater", "education-k12", "transportation"],
    },
    {
        "slug": "corporate-commercial",
        "title": "Corporate Commercial",
        "nav": "Corporate Commercial",
        "meta": "Commercial office and corporate MEP engineering - fit-outs, renovations, core systems, and workplace technology infrastructure.",
        "hero": "Workplaces engineered for performance, flexibility, and total cost of ownership.",
        "lead": "Corporate and commercial projects need efficient cores, comfortable interiors, and infrastructure that adapts as tenants and work patterns change. SGA delivers MEPFT design for offices, corporate facilities, and commercial renovations.",
        "image": "../assets/media/corporate-commercial.jpg",
        "image_alt": "Modern commercial office interior",
        "intro_title": "Core and shell to fit-out - done with precision",
        "intro": [
            "Commercial buildings succeed when systems support human performance and operational efficiency. We engineer HVAC, power, plumbing, fire, and technology pathways that meet modern workplace standards.",
            "From modest renovations to multi-floor fit-outs, you get senior-aware delivery and constructible documents - not a handoff after the fee is won.",
        ],
        "services_title": "What we do in corporate commercial",
        "services": [
            "HVAC design and zoning for offices, conference, and amenity spaces",
            "Building automation and comfort/energy optimization strategies",
            "Power distribution, lighting, and lighting controls",
            "Emergency power where program requires",
            "Plumbing for restrooms, pantries, fitness, and specialty amenities",
            "Fire alarm and suppression coordination with base building systems",
            "Structured cabling, security, access control, and A/V infrastructure",
            "Restack and renovation design in occupied buildings",
            "LEED-oriented design support with LEED AP involvement on the team",
            "Commissioning and CA for smoother turnover to facilities teams",
        ],
        "outcomes_title": "How owners and tenants benefit",
        "outcomes": [
            ("Flexible infrastructure", "Pathways and capacities planned for change without constant gut-and-replace."),
            ("Comfort and efficiency", "Systems tuned for real workplace loads and energy goals."),
            ("Cleaner coordination", "BIM-capable design that reduces trade conflicts before they hit the field."),
        ],
        "related": ["retail", "mission-critical", "commissioning"],
    },
    {
        "slug": "automation",
        "title": "Automation",
        "nav": "Automation",
        "meta": "Automation and controls-oriented MEP engineering - BAS integration, industrial controls interfaces, and facility automation infrastructure.",
        "hero": "Controls-aware engineering that makes buildings and processes operable.",
        "lead": "Automation is where design intent becomes daily operation. SGA supports building automation system design and integration, controls coordination, and the electrical/mechanical infrastructure automation depends on - across commercial, industrial, and specialty facilities.",
        "image": "../assets/media/automation.jpg",
        "image_alt": "Technology and automation systems",
        "intro_title": "From sequences to systems that run",
        "intro": [
            "Controls are not an add-on. We design with BAS, monitoring, and operational logic in mind - so startups are smoother and facilities teams inherit something usable.",
            "Whether the priority is comfort, energy, or process-adjacent reliability, we coordinate mechanical, electrical, and technology scopes around how the building will actually be controlled.",
        ],
        "services_title": "What we do in automation",
        "services": [
            "Building automation system (BAS) design and integration planning",
            "Controls strategies for HVAC plants, terminals, and critical environments",
            "Electrical infrastructure for controls, network, and powered devices",
            "Coordination of meters, sensors, and monitoring points",
            "Integration pathways for security, lighting controls, and specialty systems",
            "Support for industrial and process facility control environments",
            "Commissioning of control sequences and functional performance",
            "Troubleshooting underperforming automation implementations",
            "Documentation and training-oriented deliverables for operators",
            "Energy management and optimization through controls",
        ],
        "outcomes_title": "How clients benefit",
        "outcomes": [
            ("Operable day one", "Sequences and points lists that support meaningful functional tests."),
            ("Fewer orphan systems", "MEP and technology coordinated so controls are not left to chance."),
            ("Optimization ready", "Foundations for energy and performance improvement after occupancy."),
        ],
        "related": ["industrial", "mission-critical", "commissioning"],
    },
    {
        "slug": "water-wastewater",
        "title": "Water & Wastewater",
        "nav": "Water & Wastewater",
        "meta": "Water and wastewater facility MEP engineering - plant utilities, controls, power reliability, and support systems.",
        "hero": "Critical infrastructure engineering for water and wastewater facilities.",
        "lead": "Water and wastewater plants are 24/7 infrastructure. SGA supports mechanical, electrical, plumbing, fire, technology, and controls design for treatment and related facilities - where reliability, harsh environments, and operational continuity shape every decision.",
        "image": "../assets/media/wastewater.jpg",
        "image_alt": "Industrial water infrastructure",
        "intro_title": "Utility-class rigor",
        "intro": [
            "Water and wastewater facilities are mission systems. We bring MEPFT and automation experience suited to plant buildings, process support spaces, and electrical/controls reliability.",
            "Our industrial and municipal cross-training helps when projects combine process constraints with building code and life-safety requirements.",
        ],
        "services_title": "What we do in water & wastewater",
        "services": [
            "Electrical power distribution and reliability planning for plant environments",
            "Emergency power and critical load strategies",
            "HVAC and ventilation for process buildings and occupied support spaces",
            "Plumbing and specialty drainage coordination",
            "Fire protection appropriate to plant occupancy and hazard classifications",
            "Controls and automation infrastructure support",
            "Lighting, grounding, and electrical safety studies",
            "Technology and SCADA-adjacent pathway coordination with process teams",
            "Facility assessments and upgrade design for aging plants",
            "Construction administration in active facility conditions",
        ],
        "outcomes_title": "How utilities benefit",
        "outcomes": [
            ("Uptime mindset", "Designs that respect continuous operations and outage windows."),
            ("Harsh-environment practicality", "Material and layout decisions informed by real plant conditions."),
            ("Clear interfaces", "Coordination with process disciplines so building systems support treatment goals."),
        ],
        "related": ["municipal", "industrial", "automation"],
    },
    {
        "slug": "mission-critical",
        "title": "Mission Critical",
        "nav": "Mission Critical",
        "meta": "Mission critical MEP engineering - data centers, high-reliability power and cooling, UPS, redundancy, and commissioning.",
        "hero": "Reliability engineered for environments where downtime is not an option.",
        "lead": "Mission-critical facilities demand layered redundancy, meticulous coordination, and commissioning that proves performance. SGA designs power, cooling, fire, and technology infrastructure for high-reliability environments - and brings cross-market lessons from healthcare and industrial work into every decision.",
        "image": "../assets/media/data-center.jpg",
        "image_alt": "Data center and mission critical infrastructure",
        "intro_title": "Redundancy with constructability",
        "intro": [
            "Data centers and critical facilities are performance machines: concurrent maintainability, thermal strategy, and electrical topology must be right. We engineer those systems with field realism - so redundancy is installable and serviceable, not just diagrammed.",
            "We also design data center spaces and MDF/IDF environments as part of broader technology capability - because critical power without clean IT infrastructure is only half the job.",
        ],
        "services_title": "What we do in mission critical",
        "services": [
            "Critical power distribution, UPS, and generator system design",
            "Cooling strategies for high-density and high-reliability spaces",
            "Redundancy planning and concurrent maintainability thinking",
            "Fire protection including preaction and clean-agent approaches where appropriate",
            "Grounding, bonding, and electrical studies (including arc-flash)",
            "Data center design support and main/intermediate distribution frame design",
            "Structured cabling and cable management systems",
            "BAS and monitoring coordination for critical environments",
            "Commissioning and functional testing of critical systems",
            "Cutover-aware construction administration",
        ],
        "outcomes_title": "How operators benefit",
        "outcomes": [
            ("Reliability by design", "Topologies and capacities aligned to uptime goals and maintenance reality."),
            ("Integrated MEP and technology", "Power, cooling, fire, and IT infrastructure coordinated early."),
            ("Verified performance", "Cx pathways that test what matters before the facility goes live."),
        ],
        "related": ["healthcare", "corporate-commercial", "commissioning"],
    },
    {
        "slug": "retail",
        "title": "Retail",
        "nav": "Retail",
        "meta": "Retail MEP engineering for stores, mixed-use retail, and customer-facing facilities - fast schedules and reliable systems.",
        "hero": "Retail environments engineered for brand, comfort, and speed to open.",
        "lead": "Retail projects move quickly and must perform for customers and operators alike. SGA provides MEPFT design for retail and mixed-use commercial spaces - efficient systems, clear documentation, and technology infrastructure that supports modern store operations.",
        "image": "../assets/media/retail.jpg",
        "image_alt": "Retail and commercial storefront environment",
        "intro_title": "Fast, clean, operable",
        "intro": [
            "Retail engineering at scale prioritizes repeatable quality and schedule. We deliver constructible MEPFT packages that help teams hit opening dates without sacrificing life safety or maintainability.",
            "Whether a single flagship renovation or a standard prototype adaptation, we coordinate with architects and brand requirements while protecting the engineering fundamentals.",
        ],
        "services_title": "What we do in retail",
        "services": [
            "HVAC for sales floors, stockrooms, and back-of-house",
            "Lighting power and controls coordination with brand design",
            "Power distribution for retail equipment and flexible merchandising",
            "Plumbing for restrooms, food service tenants, and specialty uses",
            "Fire protection and alarm systems for mercantile occupancies",
            "Security, access control, and structured cabling",
            "Food-service retail support (kitchen ventilation, grease, etc.) where needed",
            "Tenant fit-out and base-building coordination",
            "Energy-conscious design for long-term operating cost",
            "CA support through punch and opening",
        ],
        "outcomes_title": "How retailers benefit",
        "outcomes": [
            ("Schedule sensitivity", "Responsive engineering that keeps pace with retail delivery."),
            ("Customer comfort", "Thermal and IAQ strategies that support dwell time and staff performance."),
            ("Clean interfaces", "Clear delineation with base building and other trades reduces field conflict."),
        ],
        "related": ["corporate-commercial", "hospitality", "ev-infrastructure"],
    },
    {
        "slug": "ev-infrastructure",
        "title": "EV Infrastructure",
        "nav": "EV Infrastructure",
        "meta": "EV charging infrastructure engineering - load studies, electrical design, site power planning, and future-ready distribution.",
        "hero": "Charging infrastructure designed for real electrical capacity - not wishful load letters.",
        "lead": "Electric vehicle infrastructure succeeds when electrical engineering is done early and honestly. SGA provides EV charging studies and design, distribution planning, and coordination with site and facility power systems so charging deployments are safe, code-compliant, and expandable.",
        "image": "../assets/media/electric-vehicle.jpg",
        "image_alt": "Electric vehicle charging infrastructure",
        "intro_title": "Power-first EV planning",
        "intro": [
            "As fleets and workplaces electrify, utility coordination and distribution design become the critical path. We focus on the electrical truth of each site: available capacity, transformer strategy, feeders, protection, and future expansion.",
            "We integrate EV infrastructure with broader facility electrical systems - grounds, lighting, technology pathways, and life-safety interfaces - so charging is part of a coherent site design.",
        ],
        "services_title": "What we do for EV infrastructure",
        "services": [
            "Electric vehicle charging studies and load assessments",
            "EVSE electrical design for workplace, fleet, retail, and campus sites",
            "Service and distribution upgrades to support charging loads",
            "Panel, feeder, and protection design for charger arrays",
            "Grounding and bonding for charging installations",
            "Coordination with utility requirements and site civil/electrical interfaces",
            "Lighting and safety power for charging areas",
            "Future-ready conduit and capacity planning for phased build-out",
            "Integration with existing emergency and life-safety systems as required",
            "Construction administration for charging deployments",
        ],
        "outcomes_title": "How owners benefit",
        "outcomes": [
            ("No surprise capacity gaps", "Studies that reveal constraints before equipment is ordered."),
            ("Expandable layouts", "Designs that allow phased charger growth without rework chaos."),
            ("Code-compliant safety", "Protection, grounding, and installation details that stand up to inspection."),
        ],
        "related": ["corporate-commercial", "retail", "transportation"],
    },
    {
        "slug": "higher-education",
        "title": "Higher Education",
        "nav": "Higher Education",
        "meta": "Higher education MEP engineering for campuses - labs, classrooms, residence life, central plants, and research-adjacent facilities.",
        "hero": "Campus systems that support teaching, research, and student life.",
        "lead": "Higher education facilities range from classrooms to labs to residence halls - each with different performance demands. SGA provides MEPFT design and commissioning for campus projects, coordinating complex programs with energy, reliability, and maintainability in mind.",
        "image": "../assets/media/higher-ed.jpg",
        "image_alt": "University campus building",
        "intro_title": "Campus complexity, clear engineering",
        "intro": [
            "Universities are living systems: central plants, diverse building types, and long capital horizons. We engineer building systems that fit campus standards, utility realities, and the need to renovate without shutting down student life.",
            "Cross-training from healthcare, labs-adjacent environments, and mission-critical work strengthens our approach to higher-ed technical facilities.",
        ],
        "services_title": "What we do in higher education",
        "services": [
            "MEPFT for academic buildings, student life, and administrative facilities",
            "Lab and technical space support: specialized exhaust, gases, and environmental control",
            "Central plant interfaces and building-level HVAC strategies",
            "Power reliability for research and critical campus functions",
            "Plumbing, medical/lab gas coordination, and specialty drainage",
            "Fire protection tailored to assembly, residential, and lab occupancies",
            "Technology infrastructure for classrooms, security, and campus networks",
            "Energy modeling support and high-performance design principles",
            "Commissioning for complex campus buildings",
            "Phased renovations in occupied academic environments",
        ],
        "outcomes_title": "How campuses benefit",
        "outcomes": [
            ("Program-ready systems", "Engineering that matches pedagogy and research needs - not generic office HVAC with a new name."),
            ("Lifecycle value", "Maintainable designs aligned with campus facilities operations."),
            ("Integrated low-voltage", "Security, A/V, and data pathways planned with power and mechanical from the start."),
        ],
        "related": ["education-k12", "healthcare", "mission-critical"],
    },
    {
        "slug": "transportation",
        "title": "Transportation",
        "nav": "Transportation",
        "meta": "Transportation facility MEP engineering - terminals, transit support, fleet facilities, and public infrastructure buildings.",
        "hero": "Systems for facilities that keep people and fleets moving.",
        "lead": "Transportation facilities combine public occupancy, operational intensity, and infrastructure durability. SGA supports MEPFT design for transportation-related buildings and support facilities - power, HVAC, plumbing, fire, and technology that stand up to heavy use.",
        "image": "../assets/media/transportation.jpg",
        "image_alt": "Transportation and transit infrastructure",
        "intro_title": "Operational buildings, public standards",
        "intro": [
            "Transportation facilities demand continuous operations, passenger experience, and maintainability. We engineer building systems for terminals, support buildings, and fleet-related facilities with that operational lens.",
            "Where EV fleet charging or industrial-type maintenance spaces are part of the program, our electrical and industrial experience becomes a direct advantage.",
        ],
        "services_title": "What we do in transportation",
        "services": [
            "HVAC for terminals, offices, and operational support spaces",
            "Power distribution for facilities and equipment-intensive areas",
            "Emergency systems and life-safety for public occupancies",
            "Plumbing and specialty drainage for high-traffic facilities",
            "Fire alarm, suppression, and notification systems",
            "Technology - security, access control, communications pathways, A/V",
            "Vehicle-related ventilation and detection where maintenance is present",
            "EV charging infrastructure for fleet and public programs",
            "Facility assessments and renovation design",
            "Construction administration in active operational environments",
        ],
        "outcomes_title": "How agencies and owners benefit",
        "outcomes": [
            ("Operations continuity", "Phasing and system strategies that respect 24/7 transportation missions."),
            ("Public-ready life safety", "Fire and egress systems engineered for assembly and transit use."),
            ("Future mobility readiness", "Electrical planning that can grow with electrification."),
        ],
        "related": ["ev-infrastructure", "municipal", "department-of-defense"],
    },
    {
        "slug": "campgrounds",
        "title": "Campgrounds",
        "nav": "Campgrounds",
        "meta": "Campground and outdoor hospitality MEP engineering - site utilities, power, plumbing, comfort stations, and support buildings.",
        "hero": "Outdoor hospitality infrastructure engineered for seasonal peaks and simple operations.",
        "lead": "Campgrounds and outdoor hospitality sites need practical power, water, wastewater interfaces, and support buildings that work for guests and staff. SGA designs MEP systems for campground facilities - balancing code compliance, durability, and cost-effective operation.",
        "image": "../assets/media/campground.jpg",
        "image_alt": "Campground and outdoor hospitality setting",
        "intro_title": "Rugged, simple, code-solid",
        "intro": [
            "Outdoor hospitality sits at the intersection of site utilities and small-building engineering. We bring commercial MEP fundamentals to comfort stations, offices, stores, and power distribution for sites - without overcomplicating what should be maintainable by lean operations teams.",
            "Experience with hospitality, retail support buildings, and EV/site power planning informs modern campground upgrades.",
        ],
        "services_title": "What we do for campgrounds",
        "services": [
            "Power distribution for sites, buildings, and amenities",
            "Electrical design for bathhouses, offices, stores, and pavilions",
            "Plumbing for comfort stations and support facilities",
            "HVAC for conditioned buildings on site",
            "Fire protection strategies appropriate to building types",
            "Lighting for safety and wayfinding",
            "Technology pathways for office, security, and guest services",
            "EV charging readiness for modern outdoor hospitality",
            "Renovation and upgrade design for aging park facilities",
            "Practical documentation for contractors and park staff",
        ],
        "outcomes_title": "How operators benefit",
        "outcomes": [
            ("Peak-season reliability", "Systems planned for occupancy swings and outdoor conditions."),
            ("Maintainable simplicity", "Designs park staff can understand and service."),
            ("Guest experience basics", "Hot water, power, lighting, and comfort that just work."),
        ],
        "related": ["hospitality", "retail", "religious"],
    },
    {
        "slug": "religious",
        "title": "Religious",
        "nav": "Religious",
        "meta": "Religious facility MEP engineering - worship spaces, education wings, assembly occupancy, and multi-use campus buildings.",
        "hero": "Gathering spaces engineered for comfort, life safety, and community use.",
        "lead": "Religious facilities are assembly spaces, classrooms, kitchens, and community centers - often all at once. SGA designs MEPFT systems for houses of worship and related facilities that support large gatherings, flexible programming, and long-term stewardship of building resources.",
        "image": "../assets/media/faith.jpg",
        "image_alt": "Religious and community gathering architecture",
        "intro_title": "Multi-use buildings, careful systems",
        "intro": [
            "Worship and community facilities need acoustic-sensitive HVAC, robust life safety, and systems that serve intermittent peak loads. We engineer those systems with respect for budget stewardship and volunteer or lean facilities operations.",
            "Our education and hospitality experience helps when campuses include schools, fellowship halls, and commercial-style kitchens.",
        ],
        "services_title": "What we do for religious facilities",
        "services": [
            "HVAC for sanctuaries, fellowship halls, classrooms, and offices",
            "Ventilation and comfort strategies for intermittent high occupancy",
            "Power, lighting, and controls for worship and multi-use spaces",
            "Plumbing for restrooms, kitchens, and specialty fixtures as applicable",
            "Fire alarm, suppression, and life-safety for assembly occupancies",
            "A/V infrastructure pathways, structured cabling, and security/access control",
            "Kitchen ventilation and food-service plumbing for community meals",
            "Additions and renovations that respect occupied ministry schedules",
            "Energy upgrades and system replacements for aging campuses",
            "Commissioning and CA for smoother openings",
        ],
        "outcomes_title": "How congregations benefit",
        "outcomes": [
            ("Comfort during peak gatherings", "Systems sized and zoned for real sanctuary and event loads."),
            ("Life-safety clarity", "Assembly occupancy requirements addressed cleanly in design."),
            ("Stewardship", "Durable, serviceable designs that protect long-term operating budgets."),
        ],
        "related": ["education-k12", "hospitality", "corporate-commercial"],
    },
    {
        "slug": "assisted-living",
        "title": "Assisted Living",
        "nav": "Assisted Living",
        "meta": "Assisted living and senior living MEP engineering - resident comfort, life safety, healthcare-adjacent systems, and reliable operations.",
        "hero": "Resident-centered environments with healthcare-informed building systems.",
        "lead": "Assisted living and senior living facilities blend residential comfort with care-driven reliability. SGA designs MEPFT systems that support resident wellbeing, staff operations, and life safety - drawing on healthcare experience where clinical adjacency and infection control matter.",
        "image": "../assets/media/assisted-living.jpg",
        "image_alt": "Senior living and care environment",
        "intro_title": "Care environments without institutional harshness",
        "intro": [
            "Senior living engineering balances hospitality comfort with care standards: domestic hot water reliability, nurse call/technology, HVAC comfort, and life safety.",
            "We design for continuous occupancy renovations, clear service access, and systems that facilities teams can run without constant crisis.",
        ],
        "services_title": "What we do in assisted living",
        "services": [
            "HVAC for resident rooms, dining, activity, and care support spaces",
            "Domestic hot water systems designed for high, continuous demand",
            "Plumbing with accessibility and care-program requirements in mind",
            "Power, emergency systems, and lighting for resident safety",
            "Fire alarm, suppression, and notification for residential care occupancies",
            "Nurse call, security, access control, and structured cabling",
            "Kitchen and food-service mechanical/plumbing support",
            "Infection-control-informed design strategies where program requires",
            "Phased renovations in occupied communities",
            "Commissioning and turnover support for operators",
        ],
        "outcomes_title": "How operators benefit",
        "outcomes": [
            ("Resident comfort and safety", "Environmental systems and life safety that support quality of life."),
            ("Staff-efficient buildings", "Technology and layouts that reduce friction in daily care operations."),
            ("Healthcare fluency", "Lessons from clinical environments applied where care acuity is rising."),
        ],
        "related": ["healthcare", "hospitality", "commissioning"],
    },
]

TITLE_BY_SLUG = {m["slug"]: m["nav"] for m in MARKETS}

ARROW = (
    '<svg viewBox="0 0 16 16" fill="none" aria-hidden="true">'
    '<path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5"/>'
    "</svg>"
)


def render(m: dict) -> str:
    services = "\n".join(f"              <li>{s}</li>" for s in m["services"])
    intro = "\n".join(f"                <p>{p}</p>" for p in m["intro"])
    outcomes = "\n".join(
        f"""            <article class="outcome-item reveal">
              <span class="outcome-item__icon" aria-hidden="true">✓</span>
              <div>
                <h3>{h}</h3>
                <p>{p}</p>
              </div>
            </article>"""
        for h, p in m["outcomes"]
    )
    related = "\n".join(
        f'            <a class="market-chip" href="{slug}.html">{TITLE_BY_SLUG[slug]} {ARROW}</a>'
        for slug in m["related"]
    )
    all_markets = "\n".join(
        f'            <a class="market-chip{" is-active" if x["slug"] == m["slug"] else ""}" href="{x["slug"]}.html">{x["nav"]}</a>'
        for x in MARKETS
    )
    title_lower = m["title"].lower()

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{m["title"]} MEP Engineering | SGA ENGINEERS</title>
    <meta name="description" content="{m["meta"]}" />
    <link rel="stylesheet" href="../css/styles.css" />
  </head>
  <body>
    <header class="site-header is-solid">
      <div class="container nav">
        <a class="logo" href="../index.html" aria-label="SGA ENGINEERS home">
          <img class="logo-img" src="../assets/logo/logo-primary-invert.png" alt="SGA ENGINEERS" width="220" height="64" />
        </a>
        <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false">
          <span></span>
        </button>
        <nav class="nav-links" aria-label="Primary">
          <a class="nav-link" href="../expertise.html">Expertise</a>
          <a class="nav-link is-active" href="../markets.html">Markets</a>
          <a class="nav-link" href="../projects.html">Selected Work</a>
          <a class="nav-link" href="../about.html">Why SGA</a>
          <a class="nav-link" href="../careers.html">Careers</a>
          <a class="btn btn--primary nav-cta" href="../contact.html">Contact</a>
        </nav>
      </div>
    </header>

    <main>
      <section class="page-hero">
        <div class="container">
          <p class="eyebrow"><a href="../markets.html" style="color: inherit">Markets</a> / {m["nav"]}</p>
          <h1>{m["hero"]}</h1>
          <p>{m["lead"]}</p>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="split reveal">
            <div class="split__body">
              <p class="eyebrow">{m["title"]}</p>
              <h2 class="section-title">{m["intro_title"]}</h2>
              <div class="prose">
{intro}
              </div>
              <div class="split__actions">
                <a class="btn btn--primary" href="../contact.html">Discuss a project</a>
                <a class="btn btn--ghost" href="../expertise.html">View expertise</a>
              </div>
            </div>
            <div class="split__media split__media--wide">
              <img src="{m["image"]}" alt="{m["image_alt"]}" width="1600" height="1200" loading="lazy" />
            </div>
          </div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          <div class="section-head reveal">
            <div>
              <p class="eyebrow">Capabilities</p>
              <h2 class="section-title">{m["services_title"]}</h2>
              <p class="section-lead">
                Full-discipline mechanical, electrical, plumbing, fire, technology, and commissioning
                services tailored to {title_lower} project realities.
              </p>
            </div>
          </div>
          <ul class="capability-list reveal market-services">
{services}
          </ul>
        </div>
      </section>

      <section class="section">
        <div class="container">
          <div class="section-head reveal">
            <div>
              <p class="eyebrow">Why SGA</p>
              <h2 class="section-title">{m["outcomes_title"]}</h2>
            </div>
          </div>
          <div class="outcome-grid">
{outcomes}
          </div>
        </div>
      </section>

      <section class="section section--soft">
        <div class="container">
          <div class="section-head reveal">
            <div>
              <p class="eyebrow">Related markets</p>
              <h2 class="section-title">Cross-market fluency</h2>
            </div>
            <a class="btn btn--ghost" href="../markets.html">All markets →</a>
          </div>
          <div class="markets-grid reveal">
{related}
          </div>
        </div>
      </section>

      <section class="section section--ink section--tight">
        <div class="container">
          <div class="section-head reveal">
            <div>
              <p class="eyebrow">Browse</p>
              <h2 class="section-title">All markets</h2>
            </div>
          </div>
          <div class="markets-grid reveal">
{all_markets}
          </div>
        </div>
      </section>

      <section class="cta-strip">
        <div class="container reveal">
          <div>
            <h2>Planning a {title_lower} project?</h2>
            <p>
              Share program, schedule, and delivery method - we’ll respond as working engineers with a
              clear read on how SGA can help.
            </p>
          </div>
          <a class="btn btn--white" href="../contact.html">Contact the team →</a>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <a class="logo" href="../index.html" aria-label="SGA ENGINEERS home">
              <img class="logo-img" src="../assets/logo/logo-primary-invert.png" alt="SGA ENGINEERS" width="220" height="64" />
            </a>
            <p>
              Licensed MEPFT engineering, commissioning, and construction administration for
              owners, architects, and project partners who value precision and integrity.
            </p>
          </div>
          <div class="footer-col">
            <h4>Firm</h4>
            <a href="../about.html">Why SGA</a>
            <a href="../expertise.html">Expertise</a>
            <a href="../markets.html">Markets</a>
            <a href="../projects.html">Selected Work</a>
            <a href="../careers.html">Careers</a>
          </div>
          <div class="footer-col">
            <h4>Services</h4>
            <a href="../expertise.html#mechanical">Mechanical</a>
            <a href="../expertise.html#electrical">Electrical</a>
            <a href="../expertise.html#commissioning">Commissioning</a>
            <a href="../expertise.html#technology">Technology</a>
          </div>
          <div class="footer-col">
            <h4>Contact</h4>
            <a href="mailto:engineer@sgaengineers.com">engineer@sgaengineers.com</a>
            <a href="mailto:info@sgaengineers.com">info@sgaengineers.com</a>
            <a href="../contact.html">Project inquiry</a>
          </div>
        </div>
        <div class="footer-bottom">
          <span>© <span data-year></span> SGA ENGINEERS. All rights reserved.</span>
          <span>Design with Integrity.</span>
        </div>
      </div>
    </footer>
    <script src="../js/main.js"></script>
  </body>
</html>
"""


def main() -> None:
    for m in MARKETS:
        path = OUT / f"{m['slug']}.html"
        path.write_text(render(m), encoding="utf-8")
        print(f"Wrote {path.name}")
    print(f"Done: {len(MARKETS)} pages")


if __name__ == "__main__":
    main()

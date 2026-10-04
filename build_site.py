from html import escape
from pathlib import Path
import json


ROOT = Path(__file__).parent
BASE_URL = "https://tmo.it"
EMAIL = "gauravmahlawat@gmail.com"
PHONE = "+91 74046 1750"

PAGE_ROUTES = {
    "index.html": "/",
    "drupal-development.html": "/drupal-development/",
    "wordpress-development.html": "/wordpress-development/",
    "react-development.html": "/react-development/",
    "python-development.html": "/python-development/",
    "shopify-development.html": "/shopify-development/",
    "hubspot-development.html": "/hubspot-development/",
    "content-management.html": "/content-management/",
    "data-analytics.html": "/data-analytics/",
    "ecommerce-development.html": "/ecommerce-development/",
    "custom-software-development.html": "/custom-software-development/",
    "quality-assurance.html": "/quality-assurance-testing/",
    "staff-augmentation.html": "/it-staff-augmentation/",
    "ui-ux-design.html": "/product-design/",
    "website-migrations.html": "/website-migration/",
    "about.html": "/about/",
    "work.html": "/work/",
    "insights.html": "/insights/",
    "faq.html": "/faq/",
    "contact.html": "/contact/",
    "privacy-policy.html": "/privacy-policy/",
    "terms-of-service.html": "/terms-of-use/",
    "cookie-policy.html": "/cookie-policy/",
}

SERVICES = [
    ("Drupal", "Drupal Development", PAGE_ROUTES["drupal-development.html"], "Drupal"),
    ("WordPress", "WordPress Development", PAGE_ROUTES["wordpress-development.html"], "WordPress"),
    ("React", "React Development", PAGE_ROUTES["react-development.html"], "React"),
    ("Python", "Python Development", PAGE_ROUTES["python-development.html"], "Python"),
    ("Shopify", "Shopify Development", PAGE_ROUTES["shopify-development.html"], "Shopify"),
    ("HubSpot", "HubSpot Development", PAGE_ROUTES["hubspot-development.html"], "HubSpot"),
    ("Content", "Content Management", PAGE_ROUTES["content-management.html"], "Manage content"),
    ("Analytics", "Data Analytics", PAGE_ROUTES["data-analytics.html"], "Explore data"),
    ("Commerce", "E-commerce Development", PAGE_ROUTES["ecommerce-development.html"], "Grow commerce"),
    ("Full stack", "Full-Stack Development", PAGE_ROUTES["custom-software-development.html"], "Build end to end"),
    ("Quality", "Quality Assurance", PAGE_ROUTES["quality-assurance.html"], "Test with confidence"),
    ("Experience", "Product Design", PAGE_ROUTES["ui-ux-design.html"], "Design the experience"),
]

SERVICE_DESCRIPTIONS = {
    "Drupal Development": "Content platforms and custom Drupal builds, upgrades and integrations.",
    "WordPress Development": "Flexible WordPress websites built for your publishers and customers.",
    "React Development": "Responsive front-end applications with a focus on clarity and speed.",
    "Python Development": "Backends, APIs and automation tailored to real business needs.",
    "Shopify Development": "Shopify storefronts and commerce journeys designed to convert.",
    "HubSpot Development": "Connected HubSpot websites and content tools for growing teams.",
    "Content Management": "Make publishing, updating and managing content easier for your team.",
    "Data Analytics": "Turn disconnected data into clear dashboards and useful decisions.",
    "E-commerce Development": "Create connected shopping experiences built around your customers.",
    "Full-Stack Development": "End-to-end web and software development, from interface to backend.",
    "Quality Assurance": "Test critical journeys and help every release feel more dependable.",
    "Product Design": "Turn customer needs into clear, accessible digital experiences.",
}

PROJECT_LINKS = [
    ("Completed project", "Satmark News", "https://satmarknews.in/", "Visit website"),
    ("Completed project", "LN Cabinetry", "https://www.lnccabinetry.com/", "Visit website"),
    ("Completed project", "Ring Concierge", "https://ringconcierge.com/", "Visit website"),
    ("Completed project", "Alpha Universe", "https://alphauniverse.com/", "Visit website"),
]


PAGES = [
    {
        "file": "index.html",
        "title": "TMO IT | Full-Service Software, Web & E-commerce Development",
        "description": "TMO IT builds and improves digital products, websites, content platforms, analytics and e-commerce experiences with end-to-end development and QA.",
        "eyebrow": "TMO IT · Full-cycle digital development",
        "heading": "Build the digital experience. <span>Grow the business behind it.</span>",
        "intro": "TMO IT plans, builds and improves the digital systems your business runs on—from full-stack software and easy-to-manage content to useful analytics and e-commerce journeys designed around your customers.",
        "sections": [
            ("End-to-end software development", "Plan, design, build and support websites, web applications and integrations with one connected team—from the first technical decisions to the ongoing improvements.", ["Front-end and back-end engineering", "APIs, integrations and migrations", "Quality checks and practical handover"]),
            ("Make content management easy", "Give editors an intuitive way to create, review and publish content. We shape the CMS and workflow around your organization, not the other way around.", ["Drupal, WordPress and HubSpot CMS", "Reusable pages and structured content", "Editorial roles, approvals and guidance"]),
            ("Understand what is working", "Bring meaningful product, campaign and commerce signals into clear reports so teams can spot patterns and decide what to improve next.", ["Analytics setup and measurement plans", "Dashboards and reporting integrations", "Journey and conversion analysis"]),
            ("Design the experience, not just the screen", "Give customers a clearer way through and give teams a more usable product, with thoughtful design carried all the way into implementation.", ["Research and user journeys", "UI systems and prototypes", "Responsive implementation"]),
            ("Add the skills you are missing", "Bring in experienced design, engineering or QA capability to support your team, your roadmap and the next delivery milestone.", ["Flexible team extension", "Collaborative delivery", "Clear communication and handover"]),
            ("Leave a stronger foundation", "The best release is not a dead end. We build with maintainability, performance and the next team handoff in mind.", ["Readable, tested implementation", "Performance-minded choices", "Practical documentation"]),
        ],
        "cards": SERVICES,
        "cards_heading": "Everything your digital business needs.",
    },
    {
        "file": "drupal-development.html",
        "title": "Drupal Development Services | TMO IT",
        "description": "Build, improve or migrate a Drupal experience with TMO IT. Get practical support for Drupal development, integrations, upgrades and ongoing quality.",
        "eyebrow": "Drupal engineering",
        "heading": "A Drupal platform built to <span>grow with you.</span>",
        "intro": "TMO IT helps teams create, extend and modernize Drupal websites and digital experiences—from focused improvements to larger platform work.",
        "sections": [
            ("Drupal, shaped around your content", "Plan a content model and publishing experience that work for the people creating content as well as the people finding it."),
            ("Build and improve with confidence", "Get support for custom modules, theming, integrations, performance improvements, accessibility and ongoing maintenance, scoped to your needs."),
            ("Upgrade or migrate without guesswork", "Assess your current Drupal setup, map content and functionality, and plan a measured path to a supported, maintainable platform."),
        ],
        "cards": [("Drupal build", "New platform development", "contact.html", "Plan"), ("Drupal upgrade", "Modernization and migrations", "website-migrations.html", "Move"), ("Quality assurance", "Test critical journeys", "quality-assurance.html", "Test")],
    },
    {
        "file": "wordpress-development.html",
        "title": "WordPress Development Services | TMO IT",
        "description": "TMO IT builds and improves WordPress websites with thoughtful design, custom development, integrations, performance and reliable quality assurance.",
        "eyebrow": "WordPress engineering",
        "heading": "A WordPress site that <span>works beautifully.</span>",
        "intro": "Create a WordPress experience that is easy to manage, quick to use and ready for your next stage of growth.",
        "sections": [
            ("Designed for your team", "Build a clear editing experience with reusable page patterns, sensible content structure and the flexibility your publishing team needs."),
            ("Custom development, not unnecessary complexity", "From themes and plugins to integrations and feature work, choose an approach that fits your actual requirements."),
            ("Performance and care after launch", "Improve loading experience, validate key journeys and keep your WordPress site easier to maintain over time."),
        ],
        "cards": [("WordPress build", "Custom themes and features", "contact.html", "Plan"), ("Site migration", "Move content and functionality", "website-migrations.html", "Move"), ("Quality assurance", "Test critical journeys", "quality-assurance.html", "Test")],
    },
    {
        "file": "react-development.html",
        "title": "React Development Services | TMO IT",
        "description": "Work with TMO IT on React applications, interfaces and front-end experiences, with product-minded engineering and quality built into delivery.",
        "eyebrow": "React engineering",
        "heading": "Interfaces that feel <span>fast, clear and considered.</span>",
        "intro": "TMO IT helps teams design and build React experiences that make complex products easier to use and easier to evolve.",
        "sections": [
            ("From interface to application", "Build responsive web applications, product interfaces and interactive experiences around real user needs and clear product goals."),
            ("A maintainable front end", "Use component-based development, thoughtful state and API integration patterns, and an architecture suited to your team's roadmap."),
            ("Quality users can feel", "Check behavior across devices, browsers and accessibility needs so the details work as well as the first impression."),
        ],
        "cards": [("Product design", "Map and refine user experiences", "ui-ux-design.html", "Design"), ("Custom software", "Build the wider product", "custom-software-development.html", "Build"), ("QA testing", "Validate every release", "quality-assurance.html", "Test")],
    },
    {
        "file": "python-development.html",
        "title": "Python Development Services | TMO IT",
        "description": "TMO IT provides Python development for web applications, APIs, integrations and automation, with an emphasis on clear scope and maintainable delivery.",
        "eyebrow": "Python engineering",
        "heading": "Reliable software, built on <span>solid foundations.</span>",
        "intro": "Turn a business need into a dependable Python-powered application, service or integration—with a team focused on clarity and long-term maintainability.",
        "sections": [
            ("Applications and APIs", "Develop web backends, APIs and service integrations that fit your product architecture and operational requirements."),
            ("Automation that gives time back", "Identify repetitive workflows and explore practical automation, data processing and system-to-system connections."),
            ("Engineering with a plan", "Make decisions about scope, security, testing and deployment early, and keep the implementation understandable as it grows."),
        ],
        "cards": [("Custom software", "Shape an application around your needs", "custom-software-development.html", "Build"), ("Quality assurance", "Test APIs and workflows", "quality-assurance.html", "Test"), ("Team extension", "Add skills to your team", "staff-augmentation.html", "Extend")],
    },
    {
        "file": "shopify-development.html",
        "title": "Shopify Development Services | TMO IT",
        "description": "TMO IT supports Shopify storefronts with custom development, integrations, user experience improvements and quality assurance for ecommerce teams.",
        "eyebrow": "Shopify engineering",
        "heading": "A storefront made for <span>better buying experiences.</span>",
        "intro": "Create a Shopify store that helps customers find, understand and buy with confidence—and gives your team a platform it can manage.",
        "sections": [
            ("Storefronts that put customers first", "Refine product discovery, navigation, product pages and checkout journeys with a focus on clarity across mobile and desktop."),
            ("Extend your Shopify setup", "Plan theme customizations, app and system integrations, and operational improvements around your commerce needs."),
            ("Test the moments that matter", "Validate product browsing, cart and checkout paths, content and integrations before changes reach your customers."),
        ],
        "cards": [("Product design", "Improve the shopping journey", "ui-ux-design.html", "Design"), ("QA testing", "Test commerce workflows", "quality-assurance.html", "Test"), ("Migrations", "Plan a platform move", "website-migrations.html", "Move")],
    },
    {
        "file": "hubspot-development.html",
        "title": "HubSpot Development Services | TMO IT",
        "description": "TMO IT helps teams improve HubSpot websites and digital experiences with custom development, thoughtful content tools and connected workflows.",
        "eyebrow": "HubSpot engineering",
        "heading": "Make your HubSpot experience <span>work harder.</span>",
        "intro": "Bring your website, content workflows and customer journeys together with HubSpot development shaped around how your team works.",
        "sections": [
            ("A flexible experience for marketing teams", "Create reusable templates and content components that help teams publish consistently without sacrificing design quality."),
            ("Connected journeys", "Improve the handoff between website experiences and the systems or workflows your business relies on."),
            ("A practical, measured improvement plan", "Start with the friction points that matter, validate them with your team and deliver changes in clear, manageable steps."),
        ],
        "cards": [("Custom development", "Connect your digital experience", "custom-software-development.html", "Build"), ("Product design", "Improve customer journeys", "ui-ux-design.html", "Design"), ("QA testing", "Validate key experiences", "quality-assurance.html", "Test")],
    },
    {
        "file": "content-management.html",
        "title": "Content Management & CMS Development | TMO IT",
        "description": "Make content easier to manage with TMO IT. We build and improve CMS platforms, publishing workflows and integrations for Drupal, WordPress and HubSpot.",
        "eyebrow": "Content management",
        "heading": "Publishing should feel <span>simple for everyone.</span>",
        "intro": "TMO IT makes content operations easier with well-structured CMS platforms, clear editorial workflows and tools that help teams publish confidently.",
        "sections": [
            ("A CMS built around your workflow", "Organize content types, permissions, review steps and reusable page patterns around how your team actually publishes—not around unnecessary platform complexity.", ["Editorial roles and approvals", "Reusable content components", "Structured, search-friendly content"]),
            ("Less friction for content teams", "Make routine updates feel straightforward. Improve preview, editing and publishing experiences so content owners can work independently and consistently.", ["Intuitive editing experiences", "Accessible content patterns", "Clear publishing guidance"]),
            ("Connect content to your wider business", "Integrate your CMS with the systems that power campaigns, customer journeys and commerce, while keeping ownership and data flows understandable.", ["Drupal, WordPress and HubSpot", "APIs and marketing integrations", "Migration and ongoing improvement"]),
        ],
        "cards": [("Drupal", "Create a flexible Drupal CMS", "drupal-development.html", "Explore"), ("WordPress", "Make WordPress easier to manage", "wordpress-development.html", "Explore"), ("Migration", "Move content with a plan", "website-migrations.html", "Explore")],
    },
    {
        "file": "data-analytics.html",
        "title": "Data Analytics, Dashboards & Reporting | TMO IT",
        "description": "TMO IT helps teams connect data, build useful dashboards and improve reporting for digital products, marketing and e-commerce decisions.",
        "eyebrow": "Data analytics",
        "heading": "Make your data easier <span>to act on.</span>",
        "intro": "Bring important signals into view. TMO IT helps teams connect digital data and create clear reporting that supports better product, marketing and commerce decisions.",
        "sections": [
            ("See the measures that matter", "Start with your business questions, then define the events and indicators that help answer them. Build a measurement plan that teams can understand and maintain.", ["Product and conversion journeys", "Campaign and channel performance", "Clear metric definitions"]),
            ("Connect data into useful views", "Bring selected data sources together and shape dashboards around the decisions your team needs to make, rather than creating reports nobody uses.", ["Analytics implementation", "Reporting dashboards", "Practical data integrations"]),
            ("Turn insight into improvement", "Use reporting to investigate friction, test ideas and track changes over time. Analytics can inform decisions; it cannot guarantee a specific business result.", ["Journey and funnel analysis", "Experiment and QA support", "Privacy-aware measurement"]),
        ],
        "cards": [("E-commerce", "Understand the shopping journey", "ecommerce-development.html", "Explore"), ("Custom software", "Build a product around your data", "custom-software-development.html", "Explore"), ("Contact", "Discuss your reporting needs", "contact.html", "Talk")],
    },
    {
        "file": "ecommerce-development.html",
        "title": "E-commerce Development & Shopify Services | TMO IT",
        "description": "TMO IT designs and develops e-commerce experiences, including Shopify storefronts, integrations and customer journeys that support online sales.",
        "eyebrow": "E-commerce development",
        "heading": "Make the path to purchase <span>feel effortless.</span>",
        "intro": "Build a considered e-commerce experience from product discovery to post-purchase. TMO IT helps connect storefront engineering, content, integrations and quality.",
        "sections": [
            ("A shopping experience that makes sense", "Help customers find the right product, understand their options and move through a clear, accessible buying journey on mobile and desktop.", ["Product discovery and navigation", "Product detail and content design", "Responsive shopping journeys"]),
            ("Commerce that works with your operations", "Connect the storefront with the tools and workflows your team uses, with careful planning for catalog, inventory, customer and order data.", ["Shopify development", "Platform and system integrations", "Catalog and content workflows"]),
            ("Improve the experience with evidence", "Combine quality checks and useful analytics to understand where customers encounter friction. Improvements can support sales, but results depend on many business factors.", ["Cart and checkout QA", "Journey measurement", "Iterative experience improvements"]),
        ],
        "cards": [("Shopify", "Build or improve a Shopify store", "shopify-development.html", "Explore"), ("Analytics", "Understand commerce performance", "data-analytics.html", "Explore"), ("Product design", "Design a clearer customer journey", "ui-ux-design.html", "Explore")],
    },
    {
        "file": "custom-software-development.html",
        "title": "Full-Stack Software Development Services | TMO IT",
        "description": "TMO IT designs, develops and supports full-stack software, web applications and integrations around your business goals and existing technology.",
        "eyebrow": "Custom software",
        "heading": "Software that fits the way <span>your business works.</span>",
        "intro": "When off-the-shelf tools are not enough, TMO IT helps turn the real problem into a useful, maintainable digital product.",
        "sections": [
            ("Begin with the problem", "Align on users, workflows, constraints and outcomes before settling on a feature list or technology choice."),
            ("Build in useful increments", "Deliver a clear first version, learn from real use and improve the product without losing sight of the bigger direction."),
            ("Keep the whole lifecycle in view", "Plan for integrations, security, testing, accessibility, performance and the people who will support the software after launch."),
        ],
        "cards": [("React", "Responsive application interfaces", "react-development.html", "Explore"), ("Python", "Backends, APIs and automation", "python-development.html", "Explore"), ("Quality assurance", "Build confidence at each release", "quality-assurance.html", "Explore")],
    },
    {
        "file": "quality-assurance.html",
        "title": "Software QA & Testing Services | TMO IT",
        "description": "Reduce release risk with TMO IT's software quality assurance: exploratory testing, functional validation, regression checks and automation planning.",
        "eyebrow": "Quality assurance",
        "heading": "Ship changes with <span>more confidence.</span>",
        "intro": "Make quality part of the delivery process—not a last-minute check. TMO IT helps teams find risk early and protect important user journeys.",
        "sections": [
            ("Testing focused on real use", "Explore functional behavior, cross-browser and responsive experiences, integrations and the workflows that matter most to your users."),
            ("A repeatable quality practice", "Define practical test coverage, clear defect reporting and regression checks that fit your team and release cadence."),
            ("Automation where it helps", "Identify stable, high-value test cases for automation while keeping human testing in the loop for usability and changing requirements."),
        ],
        "cards": [("Software development", "Build with quality in the loop", "custom-software-development.html", "Build"), ("Staff augmentation", "Extend your delivery team", "staff-augmentation.html", "Extend"), ("Contact TMO IT", "Talk about your release risks", "contact.html", "Talk")],
    },
    {
        "file": "staff-augmentation.html",
        "title": "IT Staff Augmentation & Team Extension | TMO IT",
        "description": "Add software development, QA or design capacity with TMO IT. Flexible team augmentation for product and delivery teams across time zones.",
        "eyebrow": "Team augmentation",
        "heading": "Add the capability your team <span>needs right now.</span>",
        "intro": "Extend your existing team with software, QA or design support that works alongside your people, process and priorities.",
        "sections": [
            ("An extension of your team", "Bring in targeted expertise for a delivery gap, a focused project or a period of increased workload—without losing your team's context."),
            ("Skills aligned to the work", "Discuss the role, seniority, collaboration needs, time-zone overlap and expected outcomes before shaping an engagement."),
            ("Clear communication from day one", "Agree ways of working, ownership, feedback loops and onboarding so additional capacity can contribute effectively."),
        ],
        "cards": [("Software development", "Add engineering capacity", "custom-software-development.html", "Build"), ("QA testing", "Strengthen release quality", "quality-assurance.html", "Test"), ("Product design", "Add design expertise", "ui-ux-design.html", "Design")],
    },
    {
        "file": "ui-ux-design.html",
        "title": "UI/UX & Product Design Services | TMO IT",
        "description": "TMO IT helps teams clarify product journeys and design thoughtful digital experiences through UX discovery, interface design and design systems.",
        "eyebrow": "Product design",
        "heading": "Make every interaction <span>feel considered.</span>",
        "intro": "Connect user needs and business goals with digital experiences that are clear, inclusive and ready for engineering.",
        "sections": [
            ("Understand before designing", "Map user journeys, review existing experiences and agree which problems are worth solving first."),
            ("From structure to polished interface", "Explore information architecture, wireframes and visual direction, then refine the details into a coherent responsive experience."),
            ("Design that reaches production", "Collaborate closely with developers, document reusable patterns and validate the implemented experience—not just the prototype."),
        ],
        "cards": [("React development", "Bring interfaces to life", "react-development.html", "Build"), ("Shopify", "Improve commerce experiences", "shopify-development.html", "Explore"), ("Contact TMO IT", "Discuss your design goals", "contact.html", "Talk")],
    },
    {
        "file": "website-migrations.html",
        "title": "Website & Platform Migration Services | TMO IT",
        "description": "Plan and deliver website, CMS and platform migrations with TMO IT, including content mapping, implementation, validation and launch readiness.",
        "eyebrow": "Migrations and modernization",
        "heading": "Move platforms without <span>losing the important details.</span>",
        "intro": "A good migration is more than moving pages. TMO IT helps you understand what to preserve, what to improve and how to make the transition manageable.",
        "sections": [
            ("Know what you are moving", "Inventory content, functionality, integrations, redirects, analytics and operational needs before selecting a migration path."),
            ("Protect discoverability and continuity", "Plan URL mapping, metadata, redirects, content validation and launch checks to reduce avoidable disruption."),
            ("Make the new platform easier to evolve", "Use migration as an opportunity to simplify workflows, improve experience and establish a maintainable foundation."),
        ],
        "cards": [("Drupal", "CMS development and upgrades", "drupal-development.html", "Explore"), ("WordPress", "Flexible publishing experiences", "wordpress-development.html", "Explore"), ("Contact TMO IT", "Plan a migration", "contact.html", "Talk")],
    },
    {
        "file": "about.html",
        "title": "About TMO IT | Digital Development Partner",
        "description": "Meet TMO IT, your partner for full-stack development, content platforms, data analytics, e-commerce, design and quality assurance.",
        "eyebrow": "About TMO IT",
        "heading": "All the digital capabilities. <span>One connected team.</span>",
        "intro": "TMO IT brings full-stack development, content management, data analytics, commerce, product design and quality assurance together to help teams move from a business need to a working digital experience.",
        "sections": [
            ("Full-cycle digital delivery", "From discovery, UX and architecture through development, integration, QA, launch and support, keep the work connected instead of coordinating disconnected suppliers."),
            ("More than a website build", "Make content easier to publish, make data easier to understand, and create e-commerce journeys that support customers from discovery through checkout."),
            ("Built around your context", "Bring TMO IT in for an end-to-end project or specialist support across Drupal, WordPress, React, Python, Shopify, HubSpot and analytics."),
        ],
        "cards": [("Our services", "Find the right kind of support", "index.html#services", "Explore"), ("Our work", "See how we approach proof and outcomes", "work.html", "Explore"), ("Contact", "Tell us what you are working on", "contact.html", "Talk")],
    },
    {
        "file": "work.html",
        "title": "Work & Case Studies | TMO IT",
        "description": "Explore websites TMO IT has completed and learn how the team approaches digital product work. Detailed case studies are shared with approval.",
        "eyebrow": "Selected work",
        "heading": "The best proof is work <span>we can stand behind.</span>",
        "intro": "Every project has its own context. We focus on useful outcomes, thoughtful engineering and clear collaboration—and share client stories only with permission.",
        "sections": [
            ("Selected project links", "The websites below were supplied by TMO IT as completed project work. They are linked as examples only; no client quote, project outcome or performance claim is being attributed here."),
            ("Detailed case studies", "A fuller case study can explain the business challenge, the work undertaken, the team's role and outcomes where available. Details should be published only when they are approved for public use."),
            ("Have a project in mind?", "Tell us about your goals and constraints. We can discuss relevant experience directly and agree what information may be shared."),
        ],
        "cards": PROJECT_LINKS,
        "cards_heading": "Websites completed by TMO IT",
    },
    {
        "file": "insights.html",
        "title": "Digital Product Insights | TMO IT",
        "description": "Practical perspectives from TMO IT on software development, content platforms, analytics, e-commerce, quality assurance and digital delivery.",
        "eyebrow": "Insights",
        "heading": "Clear thinking for your <span>next digital decision.</span>",
        "intro": "Useful digital work begins with useful questions. This section will bring together practical perspectives from our work across products, platforms and teams.",
        "sections": [
            ("A growing library", "We are preparing articles and guides on choosing a migration approach, building a QA practice, improving content workflows and making digital products easier to use."),
            ("Topics we care about", "Platform engineering, product delivery, test strategy, accessibility, commerce experiences and the collaboration patterns that help teams move forward."),
            ("Looking for an answer now?", "Share the question you are working through. A conversation can often help clarify the next practical step."),
        ],
        "cards": [("Migrations", "Plan platform changes carefully", "website-migrations.html", "Read"), ("Quality assurance", "Make quality part of delivery", "quality-assurance.html", "Read"), ("Contact TMO IT", "Ask us a question", "contact.html", "Talk")],
    },
    {
        "file": "faq.html",
        "title": "Frequently Asked Questions | TMO IT",
        "description": "Answers about TMO IT's full-stack development, content management, analytics, e-commerce, QA and team augmentation services.",
        "eyebrow": "Frequently asked questions",
        "heading": "A few useful answers <span>before we get started.</span>",
        "intro": "Every engagement is different. Here are some useful starting points for planning your next digital project with TMO IT.",
        "sections": [
            ("What services does TMO IT provide?", "Full-stack software and web development, CMS and content management, data analytics, e-commerce, quality assurance, product design, migrations and staff augmentation."),
            ("Which technologies do you work with?", "Our focus includes Drupal, WordPress, React, Python, Shopify and HubSpot. Share your current setup and we can discuss fit and scope."),
            ("Where do you work?", "TMO IT works with teams in India, Australia, the UK, Europe and the USA. Collaboration arrangements depend on the project and time-zone needs."),
            ("Can you make our CMS easier for editors?", "Yes. We can review the current authoring workflow, content structure, permissions and publishing steps, then recommend and implement improvements in Drupal, WordPress or HubSpot."),
            ("Can you help with analytics and reporting?", "Yes. We can help plan measurement, connect relevant data sources and build dashboards for product, campaign or commerce questions. Reports help inform decisions; they do not guarantee outcomes."),
            ("Can you help improve online sales?", "We can improve e-commerce development, product discovery, content, checkout quality and analytics to support a clearer customer journey. Sales results also depend on pricing, inventory, audience, marketing and other factors."),
            ("Do you publish pricing?", "Pricing is not currently published. Contact us with the work you have in mind and we can discuss scope and an appropriate proposal."),
            ("Can you take over an existing project or site?", "Yes, the first step is understanding the codebase or platform, current risks and access constraints. Never send passwords by email; secure access can be arranged separately."),
            ("Do you provide support after launch?", "Ongoing support can be discussed as part of the project scope, including maintenance, QA and planned improvements."),
        ],
        "cards": [("Services", "Explore how we can help", "index.html#services", "Explore"), ("Migrations", "Plan a platform move", "website-migrations.html", "Explore"), ("Contact", "Share your question", "contact.html", "Talk")],
    },
    {
        "file": "contact.html",
        "title": "Contact TMO IT | Discuss Your Digital Project",
        "description": "Contact TMO IT about full-stack development, CMS, analytics, e-commerce, QA or design. Share your goals and discuss the next step.",
        "eyebrow": "Start a conversation",
        "heading": "Tell us what you are <span>trying to make possible.</span>",
        "intro": "A little context is enough to start. Share the challenge, the platform and what a good outcome would look like—we will take it from there.",
        "sections": [
            ("Prefer email or phone?", f"Email {EMAIL} or call {PHONE}. Please do not send passwords, payment details or other sensitive information through this form."),
            ("What happens next?", "Your message opens in your own email application for you to review and send. TMO IT does not submit or store this form on the website."),
            ("Working across time zones", "TMO IT works with teams in India, Australia, the UK, Europe and the USA. Include your location and preferred meeting hours in your message so we can plan a useful first conversation."),
        ],
        "cards": [("Software development", "Custom software and applications", "custom-software-development.html", "Explore"), ("Quality assurance", "Testing and release confidence", "quality-assurance.html", "Explore"), ("Team augmentation", "Add skills and capacity", "staff-augmentation.html", "Explore")],
        "form": True,
    },
    {
        "file": "privacy-policy.html",
        "title": "Privacy Policy | TMO IT",
        "description": "Read how TMO IT handles personal information when you visit tmo.it or contact us, including contact requests, website analytics and your privacy choices.",
        "eyebrow": "Last updated: 4 October 2026",
        "heading": "Privacy <span>Policy.</span>",
        "intro": "This policy describes how the TMO IT website handles information. Review it against your live hosting setup and applicable privacy obligations.",
        "sections": [
            ("Who is responsible", "The website is operated by Gaurav under the TMO IT brand. The business address supplied for publication is 452/1D New Colony Extension, Palwal 121102, Haryana, India. For privacy questions, contact " + EMAIL + "."),
            ("Information you choose to send", "If you email us or use the contact form, your email application sends the information you choose to include to our email provider. The website form itself does not transmit or store submissions. Avoid sending sensitive personal information."),
            ("Website technical information", "The site is intended to be hosted with Hostinger. The hosting provider may process technical information such as IP address, browser details and server logs to deliver and protect the site. Confirm the applicable hosting terms and log retention in your account."),
            ("Cookies and analytics", "This site is designed not to set non-essential analytics or advertising cookies. Hosting, embedded content or services added later may use cookies or similar technologies; update this policy and obtain consent where required before enabling them."),
            ("Retention and service providers", "Email correspondence sent to the listed Gmail address is processed by the email provider and retained in that account for as long as needed to respond and manage the relationship, subject to applicable legal requirements. Hostinger may process website technical information to provide hosting."),
            ("Your rights, transfers and contact", "Depending on where you live, you may have rights to access, correct, erase, restrict or object to processing, or to complain to a privacy regulator. Contact " + EMAIL + " to make a request. Because TMO IT serves multiple regions, confirm applicable laws and any cross-border transfer safeguards with a qualified adviser. This notice may be updated as the website and its tools change."),
        ],
        "cards": [],
    },
    {
        "file": "terms-of-service.html",
        "title": "Terms of Use | TMO IT",
        "description": "Terms for using the TMO IT website, its content and contact form. Project services are subject to a separate written agreement.",
        "eyebrow": "Last updated: 4 October 2026",
        "heading": "Website <span>Terms of Use.</span>",
        "intro": "These draft terms cover use of the TMO IT website only. They do not set the terms, fees or warranties for professional services, which must be agreed separately in writing.",
        "sections": [
            ("Website operator", "The site is operated by Gaurav under the TMO IT brand at 452/1D New Colony Extension, Palwal 121102, Haryana, India."),
            ("Using this website", "You may use this website lawfully and must not interfere with its security or operation, attempt unauthorized access, or misuse its content or contact facilities."),
            ("Information on this site", "Website information is general and may change. It is not legal, financial or technical advice for your particular circumstances. Confirm project scope, deliverables, fees, intellectual property, confidentiality and support in a separate signed agreement."),
            ("Third-party sites", "Links to external websites are provided for convenience. TMO IT does not control their content, availability or privacy practices."),
            ("Availability and liability", "The site is provided on an as-available basis. To the extent permitted by applicable law, TMO IT excludes implied warranties and liability for indirect loss arising from use of the site. Nothing in these terms limits rights that cannot lawfully be excluded."),
            ("Applicable law, updates and contact", "The responsible business identity and governing law must be confirmed before publication. These draft terms should be reviewed by a qualified lawyer for the relevant jurisdictions. Updated terms will be posted on this page. Questions may be sent to " + EMAIL + "."),
        ],
        "cards": [],
    },
    {
        "file": "cookie-policy.html",
        "title": "Cookie Policy | TMO IT",
        "description": "Learn about cookies and similar technologies used on the TMO IT website, and how to manage your browser preferences.",
        "eyebrow": "Last updated: 4 October 2026",
        "heading": "Cookie <span>Policy.</span>",
        "intro": "This site is designed without non-essential analytics, advertising or tracking cookies. Review the hosting configuration and any future integrations before launch.",
        "sections": [
            ("What cookies are", "Cookies are small files stored by your browser. Similar technologies can also store or access information on a device."),
            ("Current website behavior", "The static website code does not intentionally set cookies or include analytics, advertising pixels or embedded third-party media. The hosting provider may use essential technologies for security or delivery; confirm this with your Hostinger account configuration."),
            ("Managing preferences", "You can manage or delete cookies using your browser settings. Blocking essential cookies or storage may affect some websites."),
            ("Essential technologies", "Strictly necessary technologies may be used by the hosting service to deliver pages, maintain security or balance traffic. Review the Hostinger settings for the live hosting account to confirm what applies."),
            ("Changes to this policy", "If analytics, video embeds, chat, advertising or other third-party tools are added, update this page and implement any consent controls required by applicable law before enabling them."),
            ("Contact", "Questions about cookies or privacy can be sent to " + EMAIL + "."),
        ],
        "cards": [],
    },
]


def normalize_href(href):
    path, separator, fragment = href.partition("#")
    href = PAGE_ROUTES.get(path, path) + (separator + fragment if separator else "")
    if not href.startswith(("/", "#", "mailto:", "tel:", "https://", "http://")):
        href = "/" + href
    return href


def link(href, label, css=""):
    href = normalize_href(href)
    cls = f' class="{css}"' if css else ""
    suffix = '<span class="button-arrow" aria-hidden="true">↗</span>' if "button" in css.split() else ""
    return f'<a{cls} href="{escape(href, quote=True)}">{escape(label)}{suffix}</a>'


def section_html(section, index):
    heading, paragraph, *bullets = section
    items = ""
    if bullets:
        items = "<ul>" + "".join(f"<li>{escape(item)}</li>" for item in bullets[0]) + "</ul>"
    return (
        f'<section class="content-card reveal" style="--delay:{index * 70}ms">'
        f"<h2>{escape(heading)}</h2><p>{escape(paragraph)}</p>{items}</section>"
    )


def cards_html(cards, heading=None, section_id=None):
    if not cards:
        return ""
    rendered = []
    for index, (kicker, title, href, label) in enumerate(cards, 1):
        href = normalize_href(href)
        external_attrs = ' target="_blank" rel="noopener noreferrer"' if href.startswith(("https://", "http://")) else ""
        description = SERVICE_DESCRIPTIONS.get(title, "")
        detail = f"<p class=\"service-description\">{escape(description)}</p>" if description else ""
        rendered.append(
            f'<a class="service-card reveal" href="{escape(href, quote=True)}"{external_attrs}>'
            f'<span class="card-topline"><span class="card-kicker">{escape(kicker)}</span><span class="card-index">{index:02}</span></span>'
            f"<h3>{escape(title)}</h3>{detail}<span class=\"card-link\">{escape(label)} <span aria-hidden=\"true\">↗</span></span></a>"
        )
    content = "".join(rendered)
    section_heading = heading or "More ways to move forward."
    section_id_attr = f' id="{escape(section_id, quote=True)}"' if section_id else ""
    grid_class = f"card-grid card-grid-{len(cards)}"
    return f'<section class="card-section"{section_id_attr}><div class="section-heading"><p class="eyebrow">Explore what is possible</p><h2>{escape(section_heading)}</h2></div><div class="{grid_class}">{content}</div></section>'


def homepage_story():
    process = [
        ("01", "Listen & align", "Get clear on the people, problem, constraints and outcome before jumping to a solution."),
        ("02", "Shape the work", "Agree the right scope, team and first milestone. Make decisions and trade-offs visible."),
        ("03", "Build & validate", "Work in focused increments, share progress early and test the experience as it takes shape."),
        ("04", "Launch & improve", "Prepare a considered handover, learn from real use and make the next improvement count."),
    ]
    steps = "".join(
        f'<article class="process-step reveal"><span class="step-number">{number}</span><h3>{escape(title)}</h3><p>{escape(description)}</p></article>'
        for number, title, description in process
    )
    platform_pills = "".join(
        f'<span class="platform-pill">{escape(platform)}</span>'
        for platform in ("Drupal", "WordPress", "React", "Python", "Shopify", "HubSpot", "Analytics")
    )
    return f"""
    <section class="value-band">
      <p class="eyebrow">More than a build team</p>
      <p>Build it. Manage it. Understand it. <span>Grow it.</span></p>
      <a class="text-link" href="/about/">Get to know TMO IT <span aria-hidden="true">↗</span></a>
    </section>
    <section class="process-section">
      <div class="section-heading"><p class="eyebrow">How we work</p><h2>Less theatre. More forward motion.</h2><p class="section-deck">A clear, collaborative delivery rhythm that keeps your team close to the work and the decisions that shape it.</p></div>
      <div class="process-grid">{steps}</div>
    </section>
    <section class="platform-feature">
      <div class="feature-copy"><p class="eyebrow">From first visit to loyal customer</p><h2>Content, commerce and data. <span>Connected around your business.</span></h2><p>Make publishing easier for your team. Understand what customers do. Create a clearer path to purchase and use the insight to keep improving it. We build for the business outcomes you care about—not just the launch.</p><a class="text-link" href="/contact/">Let’s talk about your digital goals <span aria-hidden="true">↗</span></a></div>
      <div class="platform-cloud" aria-label="Platforms and technologies">{platform_pills}</div>
      <div class="feature-orb" aria-hidden="true"><span>t.</span></div>
    </section>
    <section class="capability-band">
      <div><p class="eyebrow">A good fit for your next chapter</p><h2>Start with a challenge.<br><span>Find the right team around it.</span></h2></div>
      <div class="capability-list"><a href="/custom-software-development/"><span>01</span><strong>Develop across the full stack</strong><b aria-hidden="true">↗</b></a><a href="/content-management/"><span>02</span><strong>Make content easy to manage</strong><b aria-hidden="true">↗</b></a><a href="/data-analytics/"><span>03</span><strong>Turn data into clearer decisions</strong><b aria-hidden="true">↗</b></a><a href="/ecommerce-development/"><span>04</span><strong>Improve the online buying journey</strong><b aria-hidden="true">↗</b></a></div>
    </section>
    <section class="work-preview">
      <div class="section-heading section-heading-row"><div><p class="eyebrow">Selected work</p><h2>Good work speaks in outcomes.</h2></div><a class="text-link" href="/work/">Explore completed projects <span aria-hidden="true">↗</span></a></div>
      <p class="section-deck work-deck">A few websites TMO IT has completed. Each link is shared as a project reference; detailed stories and client outcomes are published only with approval.</p>
      <div class="project-grid">{project_cards_html()}</div>
    </section>"""


def project_cards_html():
    cards = []
    for index, (_, name, url, label) in enumerate(PROJECT_LINKS, 1):
        cards.append(
            f'<a class="project-card reveal" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">'
            f'<span class="project-number">0{index} / PROJECT</span><span class="project-name">{escape(name)}</span>'
            f'<span class="project-visit">{escape(label)} <span aria-hidden="true">↗</span></span></a>'
        )
    return "".join(cards)


def studio_scene():
    return """
    <div class="studio-scene" role="img" aria-label="Abstract TMO IT product studio workspace showing strategy, design and quality working together">
      <svg class="product-visual" viewBox="0 0 720 680" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <defs>
          <linearGradient id="scene-back" x1="110" y1="80" x2="620" y2="610" gradientUnits="userSpaceOnUse"><stop stop-color="#E6ECFF"/><stop offset=".48" stop-color="#B5C7F9"/><stop offset="1" stop-color="#B8EAD7"/></linearGradient>
          <linearGradient id="scene-front" x1="222" y1="94" x2="498" y2="567" gradientUnits="userSpaceOnUse"><stop stop-color="#FFF" stop-opacity=".95"/><stop offset=".5" stop-color="#F9FBFF" stop-opacity=".68"/><stop offset="1" stop-color="#C8D5FF" stop-opacity=".52"/></linearGradient>
          <linearGradient id="scene-edge" x1="258" y1="160" x2="506" y2="498" gradientUnits="userSpaceOnUse"><stop stop-color="#FFF"/><stop offset=".55" stop-color="#B8C7FF"/><stop offset="1" stop-color="#9FDCC9"/></linearGradient>
          <linearGradient id="scene-blue" x1="260" y1="350" x2="460" y2="540" gradientUnits="userSpaceOnUse"><stop stop-color="#8195F4"/><stop offset="1" stop-color="#566BC8"/></linearGradient>
          <radialGradient id="scene-light" cx="0" cy="0" r="1" gradientTransform="matrix(180 230 -205 160 280 180)" gradientUnits="userSpaceOnUse"><stop stop-color="#FFF" stop-opacity=".88"/><stop offset="1" stop-color="#FFF" stop-opacity="0"/></radialGradient>
          <filter id="scene-shadow" x="66" y="54" width="623" height="617" color-interpolation-filters="sRGB" filterUnits="userSpaceOnUse"><feGaussianBlur stdDeviation="20"/></filter>
        </defs>
        <circle cx="365" cy="342" r="252" stroke="#8092CE" stroke-opacity=".16"/>
        <circle cx="365" cy="342" r="210" stroke="#FFF" stroke-opacity=".55"/>
        <circle cx="365" cy="342" r="170" stroke="#8194CA" stroke-opacity=".13"/>
        <ellipse cx="376" cy="545" rx="187" ry="45" fill="#6375BB" fill-opacity=".2" filter="url(#scene-shadow)"/>
        <path d="M198 190C198 164 219 143 245 143H487C513 143 534 164 534 190V442C534 468 513 489 487 489H245C219 489 198 468 198 442V190Z" fill="url(#scene-back)" fill-opacity=".69" stroke="#FFF" stroke-opacity=".8" stroke-width="2" transform="rotate(-11 366 316)"/>
        <path d="M225 182C225 160 243 142 265 142H473C495 142 513 160 513 182V432C513 454 495 472 473 472H265C243 472 225 454 225 432V182Z" fill="url(#scene-front)" stroke="url(#scene-edge)" stroke-width="2" transform="rotate(7 369 307)"/>
        <path d="M225 182C225 160 243 142 265 142H473C495 142 513 160 513 182V432C513 454 495 472 473 472H265C243 472 225 454 225 432V182Z" fill="url(#scene-light)" transform="rotate(7 369 307)"/>
        <g transform="rotate(7 369 307)">
          <rect x="260" y="180" width="53" height="53" rx="18" fill="url(#scene-blue)"/>
          <path d="M278 207H295M286.5 198.5V215.5" stroke="white" stroke-width="2" stroke-linecap="round"/>
          <rect x="327" y="188" width="130" height="8" rx="4" fill="#273455" fill-opacity=".75"/>
          <rect x="327" y="205" width="90" height="6" rx="3" fill="#71809E" fill-opacity=".56"/>
          <rect x="260" y="258" width="218" height="119" rx="18" fill="white" fill-opacity=".67" stroke="white" stroke-opacity=".88"/>
          <path d="M282 343L320 315L348 328L390 284L423 303L455 273" stroke="#617BE5" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M282 353H455" stroke="#8792AE" stroke-opacity=".16" stroke-width="2"/>
          <circle cx="320" cy="315" r="5" fill="#FFF" stroke="#617BE5" stroke-width="3"/>
          <circle cx="390" cy="284" r="5" fill="#FFF" stroke="#617BE5" stroke-width="3"/>
          <rect x="260" y="394" width="101" height="48" rx="14" fill="#E7ECFF" fill-opacity=".9"/>
          <rect x="375" y="394" width="103" height="48" rx="14" fill="#E4F5EC" fill-opacity=".9"/>
          <circle cx="282" cy="418" r="8" fill="#8297F1" fill-opacity=".82"/>
          <rect x="298" y="410" width="44" height="5" rx="2.5" fill="#52628B" fill-opacity=".6"/>
          <rect x="298" y="420" width="32" height="4" rx="2" fill="#8B95AC" fill-opacity=".55"/>
          <circle cx="397" cy="418" r="8" fill="#76C9A4" fill-opacity=".82"/>
          <path d="M393 418L396 421L402 414" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <rect x="413" y="410" width="48" height="5" rx="2.5" fill="#52628B" fill-opacity=".6"/>
          <rect x="413" y="420" width="34" height="4" rx="2" fill="#8B95AC" fill-opacity=".55"/>
        </g>
        <path d="M541 190L547 206L563 212L547 218L541 234L535 218L519 212L535 206L541 190Z" fill="#FFF"/>
        <circle cx="183" cy="415" r="7" fill="#77C9AA"/>
        <circle cx="548" cy="401" r="5" fill="#8297F1"/>
      </svg>
      <div class="scene-chip chip-design"><span class="chip-icon">✳</span><span><b>Design</b><small>Made for people</small></span></div>
      <div class="scene-chip chip-quality"><span class="chip-icon chip-check">✓</span><span><b>Quality</b><small>Built in from day one</small></span></div>
      <span class="scene-caption">Thoughtfully connected. Ready for what’s next.</span>
    </div>"""


def form_html():
    return """
    <section class="contact-panel reveal">
      <form id="contact-form">
        <label for="name">Your name</label><input id="name" name="name" autocomplete="name" required>
        <label for="email">Work email</label><input id="email" name="email" type="email" autocomplete="email" required>
        <label for="company">Company <span class="optional">(optional)</span></label><input id="company" name="company" autocomplete="organization">
        <label for="message">What would you like to work on?</label><textarea id="message" name="message" rows="5" required></textarea>
        <button class="button button-dark" type="submit">Continue in your email app <span class="button-arrow" aria-hidden="true">↗</span></button>
        <p class="form-note">Your message stays in your browser until your email app opens. You choose whether to send it.</p>
      </form>
    </section>"""


def schema_for(page):
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "TMO IT",
        "url": BASE_URL,
        "email": EMAIL,
        "telephone": "+917404671750",
        "areaServed": ["India", "Australia", "United Kingdom", "Europe", "United States"],
    }
    result = [org, {"@context": "https://schema.org", "@type": "WebSite", "name": "TMO IT", "url": BASE_URL}]
    if page["file"] != "index.html":
        result.append({
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": page["title"],
            "description": page["description"],
            "url": BASE_URL + PAGE_ROUTES[page["file"]],
        })
    if page["file"] in {p["file"] for p in PAGES if p["file"] not in {"index.html", "about.html", "work.html", "insights.html", "faq.html", "contact.html", "privacy-policy.html", "terms-of-service.html", "cookie-policy.html"}}:
        result.append({
            "@context": "https://schema.org",
            "@type": "Service",
            "name": page["title"].split("|")[0].strip(),
            "provider": {"@type": "Organization", "name": "TMO IT", "url": BASE_URL},
            "areaServed": ["India", "Australia", "United Kingdom", "Europe", "United States"],
            "url": BASE_URL + PAGE_ROUTES[page["file"]],
        })
    return json.dumps(result, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def render(page):
    filename = page["file"]
    canonical = BASE_URL + PAGE_ROUTES[filename]
    page_content = "".join(section_html(section, i) for i, section in enumerate(page["sections"]))
    extra = form_html() if page.get("form") else ""
    links = "".join(link(item[2], item[1]) for item in SERVICES)
    nav = (
        '<a class="brand" href="/" aria-label="TMO IT home"><span class="brand-mark">t.</span><span>TMO<span class="brand-period">.</span><small class="brand-it">IT</small></span></a>'
        '<button class="menu-toggle" aria-expanded="false" aria-controls="site-nav"><span class="sr-only">Toggle navigation</span><span></span><span></span></button>'
        '<nav class="site-nav" id="site-nav" aria-label="Main navigation">'
        '<a href="/#services">Services</a><a href="/about/">About</a><a href="/work/">Work</a><a href="/insights/">Insights</a><a href="/faq/">FAQ</a>'
        '<a class="nav-contact" href="/contact/">Let’s talk <span aria-hidden="true">↗</span></a></nav>'
    )
    footer = (
        '<footer class="site-footer"><span class="footer-watermark" aria-hidden="true">TMO IT</span><div class="footer-main"><div><a class="brand footer-brand" href="/"><span class="brand-mark">t.</span><span>TMO<span class="brand-period">.</span><small class="brand-it">IT</small></span></a>'
        '<p>Build. Manage. Understand.<br>Grow with confidence.</p></div>'
        f'<div><h2>Services</h2><div class="footer-links footer-service-links">{links}</div></div>'
        '<div><h2>Explore</h2><div class="footer-links"><a href="/content-management/">Content management</a><a href="/data-analytics/">Data analytics</a><a href="/ecommerce-development/">E-commerce</a><a href="/about/">About</a><a href="/work/">Work</a><a href="/contact/">Contact</a></div></div>'
        '<div><h2>Contact</h2><div class="footer-links"><a href="mailto:gauravmahlawat@gmail.com">gauravmahlawat@gmail.com</a><a href="tel:+917404671750">+91 74046 1750</a></div></div></div>'
        '<div class="footer-bottom"><span>© 2026 TMO IT. All rights reserved.</span><div><a href="/privacy-policy/">Privacy</a><a href="/terms-of-use/">Terms</a><a href="/cookie-policy/">Cookies</a></div></div></footer>'
    )
    home = filename == "index.html"
    cards = cards_html(page.get("cards", []), page.get("cards_heading"), "services" if home else None)
    home_story = homepage_story() if home else ""
    hero_visual = studio_scene() if home else (
        '<div class="hero-orbit" aria-hidden="true"><div class="orbit-ring"></div><div class="orbit-core"><span>t.</span></div><div class="orbit-label label-build">build</div><div class="orbit-label label-design">design</div><div class="orbit-label label-quality">quality</div></div>'
    )
    intro_strip = (
        '<section class="intro-strip"><div><p class="eyebrow">A better way to build digital</p><p>Good technology should make the <strong>next step feel simpler.</strong></p></div><span class="strip-symbol" aria-hidden="true">✳</span></section>'
        if home else
        '<section class="intro-strip"><div><p class="eyebrow">An extension of your team</p><p>From the first question to the next release, <strong>we make progress feel possible.</strong></p></div><span class="strip-symbol" aria-hidden="true">✳</span></section>'
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f5f7fa">
  <title>{escape(page["title"])}</title>
  <meta name="description" content="{escape(page["description"], quote=True)}">
  <link rel="canonical" href="{escape(canonical, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="TMO IT">
  <meta property="og:title" content="{escape(page["title"], quote=True)}">
  <meta property="og:description" content="{escape(page["description"], quote=True)}">
  <meta property="og:url" content="{escape(canonical, quote=True)}">
  <meta name="twitter:card" content="summary">
  <script type="application/ld+json">{schema_for(page)}</script>
  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="header-inner">{nav}</div></header>
  <main id="main">
    <section class="hero {"hero-home" if home else "hero-inner"}">
      <div class="hero-glow glow-one"></div><div class="hero-glow glow-two"></div>
      <div class="hero-content">
        <p class="eyebrow"><span class="eyebrow-dot"></span>{escape(page["eyebrow"])}</p>
        <h1>{page["heading"]}</h1>
        <p class="hero-copy">{escape(page["intro"])}</p>
        <div class="hero-actions">{link("contact.html", "Start a conversation", "button button-dark")}{link("/#services", "Explore services", "button button-glass")}</div>
      </div>
      {hero_visual}
      <div class="hero-bottom"><span>India · Australia · UK · Europe · USA</span><span>Strategy&nbsp; / &nbsp;Design&nbsp; / &nbsp;Engineering</span></div>
    </section>
    {intro_strip}
    <div class="content-layout"><div class="content-column">{page_content}{extra}</div></div>
    {cards}
    {home_story}
    <section class="closing-cta"><p class="eyebrow">Have a challenge in mind?</p><h2>Let’s make the next step <span>clear.</span></h2><p>Tell us what you are building, improving or moving.</p>{link("contact.html", "Talk to TMO IT", "button button-light")}</section>
  </main>
  {footer}
  <script src="/app.js" defer></script>
</body>
</html>
"""


def main():
    active_outputs = {ROOT / page["file"] for page in PAGES}
    for page in PAGES:
        route = PAGE_ROUTES[page["file"]]
        output = ROOT / "index.html" if route == "/" else ROOT / route.strip("/") / "index.html"
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render(page), encoding="utf-8")
    for legacy_file in active_outputs - {ROOT / "index.html"}:
        legacy_file.unlink(missing_ok=True)
    urls = "\n".join(
        f"  <url><loc>{BASE_URL}{PAGE_ROUTES[page['file']]}</loc><changefreq>{'weekly' if page['file'] in {'index.html', 'insights.html'} else 'monthly'}</changefreq><priority>{'1.0' if page['file'] == 'index.html' else '0.7'}</priority></url>"
        for page in PAGES
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nSitemap: https://tmo.it/sitemap.xml\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

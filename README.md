# Wilderness Rabbit Photography

A Django-powered portfolio & print store for a photographer. Browse a curated catalog, add favourites to a cart, and pay securely with Stripe. Images are served from Cloudinary for fast, responsive delivery.

![Hero screenshot placeholder](assets/read_me_img/mockup.png)

 **Live site:** <https://wilderness-rabbit-47634ce133dc.herokuapp.com>  
 **Repository:** <https://github.com/rory-codes/wildness_rabbit_photography>

 ## Table of Contents
- [Overview](#overview)
- [UX](#ux)
  - [Personas](#personas)
  - [User Stories (Agile)](#user-stories-agile)
  - [MoSCoW Prioritisation](#moscow-prioritisation)
  - [Sprint Plan](#sprint-plan)
- [Features](#features)
  - [Current](#current)
- [Data Model](#data-model)
- [Security, Performance & Accessibility](#security-performance--accessibility)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Production (Heroku)](#production-heroku)
  - [Local Development](#local-development)
- [Environment Variables](#environment-variables)
- [Credits](#credits)
- [License](#license)

---

## Overview
**Wilderness Rabbit Photography** is a full‑stack web app built with Django 5 that showcases a photographer’s portfolio and enables simple e‑commerce for prints. It focuses on a clean, mobile‑first gallery experience, fast media delivery, and an approachable checkout.

### Project goals
* Showcase images in a performance‑friendly grid and detail pages.  
* Convert interested visitors into customers via a frictionless cart/checkout.  
* Provide the owner with simple catalog management and order tracking.
* Use a range of software languages including HTML5, CSS3, JavaScipt, Python.
* Responsive gallery grid with server‑side pagination
* Photo detail pages (Cloudinary responsive images)
* Cart add/update/remove; mini‑cart indicator
* Stripe checkout with webhooks
* Account creation & email verification (django‑allauth)
* Testimonials
*  enquiries
*  Django admin for catalog management
*  Static files via WhiteNoise; production ready Procfile


## UX

### User profiles

| User profile | Summary | Key Goals |
|---|---|---|
| **Visitor (Guest)** | Lands on site from search/social | Browse gallery, filter by category, view large images, enquire or buy |
| **Registered Customer** | Returns to purchase | Faster checkout, saved address, view order history, leave testimonial |
| **Photographer (Site Owner)** | Manages content & orders | Upload images, set pricing/variants, approve testimonials, see orders |

### User Stories 
### Must haves
* **Browse the gallery (catalog list + pagination):** As a visitor, I want to browse the photo catalog so I can discover images to buy.
* **View photo detail:** As a visitor, I want a photo detail page so I can evaluate and buy.
* **Cart: add/update/remove:** As a shopper, I want to manage my cart so I can purchase multiple items.
* **Checkout with Stripe:** As a shopper, I want a secure checkout so I can pay and receive confirmation.
* **Allauth (signup/login/reset):** As a visitor, I want to create an account so I can track orders and checkout faster.
* **Profile & Order History:** As a customer, I want to update my profile and see past orders.
* **Testimonials & Enquiries:** As a visitor, I want to leave feedback or ask a question.
* **Owner: manage catalog:** As the photographer, I want to add/edit photos with prices and categories so I can run the shop.

### Should haves
* **Search & Filters:** As a visitor, I want to search and filter the gallery so I can find what I like quickly.
* **Favourites:** As a customer, I want to favourite photos so I can revisit them later.
* **Performance and image optimisation:** As a visitor, I want fast pages so the site feels snappy on mobile.
* **Basic shipping and tax configuration:** As a shopper, I want charges to be clear so there are no surprises.
* **Owner notifications:** As the photographer, I want alerts for new orders/enquiries so I can respond quickly.

### Could haves
* **Discount codes:** As a shopper, I want to apply a promo code so I can get a discount.
* **Guest checkout:** As a visitor, I want to check out as a guest so I don’t have to register.
* **Social media logins:** As a visitor, I want quick sign-in so I can avoid passwords.

#### Sprint Plan 
### Sprint 1 – Foundations & Auth (Must)

* **Goals:** Project scaffolding, deployment baseline, authentication.
* **Deliverables:** Working Django app on Heroku with web dyno; allauth flows; base templates; gallery & product detail read‑only; Cloudinary & WhiteNoise configured; error pages.
* **Definition of Done (DoD):** Deployed; lint passes; key happy‑path manual test plan complete. Risks/Mitigations: Env config drift → env sample & django-environ; Procfile/dynos → checklist.

### Sprint 2 – Catalog & Cart (Must)

* **Goals:** Shoppable catalog and robust basket.
* **Deliverables:** Add/update/remove cart; totals; messages; responsive cards; category pages.
* **DoD:** Unit tests for cart math; a11y checks; pagination stable under >100 items.

### Sprint 3 – Checkout & Orders (Must/Should)
* **Goals:** Payments, orders, profiles.
* **Deliverables:** Stripe checkout + webhooks; order creation; email receipts; profile with order history & saved address.
* **DoD:** Test cards succeed/fail; webhook idempotency; email previews.

### Sprint 4 – Content & Enhancements (Should/Could)
* **Goals:** Marketing & UX polish.
* **Deliverables:** Search/filter/sort; testimonials with moderation; enquiry form; SEO/sitemap; optional wishlist/lightbox/coupons/blog.
* **DoD:** Lighthouse ≥ 90 perf/a11y/best‑practices; docs updated; release notes.


## Features

### Wireframes
#### Desktop
![Desktop](assets/wireframes/wireframe_desktop.png)
#### Tablet
![Tablet](assets/wireframes/wireframe_tablet.png)
#### Mobile
![mobile](assets/wireframes/wireframe_mobile.png)

### Security, Performance & Accessibility
* **Security:** env‑based secrets; CSRF protection; HTTPS on production; webhook signature verification; admin limited to staff.
* **Performance:** Cloudinary transformations; lazy‑loading; compressed static files via WhiteNoise; DB indexing on common filters.
* **Accessibility:** Semantic HTML, focus states, aria labels on pagination & buttons; colour‑contrast checked; images include alt text.

---

### Technologies
* **Backend:** Python 3.13, Django 5.2, PostgreSQL (Heroku Postgres), SQLite (dev)
* **Auth:** django‑allauth
* **Payments:** Stripe
* **Media:** Cloudinary + `django-cloudinary-storage`
* **Styling/UI:** Django templates, crispy‑forms + crispy‑bootstrap5
* **Static & WSGI:** WhiteNoise, Gunicorn
* **Config:** `dj-database-url`, `python-dotenv`
* **Hosting:** Heroku (Heroku‑24 stack)

## Data Model
### Entity relationship diagram
![ER diagram](assets/read_me_img/er_diagram.png)
### Flow diagram
![Flow diagram](assets/read_me_img/flow_diagram.png)
### Stripe flow diagram
![Stripe flow diagram](assets/read_me_img/stripe_flow_diagram.png)
### Admin flow diagram
![Admin/Photographer flow diagram](assets/read_me_img/admin_photographer_flow.png)
### Photo/photo variant/cloudinary flow diagram
![Photo/variant/cloudinary flow diagram](assets/read_me_img/photo_variant_cloudinary_flow.png)

## Deployment
### Set up
#### Create and activate virtual enviromnent (venv):
* python -m venv .venv 
#### Install dependencies:
* pip install -r requirements.txt

### Local deployment
#### Apply database migrations:
* python manage.py makemigrations
* python manage.py migrate
#### Collect static files:
* python manage.py collectstatic
#### Update environment variables:
* DEBUG=False
* ALLOWED_HOSTS
* DATABASE_URL
#### Run the development server:
* python manage.py runserver
* This will open the application locally at: http://127.0.0.1:8000/

### Deployment to Heroku
#### Ensure required files are present:
* requirements.txt 
* Procfile (web: gunicorn wilderness_rabbit.wsgi)
#### Log in to Heroku and create an app:
* heroku login
* heroku create wilderness-rabbit
#### Set environment variables:
* heroku config:set DEBUG=False
* heroku config:set ALLOWED_HOSTS=wilderness-rabbit.herokuapp.com
* heroku config:set DATABASE_URL
#### Push to Heroku:
* git push heroku main
#### Run migrations and collect static files:
* heroku run python manage.py migrate
* heroku run python manage.py collectstatic
#### Open the deployed application:
* heroku open
* This will open the application at: https://wilderness-rabbit-47634ce133dc.herokuapp.com/
-
## Testing
### Manual testing
**Navigation**
**Catalog**
**Footer**
**Login/Signup(Allauth)**
**Enquiries**
**Testimonials**

## Issues/Fixes





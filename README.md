# Wilderness Rabbit Photography

A Django-powered portfolio & print store for a photographer. Browse a curated catalog, add favourites to a cart, and pay securely with Stripe. Images are served from Cloudinary for fast, responsive delivery.

![Hero screenshot placeholder](docs/screenshots/hero.png)

 **Live site:** <https://wilderness-rabbit-47634ce133dc.herokuapp.com>  
 **Repository:** <https://github.com/rory-codes/wildness_rabbit_photography>

 ## Table of Contents
- [Overview](#overview)
- [UX](#ux)
  - [Personas](#personas)
  - [User Stories (Agile)](#user-stories-agile)
  - [MoSCoW Prioritisation](#moscow-prioritisation)
- [Features](#features)
  - [Current](#current)
  - [Planned](#planned)
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

**Goals**
- Showcase images in a performance‑friendly grid and detail pages.  
- Convert interested visitors into customers via a frictionless cart/checkout.  
- Provide the owner with simple catalog management and order tracking.

## UX

### User profiles

| User profile | Summary | Key Goals |
|---|---|---|
| **Visitor (Guest)** | Lands on site from search/social | Browse gallery, filter by category, view large images, enquire or buy |
| **Registered Customer** | Returns to purchase | Faster checkout, saved address, view order history, leave testimonial |
| **Photographer (Site Owner)** | Manages content & orders | Upload images, set pricing/variants, approve testimonials, see orders |
| **Admin (Technical)** | Keeps the site healthy | Manage staff/admin access, view logs, moderate content |

### User Stories (Agile)
Stories are written in the format: _As a [persona], I want [goal] so I can [benefit]._  Each has **Acceptance Criteria** in **G/W/T** (Given / When / Then) style and **Tasks**.

### Must haves

#### Browse the gallery (catalog list + pagination)
**As a visitor, I want to browse the photo catalog so I can discover images to buy.**

#### View photo detail
**As a visitor, I want a photo detail page so I can evaluate and buy.**

#### Cart: add/update/remove
**As a shopper, I want to manage my cart so I can purchase multiple items.**

#### Checkout with Stripe
**As a shopper, I want a secure checkout so I can pay and receive confirmation.**

#### Auth (signup/login/reset)
**As a visitor, I want to create an account so I can track orders and checkout faster.**

#### Profile & Order History
**As a customer, I want to update my profile and see past orders.**

#### Testimonials & Enquiries
**As a visitor, I want to leave feedback or ask a question.**

#### Owner: manage catalog
**As the photographer, I want to add/edit photos with prices and categories so I can run the shop.**

### Should haves

#### Search & Filters
**As a visitor, I want to search and filter the gallery so I can find what I like quickly.**

#### Favourites
**As a customer, I want to favourite photos so I can revisit them later.**

#### Performance and image optimisation
**As a visitor, I want fast pages so the site feels snappy on mobile.**

#### Basic shipping and tax configuration
**As a shopper, I want charges to be clear so there are no surprises.**

#### Owner notifications 
**As the photographer, I want alerts for new orders/enquiries so I can respond quickly.**

### Could haves

#### Discount codes
**As a shopper, I want to apply a promo code so I can get a discount.**

#### Guest checkout
**As a visitor, I want to check out as a guest so I don’t have to register.**

#### Social media logins 
**As a visitor, I want quick sign-in so I can avoid passwords.**


### MoSCoW Prioritisation

**Must haves (MVP):** 1) Browse gallery, 2) Photo detail, 3) Cart, 4) Checkout (Stripe), 5) Auth, 6) Profile & orders, 7) Testimonials/Enquiries, 8) Owner catalog management via admin.

**Should haves:** 9) Search & filters, 10) Favourites, 11) Image optimisation, 12) Basic shipping/tax, 13) Owner notifications.

**Could haves:** 14) Discount codes, 15) Guest checkout, 16) Social login.

## Features

### Current
- Responsive gallery grid with server‑side pagination
- Photo detail pages (Cloudinary responsive images)
- Cart add/update/remove; mini‑cart indicator
- Stripe checkout with webhooks
- Account creation & email verification (django‑allauth)
- Profile page & order history
- Testimonials (with admin approval) & enquiries
- Django admin for catalog management
- Static files via WhiteNoise; production ready Procfile

### Planned
- Search & filter sidebar
- Favourites (wishlist)
- Coupons/discount codes
- Flat shipping/tax configuration
- Owner notifications for orders/enquiries
- Basic analytics dashboard

---

## Data Model


## Security, Performance & Accessibility
- **Security:** env‑based secrets; CSRF protection; HTTPS on production; webhook signature verification; admin limited to staff.
- **Performance:** Cloudinary transformations; lazy‑loading; compressed static files via WhiteNoise; DB indexing on common filters.
- **Accessibility:** Semantic HTML, focus states, aria labels on pagination & buttons; colour‑contrast checked; images include alt text.

---

## Technologies
- **Backend:** Python 3.13, Django 5.2, PostgreSQL (Heroku Postgres), SQLite (dev)
- **Auth:** django‑allauth
- **Payments:** Stripe
- **Media:** Cloudinary + `django-cloudinary-storage`
- **Styling/UI:** Django templates, crispy‑forms + crispy‑bootstrap5
- **Static & WSGI:** WhiteNoise, Gunicorn
- **Config:** `dj-database-url`, `python-dotenv`
- **Hosting:** Heroku (Heroku‑24 stack)


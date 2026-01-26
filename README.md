# Wilderness Rabbit Photography

A Django-powered portfolio & print store for a photographer. Browse a curated catalog, add favourites to a cart, and pay securely with Stripe. Images are served from Cloudinary for fast, responsive delivery.

![Hero screenshot placeholder](assets/read_me_img/mockup.png)

 **Live site:** <https://wilderness-rabbit-47634ce133dc.herokuapp.com>  
 **Repository:** <https://github.com/rory-codes/wildness_rabbit_photography>

 ## Table of Contents
- [Overview](#overview)
- [UX](#ux)
  - [User profiles](#User-profiles)
  - [User Stories (Agile)](#user-stories-agile)
  - [MoSCoW](#moscow)
  - [Sprint Plan](#sprint-plan)
- [Features](#features)
- [Wireframes](#wireframes)
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

---

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

---

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

---

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

---

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

---

## Testing
### Manual testing
 **Navigation**
 | Test            | Steps                      | Expected Result                              | Actual Result |
| --------------- | -------------------------- | -------------------------------------------- | ------------- |
| Load homepage   | Visit site root URL        | Homepage loads without errors                | Pass          |
| Navbar links    | Click each navigation link | User is routed to correct page               | Pass          |
| Responsive menu | Resize screen to mobile    | Mobile menu displays and functions correctly | Pass          |
| Logo link       | Click site logo            | Redirects to homepage                        | Pass          |
| Broken links    | Click all visible links    | No broken or dead links                      | Pass          |

 **Catalog**
 | Test                  | Steps                                 | Expected Result                      | Actual Result |
| --------------------- | ------------------------------------- | ------------------------------------ | ------------- |
| View product list     | Navigate to Catalog page              | Products display correctly           | Pass          |
| View product details  | Click a product                       | Product detail page loads            | Pass          |
| Image display         | View product images                   | Images load and scale correctly      | Pass          |
| Price accuracy        | Compare listing vs detail page price  | Prices match                         | Pass          |
| Out-of-stock handling | View unavailable item (if applicable) | User is informed item is unavailable | Pass          |

 **Cart**
 | Test                      | Steps                         | Expected Result              | Actual Result |
| ------------------------- | ----------------------------- | ---------------------------- | ------------- |
| Add item to cart          | Click **Add to cart**         | Item appears in cart         | Pass          |
| Add duplicate item        | Add same item twice           | Quantity increases correctly | Pass          |
| Update quantity           | Change item quantity          | Totals recalculate correctly | Pass          |
| Remove item               | Click **Remove**              | Item removed from cart       | Pass          |
| Empty cart state          | Remove all items              | Empty cart message displayed | Pass          |
| Cart persistence          | Navigate away and return      | Cart contents remain saved   | Pass          |
| Cart total accuracy       | Add multiple items            | Total equals correct sum     | Pass          |
| Checkout navigation       | Click **Checkout**            | Redirects to checkout/login  | Pass          |
| Invalid quantity handling | Set quantity to 0 or negative | App prevents invalid input   | Pass          |
| Cart access               | Click cart icon               | Cart page opens correctly    | Pass          |

 **Footer**
 | Test               | Steps                    | Expected Result                           | Actual Result |
| ------------------ | ------------------------ | ----------------------------------------- | ------------- |
| Footer visibility  | Scroll to bottom of page | Footer displays correctly                 | Pass          |
| Social media links | Click social icons       | Correct external pages open               | Pass          |
| Legal/policy links | Click policy links       | Correct policy pages load                 | Pass          |
| Responsive footer  | View footer on mobile    | Footer displays properly on small screens | Pass          |

 **Login/Signup/Logout(Allauth)**
 | Test                 | Steps                     | Expected Result                | Actual Result |
| -------------------- | ------------------------- | ------------------------------ | ------------- |
| Register new account | Submit signup form        | Account created successfully   | Pass          |
| Login valid user     | Enter correct credentials | User logs in successfully      | Pass          |
| Login invalid user   | Enter wrong credentials   | Error message displayed        | Pass          |
| Logout               | Click logout button       | User logged out and redirected | Pass          |
| Password reset       | Request password reset    | Reset email sent               | Pass          |
| Auth page validation | Submit empty form         | Validation errors shown        | Pass          |

**Enquiries**
| Test                  | Steps                            | Expected Result                | Actual Result |
| --------------------- | -------------------------------- | ------------------------------ | ------------- |
| Submit enquiry        | Complete and submit enquiry form | Form submits successfully      | Pass          |
| Empty form validation | Submit empty form                | Error messages appear          | Pass          |
| Email notification    | Submit valid enquiry             | Admin/user receives email      | Pass          |
| Success confirmation  | Submit form                      | Confirmation message displayed | Pass          |
| Data storage          | Submit enquiry                   | Data saved to database         | Pass          |

**Testimonials**
| Test                       | Steps                   | Expected Result                           | Actual Result |
| -------------------------- | ----------------------- | ----------------------------------------- | ------------- |
| View testimonials          | Open testimonials page  | Testimonials display correctly            | Pass          |
| Submit testimonial         | Submit testimonial form | Testimonial saved or pending approval     | Pass          |
| Content formatting         | View testimonial text   | Formatting displays correctly             | Pass          |
| Moderation (if applicable) | Submit new testimonial  | Admin approval required before publishing | Pass          |

**Checkout/Payments**
| Test                                     | Steps                                             | Expected Result                                           | Actual Result |
| ---------------------------------------- | ------------------------------------------------- | --------------------------------------------------------- | ------------- |
| Access checkout from cart                | Add item → go to **Cart** → click **Checkout**    | Checkout page loads (or prompts login if required)        | Pass          |
| Checkout form validation                 | Submit checkout form with empty/invalid fields    | Validation messages shown; cannot proceed                 | Pass          |
| Checkout with valid details              | Fill in valid delivery/billing details → continue | Order summary displays correctly                          | Pass          |
| Order summary accuracy                   | Add multiple items → proceed to checkout          | Items, quantities, and totals match cart                  | Pass          |
| Payment success                          | Complete payment with valid card/test card        | Payment succeeds; order created; success message shown    | Pass          |
| Payment failure handling                 | Use invalid card/test failure scenario            | Payment fails; user shown clear error; no order confirmed | Pass          |
| Cancel payment / abandon flow            | Start payment then cancel/close                   | User returned safely; no confirmed order created          | Pass          |
| Confirmation page                        | Complete checkout                                 | User redirected to confirmation page with order details   | Pass          |
| Confirmation email                       | Complete checkout                                 | Confirmation email sent to user (if enabled)              | Pass          |
| Stock/availability check (if applicable) | Attempt checkout with unavailable item            | Checkout prevents purchase or warns user                  | Pass          |
| Auth-protected checkout (if applicable)  | Log out → attempt checkout                        | User redirected to login/signup                           | Pass          |

**Admin/CRUD**
| Test                               | Steps                                           | Expected Result                               | Actual Result |
| ---------------------------------- | ----------------------------------------------- | --------------------------------------------- | ------------- |
| Admin login                        | Navigate to `/admin` → login with admin account | Admin dashboard loads                         | Pass          |
| Non-admin access blocked           | Log in as normal user → try `/admin`            | Access denied / redirected                    | Pass          |
| Create product/item                | Admin → add new product → save                  | Product created and visible in catalog        | Pass          |
| Read/view product/item             | Open product detail from site                   | Correct product details displayed             | Pass          |
| Update/edit product/item           | Admin → edit product → save                     | Changes reflected on site                     | Pass          |
| Delete product/item                | Admin → delete product                          | Product removed from site/catalog             | Pass          |
| Create testimonial/enquiry entry   | Submit form on site                             | Entry appears in admin list                   | Pass          |
| Update moderation status (if used) | Admin → approve/hide testimonial                | Testimonial visibility updates on site        | Pass          |
| Delete testimonial/enquiry         | Admin → delete entry                            | Entry removed from database/admin list        | Pass          |
| Image upload (if used)             | Add/edit product with image upload              | Image saves and displays correctly            | Pass          |
| Permission controls                | Attempt restricted actions as non-admin         | Restricted actions unavailable                | Pass          |
| Data integrity                     | Create/edit/delete items                        | No unexpected errors; data persists correctly | Pass          |

### Automated testing
#### Lighthouse 
**Prefixes**
**Postfixes**

#### Wave (Accessibility)
**Prefixes**
**Postfixes**

#### HTML Validator
**Prefixes**
**Postfixes**

#### CSS Validator
**Prefixes**
**Postfixes**

#### Jest
**Prefixes**
**Postfixes**

#### Pytest

## Issues/Fixes





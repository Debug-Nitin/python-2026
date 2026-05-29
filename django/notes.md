# Django Notes (restructured)

## Overview

- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- It follows the MTV (Model–Template–View) architectural pattern, which is similar to MVC but with different naming:
  - Model: data layer (ORM/database schema)
  - Template: presentation layer (HTML rendering)
  - View: request/response and business logic (acts like the controller in MVC)

## Project vs App

- Project: a single Django project (contains global settings, URL configuration, WSGI/ASGI entrypoints).
- App: a self-contained module that provides a specific piece of functionality (e.g., `coupons`, `blog`).
- A project can contain many apps; apps are reusable and help teams work independently.

## Typical Folder / File Levels

- Root (workspace) — may contain `README`, `requirements.txt`, etc.
- Project level — created with `django-admin startproject`, contains `manage.py` and the project package with `settings.py`, `urls.py`, `wsgi.py`/`asgi.py`.
- App level — created with `python manage.py startapp <appname>`, contains `models.py`, `views.py`, `tests.py`, `apps.py`, `migrations/`, `templates/`, `static/`.

## Default Database

- Default: SQLite (file-based) for quick development; configured in `settings.py` under the `DATABASES` setting.
- You can change to other engines (PostgreSQL, MySQL, MariaDB, etc.) by updating `DATABASES` and installing the appropriate DB driver.

## Middleware

- Middleware is a lightweight plugin system for processing requests and responses (configured in `settings.py` under `MIDDLEWARE`).
- Django includes several common middleware classes by default (security, session, authentication, CSRF protection, etc.).

## Request Flow (high level)

1. URL dispatcher (`urls.py`) matches the incoming path to a view.
2. View handles the request, interacts with models as needed, and returns a response (often rendering a template).
3. Template renders HTML using the context supplied by the view (if applicable).

## Useful Notes

- Check `settings.py` for project-wide configuration (databases, middleware, installed apps, templates).
- Use `manage.py` for common tasks: `runserver`, `migrate`, `makemigrations`, `createsuperuser`, `startapp`.
- Keep apps small and focused so they remain reusable across projects.

## Next steps you might want

- Expand any section into examples (e.g., sample `DATABASES` config, common middleware list).
- Add quick command cheatsheet for `manage.py` and common troubleshooting tips.

---

Updated and clarified for readability and correctness.

you can add templates in django in your way it is not defined in a particular way

we use render to return the template from views

there is templating engine in django it means you can insert your code in template anywhere

remember how to inject data in template

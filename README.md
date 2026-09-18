# Ethérea Pilates

Sitio web del estudio **Ethérea Pilates**: página única (one-page) construida con HTML, CSS y JavaScript puro, sin dependencias de build ni frameworks. Funciona abriendo `index.html` directamente o publicada en GitHub Pages.

## Estructura del proyecto

```
├── index.html              # Página principal (todas las secciones)
├── assets/
│   ├── css/style.css       # Estilos del sitio
│   ├── js/script.js        # Interactividad (menú, scroll, carrusel, formulario)
│   └── favicon.svg         # Ícono del sitio
└── .github/workflows/
    └── deploy.yml          # Publicación automática a GitHub Pages
```

## Secciones incluidas

- **Inicio**: hero con llamado a la acción y estadísticas.
- **Nosotros**: presentación del estudio.
- **Clases**: Reformer, Mat, Terapéutico, Privadas, Prenatal y Grupal.
- **Horarios**: tabla semanal de referencia.
- **Instructoras**: equipo del estudio.
- **Testimonios**: carrusel de opiniones.
- **Contacto**: datos de contacto, redes sociales y formulario (validación en el navegador, sin backend).

## Cómo personalizar tu información

Antes de publicar, actualiza estos datos en `index.html`:

1. **Contacto** (sección `#contacto`): dirección, teléfono/WhatsApp, correo y horario de atención.
2. **Redes sociales**: reemplaza los `href="#"` de `.social-links` con tus enlaces reales de Instagram, Facebook y WhatsApp.
3. **Equipo**: nombres, roles y descripciones en la sección `#instructoras`.
4. **Horarios**: ajusta la tabla en `#horarios` según tu disponibilidad real.
5. **Formulario de contacto**: actualmente es solo del lado del cliente (muestra un mensaje de confirmación pero no envía correos). Para recibir los mensajes de verdad, conéctalo a un servicio como Formspree, EmailJS o tu propio backend, cambiando el `action`/lógica de envío en `assets/js/script.js`.

## Cómo ver el sitio localmente

Solo abre `index.html` en tu navegador, o levanta un servidor simple:

```bash
python3 -m http.server 8000
# luego visita http://localhost:8000
```

## Cómo publicarlo (GitHub Pages)

Este repositorio incluye un workflow (`.github/workflows/deploy.yml`) que publica el sitio automáticamente en GitHub Pages con cada push a `main`.

Para activarlo:

1. Ve a **Settings → Pages** en tu repositorio de GitHub.
2. En **Source**, selecciona **GitHub Actions**.
3. Haz push a la rama `main` (o ejecuta el workflow manualmente desde la pestaña **Actions**).
4. Tu sitio quedará disponible en `https://<tu-usuario>.github.io/<nombre-del-repo>/`.

> Si esta es la primera publicación del repositorio, es posible que también debas definir `main` como rama predeterminada en **Settings → General → Default branch**.

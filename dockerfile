# Usamos la versión exacta que tenías
FROM odoo:17.0

# Copiamos tu archivo de configuración al sitio correcto dentro del contenedor
COPY ./config /etc/odoo

# Copiamos tus módulos (addons) dentro del contenedor
COPY ./addons /mnt/extra-addons

# Volvemos a ser el usuario odoo por seguridad
USER odoo
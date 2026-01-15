import everforest

# Cargar la configuración automática (el autoconfig.yml)
config.load_autoconfig()

import everforest

# Cargar el tema (puedes cambiar 'dark' por 'light' y 'hard' por 'medium' o 'soft')
everforest.set(c, scheme="dark", intensity="hard")
c.colors.webpage.darkmode.enabled = True

c.fonts.default_family = "JetBrains Nerd Font Mono"
c.fonts.hints = "bold 14pt default_family"
c.fonts.downloads = "default_family"
c.fonts.contextmenu = "default_family"
c.fonts.messages.error = "default_family"
c.fonts.messages.info = "default_family"
c.fonts.messages.warning = "default_family"
c.fonts.prompts = "default_family"
c.fonts.statusbar = "default_family"
c.fonts.tabs.selected = "default_family"
c.fonts.tabs.unselected = "default_family"
c.fonts.tooltip = "default_family"
c.fonts.completion.entry = "default_family"  # Era 'completation'
c.fonts.completion.category = "default_family"  # Era 'category'
c.hints.padding = {"top": 2, "bottom": 2, "left": 5, "right": 5}
c.hints.radius = 2

c.zoom.default = 125

# barra de pestañas abajo
c.tabs.position = "bottom"

c.downloads.location.directory = "~/Downloads"

# No preguntar dónde guardar (descarga directa)
c.downloads.location.prompt = False

# Posición de la barra de descargas (abajo)
c.downloads.position = "bottom"

# Cantidad máxima de descargas visibles
c.downloads.remove_finished = 15000

# Guardar la sesión automáticamente al cerrar
c.auto_save.session = True

c.content.autoplay = False

c.scrolling.smooth = True

# --- BLOQUEO DE ANUNCIOS (ADBLOCK) ---
# sudo pacman -S python-adblock
# Activar el motor de bloqueo nativo
c.content.blocking.enabled = True
c.content.blocking.method = "both"

# Listas de bloqueo (puedes añadir más si quieres)
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
]

# Presiona 'alt-p' para alternar el bloqueo de publicidad
config.bind("<Alt-p>", "config-cycle content.blocking.enabled true false")

# Intercambiar J y K para la navegación de pestañas
config.bind("J", "tab-prev")
config.bind("K", "tab-next")

# Atajo para alternar el modo oscuro en la página actual
config.bind("<Alt-d>", "config-cycle colors.webpage.darkmode.enabled true false")

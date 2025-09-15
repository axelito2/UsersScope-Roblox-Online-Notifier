# UsersScope - Roblox Online Notifier

**UsersScope** es un pequeño script en Python que permite monitorear el estado de usuarios de Roblox y enviar notificaciones a un canal de Discord vía webhook cuando el usuario está online o jugando.

---

## Características
- Consulta si un usuario de Roblox está online, offline, jugando o en estudio.
- Envía notificaciones a un webhook de Discord.
- Muestra la información de DisplayName y Username en la consola.
- Incluye mensajes y banners ASCII para hacerlo más visual en consola.

---

## Requisitos
- Python 3.7 o superior
- Librerías:
  - `requests`  
  Puedes instalarla con:
  ```bash 
  pip install requests
  ```
---

## Uso
1. Clona el repositorio
  ```bash
  git clone https://github.com/tuusuario/UsersScope.git
  ```
2. En la terminal, ejecuta el script
   ```bash
    python main.py
   ```
3.Ingresa el UserId de Roblox que quieres monitorear y tu DiscordId para recibir las notificaciones.

4.El bot comenzará a enviar mensajes al webhook cada 2 minutos indicando el estado del usuario.

## Seguridad
- Nunca compartas tu webhooks `UserData` si vas a subirlo como modificacion
- Esto es para uso personal y educativo. RESPETA LOS TERMINOS DE USO DE ROBLOX Y DISCORD. NO ME HAGO RESPONSABLE DE DAÑOS!

## Creditos
-Roblox and Discord: @axelitogamertv2

Eso es todo. Usenlo con cuidado. :P

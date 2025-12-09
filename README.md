# Sistema de Control con RFID y Dashboard en Tiempo Real  
ESP32 + Python Flask + SSE

## 📌 Descripción General
Este proyecto implementa un sistema de registro de entradas y salidas utilizando un lector RFID conectado a un ESP32.  
Cada vez que una tarjeta es detectada, el ESP32 envía la información al servidor Python (Flask), el cual transmite los eventos a un dashboard web en tiempo real mediante Server-Sent Events (SSE).

El sistema permite visualizar el estado actual de cada tarjeta (dentro/fuera) y un historial básico de eventos.

---

## 📡 Componentes Utilizados

### **Hardware**
- ESP32
- Lector RFID RC522
- Tags RFID
- Conexión WiFi
- Equipos ubiquiti nanostation

### **Software**
- Python 3
- Flask (servidor web)
- HTML/CSS/JavaScript (dashboard)
- Arduino IDE para programar el ESP32

---

## 📂 Estructura del Proyecto
### **Servidor**
- servidor.py
- static/dashboard.html
### **Programa ESP 32**
- arduinoFinalEnfaIV/arduinoFinalEnfaIV.ino
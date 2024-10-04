# Vanguard - Mejora en la Interfaz de Usuario (UI) y Análisis de Rendimiento

## Descripción del Proyecto
**Vanguard**, una de las principales compañías de gestión de inversiones en los EE. UU., ha lanzado una interfaz de usuario (UI) modernizada para mejorar la experiencia digital de sus clientes. Esta nueva UI busca ofrecer un recorrido más intuitivo con indicaciones contextuales, permitiendo una navegación más fluida y eficiente.

El objetivo principal de este proyecto es analizar si la nueva UI ha incrementado la tasa de finalización de los usuarios y estudiar su comportamiento tras la implementación.

## Pregunta Clave
- **¿La nueva interfaz de usuario (UI) llevó a tasas de finalización más altas para los clientes de Vanguard?**

---

## Descripción General de los Datos

Los datos utilizados para el análisis se dividen en tres categorías principales:

1. **Perfiles de Clientes (Client Profiles)**  
   - Información sobre: antigüedad, edad, género, número de cuentas, saldo total y frecuencia de interacción.
   
2. **Huella Digital (Digital Footprints)**  
   - Registros de las interacciones de los clientes con el sitio web:  
     - Pasos del proceso.  
     - Marcas de tiempo.  
   
3. **Lista del Experimento (Experiment Roster)**  
   - Detalles sobre la asignación de clientes a grupos de control (interfaz tradicional) y de prueba (nueva interfaz).

---

## Análisis Exploratorio de Datos (EDA)

### 1. Demografía de los Clientes
El análisis de los perfiles reveló las siguientes características demográficas:
- **Edad promedio de los clientes**.
- **Antigüedad promedio** con Vanguard.
- **Distribución por género**.
- **Distribución por número de cuentas**.
- **Saldo total por cliente**.

![image](https://github.com/user-attachments/assets/49b1f0fd-f8d4-4424-bae2-1504c6ab9dab)


![image](https://github.com/user-attachments/assets/f28d669b-7290-477d-92bb-90eccf3149d1)

![Captura de pantalla 2024-10-04 141214](https://github.com/user-attachments/assets/63c3b005-423c-47a6-bd96-b8c81eaf08b2)

![Captura de pantalla 2024-10-04 141353](https://github.com/user-attachments/assets/d2143034-01f8-464e-b8a3-9a3bf17b4014)

### 2. Comportamiento de los Clientes
Análisis de la interacción digital de los clientes, donde se encontró:
- **Promedio de inicios de sesión** en los últimos 6 meses.
- **Número promedio de llamadas al servicio al cliente** en los últimos 6 meses.
- **Pasos de navegación más frecuentes** y **errores que afectan la usabilidad**.

![image](https://github.com/user-attachments/assets/9c8d816e-31da-417c-a3bd-e8261f7119bf)

![image](https://github.com/user-attachments/assets/3c81794a-6a44-4f65-b880-5d04763722eb)

---

## Métricas de Rendimiento (KPI)

1. **Tasa de Finalización (Completion Rate):**  
   Proporción de usuarios que completan todo el proceso llegando al paso de "confirmación".  
   _Un aumento en esta métrica indicaría una mejor experiencia de usuario._

2. **Tiempo Promedio en Cada Paso (Time Spent on Each Step):**  
   Evalúa si la nueva UI reduce el tiempo necesario para completar cada etapa del proceso.

3. **Tasa de Errores (Error Rates):**  
   Mide el porcentaje de usuarios que retroceden en el proceso, lo que puede indicar problemas de usabilidad.

---

## Pruebas de Hipótesis

### Hipótesis 1: Eficiencia de la Nueva UI  
- **Hipótesis Nula (H0):** No hay diferencia en la tasa de finalización entre el grupo de control (UI tradicional) y el grupo de prueba (nueva UI).  
- **Hipótesis Alternativa (H1):** La tasa de finalización es mayor en el grupo de prueba en comparación con el grupo de control.

### Hipótesis 2: Diferencias por Demografía  
- **Hipótesis Nula (H0):** No hay diferencias significativas en la tasa de finalización entre distintos grupos demográficos.  
- **Hipótesis Alternativa (H1):** Existen diferencias significativas en la tasa de finalización entre los grupos demográficos en el grupo de prueba.

---

## Conclusiones

- **Rechazo de la Hipótesis Nula (H0):**  
   La nueva interfaz de usuario mostró un aumento significativo en la tasa de finalización del proceso en comparación con la UI tradicional, apoyando la hipótesis alternativa (H1). Además, se observaron diferencias en la tasa de finalización según los grupos demográficos.
   
- **Efectividad de la Nueva Interfaz:**  
   Las innovaciones implementadas, como las indicaciones contextuales, han mejorado la usabilidad y accesibilidad, resultando en un proceso más fluido y en un aumento de la satisfacción del cliente.

![image](https://github.com/user-attachments/assets/529fb387-f4c5-491a-97e1-29504566d74f)



---

## Resumen de Hallazgos Clave

- **Tasa de Finalización:**  
   La nueva UI aumentó significativamente la tasa de finalización en comparación con la UI anterior.
  
- **Satisfacción del Cliente:**  
   La interfaz renovada mejoró el proceso, haciéndolo más accesible y eficiente para los usuarios.

---

Para más detalles sobre el análisis y los datos, consulte los archivos correspondientes.

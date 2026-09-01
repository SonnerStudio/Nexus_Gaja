# Nexus Gaja

> *Por la paz global y el entendimiento mutuo*


![Nexus Gaja Logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** es una red de comunicación inteligente y sensible al contexto diseñada para revolucionar la comunicación global.

## Propósito y Visión

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

En un mundo globalizado, el idioma suele ser la mayor barrera. El objetivo principal de Nexus Gaja es permitir una comunicación fluida, sin barreras y contextualmente precisa entre las personas, independientemente de si hablan un idioma común.

No se trata solo de traducir palabras rígidamente, sino de **transferir significado**. Nexus Gaja conecta a las personas a un nivel más profundo al comprender matices culturales, regionales y contextuales, permitiendo así conversaciones genuinas y auténticas.

## Posibilidades y Características
- **Comunicación Multimedia**: El sistema procesa no solo texto, sino también imagen, audio y video. Esto permite conversaciones totalmente inmersivas (p. ej., videollamadas o mensajes de voz) en tiempo real a través de las barreras del idioma.
- **Sensibilidad al Contexto**: Reconocimiento de ironía, modismos, jerga y dialectos regionales que los traductores convencionales a menudo malinterpretan.
- **Red Multiplataforma**: Sirve como base para chats privados, hilos de foros (publicaciones con comentarios) e interacciones de la comunidad global.

---

## Arquitectura Técnica (Concepto Central)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

El núcleo técnico de Nexus Gaja es un modelo de comunicación desarrollado a medida que se divide estrictamente en tres capas:

1. **Original**: El objeto de comunicación (mensaje) creado por el remitente siempre permanece inmutable.
2. **Interpretación Semántica**: El sistema analiza no solo las palabras, sino el significado real.
3. **Representación en el Idioma de Destino**: La IA simplemente crea una representación temporal o en caché del original para el destinatario respectivo en función de su idioma preferido. Las traducciones nunca sobrescriben el mensaje original.

### Dependencia del Contexto
Las traducciones en Nexus Gaja nunca ven los mensajes de forma aislada. El motor considera toda la jerarquía:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Eficiencia mediante Traducción Bajo Demanda
La traducción se produce de manera eficiente en cuanto a recursos solo **bajo demanda**. Cuando un usuario solicita contenido, se traduce a su idioma predeterminado. Una vez generada una traducción para un idioma específico, se almacena de forma permanente (caché) para acelerar drásticamente futuras solicitudes.

## Moderación Asistida por IA (WP 1.8.4)

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

Con la Moderación Asistida por IA, damos un paso importante desde la idea del producto hacia la arquitectura técnica, teniendo en cuenta las normativas actuales de la UE (requisitos de transparencia de la Ley de IA de la UE según el Art. 50; Ley de Servicios Digitales con justificaciones comprensibles y opciones de apelación).

### 1. Principio Básico
La frase más importante para la arquitectura es: **La IA de moderación es un sistema de revisión, no un sistema de gobierno autónomo.**
Está diseñada para ayudar a los humanos en la moderación, no para determinar por sí misma qué opiniones pueden existir en Nexus Gaja.
Diferenciamos tres niveles:
- **Detección:** "Podría haber una violación de las reglas aquí".
- **Evaluación:** "La probabilidad de una violación de las reglas es, por ejemplo, del 94%".
- **Decisión:** "¿Qué medida se tomará realmente?"
El tercer nivel debe ser controlado por un humano en casos graves.

### 2. La IA de Moderación como Subsistema
En lugar de una sola IA, se establece un subsistema robusto:
```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Language AI        Safety AI          Fraud AI
       │                  │                  │
       ├──────────────┬───┴──────────────┬───┤
       │              │                  │
 Translation      Behaviour          Identity
 Analysis         Analysis            Signals
       │              │                  │
       └──────────────┼──────────────────┘
                      ▼
               Risk Assessment
                      │
                      ▼
               Human Review
```

### 3. Los Módulos de IA Más Importantes
Nexus Gaja utiliza nueve áreas de análisis especializadas:
- **M1 – Language Understanding**: Detecta idioma, dialecto, jerga, indicadores de ironía, problemas de traducción.
- **M2 – Toxicity / Abuse Detection**: Detecta insultos, ataques personales, acoso.
- **M3 – Threat Detection**: Detecta posibles amenazas, chantaje, anuncios de violencia.
- **M4 – Hate / Dehumanization Detection**: Detecta ataques dirigidos contra personas debido a afiliaciones específicas.
- **M5 – Spam / Manipulation Detection**: Detects spam, comportamiento de bots, manipulación coordinada.
- **M6 – Fraud Detection**: Detecta intentos de fraude sospechosos, phishing, ingeniería social.
- **M7 – Identity Integrity**: Verifica señales relacionadas con el robo de cuentas, múltiples cuentas, evasión de bloqueos.
- **M8 – Media Safety**: Analiza imágenes, audio, video, documentos.
- **M9 – Context Engine**: El módulo más importante. Reúne los hallazgos individuales.

### 4. Por qué el Motor de Contexto es Crucial
Una simple búsqueda de palabras clave sería insuficiente. "Me muero de risa con él" semánticamente contiene violencia pero es una expresión figurada. "Mañana a las 20:00 le dispararé frente a su casa" es una situación completamente diferente. La IA debe entender qué significa la declaración en su contexto específico.

### 5. Moderación Multilingüe
La moderación no puede simplemente comparar palabras. Debe analizar el nivel semántico (p. ej., modismos alemanes vs. modismos japoneses vs. expresiones regionales).

### 6. Idioma Original + Traducción
El original y la traducción se analizan por separado. Solo entonces tiene lugar el "Combined Moderation Assessment". Esto permite a Nexus Gaja determinar si la traducción en sí pudo haber agravado o alterado los hechos.

### 7. Puntuación de Confianza (Confidence Score)
Cada evaluación de IA recibe una puntuación de confianza (p. ej., Probabilidad de amenaza: 0.96). Sin embargo: **Puntuación de Confianza ≠ Verdad.** Una puntuación del 96% solo significa que el modelo está muy seguro de su clasificación, no necesariamente que el usuario sea culpable.

### 8. La Incertidumbre se Convierte en una Señal
Si la IA está insegura (p. ej., Amenaza: 0.62, Sátira: 0.54), no debe simplemente aplicar reglas estrictas. En cambio, la incertidumbre se integra directamente en la arquitectura: **Human Review Required** (Se requiere revisión humana).

### 9. Cuatro Zonas de Decisión
- 🟢 **GREEN**: Altamente probable que cumpla con las normas. → sin acción.
- 🟡 **YELLOW**: Posible violación. → observar / proporcionar una advertencia si es necesario.
- 🟠 **ORANGE**: Probable violación. → revisión de moderación.
- 🔴 **RED**: Posible violación grave. → medida de protección inmediata + revisión humana.

### 10. No hay "Castigo de IA"
**La IA no impone sanciones finales.** Puede activar medidas técnicas inmediatas (p. ej., retener temporalmente un mensaje) por graves problemas de seguridad, pero la decisión final sigue siendo verificable.

### 11. Las Medidas de Protección Pueden Ocurrir Automáticamente
En caso de una amenaza concreta (Threat detected → High confidence → Temporary restriction → Human review → Decision), protegemos al usuario amenazado sin convertir a la IA en juez.

### 12. La IA Debe Poder Justificar Sus Decisiones
La DSA requiere razones claras y específicas. La IA proporciona un razonamiento estructurado: Regla (NG-CONDUCT-004), Detectado (Posible amenaza concreta), Confianza (0.94), Contexto relevante (4 mensajes anteriores), Acción recomendada (Revisión humana).

### 13. La IA No Debe Alterar el Contenido en Secreto
**La IA de moderación nunca debe alterar el contenido original sin que se note.** Durante la corrección automática, la traducción o el resumen, el original siempre se conserva.

### 14. Contenido Generado por IA
Distinguimos entre: Creado por humanos, Asistido por IA, Generado por IA y Manipulado por IA. Esto pasará a formar parte de los metadatos del contenido.

### 15. Etiquetado de Contenido de IA y Capa de Procedencia de IA
Según las reglas de transparencia de la Ley de IA de la UE (vigente en agosto de 2026), el contenido generado por IA debe ser identificable. Proporcionamos una capa de procedencia de IA (AI Provenance Layer) que almacena metadatos (Origen de IA, Modelo, Marca de tiempo, Revisión humana).

### 16. Detección de Deepfakes
La arquitectura tiene como objetivo detectar imágenes sintéticas, voces clonadas y deepfakes. Sin embargo, la detección no es automáticamente una prueba.

### 17. No hay "Máquina de la Verdad" Automática (Moderación ≠ Fact Checking)
Un sistema verifica: "¿Viola el contenido las reglas?" (Content Moderation), otro proporciona: "¿Qué información y fuentes hay disponibles?" (Information Assistance). Las opiniones no se eliminan simplemente por ser "incorrectas".

### 18. Protección Contra Malas Interpretaciones Culturales
La IA requiere **Modelos de Contexto Cultural** para evitar que las normas de comunicación de un país se asuman como un estándar global.

### 19. Ironía, Sátira y Humor
La IA utiliza el contexto, emojis, el historial de conversaciones y estructuras de ironía conocidas, pero debe permitir la incertidumbre cuando los significados son ambiguos.

### 20. Ningún Castigo Basado en una Sola Puntuación de IA
Ninguna intervención de moderación severa puede basarse únicamente en un solo resultado de clasificación automatizada (Texto + Contexto + Comportamiento + Idioma + Medios + Motor de Reglas = Evaluación de Riesgos).

### 21. Señales de Comportamiento del Usuario y Sin Sistema de Crédito Social
This relates to technical abuse signals (e.g., massive spamming), not a general social credit system. Nexus Gaja does not maintain a Social Credit System: moderation serves safety, not evaluating a person's value.

### 22. La IA de Moderación Debe Ser Auditable
Todas las decisiones automatizadas relevantes se registran (Event-ID, Rule-ID, Confidence, Human-Review, etc.) para garantizar la trazabilidad.

### 23. Falsos Positivos, Falsos Negativos y Métricas de Calidad
Se monitorean los tipos de errores. Un panel mide la Precisión, la Exhaustividad (Recall) y, especialmente, la **Tasa de Reversión de Apelaciones** (Appeal Reversal Rate: número de apelaciones exitosas).

### 24. Equidad Lingüística y Sesgo de Traducción
La calidad de la moderación debe ser comparable en todos los idiomas admitidos (Benchmark de Moderación Multilingüe). Si los resultados de la moderación difieren entre el original y la traducción (Conflicto de Traducción), esto debe revisarse específicamente.

### 25. Propuesta de Arquitectura y Motor de Políticas
Las reglas (Policy Engine) no están codificadas de forma rígida en los modelos de IA. La IA proporciona hallazgos; el Policy Engine decide en base a las reglas actuales. Esto permite **cambios de modelo sin cambios de reglas**.

### 26. El Humano Sigue Siendo la Autoridad Final
- **NG-AI-MOD-001**: La IA ayuda en la detección y clasificación, pero no reemplaza la revisión humana en decisiones severas.
- **NG-AI-MOD-002**: Las decisiones de moderación automatizada deben ser rastreables, registrables y verificables.

**Resumen**: Estamos construyendo un sistema de cuatro etapas: Detección de IA, Análisis de Contexto y Riesgo, Motor de Políticas (Policy Engine) y Gobernanza Humana. Esto permite una fuerte automatización sin crear una peligrosa arquitectura de "IA como Juez".

## Principios de Financiación y Modelo de Ingresos (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

Para Nexus Gaja se aplica un principio económico sumamente importante: **Sin publicidad tradicional dentro de la plataforma.**
Esto distingue fundamentalmente a Nexus Gaja de muchas de las redes sociales actuales. Sin embargo, esto no significa que Nexus Gaja no pueda tener un carácter comercial. Por el contrario, la plataforma debe ser económicamente viable para que su propósito social pueda perdurar. La actividad económica es un medio para un fin, no el propósito principal de la plataforma.

### 1. Principio NG-FIN-001
Nexus Gaja financia sus operaciones a través de fuentes de ingresos transparentes y separadas de los intereses de los usuarios, y no mediante la monetización de la atención o los datos personales de sus usuarios.

### 2. Sin Publicidad Tradicional
Están específicamente prohibidos:
- Anuncios tipo banner
- Anuncios emergentes (Pop-ups)
- Videos publicitarios de reproducción automática
- Publicaciones patrocinadas en el feed estándar
- Perfiles publicitarios personalizados
- Venta de perfiles de usuario o datos personales
- Publicidad derivada de conversaciones privadas.

Nexus Gaja sigue siendo un **espacio de comunicación en lugar de un espacio publicitario**.

### 3. Financiación Sin Publicidad (Los 6 Pilares)
La financiación se basa en seis pilares:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   PREMIUM       ORGANIZACIÓN    DONACIONES
       │             │             │
       ├─────────────┼─────────────┤
       ▼             ▼             ▼
  SUBVENCIONES   ASOCIACIONES    SERVICIOS
```

#### Pilar 1 – Membresía Básica Gratuita
**Nexus Gaja Free** permite el entendimiento internacional básico para todos (perfil, comunicación internacional, publicaciones, comunidades, chats, traducción básica) sin costo alguno.

#### Pilar 2 – Ofertas Premium
Ofertas de pago voluntario (**Nexus Gaja Plus**) que proporcionan mayores límites de almacenamiento, mayor calidad multimedia, mayores cuotas de IA y funciones organizativas.
**Importante (Freemium en lugar de Dark Freemium):** La comunicación básica nunca debe ser degradada artificialmente.

#### Pilar 3 – Organizaciones
Cuentas especiales para escuelas, universidades, ONG, empresas y municipios (**Nexus Gaja Organization**). Las escuelas pueden recibir apoyo mediante tarifas institucionales como multiplicadores del entendimiento internacional.

#### Pilar 4 – Donaciones
El **Fondo de Financiación de Nexus Gaja** acepta donaciones generales y asignadas (ej. "para comunicación juvenil internacional"). Un **Ledger de Asignación de Fondos** garantiza la asignación transparente.
**Fondo de Propósito y Tómbola:** Una parte de las donaciones alimenta un fondo para uso gratuito o con descuento. Un mecanismo de tómbola puede asignar estos fondos de forma transparente y auditable.

#### Pilar 5 – Financiación Institucional
Fundaciones, programas de financiación cultural o programas estatales.
**NG-FIN-002:** El apoyo financiero no compra el control editorial ni técnico (Independencia).

#### Pilar 6 – Servicios Comerciales
Servicios B2B como **Traducción como Servicio** (API), comunicación organizativa o salas de conferencias internacionales, sin sobrecargar el feed estándar del usuario.

### 4. Sin Monetización de Datos y Economía de Vigilancia
**NG-FIN-003:** Los datos personales de los usuarios no son una mercancía. No hay venta de listas, perfiles ni historiales. Nexus Gaja no se beneficia de la vigilancia psicológica (Economía de Vigilancia).

### 5. Transparencia Financiera y Libro de Fondos
**Transparencia Financiera de Nexus Gaja:** Publicación de estructuras financieras agregadas. Las donaciones asignadas reciben contabilidad técnica (ID de Fondo → Propósito → Saldo → Asignación). No hay subsidios cruzados de fines sociales hacia el marketing corporativo.

### 6. Modelo de Financiación Solidaria
Los precios se basan en la orientación a los costos, la equidad y la solidaridad.
**Premium Solidario:** Opción voluntaria para que los usuarios Premium financien parte del acceso de otro usuario. La solidaridad forzada o una sociedad de clases premium (menos respeto/moderación para los usuarios gratuitos) está estrictamente prohibida.

### 7. KPI Económicos en Lugar de Economía de Interacción
Sin dependencia de mantener a los usuarios "en línea el mayor tiempo posible" (sin ragebait, feeds infinitos).
En su lugar, utilizamos métricas como:
- **Índice de Comunicación Global (GCI):** Relaciones de comunicación exitosas entre personas de diferentes regiones lingüísticas/culturales.
- **Ratio de Sostenibilidad de la Plataforma (PSR):** Ingresos recurrentes / costos operativos recurrentes (Objetivo ≥ 1).

### 8. Lo que Expresamente NO Queremos (Lista Negativa)
Nexus Gaja **no** se financia a través de:
❌ Venta de datos personales
❌ Publicidad tradicional personalizada
❌ Monitoreo del comportamiento del usuario para fines publicitarios
❌ Venta de datos de comunicación privados
❌ Uso oculto de datos para la IA
❌ Barreras de pago Premium manipulativas
❌ Restricción artificial de alcance para monetización
❌ Influencia política pagada
❌ Compra de decisiones de moderación privilegiadas.

### 9. Arquitectura Financiera Preliminar
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
          USERS          ORGANIZATIONS      ENTERPRISE
             │                │                │
             └────────────────┼────────────────┘
                              │
                       PLATFORM SERVICES
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       PREMIUM             DONATIONS            API
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
               GENERAL FUND       RESTRICTED FUNDS
                                        │
                                        ▼
                                  SOCIAL PURPOSE
```

### Resumen de Principios de Financiación (NG-FIN)
- **NG-FIN-001:** Sin financiación a través de publicidad tradicional.
- **NG-FIN-002:** Sin control editorial/técnico a través del apoyo financiero.
- **NG-FIN-003:** Los datos personales no son una mercancía.
- **NG-FIN-004:** La comunicación básica sigue siendo accesible sin pago.
- **NG-FIN-005:** Las ofertas Premium no deben degradar a los usuarios gratuitos.
- **NG-FIN-006:** Los fondos asignados se gestionan según su propósito.
- **NG-FIN-007:** Gestión transparente de donaciones y subvenciones.
- **NG-FIN-008:** Los servicios B2B comerciales no comprometen la independencia.
- **NG-FIN-009:** Enfoque en la sostenibilidad en lugar de la máxima monetización.
- **NG-FIN-010:** La estructura asegura de forma permanente el propósito social.

## Arquitectura de API, Interfaces y Comunicación (WP 1.11.3)

Para garantizar la estabilidad, seguridad y escalabilidad del sistema, Nexus Gaja sigue estrictamente una arquitectura basada en API y orientada a eventos.

### Principios Fundamentales
- **Sin acceso directo a bases de datos:** Los componentes se comunican exclusivamente a través de interfaces definidas (APIs o Eventos), nunca mediante consultas directas a las bases de datos de otros servicios.
- **API Gateway:** Todas las peticiones externas de clientes pasan por un API Gateway que gestiona la autenticación, el enrutamiento y la limitación de peticiones.
- **Abstracción de Proveedores:** Los servicios externos (modelos de IA, proveedores de pago, motores de traducción) se integran a través de capas de abstracción. Esto evita dependencias rígidas y permite cambiar de proveedor de forma flexible.

### Patrones de Comunicación
- **APIs Síncronas (REST/HTTPS):** Se utilizan para peticiones inmediatas como inicio de sesión, configuración de perfiles o traducciones directas.
- **Eventos Asíncronos (Event Bus):** El sistema nervioso central de Nexus Gaja para procesos desacoplados y en diferido (ej. `Message.Created` desencadena de forma asíncrona la moderación, la traducción y las notificaciones).
- **Tiempo Real (WebSocket):** Canales dedicados para el chat en vivo y los indicadores de estado de escritura.

### Seguridad y Fiabilidad
- **Modelo Zero-Trust:** El tráfico de red interno no es automáticamente de confianza; la comunicación sensible entre servicios requiere autenticación.
- **Idempotencia y Patrón Outbox:** Las operaciones críticas (como donaciones o mensajes) están diseñadas para ser idempotentes y evitar el procesamiento duplicado, utilizando el patrón Outbox para asegurar que los eventos nunca se pierdan incluso durante transacciones de base de datos.

## Modelo de Dominio MVP (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja emplea una arquitectura estrictamente orientada al dominio (ADR-025), diseñada como un monolito modular con límites claros. Esto previene la complejidad prematura de los microservicios, manteniendo la flexibilidad para separarlos más adelante.

### Entidades Centrales
La arquitectura separa conceptos explícitamente para asegurar la integridad de los datos y evitar errores como "Nombre de usuario = Persona":
- **Identidad y Cuentas:** `Person` ≠ `User Account` ≠ `Identity Verification`. Una persona verificada participa mediante una cuenta, pero las entidades permanecen separadas.
- **Comunicación:** `Message` ≠ `Translation`. El mensaje original es inmutable; las traducciones son entidades vinculadas.
- **Moderación:** `Report` ≠ `Moderation Decision`. Un reporte es solo un aviso; un caso de moderación realiza la investigación.
- **Finanzas:** `Donation` ≠ `Fund Balance`. Los pagos se registran mediante un libro mayor (ledger) inmutable.

### Dominios Interconectados
El sistema se divide en dominios lógicos (Bounded Contexts): Identidad, Cuenta, Organización, Comunicación, Comunidad, Idioma, Moderación, Notificación, Finanzas y Gobernanza.

## Estado del Proyecto
El proyecto se encuentra en la fase activa de arquitectura y planificación.
Las decisiones arquitectónicas en curso se documentan en la carpeta `/docs`.

---

## Licencia y Propiedad Intelectual

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Todos los derechos reservados.**

**Nexus Gaja** es propiedad intelectual exclusiva de **Jan Friske**, que opera bajo **SonnerStudio**.

Jan Friske es el único creador, arquitecto y propietario de Nexus Gaja, incluyendo todos los conceptos, arquitecturas, modelos de dominio, identidad de marca y documentación asociada.

**Ningún derecho, licencia o interés de propiedad es otorgado a terceros**, independientemente de su tamaño, posición en el mercado o influencia en la industria tecnológica.

### Lo que NO está permitido sin consentimiento escrito explícito:
- ❌ Copiar, reproducir o distribuir este software o su documentación
- ❌ Modificar, adaptar o crear obras derivadas
- ❌ Uso comercial de cualquier parte de Nexus Gaja
- ❌ Usar el contenido de este repositorio como **datos de entrenamiento para sistemas de IA/LLM**
- ❌ Sublicenciar o transferir derechos a terceros

### Contacto
Para consultas de licencias: [github.com/SonnerStudio](https://github.com/SonnerStudio)

➡️ Ver términos completos de licencia en [LICENSE](LICENSE)

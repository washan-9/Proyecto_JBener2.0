# Design System Document · JBener Dashboard
> Basado en el análisis visual del dashboard Stakent — adaptado al proyecto JBener

**Versión:** 1.0  
**Fecha:** Marzo 2026  
**Referencia visual:** Stakent · Top Staking Assets

---

## 1. Filosofía de Diseño

El diseño sigue una estética **dark financial** — densa en información pero nunca caótica. Cada elemento tiene un propósito funcional. La jerarquía visual guía al usuario desde lo macro (métricas globales) hacia lo micro (detalle de un activo) sin fricción.

**Principios clave:**
- **Densidad con aire** — mucha información en pantalla, pero con padding generoso que evita la sensación de agobio.
- **Color como señal, no decoración** — el naranja/verde/rojo comunica estado, no estética.
- **Tipografía como dato** — los números son el protagonista; las etiquetas son soporte.
- **Profundidad sutil** — capas de oscuridad distintas crean jerarquía sin bordes agresivos.

---

## 2. Paleta de Colores

### 2.1 Colores base (fondos)

| Token | Hex | Uso |
|---|---|---|
| `--bg-root` | `#0d0f14` | Fondo más profundo — body, backdrop |
| `--bg-primary` | `#13161f` | Contenedor principal del app |
| `--bg-card` | `#1a1d27` | Cards, paneles, sidebar |
| `--bg-card-hover` | `#1f2230` | Estado hover de cards |
| `--bg-elevated` | `#242738` | Inputs, badges, elementos elevados |
| `--bg-overlay` | `#2a2d3e` | Tooltips, dropdowns |

### 2.2 Colores de acento

| Token | Hex | Uso |
|---|---|---|
| `--accent-orange` | `#F7931A` | Acción primaria, brand, CTA principal |
| `--accent-orange-soft` | `rgba(247,147,26,0.12)` | Fondos de badges naranja |
| `--accent-purple` | `#7c5cfc` | Acento secundario, gradientes, highlights |
| `--accent-purple-soft` | `rgba(124,92,252,0.15)` | Fondos de elementos purple |
| `--accent-purple-dark` | `#4b2fa0` | Gradiente profundo del CTA card |

### 2.3 Colores semánticos

| Token | Hex | Uso |
|---|---|---|
| `--positive` | `#22c55e` | Ganancias, variaciones positivas, uptrend |
| `--positive-soft` | `rgba(34,197,94,0.12)` | Fondo de badges positivos |
| `--negative` | `#ef4444` | Pérdidas, variaciones negativas, downtrend |
| `--negative-soft` | `rgba(239,68,68,0.12)` | Fondo de badges negativos |
| `--warning` | `#f59e0b` | Alertas, estados pendientes |
| `--neutral` | `#6b7280` | Datos sin variación, estados neutros |

### 2.4 Colores de texto

| Token | Hex | Uso |
|---|---|---|
| `--text-primary` | `#e8eaed` | Títulos, valores principales, labels activos |
| `--text-secondary` | `#9ca3af` | Subtítulos, labels de apoyo |
| `--text-muted` | `#6b7280` | Metadata, timestamps, hints |
| `--text-disabled` | `#374151` | Elementos deshabilitados |

### 2.5 Bordes

| Token | Valor | Uso |
|---|---|---|
| `--border-subtle` | `rgba(255,255,255,0.05)` | Separadores entre secciones |
| `--border-default` | `rgba(255,255,255,0.08)` | Bordes de cards y paneles |
| `--border-strong` | `rgba(255,255,255,0.14)` | Bordes en hover, inputs focused |
| `--border-accent` | `rgba(247,147,26,0.30)` | Bordes de elementos activos/seleccionados |

---

## 3. Tipografía

### 3.1 Familias

```css
--font-display: 'Syne', sans-serif;      /* Títulos, nombres de secciones */
--font-body:    'Inter', sans-serif;     /* Cuerpo, labels, navegación */
--font-data:    'DM Mono', monospace;    /* Valores numéricos, porcentajes, precios */
```

> **Regla de oro:** Todo número financiero usa `--font-data`. Todo lo demás usa `--font-body`. Los títulos de sección grandes usan `--font-display`.

### 3.2 Escala tipográfica

| Nombre | Tamaño | Peso | Fuente | Uso |
|---|---|---|---|---|
| `display-xl` | 40px | 800 | Syne | Valor principal de un activo (ej: 31.39686) |
| `display-lg` | 28px | 700 | Syne | Título de sección (ej: "Top Staking Assets") |
| `display-md` | 22px | 700 | Syne | Subtítulo de card, nombre de activo |
| `data-xl` | 32px | 700 | DM Mono | Porcentaje destacado (ej: 13.62%) |
| `data-lg` | 20px | 600 | DM Mono | Precio, valor secundario |
| `data-md` | 14px | 500 | DM Mono | Variación 24h, datos de tabla |
| `data-sm` | 12px | 400 | DM Mono | Timestamps, metadata numérica |
| `label-lg` | 14px | 600 | Inter | Labels de métricas, nav items activos |
| `label-md` | 12px | 500 | Inter | Labels secundarios, badges |
| `label-sm` | 11px | 500 | Inter | Uppercase labels, categorías |
| `body-md` | 13px | 400 | Inter | Texto descriptivo, tooltips |

### 3.3 Reglas de uso

- Los **porcentajes de reward** son siempre `data-xl` con color semántico (verde/rojo).
- Los **nombres de activos** combinan `display-md` (nombre) + `label-sm` uppercase (tipo).
- Los **timestamps** usan `data-sm` en `--text-muted`.
- **Nunca** mezclar `font-data` y `font-body` en la misma línea de información.

---

## 4. Espaciado y Layout

### 4.1 Sistema de espaciado (base 4px)

| Token | Valor | Uso |
|---|---|---|
| `--space-1` | 4px | Gaps mínimos entre elementos inline |
| `--space-2` | 8px | Padding interno de badges y chips |
| `--space-3` | 12px | Gap entre ícono y texto |
| `--space-4` | 16px | Padding interno de cards pequeñas |
| `--space-5` | 20px | Gap entre cards en un grid |
| `--space-6` | 24px | Padding interno de cards normales |
| `--space-8` | 32px | Separación entre secciones |
| `--space-10` | 40px | Padding de secciones principales |

### 4.2 Layout general

```
┌─────────────────────────────────────────────────────────┐
│  TOPBAR (56px)  ·  usuario · búsqueda · acciones        │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│   SIDEBAR    │           MAIN CONTENT                   │
│   (220px)    │           (fluid)                        │
│              │                                          │
│  nav items   │  tab bar → secciones                     │
│  sub-items   │  grid de cards                           │
│  activos     │  panel de detalle                        │
│              │                                          │
│  footer CTA  │                                          │
└──────────────┴──────────────────────────────────────────┘
```

**Grid del contenido principal:**
- Sección superior: `grid 3 columnas + 1 CTA card` (ratio aprox 1:1:1:1.2)
- Sección inferior: `1 columna fluid` (panel de detalle de activo)
- Gap entre columnas: `20px`

### 4.3 Border radius

| Token | Valor | Uso |
|---|---|---|
| `--radius-sm` | 6px | Badges, chips pequeños, tags |
| `--radius-md` | 10px | Botones, inputs |
| `--radius-lg` | 14px | Cards pequeñas, paneles internos |
| `--radius-xl` | 18px | Cards principales, modales |
| `--radius-full` | 9999px | Pills, avatares circulares |

---

## 5. Componentes

### 5.1 Cards de activo (Asset Card)

Estructura interna de cada card de criptoactivo en el grid principal:

```
┌─────────────────────────────────┐
│  [icono]  Tipo (label-sm)       │  ← header
│  Nombre del Activo              │
│                          [↗]   │
├─────────────────────────────────┤
│  Reward Rate   (label-sm)       │  ← métrica principal
│  13.62%        (data-xl)        │
│  ▲ 6.25%       (positivo)       │
├─────────────────────────────────┤
│  [sparkline chart]              │  ← mini gráfico
│  +$2,966 (badge positivo)       │
└─────────────────────────────────┘
```

**Especificaciones:**
- Fondo: `--bg-card`
- Border: `1px solid --border-default`
- Border radius: `--radius-xl`
- Padding: `20px`
- El badge de variación ($) se superpone al extremo derecho del sparkline.
- En hover: `border-color: --border-strong`, `transform: translateY(-2px)`

### 5.2 Sidebar

**Estructura:**
```
Logo + nombre app
─────────────────
Tabs principales (Staking / Stablecoin)
─────────────────
Nav items con ícono:
  • Dashboard        [activo]
  • Assets
  • Staking Providers
  • Staking Calculator
  • Data API         [external link badge]
  • Liquid Staking   [beta badge]
─────────────────
Active Staking [n]   [expandible]
  ↳ sub-items de activos con color dot + nombre + monto
─────────────────
[footer] Activate Super CTA
```

**Nav item activo:**
- Fondo: `--bg-elevated`
- Texto: `--text-primary`
- Borde izquierdo: `3px solid --accent-orange`
- Border radius: `--radius-md`

**Sub-items de activos:**
- Dot de color único por activo (rojo, naranja, purple, azul...)
- Nombre en `label-md`, monto en `data-sm --text-muted`
- Estado disabled: opacidad 50%

### 5.3 Botones

#### Primario (filled)
```css
background:    --accent-orange
color:         #000000
font:          label-lg, Inter 600
padding:       10px 20px
border-radius: --radius-md
hover:         brightness(1.1), translateY(-1px)
```

#### Secundario (outlined)
```css
background:    transparent
border:        1px solid --border-strong
color:         --text-primary
font:          label-lg, Inter 600
padding:       10px 20px
border-radius: --radius-md
hover:         background --bg-elevated
```

#### Ghost (dark filled)
```css
background:    --bg-elevated
color:         --text-secondary
font:          label-md, Inter 500
padding:       8px 14px
border-radius: --radius-md
hover:         color --text-primary
```

#### CTA especial (gradiente)
```css
background:    linear-gradient(135deg, #7c5cfc, #4b2fa0)
color:         #ffffff
font:          label-lg, Inter 600
padding:       12px 20px
border-radius: --radius-md
width:         100%
```
> Usado en el panel "Liquid Staking Portfolio" para "Connect with Wallet".

### 5.4 Badges y chips

#### Badge de variación positiva
```css
background:  --positive-soft
color:       --positive
font:        data-sm, DM Mono 500
padding:     3px 8px
border-radius: --radius-sm
prefix:      ▲ o +
```

#### Badge de variación negativa
```css
background:  --negative-soft
color:       --negative
font:        data-sm, DM Mono 500
padding:     3px 8px
border-radius: --radius-sm
prefix:      ▼ o −
```

#### Badge de estado (New, Beta, Pro)
```css
background:  --accent-purple-soft
color:       --accent-purple
font:        label-sm 11px uppercase, Inter 600
padding:     2px 8px
border-radius: --radius-sm
letter-spacing: 0.08em
```

#### Chip de filtro (24H, Proof of Stake, Desc)
```css
background:  --bg-elevated
color:       --text-secondary
font:        label-md, Inter 500
padding:     6px 12px
border-radius: --radius-full
border:      1px solid --border-default
gap interno: 6px (ícono + texto)
hover:       border-color --border-strong
active:      color --text-primary
```

### 5.5 Sparkline Charts (mini gráficos)

- Librería sugerida: **Chart.js** con tipo `line`
- Sin ejes, sin grillas, sin leyenda
- `tension: 0.4` para curva suave
- Línea positiva: `stroke #22c55e`, fill `rgba(34,197,94,0.08)`
- Línea negativa: `stroke #ef4444`, fill `rgba(239,68,68,0.08)`
- Puntos: `radius 3px` solo en el punto final
- Altura fija: `60px`
- `responsive: true`, `maintainAspectRatio: false`

### 5.6 Panel de detalle de activo

Sección inferior con información extendida de un activo seleccionado:

```
┌──────────────────────────────────────────────────────────────┐
│ Header: nombre activo + íconos de acción + "View Profile"   │
├──────────────────────────────────────────────────────────────┤
│ "Current Reward Balance" (label)                            │
│ 31.39686    (display-xl, DM Mono)   [Upgrade] [Unstake]    │
├──────────────────────────────────────────────────────────────┤
│ Momentum ↕  │  General ↕  │  Risk ↕  │  Reward ↕           │
│ (tabs expandibles con ícono de sort)                        │
├──────────────────────────────────────────────────────────────┤
│  Métrica 1    │  Métrica 2   │  Métrica 3   │  Métrica 4   │
│  −0.82%       │  $41.99      │  60.6%       │  [progress]  │
└──────────────────────────────────────────────────────────────┘
```

**Investment Period slider:**
- Track: `--bg-elevated`, altura `4px`
- Thumb: botón circular con ícono pause, fondo `--bg-card`, border `--border-strong`
- Fill activo: `--accent-purple`

### 5.7 Topbar

```
[Logo]          [Avatar + Nombre + dropdown]    [Deposit CTA]    [notif] [search] [settings]
```

- Altura: `56px`
- Fondo: `--bg-card` con `border-bottom: 1px solid --border-subtle`
- Avatar: `32px`, `border-radius: --radius-full`
- Badge de notificaciones: dot naranja `8px` superpuesto al ícono
- Search bar: `--bg-elevated`, `border-radius: --radius-full`, `width: 180px`

---

## 6. Iconografía

- **Estilo:** línea fina (1.5px stroke), esquinas redondeadas, sin relleno sólido.
- **Tamaño estándar:** `16px` para nav items, `20px` para acciones de card, `24px` para sección headers.
- **Color:** heredan `--text-secondary` por defecto; `--text-primary` en hover/activo.
- **Íconos de activos cripto:** círculos con logo de la chain (Ethereum, BNB, Polygon). Fondo con color brand del activo a `15%` de opacidad.
- **Librerías sugeridas:** Lucide Icons, Phosphor Icons (ambas tienen variante thin/regular compatible con este estilo).

---

## 7. Microinteracciones y Animaciones

### 7.1 Principios
- **Duración corta:** entre `150ms` y `300ms`. Nada más lento.
- **Easing:** `cubic-bezier(0.4, 0, 0.2, 1)` para la mayoría. `cubic-bezier(0.34, 1.56, 0.64, 1)` para elementos que "saltan" (progress bars, contadores).
- **Solo transform y opacity:** nunca animar `width`, `height` ni `color` directamente (costoso en GPU).

### 7.2 Catálogo de animaciones

| Elemento | Animación | Duración |
|---|---|---|
| Card hover | `translateY(-2px)` + `border-color` | 180ms ease |
| Botón hover | `translateY(-1px)` + `brightness(1.1)` | 150ms ease |
| Tab switch | fade + translateX del contenido | 200ms ease |
| Contadores (métricas) | count-up desde 0 al valor real | 900ms ease-out cubic |
| Progress bar | width de 0% al valor real | 1200ms cubic-bezier con bounce |
| Badge de aparición | `scale(0.8) opacity(0)` → `scale(1) opacity(1)` | 200ms ease |
| Sparkline draw | `stroke-dashoffset` de largo a 0 | 800ms ease-in-out |
| Page load (cards) | `fadeUp` staggered, delay +50ms por card | 400ms ease |

### 7.3 `fadeUp` (animación base de entrada)
```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

---

## 8. Estados de los Componentes

### 8.1 Estados de datos en tiempo real

| Estado | Indicador visual |
|---|---|
| Cargando | Skeleton con shimmer animado (`--bg-elevated` → `--bg-overlay` → `--bg-elevated`) |
| Error | Border `--negative`, ícono de alerta, texto en `--negative` |
| Sin datos | Ilustración centrada + texto `--text-muted` + CTA opcional |
| Desactualizado | Badge "Last update X min ago" en `--text-muted` con ícono de reloj |

### 8.2 Estados de activos

| Estado | Color dot | Opacidad item |
|---|---|---|
| Activo / staking | Color brand del activo | 100% |
| Inactivo | `--neutral` | 50% |
| En proceso | `--warning` parpadeante | 80% |

---

## 9. Responsive y Adaptación Móvil

### 9.1 Breakpoints

| Nombre | Ancho | Comportamiento |
|---|---|---|
| `mobile` | < 768px | Sidebar colapsado a bottom nav de 5 ítems |
| `tablet` | 768–1024px | Sidebar de íconos (64px), grid de 2 columnas |
| `desktop` | 1024–1440px | Layout completo, grid de 3 columnas + CTA |
| `wide` | > 1440px | Máximo `1400px` de ancho, centrado |

### 9.2 Adaptaciones en móvil

- El grid de cards pasa a **scroll horizontal** con `snap scrolling`.
- El panel de detalle de activo ocupa **pantalla completa** (bottom sheet).
- El topbar muestra solo logo + avatar + notificaciones.
- Los filtros de chips se mueven a un bottom sheet de filtros.

---

## 10. Tokens CSS — Referencia rápida

```css
:root {
  /* Fondos */
  --bg-root:          #0d0f14;
  --bg-primary:       #13161f;
  --bg-card:          #1a1d27;
  --bg-card-hover:    #1f2230;
  --bg-elevated:      #242738;
  --bg-overlay:       #2a2d3e;

  /* Acentos */
  --accent-orange:    #F7931A;
  --accent-purple:    #7c5cfc;

  /* Semánticos */
  --positive:         #22c55e;
  --negative:         #ef4444;
  --warning:          #f59e0b;

  /* Texto */
  --text-primary:     #e8eaed;
  --text-secondary:   #9ca3af;
  --text-muted:       #6b7280;

  /* Bordes */
  --border-subtle:    rgba(255,255,255,0.05);
  --border-default:   rgba(255,255,255,0.08);
  --border-strong:    rgba(255,255,255,0.14);
  --border-accent:    rgba(247,147,26,0.30);

  /* Espaciado */
  --space-1: 4px;  --space-2: 8px;   --space-3: 12px;
  --space-4: 16px; --space-5: 20px;  --space-6: 24px;
  --space-8: 32px; --space-10: 40px;

  /* Radios */
  --radius-sm:   6px;
  --radius-md:   10px;
  --radius-lg:   14px;
  --radius-xl:   18px;
  --radius-full: 9999px;

  /* Tipografía */
  --font-display: 'Syne', sans-serif;
  --font-body:    'Inter', sans-serif;
  --font-data:    'DM Mono', monospace;

  /* Transiciones */
  --transition-fast:   150ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow:   400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## 11. Aplicación al Proyecto JBener

Este design system se mapea directamente al dashboard de JBener de la siguiente manera:

| Componente Stakent | Equivalente JBener |
|---|---|
| Asset cards (ETH, BNB, Polygon) | Métricas cards (Saldo, Patrimonio, Cripto, Meta) |
| Reward Rate % | Progreso de meta % |
| Sparkline chart | Gráfico de evolución patrimonial |
| Active Staking sidebar items | Historial de movimientos recientes |
| Investment Period slider | Filtro de temporalidad del gráfico |
| Liquid Staking CTA card | Card de resumen SUNAT |
| Momentum / General / Risk / Reward tabs | Tabs de filtro del historial |
| "Connect with Wallet" CTA | Botón "Registrar movimiento" |

### Adaptaciones específicas para JBener

- El **color brand** de cada categoría sigue la misma lógica que el color de cada chain cripto: Sueldo → verde, Cripto → naranja, Gasto → rojo, Préstamo → purple.
- La **barra de progreso** de la meta reemplaza al slider de Investment Period con la misma estética pero sin interacción.
- Los **chips de filtro** (7D, 30D, 6M, Todo) son idénticos a los filtros de temporalidad de Stakent.
- El **panel de detalle** inferior puede usarse para mostrar el detalle de un movimiento seleccionado del historial.

---

*Design System Document v1.0 · JBener · Marzo 2026*  
*Referencia visual: Stakent — stakent.com*

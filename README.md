# Umbral del Saber

RPG académico de fantasía oscura, de uso personal, con cuatro sendas y contenido **DEMO**. Funciona con archivos estáticos, sin cuenta, IA, API, backend ni dependencias para jugar. Los 40 ejercicios incluidos demuestran el sistema; no equivalen a tus guías ni a tu programa oficial.

## Inicio y despliegue

- Publicación: **descomprime el ZIP y sube todos los archivos y carpetas** (`src/`, `content/`, `assets/`, etc.) a la raíz de un repositorio público de GitHub (incluidos `index.html`, `src`, `assets`, `content`, `sw.js`). En **Settings → Pages → Build and deployment**, selecciona **Deploy from a branch**, rama `main`, carpeta `/(root)`. Abre la URL que muestre Pages; puede demorar unos minutos.
- Prueba local: desde esta carpeta ejecuta `python3 -m http.server 8765` y visita `http://localhost:8765/`. Abrir `index.html` con `file://` no sirve porque el navegador bloquea la lectura de JSON mediante `fetch`.
- La aplicación usa solo rutas relativas (`./`), compatibles con un repositorio en una subruta de GitHub Pages. El guardado queda en `localStorage` del navegador y **no se sincroniza** entre dispositivos. El `index.html` lleva el motor y las cuatro unidades demo incorporados: también inicia si GitHub Pages todavía no tiene las carpetas `src/` o `content/`, y muestra el problema de publicación. La carpeta `content/` sigue siendo necesaria para instalar unidades nuevas. El service worker conserva los archivos visitados para uso sin conexión después de su primera carga; al publicar material nuevo, abre una vez el juego con conexión para actualizarlo.
- Valida y reconstruye antes de subir cambios: `npm ci` y `npm run build`. Para ejecutar las pruebas de desarrollo, ejecuta `npm ci` y `npm test` (Node 20.19 o superior). El juego desplegado no requiere instalar paquetes.

## Cómo añadir contenido nuevo

1. Pide a ChatGPT que convierta tus materiales reales en **una unidad con el esquema de abajo**. Revisa cada respuesta y explicación contra la fuente; el juego no verifica su veracidad académica.
2. Guarda el archivo `.json` en `content/calculo/`, `content/fisica/`, `content/programacion/` o `content/bases-de-datos/`. También se acepta `.md` con un bloque de código `json` que contenga el objeto completo. Usa nombres de archivo como `unidad-02.json`.
3. Incluye por lo menos cuatro ejercicios corregibles automáticamente para que el jefe pueda desbloquearse. Ejecuta `npm run build` después de `npm ci`. El comando detecta archivos, comprueba su estructura, actualiza `content/manifest.json` y reconstruye `index.html`. Si hay errores, no genera un manifiesto nuevo. Un sitio estático no puede descubrir archivos nuevos en una carpeta sin este paso.
4. Prueba con un servidor local y confirma que la unidad aparece en la senda correcta. Sube también el **manifiesto actualizado**. Las unidades con `order` mayor aparecen después; se desbloquean al derrotar al jefe anterior.
5. Para añadir una materia completamente nueva, define también su identidad visual en `src/config.js` y una carpeta permitida en `src/content.js` y `tools/validate-content.mjs`.

## Esquema de unidad (versión 1)

```json
{
  "schemaVersion": 1,
  "id": "unidad-ejemplo",
  "subject": "calculo",
  "title": "Título de la unidad",
  "description": "Descripción breve",
  "order": 2,
  "demo": false,
  "exercises": [
    {
      "id": "pregunta-01",
      "topic": "concepto-uno",
      "subtopic": "subtema-opcional",
      "type": "multiple-choice",
      "difficulty": 2,
      "question": "¿Cuánto es 2 + 2?",
      "options": ["3", "4", "5"],
      "answer": "4",
      "explanation": "Dos más dos son cuatro.",
      "hint": "Suma dos unidades a dos.",
      "tags": ["aritmetica"]
    }
  ]
}
```

Tipos admitidos: `multiple-choice`, `true-false` (ambos con `options` y `answer` exacta), `numeric` (número en `answer`, opcional `tolerance` absoluta o `relativeTolerance`), `short`, `written`, `predict-code`, `complete-code`, `debug-code`, `logic`, `puzzle`, `timed`. Para estos últimos se requiere una rúbrica:

- `"rubric":{"mode":"exact","accepted":["respuesta","variante"]}`: compara minúsculas, tildes y espacios normalizados; no resuelve equivalencias algebraicas generales.
- `"rubric":{"mode":"keywords","required":[["sinónimo A","sinónimo B"],["otro término"]]}`: exige un término por grupo. Úsalo solo para respuestas acotadas; no juzga el significado ni la calidad del razonamiento.
- `"rubric":{"mode":"self-check"}`: presenta el modelo y la explicación para comparar; **no** otorga XP, dominio ni abre salas porque no existe corrección automática fiable.
- `timed` requiere `seconds` (mínimo 10). Las respuestas numéricas aceptan coma decimal y tolerancia indicada. `code` es texto mostrado, nunca ejecutado. Incluye una solución y explicación comprobadas para cada ejercicio.

Ejemplo Markdown: una explicación en prosa seguida de ` ```json `, el objeto completo de la unidad, y ` ``` `. Solo el bloque JSON se carga al juego. Un error de archivo se muestra en la pantalla Mundo y Progreso; las demás unidades permanecen disponibles.

## Mecánicas y límites

- Navega por seis salas por unidad. El guardián exige cuatro ejercicios distintos y al menos 60% de aciertos. El combate tiene dado original de 20 caras, acciones de ataque, conjuro y defensa, y tres fases para jefes. Respuestas correctas mejoran la tirada y el daño; los fallos permiten seguir intentando.
- El dominio por tema usa aciertos ponderados por dificultad, diversidad de preguntas y práctica en días distintos. Un mismo ejercicio solo puntúa una vez por día. Los fallos y ejercicios vencidos regresan con más frecuencia. Los porcentajes son una estimación de práctica, no una nota oficial. Las estadísticas de tipo y dificultad quedan en el guardado.
- Cada respuesta válida da XP. Por cada cinco ejercicios válidos hay una probabilidad del 55% de recibir un cofre; sus rarezas son común 78%, raro 19%, épico 3%. La recompensa de cada misión se reclama una vez. La habilidad por dominio mejora el combate cuando se alcanza el estado “dominado”.
- El temporizador alterna 45/10 minutos y puede pausarse. No da XP por estar abierto. Su tiempo se corrige al regresar; no acumula ciclos ausentes. El sonido es sintetizado localmente.
- La persistencia es solo `localStorage`. El modo privado, el borrado de datos o cambiar de navegador puede perder la partida; no hay exportación de guardados. Si se agota el almacenamiento, la consola muestra el fallo. No hay cuenta ni servidor.

## Estructura

`index.html` abre el juego y contiene una copia compilada del motor y la demo; `tools/build.mjs` la regenera desde `src/` y `content/`;  `styles.css` da estilo responsive; `src/main.js` orquesta escenas e interfaz; `src/content.js` valida y carga unidades; `src/learning.js` calcula práctica y dominio; `src/combat.js`, `src/economy.js`, `src/missions.js`, `src/timer.js`, `src/store.js` separan las mecánicas; `src/avatar.js` dibuja pixel art SVG original; `assets/` contiene el icono; `content/` contiene unidades; `tools/validate-content.mjs` genera el manifiesto; `sw.js` conserva recursos para uso sin conexión; `tests/` contiene pruebas.

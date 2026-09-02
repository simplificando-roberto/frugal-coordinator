# Frugal coordinator

Frugal coordinator is a public skill for teams that use an expensive model to direct work but want cheaper models to perform the bounded parts. The coordinator keeps authority and final review. Leaves research, summarize, check, and implement within clear limits.

It captures a practical operating pattern: avoid repeated expensive context, write one shared brief, send each leaf only its needed sections, wait without polling, and consume cheap digests instead of raw logs.

## Install

Copy the `frugal-coordinator` folder into the skills directory used by your agent. Keep its `SKILL.md`, `references`, and `assets` together so links and templates remain available. Then customize the items listed in `SKILL.md` under "Adapt this skill" before enabling it for a team.

## Example use

Ask the coordinating agent to use `frugal-coordinator` for a bounded project. It creates a brief, delegates independent research or implementation leaves through `<delegation-tool>`, records each workflow ID, waits with `<durable-wait-command>`, reviews concise digests, and performs final checks itself.

## License

MIT. See [LICENSE](LICENSE).

## Resumen en español

Esta skill reduce el gasto del modelo coordinador.

El coordinador mantiene el objetivo, las decisiones y la verificación final.

Los modelos baratos hacen investigación, resúmenes y tareas acotadas.

Cada hoja recibe solo el contexto que necesita.

El brief compartido evita repetir antecedentes en cada prompt.

Las esperas deben ser durables y no deben usar sondeo.

Los logs largos y los diffs pasan primero por un digest barato.

Los secretos y las acciones irreversibles se quedan con el coordinador.

Un resultado de una hoja no autoriza acciones externas.

Cada equipo debe adaptar modelos, presupuestos y comandos.

La propagación de reglas usa bloques gestionados e idempotentes.

La licencia es MIT.


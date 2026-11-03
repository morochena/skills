---
name: ui-craft
description: Apply concise interface design and UX, developer, and agent experience principles when designing, building, or changing a user interface.
---

# UI Craft

Apply these principles to the UI work requested, alongside the project's established design system and constraints. Keep changes within the requested scope.

## Make the interface clear

- Remove taglines, helper text, and secondary labels that repeat what the interface already communicates or add no useful information. Prefer clear structure, hierarchy, placement, and specific control labels over explanatory copy.
- If a screen relies on extra prose to explain its structure or basic actions, improve the layout or interaction first. Retain concise text that users need to understand a choice, requirement, consequence, status, error, or recovery. Keep visible and accessible labels where needed; do not sacrifice accessibility or discoverability for minimalism.

## Improve the whole experience

Choose solutions that improve the user experience (UX), developer experience (DX), and agent experience (AX) together where practical:

- **UX:** Make the interface understandable, accessible, responsive, and predictable in real use.
- **DX:** Favor clear, maintainable code and established components and patterns; avoid unnecessary abstractions and duplication.
- **AX:** Make behavior and structure easy for future agents to inspect, navigate, change, and verify. Prefer semantic markup, clear names, predictable state, and existing project verification paths. Do not add agent-facing instructions to the product UI.

When these aims compete, make the tradeoff explicit in the implementation and report material compromises. Preserve existing behavior and contracts unless the requested change requires otherwise. Check the affected user flows and states with verification appropriate to the change; disclose any meaningful gap or regression risk.

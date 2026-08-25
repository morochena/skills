# Feature Map Contract

Use the feature map as the maintained source for user-path verification. Keep implementation details in code and helpers. Keep user entry points, stable control handles, required state, exact commands, and observable proof in the map.

## Index

Write `features/README.md` with these sections:

- A short statement of the app and purpose of the map.
- **Baseline preconditions:** launch target, isolated state, seed data, required tools, and doctor result.
- **Driving conventions:** starting state, stable handle rules, command wrapper, and reset behavior.
- **Proof and skip reporting:** required artifacts, second-view checks for mutations, and the information required for an unreachable path.
- **Features:** one link and one scope sentence for each sibling feature file.

The index and the sibling files must agree. Do not list a feature that has no file, and do not leave an unlisted feature file.

## Feature Files

Each feature file must use this structure:

```markdown
# <Feature name>

<One paragraph that describes the user-visible behavior.>

## Sub-features

- `<short-id>` <One observable behavior.>

## How to get to it (user POV)

- <Each menu, button, keyboard, command, route, or other user entry point.>

## Driving it with <harness>

Preconditions:

- <Required healthy state, fixture, account, permission, or platform.>

- **<Action>.** <User action.> Run `<exact command>`. <Observable result.>
- **Proof.** Run `<exact capture or read command>`. <Required evidence.>

## Gotchas

- <A real trap that can invalidate or waste a verification run.>
```

Use the four H2 headings in the shown order. Pair each user action with an exact control command and an observable result. Report an unreachable entry point with the attempted route and the unmet precondition. Do not report a different entry point as proof for the skipped path.

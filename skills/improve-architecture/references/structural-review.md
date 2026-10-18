# Structural Review

Use these questions when structural complexity or ownership is material to the audit. Check observed behavior, repository constraints, and counterexamples before recommending a change. A design smell alone is not a contract violation. Treat a new architectural preference as a proposal.

## Reader Load

Assess two independent costs: the layers a reader must trace to answer a question, and the mutable state they must remember. A flat module with hidden state can be as difficult as a chain of adapters.

Trace a representative question such as where a value comes from or what can change it. Look for pass-through layers, synchronized derived state, or mutations whose scope exceeds their use. Prefer changes that remove a demonstrated cost. A short file, fewer lines, or a single caller is not proof of lower reader load.

## Interface Depth

Write a representative caller's usage and identify which decisions it must make. Does the interface let the caller complete a domain operation, or must it coordinate internal stages and know their ordering?

A useful boundary hides substantial policy or mechanism behind a manageable interface. A wrapper that repeats its dependency's methods may add another vocabulary without hiding anything. Preserve forwarding layers that enforce policy, adapt a protocol, or provide an established framework boundary. Do not collapse a justified boundary solely because it has one implementation.

## Domain Shape and Representations

Check whether coordinated booleans, repeated conditionals, or optional-field combinations encode a state model implicitly. A union, state machine, lookup table, or suitable collection should remove invalid states or duplicated decisions rather than merely relocate them.

Follow external data into the domain. Parse untrusted values at trust boundaries, derive types from authoritative schemas where practical, and preserve meaningful internal invariant checks. Storage and transport details should stay private when they are not the module's intended public contract. Protocol libraries may legitimately expose protocol types.

## State Ownership

Find every writer to important state, including persisted records, caches, generated files, and verification fixtures. Establish whether multiple actors actually need one mutable object. Independent facts can have separate owners and be combined when read.

For inherently shared state, check the enforced transaction, atomic update, lock, or single-writer mechanism. Check retry and partial-failure behavior when a change affects it. Naming an owner in prose does not serialize concurrent writes.

## Information Leakage

Look for a representation or policy decision repeated across modules. If changing it requires coordinated edits, identify the knowledge that crossed the boundary and whether that exposure is intentional.

Modules named after execution stages such as load, validate, and save can scatter the same domain knowledge. Group responsibility around the decisions it owns when that reduces coupling. Execution stages are still useful boundaries when they have distinct contracts or operational constraints.

## Hand-Synchronized Lists

Find inventories, registries, schemas, or configuration that require the same addition in multiple places. Prefer one authoritative source and derived views. When duplication is intentional and generation is impractical, use a focused agreement check if its maintenance cost is justified.

Before deleting an apparent duplicate, check for different consumer contracts, release versions, or ownership boundaries. Demonstrate which divergence would be a defect and which differences must remain possible.

## Choosing a Remediation

Name the invariant or recurring change that becomes easier, the decisions the new boundary hides, and the existing behavior it must preserve. Keep remediation within the selected scope and lifecycle policy. A cleaner hypothetical design does not authorize a rewrite or removal of compatibility guarantees.

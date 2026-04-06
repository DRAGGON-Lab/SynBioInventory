# Contributing

Thank you for contributing to SynBioInventory.

This project sits at the intersection of synthetic biology, standards, and research software engineering. Contributions should aim to improve correctness, usability, and maintainability.

## Ways to contribute

- improve documentation
- implement or refine the SBOL package
- improve backend integration with SynBioHub
- improve frontend usability on mobile and desktop
- add tests and fixtures
- propose product or architecture improvements

## Contribution principles

### Be explicit
Write code and documentation so that future lab members and collaborators can understand why a decision was made.

### Respect layer boundaries
Keep domain, API, and UI concerns separated.

### Prefer small, reviewable changes
Large sweeping changes are harder to validate.

### Document assumptions
If a SynBioHub behavior is inferred and not yet tested live, note it clearly.

## Pull request expectations

A good pull request should:

- explain the problem it solves,
- describe the design choice,
- mention any tradeoffs,
- include tests where appropriate,
- update relevant documentation.

## Branching suggestion

A simple workflow is sufficient at the start:

- `main` for stable repository state
- short-lived feature branches for active work

Suggested branch names:

- `feature/sbol-package-scaffold`
- `feature/backend-auth-stub`
- `feature/frontend-collection-browser`
- `docs/product-architecture-refresh`

## Commit style suggestion

Use clear commit messages such as:

- `docs: add initial architecture and product docs`
- `feat: scaffold inventory package factories`
- `feat: add backend stub collection routes`
- `test: add placement validation tests`

## Definition of done

A change is done when:

- it works for the intended scope,
- it does not break the core workflow,
- it is documented enough to maintain,
- it includes tests where the change justifies them.

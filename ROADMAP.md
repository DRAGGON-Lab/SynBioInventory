# Roadmap

## Guiding idea

Build a reliable manual inventory workflow first. Use that workflow to generate clean structured data. Then layer automation on top.

## Phase 0: repository and planning

- define product scope
- define architecture
- scaffold repository docs
- agree on MVP boundaries

## Phase 1: SBOL package MVP

- define namespaces and constants
- implement inventory and storage factories
- implement validation rules
- implement serialization helpers
- add package tests

## Phase 2: backend MVP

- implement stub auth flow
- implement root collections and subcollections routes
- implement inventory create flow
- implement image attachment orchestration
- add live SynBioHub service wrapper

## Phase 3: frontend MVP

- implement login page
- implement collection browser
- implement create implementation page
- implement review page
- implement success page
- validate phone-first interaction

## Phase 4: end-to-end hardening

- test against real SynBioHub instance
- refine error handling
- improve upload behavior
- add more metadata fields if useful

## Phase 5: next capabilities

- search and browse created inventory objects
- edit and move operations
- richer storage validation
- barcode support

## Phase 6: intelligent assistance

- define image dataset standards
- train image classifiers on attached images
- add prediction suggestion to create flow
- keep user confirmation in the loop

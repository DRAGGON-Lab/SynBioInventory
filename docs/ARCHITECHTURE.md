# Architecture

## Overview

SynBioInventory is organized as a layered system with a strong separation between domain logic, orchestration, and user interface.

```text
React Frontend
      |
      v
FastAPI Backend
      |
      v
SBOL Inventory Package
      |
      v
SynBioHub
```

The architecture is designed to support an MVP centered on manual curation and image attachment, while leaving room for future automation such as ML-assisted image classification, barcode support, and richer inventory management operations.

## Architectural goals

The architecture should satisfy the following goals:

- keep SBOL-specific logic out of the frontend,
- keep SynBioHub integration out of the reusable domain package,
- make local development possible without a live SynBioHub instance,
- support future capabilities without rewriting the core object model,
- remain simple enough to maintain in a small research software team.

## System components

## 1. Frontend

### Responsibilities

The frontend is responsible for:

- presenting the login workflow,
- browsing collections hierarchically,
- selecting a destination collection,
- capturing metadata for the new inventory object,
- uploading and previewing one or more images,
- reviewing the submission,
- displaying success and error states.

### Technology direction

- React
- TypeScript
- responsive, mobile-first design

### Design notes

The application should avoid desktop-only interaction patterns such as double-click. Collection navigation should instead use explicit actions:

- single tap selects,
- chevron or open button enters subcollections,
- breadcrumb navigation shows context,
- choose button confirms destination.

This is more robust on phones and still works well on laptops.

## 2. Backend API

### Responsibilities

The backend coordinates the workflow between the frontend, the SBOL package, and SynBioHub.

Its responsibilities include:

- handling SynBioHub authentication,
- maintaining server-side session state or tokens,
- exposing simplified collection navigation endpoints,
- validating create requests,
- calling the SBOL package to generate inventory objects,
- serializing and submitting SBOL documents,
- attaching uploaded images,
- returning a concise result to the frontend.

### Technology direction

- Python 3.11+
- FastAPI
- HTTP client for SynBioHub API requests

### Why the backend is required

The frontend should not directly construct SBOL objects or handle low-level SynBioHub submission behavior. Keeping this logic in the backend:

- improves security,
- centralizes validation,
- simplifies the frontend,
- makes testing easier,
- makes future integrations easier.

## 3. SBOL inventory package

### Responsibilities

The Python package encapsulates the domain model and SBOL serialization rules.

It should contain:

- namespaces and constants,
- extension-aware inventory and storage classes or helpers,
- factory functions for inventory objects,
- factory functions for storage nodes,
- placement validation rules,
- serialization helpers.

### Design philosophy

This package should be usable independently of the web application. It should be possible to import it from scripts, notebooks, tests, or other services.

That makes the core inventory model reusable beyond the initial UI.

## Domain model

## Inventory objects

The first three inventory object types are:

- `ExtractedPlasmid`
- `BacterialStock`
- `SolidMediaPlate`

These map to SBOL `Implementation` objects with custom annotations such as:

- `inventory_kind`
- `stored_at`
- optional operational metadata like `barcode`, `lot_id`, and `notes`

## Storage objects

The storage hierarchy is represented as nested SBOL `Collection`-based objects:

- `FridgeMinus80C`
- `FridgeMinus20C`
- `Fridge4C`
- `Shelf`
- `Box`
- `Slot`

The storage graph is used to express physical containment.

## Storage containment model

```text
Fridge -> Shelf -> Box -> Slot -> Implementation
```

This gives a clean, explicit model for physical location.

## Validation rules

Initial placement rules:

- `ExtractedPlasmid` may only be placed in `FridgeMinus20C`
- `BacterialStock` may only be placed in `FridgeMinus80C`
- `SolidMediaPlate` may only be placed in `Fridge4C`

Future validation may include:

- box capacity,
- slot occupancy,
- allowed subcollection types,
- movement history,
- image requirements.

## Data flow

## Login flow

1. frontend sends credentials to backend
2. backend authenticates against SynBioHub
3. backend stores token or session server-side
4. frontend receives authenticated session state

## Collection navigation flow

1. frontend requests root collections
2. backend calls SynBioHub root collection endpoint
3. frontend displays collections
4. when user opens a collection, frontend requests subcollections
5. backend returns subcollection data
6. user chooses one collection as destination

## Create inventory flow

1. user selects inventory type and enters metadata
2. user uploads one or more images
3. frontend sends multipart request to backend
4. backend validates request
5. backend builds SBOL document using package
6. backend submits document to SynBioHub
7. backend attaches images to created object
8. backend returns created object URI and summary
9. frontend shows success view

## Development modes

## Stub mode

A stub SynBioHub integration should be available for local development. In stub mode:

- login is simulated,
- collection navigation uses mock data,
- object creation returns deterministic fake URIs,
- image attachment is simulated.

This enables frontend and backend development before real SynBioHub integration is fully tested.

## Live integration mode

In live mode, the backend communicates with a real SynBioHub instance.

Configuration should be environment-driven.

## Security considerations

- keep SynBioHub tokens server-side,
- avoid storing credentials in localStorage,
- validate uploaded files,
- set file size limits,
- log operations without logging secrets,
- sanitize user-supplied metadata before using it in generated names or paths.

## Future architecture extensions

The architecture should be ready for:

- image classification service,
- barcode scanning,
- inventory search,
- edit and move operations,
- audit trail and movement history,
- bulk uploads,
- role-based workflows,
- lab-specific policy plugins.

The current decomposition already supports those directions without forcing a redesign.

## Suggested backend modules

```text
server/app/
├── main.py
├── config.py
├── api/
│   ├── routes_auth.py
│   ├── routes_collections.py
│   ├── routes_inventory.py
│   └── routes_health.py
├── services/
│   ├── synbiohub_client.py
│   ├── inventory_service.py
│   └── attachment_service.py
├── schemas/
│   ├── auth.py
│   ├── collections.py
│   └── inventory.py
└── deps.py
```

## Suggested package modules

```text
packages/draggon_inventory_sbol/src/draggon_inventory_sbol/
├── __init__.py
├── namespaces.py
├── schema.py
├── factories.py
├── validation.py
└── serialize.py
```

## Suggested frontend modules

```text
web/src/
├── pages/
│   ├── LoginPage.tsx
│   ├── CollectionBrowserPage.tsx
│   ├── CreateImplementationPage.tsx
│   ├── ReviewSubmitPage.tsx
│   └── SuccessPage.tsx
├── components/
│   ├── CollectionList.tsx
│   ├── CollectionRow.tsx
│   ├── ImageUpload.tsx
│   └── BottomActionBar.tsx
├── hooks/
├── lib/
└── app/
```

## Architectural risks

### Risk 1: SynBioHub integration details differ in practice
Mitigation: implement a service layer and keep TODO markers where live testing is needed.

### Risk 2: SBOL extension model becomes too rigid
Mitigation: isolate schema decisions in the package and keep annotations minimal in the MVP.

### Risk 3: mobile usability is neglected
Mitigation: test the workflow on real phones early and avoid desktop-only assumptions.

### Risk 4: image uploads become inconsistent for future ML
Mitigation: provide simple capture guidance and require implementation type selection from the start.

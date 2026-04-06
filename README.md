# SynBioInventory

SynBioInventory is a mobile-first, SBOL-enabled inventory system for tracking **physical implementations of synthetic biology designs** in SynBioHub.

The project is being developed by the **DRAGGON Lab** to solve a common operational gap in synthetic biology workflows: digital designs are often well represented, but their physical realizations in freezers, fridges, boxes, and slots are not tracked with the same rigor.

SynBioInventory addresses that gap by combining:

- a **Python SBOL package** for generating and validating inventory representations,
- a **backend service** that mediates communication with SynBioHub,
- and a **phone-first React frontend** for real-world bench use.

The MVP focuses on one high-value workflow:

1. authenticate into SynBioHub,
2. navigate collections hierarchically,
3. choose a destination collection,
4. create an inventory object representing a physical implementation,
5. attach one or more images as evidence,
6. submit the result back to SynBioHub.

This first release deliberately avoids machine learning. Instead, it is designed to create a **well-labeled, high-quality image dataset** attached to manually curated inventory objects. That dataset can later be used to train image recognition models for assisted classification.

## Why this project exists

In many synthetic biology labs, the digital and physical worlds drift apart.

A plasmid may be present in SynBioHub as a design object, but the extracted DNA tube in the freezer may only be tracked in spreadsheets, ad hoc notes, or labels on boxes. A strain stock may be represented in a design repository, yet the actual cryotube location may not be represented in a machine-readable way. This leads to friction in reproducibility, onboarding, reuse, and day-to-day operations.

SynBioInventory aims to make the physical inventory layer **standards-aware, structured, searchable, and extensible**, while remaining simple enough to use from a phone at the bench.

## Core concepts

### Inventory objects
The initial MVP supports three implementation categories:

- **ExtractedPlasmid**
- **BacterialStock**
- **SolidMediaPlate**

These are represented as SBOL `Implementation` objects with custom inventory annotations.

### Storage hierarchy
The physical storage model is represented as a hierarchy of storage nodes:

- **FridgeMinus80C**
- **FridgeMinus20C**
- **Fridge4C**
- **Shelf**
- **Box**
- **Slot**

These are represented as SBOL `Collection`-based objects with custom storage annotations.

### Evidence images
Users can upload one or more images during creation of an inventory object. These images are attached to the resulting SynBioHub object and serve both as operational documentation and as future ML training data.

## Product scope

### In scope for MVP

- SynBioHub login
- hierarchical collection navigation
- collection selection
- manual implementation type selection
- optional metadata entry
- image upload and preview
- creation of SBOL inventory objects
- submission to SynBioHub
- attachment of uploaded images to created objects

### Explicitly out of scope for MVP

- automated image classification
- object detection or image segmentation
- batch inventory import
- barcode scanning
- role-based access control beyond SynBioHub authentication
- full inventory editing lifecycle
- offline-first synchronization

## Proposed repository structure

```text
SynBioInventory/
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── DEVELOPMENT.md
├── .gitignore
├── .env.example
├── docker-compose.yaml
├── docs/
│   ├── architecture.md
│   ├── product.md
│   └── api.md
├── packages/
│   └── draggon_inventory_sbol/
├── server/
│   └── app/
└── web/
    └── src/
```

## Initial architecture summary

The system is divided into three layers:

### 1. `draggon_inventory_sbol` Python package
Responsible for:

- SBOL schema extensions
- inventory object factories
- storage object factories
- placement validation
- SBOL serialization

### 2. Backend API server
Responsible for:

- SynBioHub authentication
- collection browsing and subcollection traversal
- request orchestration
- inventory object creation
- SynBioHub submission
- image attachment

### 3. Frontend web app
Responsible for:

- user login
- collection navigation
- implementation creation form
- image upload
- review and submit flow
- mobile-friendly interaction

More detail is in [docs/architecture.md](docs/architecture.md).

## Technology direction

### Backend
- Python 3.11+
- FastAPI
- pySBOL2
- HTTP client for SynBioHub API integration

### Frontend
- React
- TypeScript
- mobile-first responsive UI

### Deployment
- Docker Compose for local development
- future containerized deployment for lab or institutional infrastructure

## Design principles

SynBioInventory should be:

- **bench-friendly**: easy to use on a phone with gloves off and limited attention,
- **standards-aware**: built around SBOL rather than disconnected ad hoc metadata,
- **extensible**: ready for future ML, barcoding, and richer inventory workflows,
- **modular**: domain logic in the SBOL package, orchestration in the backend, UX in the frontend,
- **traceable**: every created object should have reproducible metadata and attached evidence.

## Recommended first milestones

### Milestone 1: Repository and documentation scaffold
Create repo docs, agree on scope, define architecture, and scaffold local development.

### Milestone 2: SBOL package MVP
Implement storage and inventory object factories plus validation logic.

### Milestone 3: Backend MVP
Implement SynBioHub login, collection browsing, object creation, and image attachment.

### Milestone 4: Frontend MVP
Implement phone-first flows for login, browse, create, review, and submit.

### Milestone 5: End-to-end validation
Test the complete workflow against a real or staging SynBioHub instance.

## Immediate setup checklist

- [ ] create repository labels, issues, and project board
- [ ] add license
- [ ] scaffold package, server, and web directories
- [ ] configure local environment variables
- [ ] implement stub SynBioHub service for development
- [ ] define example SBOL objects and test fixtures
- [ ] connect frontend to backend stub APIs
- [ ] validate the first successful create-and-attach workflow

## Suggested next files to read

- [docs/product.md](docs/product.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/api.md](docs/api.md)
- [DEVELOPMENT.md](DEVELOPMENT.md)
- [ROADMAP.md](ROADMAP.md)

## Status

This repository now includes an initial runnable MVP scaffold:

- `packages/draggon_inventory_sbol`: domain schema, factories, validation, and RDF/XML serialization helper.
- `server/app`: FastAPI API with stub-mode SynBioHub service and inventory orchestration flow.
- `web/src`: React + TypeScript mobile-first flow for login, collection browsing, create, review, and success.

## Running locally

### 1) Python package + backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e packages/draggon_inventory_sbol
pip install -e server
uvicorn app.main:app --reload --app-dir server
```

### 2) Frontend

```bash
cd web
npm install
npm run dev
```

### 3) Execute tests

```bash
pytest packages/draggon_inventory_sbol/tests
pytest server/tests
```

# Development

## Purpose

This file describes how to set up local development for SynBioInventory and how to approach the codebase during the early scaffold phase.

## Development goals

The initial development goals are:

- make the repository runnable locally,
- scaffold package, backend, and frontend cleanly,
- support development without a live SynBioHub instance,
- make the first end-to-end happy path testable early.

## Local stack

Planned local components:

- Python package for SBOL inventory logic
- FastAPI backend
- React TypeScript frontend
- Docker Compose orchestration

## Recommended setup steps

1. clone the repository
2. create environment files from examples
3. run backend and frontend in stub mode
4. verify login, collection browsing, and create flow against mock data
5. begin replacing stubs with real integration points

## Environment variables

Suggested root `.env.example` entries:

```env
SYNBIOHUB_BASE_URL=https://your-synbiohub-instance.org
SYNBIOHUB_USE_STUB=true
BACKEND_PORT=8000
FRONTEND_PORT=3000
MAX_UPLOAD_MB=10
```

## Working agreements

### Keep domain logic isolated
If a function is about SBOL object creation or validation, it should live in the Python package, not in the web layer.

### Keep SynBioHub logic behind a service layer
Direct HTTP calls to SynBioHub should not be scattered across route handlers.

### Prefer small, testable modules
Avoid giant files for routes, services, or components.

### Build the happy path first
Optimize for a working create-and-attach flow before adding extra polish.

## Suggested first implementation order

1. repository scaffold
2. package namespaces and factories
3. placement validation tests
4. backend stub auth and collection routes
5. frontend login and collection browser
6. create inventory endpoint in stub mode
7. image upload and success flow
8. real SynBioHub integration testing

## Testing priorities

### Package tests
- object factories create expected annotations
- placement validation behaves correctly
- serialization produces valid outputs

### Backend tests
- auth happy path in stub mode
- root and subcollection routes
- inventory create happy path
- invalid placement returns proper error

### Frontend tests
- collection selection behavior
- review page renders chosen metadata and images
- submit flow handles success response

## Code review checklist

- does the code respect package/backend/frontend boundaries?
- does the code introduce unnecessary coupling?
- are error states visible to users?
- are TODOs clearly marked when live SynBioHub testing is required?
- does the flow still work on a phone-sized viewport?

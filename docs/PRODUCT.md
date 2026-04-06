# Product

## Product vision

SynBioInventory is a standards-aware inventory interface for the physical layer of synthetic biology.

Its purpose is to help laboratories track real physical instances of biological designs in a way that is structured, machine-readable, and operationally useful. It is designed to bridge the gap between digital design repositories and day-to-day physical inventory work at the bench.

The initial product is intentionally narrow. It focuses on a single workflow that delivers immediate value while laying the foundation for future intelligence.

## Problem statement

Synthetic biology labs often maintain design repositories, but physical inventory tracking is fragmented.

Common pain points include:

- physical samples stored in freezers or fridges without machine-readable location tracking,
- reliance on spreadsheets, handwritten notes, or memory,
- inconsistent naming and annotation of physical implementations,
- difficulty onboarding new users into lab inventory practices,
- poor linkage between design objects and their realized physical instances,
- lack of structured image evidence for physical samples.

These problems reduce reproducibility, create delays, and make reuse harder.

## Product hypothesis

If users can create inventory objects directly in a mobile-friendly interface connected to SynBioHub, and if those objects can include physical location and attached images, then labs will gain a more reliable and scalable method for managing implementations while simultaneously generating structured data for later automation.

## Target users

### Primary users

- synthetic biology researchers
- graduate students and postdocs
- lab managers
- research software engineers supporting lab operations

### Secondary users

- principal investigators
- external collaborators
- standards and infrastructure developers
- future ML developers using the curated image dataset

## MVP scope

The MVP includes the following user journey:

1. the user logs into SynBioHub,
2. the user navigates collections hierarchically,
3. the user chooses a destination collection,
4. the user selects an implementation type,
5. the user enters optional metadata,
6. the user uploads one or more images,
7. the backend creates the SBOL representation,
8. the object is submitted to SynBioHub,
9. the images are attached to the object,
10. the user receives confirmation and the created URI.

## What the MVP is not trying to solve

The MVP is not trying to be a complete lab inventory platform.

It does not yet include:

- automated image classification,
- inventory search and edit workflows,
- movement tracking over time,
- barcode scanning,
- batch upload,
- analytics dashboards,
- user roles beyond SynBioHub authentication,
- offline synchronization.

This focus is deliberate.

## Primary user stories

### Story 1: create a bacterial stock entry from a phone
As a researcher, I want to select the correct freezer-related collection, choose `BacterialStock`, upload a photo of the cryotube, and create a structured object in SynBioHub so the physical stock is linked to the digital system.

### Story 2: create an extracted plasmid entry
As a researcher, I want to place an `ExtractedPlasmid` in the correct storage hierarchy and attach images so the DNA prep is documented and traceable.

### Story 3: create a solid media plate entry
As a researcher, I want to create a `SolidMediaPlate` entry and attach a photo so the plate is represented in SynBioHub and can later contribute to training data.

### Story 4: curate future training data
As a lab developer, I want users to manually label inventory objects while attaching images so that future ML systems have a clean labeled dataset.

## Product principles

### 1. mobile-first for real lab use
The product should be easy to operate from a phone near the bench or freezer.

### 2. standards-first, not spreadsheet-first
The internal representation should align with SBOL rather than inventing disconnected data structures.

### 3. simple workflows beat clever workflows
The MVP should reduce friction and ambiguity rather than add automation too early.

### 4. human-confirmed data now enables better automation later
Manual implementation type selection in the MVP is a feature, not a limitation.

### 5. operational value and dataset value should reinforce each other
Every successful creation should both help the lab today and improve future training data.

## Functional requirements

### Authentication
- user can log into SynBioHub
- session state is preserved appropriately
- user can log out

### Collection navigation
- user can view root collections
- user can open subcollections
- user can navigate through nested collections
- user can select one destination collection
- selected destination is clearly shown

### Inventory creation
- user can choose one of three implementation types
- user can provide optional metadata fields
- user can upload one or more images
- user can review before submit

### Submission
- backend creates valid SBOL inventory representation
- backend submits it to SynBioHub
- backend attaches images to the created object
- backend returns the created URI

### Validation
- placement rules are validated in backend or package layer
- unsupported submissions fail with meaningful errors
- invalid image types or oversized files are rejected cleanly

## Non-functional requirements

### Usability
- touch-friendly controls
- clear feedback during loading and submission
- minimal cognitive load

### Reliability
- deterministic object creation behavior
- recoverable error messages
- graceful handling of SynBioHub failures

### Extensibility
- future ML can be added without redesigning the core flow
- future storage types and object types can be added cleanly

### Maintainability
- domain logic is isolated
- SynBioHub integration is abstracted
- codebase is testable

## Success criteria for MVP

The MVP is successful if a lab user can:

- log in,
- choose a collection,
- create an implementation object,
- attach one or more images,
- and see that object created in SynBioHub.

Additional strong indicators of success:

- users can complete the workflow comfortably from a phone,
- image attachments are consistent enough to support future dataset use,
- the architecture remains clean after the first implementation.

## Risks and product mitigations

### Risk: users get confused during hierarchical navigation
Mitigation: explicit open/select actions, breadcrumbs, and clear current selection state.

### Risk: too much metadata is requested
Mitigation: keep required fields minimal in the MVP.

### Risk: image uploads become noisy for future ML
Mitigation: add simple capture guidance and manual implementation selection.

### Risk: users expect full inventory management immediately
Mitigation: communicate MVP scope clearly in README and product docs.

## Future roadmap themes

### Near-term
- search and browse created inventory objects
- edit metadata
- move objects between locations
- improve attachment handling

### Mid-term
- barcode support
- richer storage policies
- movement history
- bulk operations

### Long-term
- image classification assistance
- inventory analytics
- dataset export workflows
- integration with richer DBTL pipelines

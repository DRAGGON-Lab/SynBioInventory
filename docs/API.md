# API Draft

## Overview

This document describes the initial backend API planned for the SynBioInventory MVP.

The backend API exists to simplify the frontend and centralize SynBioHub integration logic.

## Authentication

### `POST /api/auth/login`
Authenticate the user against SynBioHub.

**Request body**
```json
{
  "username": "user@example.org",
  "password": "secret"
}
```

**Response**
```json
{
  "authenticated": true,
  "username": "user@example.org"
}
```

### `POST /api/auth/logout`
Clear the current application session.

### `GET /api/auth/me`
Return current session information.

## Collections

### `GET /api/collections/root`
Return root collections visible to the user.

**Response shape**
```json
[
  {
    "uri": "https://example.org/collection/root1",
    "display_id": "root1",
    "name": "Root Collection 1",
    "description": "Example",
    "has_subcollections": true
  }
]
```

### `GET /api/collections/subcollections?uri=<collection_uri>`
Return subcollections of the provided collection.

## Inventory

### `GET /api/inventory/types`
Return supported implementation types.

**Response**
```json
[
  {
    "key": "ExtractedPlasmid",
    "label": "Extracted Plasmid"
  },
  {
    "key": "BacterialStock",
    "label": "Bacterial Stock"
  },
  {
    "key": "SolidMediaPlate",
    "label": "Solid Media Plate"
  }
]
```

### `POST /api/inventory/create`
Create an inventory object and attach one or more images.

**Content type**
`multipart/form-data`

**Fields**
- `destination_collection_uri`
- `implementation_type`
- `name` (optional)
- `notes` (optional)
- `built_uri` (optional)
- `images` (one or more files)

**Response**
```json
{
  "created_uri": "https://example.org/user/object_001",
  "destination_collection_uri": "https://example.org/collection/slot_a4",
  "implementation_type": "BacterialStock",
  "attached_images": 2,
  "message": "Inventory object created successfully"
}
```

## Error handling

The API should return clear structured errors.

Suggested shape:
```json
{
  "error": {
    "code": "INVALID_PLACEMENT",
    "message": "BacterialStock must be placed under FridgeMinus80C"
  }
}
```

## Development mode

In local stub mode, all endpoints should remain available, but SynBioHub-backed operations should be simulated.

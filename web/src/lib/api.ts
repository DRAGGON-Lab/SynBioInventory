import type {
  CollectionSummary,
  CreateInventoryRequest,
  CreateInventoryResponse,
  InventoryTypeSummary,
} from './types'

const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000'

export async function login(username: string, password: string) {
  const response = await fetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  })
  if (!response.ok) throw new Error('Login failed')
  return response.json()
}

export async function listRootCollections(): Promise<CollectionSummary[]> {
  const res = await fetch(`${API_BASE}/api/collections/root`)
  return res.json()
}

export async function listSubcollections(uri: string): Promise<CollectionSummary[]> {
  const res = await fetch(`${API_BASE}/api/collections/subcollections?uri=${encodeURIComponent(uri)}`)
  return res.json()
}

export async function listInventoryTypes(): Promise<InventoryTypeSummary[]> {
  const res = await fetch(`${API_BASE}/api/inventory/types`)
  return res.json()
}

export async function createInventory(
  payload: CreateInventoryRequest,
): Promise<CreateInventoryResponse> {
  const formData = new FormData()
  formData.set('destination_collection_uri', payload.destinationCollectionUri)
  formData.set('destination_storage_kind', payload.destinationStorageKind)
  formData.set('implementation_type', payload.implementationType)
  formData.set('object_uri', payload.objectUri)
  if (payload.barcode) formData.set('barcode', payload.barcode)
  if (payload.lotId) formData.set('lot_id', payload.lotId)
  if (payload.notes) formData.set('notes', payload.notes)
  if (payload.builtUri) formData.set('built_uri', payload.builtUri)
  payload.images.forEach((file) => formData.append('images', file))

  const res = await fetch(`${API_BASE}/api/inventory/create`, { method: 'POST', body: formData })
  if (!res.ok) {
    const text = await res.text()
    throw new Error(text)
  }
  return res.json()
}

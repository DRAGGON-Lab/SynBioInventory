import { useEffect, useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

import { ImageUpload } from '../components/ImageUpload'
import { Layout } from '../components/Layout'
import { listInventoryTypes } from '../lib/api'
import type { CollectionSummary, InventoryTypeSummary } from '../lib/types'

export function CreateImplementationPage() {
  const navigate = useNavigate()
  const location = useLocation()
  const destination = (location.state as { destination?: CollectionSummary })?.destination
  const [types, setTypes] = useState<InventoryTypeSummary[]>([])
  const [implementationType, setImplementationType] = useState('ExtractedPlasmid')
  const [objectUri, setObjectUri] = useState('')
  const [storageKind, setStorageKind] = useState('FridgeMinus20C')
  const [barcode, setBarcode] = useState('')
  const [lotId, setLotId] = useState('')
  const [notes, setNotes] = useState('')
  const [images, setImages] = useState<File[]>([])

  useEffect(() => {
    listInventoryTypes().then(setTypes)
  }, [])

  if (!destination) {
    return (
      <Layout>
        <p>No destination selected.</p>
        <button onClick={() => navigate('/collections')}>Back to browser</button>
      </Layout>
    )
  }

  return (
    <Layout>
      <h1>Create Inventory Implementation</h1>
      <div className="card">
        <p className="muted">Destination: {destination.name}</p>
        <label>
          Implementation type
          <select value={implementationType} onChange={(e) => setImplementationType(e.target.value)}>
            {types.map((type) => (
              <option key={type.key} value={type.key}>
                {type.label}
              </option>
            ))}
          </select>
        </label>
        <label>
          Destination storage kind
          <select value={storageKind} onChange={(e) => setStorageKind(e.target.value)}>
            <option>FridgeMinus80C</option>
            <option>FridgeMinus20C</option>
            <option>Fridge4C</option>
          </select>
        </label>
        <label>
          Object URI suffix
          <input
            value={objectUri}
            onChange={(e) => setObjectUri(e.target.value)}
            placeholder="e.g., bacterial_stock_001"
            required
          />
        </label>
        <label>
          Barcode (optional)
          <input value={barcode} onChange={(e) => setBarcode(e.target.value)} />
        </label>
        <label>
          Lot ID (optional)
          <input value={lotId} onChange={(e) => setLotId(e.target.value)} />
        </label>
        <label>
          Notes (optional)
          <textarea value={notes} onChange={(e) => setNotes(e.target.value)} />
        </label>
        <ImageUpload files={images} onChange={setImages} />
        <button
          type="button"
          onClick={() =>
            navigate('/review', {
              state: {
                destination,
                form: { implementationType, objectUri, storageKind, barcode, lotId, notes, images },
              },
            })
          }
          disabled={!objectUri}
        >
          Review Submission
        </button>
      </div>
    </Layout>
  )
}

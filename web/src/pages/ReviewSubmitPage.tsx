import { useState } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'

import { Layout } from '../components/Layout'
import { createInventory } from '../lib/api'
import type { CollectionSummary } from '../lib/types'

type ReviewState = {
  destination: CollectionSummary
  form: {
    implementationType: string
    objectUri: string
    storageKind: string
    barcode: string
    lotId: string
    notes: string
    images: File[]
  }
}

export function ReviewSubmitPage() {
  const navigate = useNavigate()
  const location = useLocation()
  const state = location.state as ReviewState | undefined
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  if (!state) {
    return (
      <Layout>
        <p>Nothing to review.</p>
      </Layout>
    )
  }

  const review = state

  async function onSubmit() {
    setSubmitting(true)
    setError(null)
    try {
      const result = await createInventory({
        destinationCollectionUri: review.destination.uri,
        destinationStorageKind: review.form.storageKind,
        implementationType: review.form.implementationType,
        objectUri: review.form.objectUri,
        barcode: review.form.barcode || undefined,
        lotId: review.form.lotId || undefined,
        notes: review.form.notes || undefined,
        images: review.form.images,
      })
      navigate('/success', { state: result })
    } catch (err) {
      setError((err as Error).message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <Layout>
      <h1>Review and Submit</h1>
      <div className="card">
        <p>Destination: {review.destination.uri}</p>
        <p>Type: {review.form.implementationType}</p>
        <p>Object URI: {review.form.objectUri}</p>
        <p>Images: {review.form.images.length}</p>
        {error && <p style={{ color: '#b91c1c' }}>{error}</p>}
        <button type="button" onClick={onSubmit} disabled={submitting}>
          {submitting ? 'Submitting…' : 'Submit'}
        </button>
      </div>
    </Layout>
  )
}

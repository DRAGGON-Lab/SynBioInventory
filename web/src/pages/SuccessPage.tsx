import { useLocation, useNavigate } from 'react-router-dom'

import { Layout } from '../components/Layout'
import type { CreateInventoryResponse } from '../lib/types'

export function SuccessPage() {
  const navigate = useNavigate()
  const location = useLocation()
  const result = location.state as CreateInventoryResponse | undefined

  return (
    <Layout>
      <h1>Inventory Created</h1>
      <div className="card">
        {result ? (
          <>
            <p>{result.message}</p>
            <p>
              Created URI: <code>{result.created_uri}</code>
            </p>
            <p>Attached images: {result.attached_images}</p>
          </>
        ) : (
          <p>No result data available.</p>
        )}
        <button onClick={() => navigate('/collections')} type="button">
          Create Another
        </button>
      </div>
    </Layout>
  )
}

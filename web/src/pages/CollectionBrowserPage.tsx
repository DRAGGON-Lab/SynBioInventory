import { useEffect, useMemo, useState } from 'react'
import { useNavigate } from 'react-router-dom'

import { Breadcrumbs } from '../components/Breadcrumbs'
import { CollectionList } from '../components/CollectionList'
import { Layout } from '../components/Layout'
import { listRootCollections, listSubcollections } from '../lib/api'
import type { CollectionSummary } from '../lib/types'

export function CollectionBrowserPage() {
  const navigate = useNavigate()
  const [path, setPath] = useState<CollectionSummary[]>([])
  const [items, setItems] = useState<CollectionSummary[]>([])
  const [selected, setSelected] = useState<CollectionSummary | null>(null)

  useEffect(() => {
    listRootCollections().then(setItems)
  }, [])

  const currentPathLabel = useMemo(() => path.map((node) => node.display_id).join(' / '), [path])

  async function openNode(node: CollectionSummary) {
    const children = await listSubcollections(node.uri)
    setPath((prev) => [...prev, node])
    setItems(children)
  }

  async function navigateTo(idx: number) {
    const targetPath = path.slice(0, idx + 1)
    setPath(targetPath)
    const target = targetPath[targetPath.length - 1]
    const children = await listSubcollections(target.uri)
    setItems(children)
  }

  return (
    <Layout>
      <h1>Choose Destination Collection</h1>
      <div className="card">
        <p className="muted">Single tap selects. Open navigates into subcollections.</p>
        <Breadcrumbs chain={path} onNavigate={navigateTo} />
        <CollectionList
          items={items}
          selectedUri={selected?.uri}
          onSelect={setSelected}
          onOpen={openNode}
        />
      </div>
      <div className="card">
        <div className="muted">Current path: {currentPathLabel || 'Root'}</div>
        <div className="muted">Selected: {selected?.display_id ?? 'None'}</div>
        <button
          disabled={!selected}
          onClick={() => navigate('/create', { state: { destination: selected } })}
          type="button"
        >
          Choose Collection
        </button>
      </div>
    </Layout>
  )
}

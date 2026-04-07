import type { CollectionSummary } from '../lib/types'

type Props = {
  chain: CollectionSummary[]
  onNavigate: (index: number) => void
}

export function Breadcrumbs({ chain, onNavigate }: Props) {
  return (
    <div className="breadcrumb">
      {chain.map((item, idx) => (
        <button key={item.uri} type="button" onClick={() => onNavigate(idx)}>
          {item.display_id}
        </button>
      ))}
    </div>
  )
}
